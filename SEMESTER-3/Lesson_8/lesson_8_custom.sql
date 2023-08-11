CREATE TABLE customers (
    customer_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email_address VARCHAR(300) NULL,
    home_phone VARCHAR(100) NULL,
    city VARCHAR(50) NULL,
    state_name VARCHAR(50) NULL,
    years_old INTEGER NULL
);

CREATE TABLE customers_log (
    changed_by VARCHAR(100) NOT NULL,
    time_changed TIMESTAMP NOT NULL
);

CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY,
    high_spender INTEGER NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    total_spent INTEGER NULL
);

CREATE TABLE orders (
    order_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    quantity INTEGER NULL,
    notes VARCHAR(100) NULL
);

-- update, delete, insert, truncate
-- OLD and NEW represent the states of the row in the table before or after the triggering event.
-- 1
create OR REPLACE FUNCTION insert_function() RETURNS TRIGGER AS 
$$ BEGIN 
    NEW.last_name := 'UNKNOWN';
    RETURN NEW;
END; 
$$ LANGUAGE PLPGSQL;


-- 2
CREATE OR REPLACE FUNCTION log_customers_change() RETURNS TRIGGER AS $$ BEGIN
INSERT INTO
    customers_log (changed_by, time_changed)
VALUES
    (User, DATE_TRUNC('minute', NOW()));
RETURN NEW;
END;
$$ LANGUAGE PLPGSQL;


-- 3
CREATE
OR REPLACE FUNCTION statement_function() RETURNS TRIGGER AS $$ BEGIN
INSERT INTO
    customers_log 
VALUES
    ((select first_name from customers where customer_id = 1), NOW());
RETURN NEW;
END;
$$ LANGUAGE PLPGSQL;


-- 4
CREATE OR REPLACE FUNCTION set_low_spender() RETURNS TRIGGER AS $$
  BEGIN
    NEW.high_spender = 0;
    RETURN NEW;
  END;
$$ LANGUAGE PLPGSQL;

CREATE OR REPLACE FUNCTION set_high_spender() RETURNS TRIGGER AS $$
  BEGIN
    NEW.high_spender = 1;
    RETURN NEW;
  END;
$$ LANGUAGE PLPGSQL;


-- 5
CREATE OR REPLACE FUNCTION update_first() RETURNS TRIGGER AS $$
  BEGIN
    NEW.notes = CONCAT(NEW.notes, 'update_first ran ');
    RETURN NEW;
  END;
$$ LANGUAGE PLPGSQL;

CREATE OR REPLACE FUNCTION update_second() RETURNS TRIGGER AS $$
  BEGIN
    NEW.notes = CONCAT(NEW.notes, 'update_second ran ');
    RETURN NEW;
  END;
$$ LANGUAGE PLPGSQL;




