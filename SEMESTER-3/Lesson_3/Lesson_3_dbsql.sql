-- CREATE TABLE celebs (
--    id INTEGER,
-- 	  name TEXT,
-- 	  age INTEGER
-- );


-- INSERT INTO celebs (id, name, age)
-- VALUES (1, 'Justin Bieber', 22);

-- INSERT INTO celebs (id, name, age)
-- VALUES (2, 'John Wick', 50);

-- INSERT INTO celebs (id, name, age)
-- VALUES (3, 'HAHAHAHA', 10);


-- ALTER TABLE celebs
-- ADD COLUMN twitter_handle varchar(50);


-- UPDATE celebs
-- SET twitter_handle = 'random@random.com';
-- WHERE id = 3;


-- DELETE FROM celebs
-- WHERE id == 1;


-- CREATE TABLE celebs (
-- 	id INTEGER PRIMARY KEY,
-- 	name TEXT UNIQUE,
-- 	date_of_birth TEXT NOT NULL,
-- 	date_of_death TEXT DEFAULT 'Not Applicable'
-- 	);


-- INSERT INTO celebs (id, name, date_of_birth)
-- VALUES (2, 'Jusrin', '2022-12-21');

-- INSERT INTO celebs (id, name, date_of_birth)
-- VALUES (1, 'Justin', '2022-12-12');


-- CREATE TABLE friends (	
-- 	  id INTEGER PRIMARY KEY,
--    name TEXT UNIQUE,
--    birthday date NOT NULL
-- );	


-- INSERT INTO friends (id, name, birthday)
-- VALUES (1, 'James Monro', '1940-05-30');

-- INSERT INTO friends (id, name, birthday)
-- VALUES (2, 'Justin', '2005-07-12');

-- INSERT INTO friends (id, name, birthday)
-- VALUES (3, 'Christian', '2003-07-25');	


-- UPDATE friends
-- SET name = 'Flash'
-- WHERE id = 1;


-- ALTER TABLE friends
-- ADD COLUMN mail varchar(50);


-- UPDATE friends
-- SET mail = 'random@random.com';


-- DELETE FROM friends
-- WHERE id == 1;


SELECT * FROM friends;