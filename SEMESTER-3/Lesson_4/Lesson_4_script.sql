-- CREATE TABLE if not exists friends (	
-- 	id INTEGER PRIMARY KEY,
--    name TEXT UNIQUE,
--    birthday date NOT NULL
-- );	
--
-- INSERT INTO friends (id, name, birthday)
-- VALUES (1, 'James Monro', '1940-05-30');
--
--INSERT INTO friends (id, name, birthday)
--VALUES (2, 'Justin', '2005-07-12');	
--
-- INSERT INTO friends (id, name, birthday)
-- VALUES (3, 'Christian', '2003-07-25');	


UPDATE friends SET name = 'Flash' WHERE id = 1;

ALTER TABLE friends
ADD COLUMN mail varchar(50);


UPDATE friends
 SET mail = 'random@random.com';
 DELETE FROM friends
 WHERE id = 1;


SELECT * FROM friends;