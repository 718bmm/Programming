drop schema if exists cc_user cascade;

create schema cc_user;

set
    SEARCH_PATH = cc_user;
    
create table customers (
customer_id INTEGER generated always as identity primary key,
first_name VARCHAR(100) not null,
last_name VARCHAR(100) not null,
email_adress VARCHAR(300) null,
home_phone VARCHAR(100) null,
city VARCHAR(50) null,
state_name VARCHAR(50) null,
years_old INTEGER null
);
create table customers_log (
changed_by VARCHAR(100) not null,
time_changed TIMESTAMP not NULL
);

create trigger insert_trigger
before update on customers 
for each row 
execute procedure insert_function();

select * from customers;

update customers 
set years_old = 42
where last_name = 'Hall';

select * from customers;

CREATE OR REPLACE FUNCTION log_customers_change() RETURNS TRIGGER AS $$ BEGIN
INSERT INTO
    customers_log (changed_by, time_changed)
VALUES
    (User, DATE_TRUNC('minute', NOW()));
RETURN NEW;
END;
$$ LANGUAGE PLPGSQL;

CREATE TABLE customers_log (
    changed_by VARCHAR(100) NOT NULL,
    time_changed TIMESTAMP NOT NULL
);

CREATE OR REPLACE FUNCTION log_customers_change() RETURNS TRIGGER AS $$ BEGIN
INSERT INTO
    customers_log (changed_by, time_changed)
VALUES
    (User, DATE_TRUNC('minute', NOW()));
RETURN NEW;
END;
$$ LANGUAGE PLPGSQL;

create table customers_log (
changed_by VARCHAR(100) not null,
time_changed TIMESTAMP not null 
);
create table clients (
client_id INTEGER generated always as identity primary key,
HIGH_SPENDER INTEGER null,
FIRST_NAME VARCHAR(100) not null,
LAST_NAME VARCHAR(100) not null,
TOTAL_SPENT INTEGER null 
);
     
   CREATE TABLE customers_log (
  id SERIAL PRIMARY KEY,
  table_name VARCHAR(255) NOT NULL,
  action VARCHAR(255) NOT NULL,
  timestamp TIMESTAMPTZ DEFAULT NOW()
);

CREATE OR REPLACE FUNCTION address_insert_trigger()
  RETURNS TRIGGER AS $$
  BEGIN
    INSERT INTO customers_log (table_name, action)
    VALUES ('address', 'insert');
    RETURN NEW;
  END;
$$ LANGUAGE plpgsql;





CREATE TRIGGER category_insert
  AFTER INSERT ON category
  FOR EACH ROW
  EXECUTE FUNCTION category_insert_trigger();

CREATE OR REPLACE FUNCTION dish_insert_trigger()
  RETURNS TRIGGER AS $$
  BEGIN
    INSERT INTO customers_log (table_name, action)
    VALUES ('dish', 'insert');
    RETURN NEW;
  END;
$$ LANGUAGE plpgsql;






CREATE TRIGGER address_insert
  AFTER INSERT ON address
  FOR EACH ROW
  EXECUTE FUNCTION address_insert_trigger();

CREATE OR REPLACE FUNCTION category_insert_trigger()
  RETURNS TRIGGER AS $$
  BEGIN
    INSERT INTO customers_log (table_name, action)
    VALUES ('category', 'insert');
    RETURN NEW;
  END;
$$ LANGUAGE plpgsql;