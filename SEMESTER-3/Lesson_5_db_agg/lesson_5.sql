create table book (
	title varchar(100),
	isbn varchar(50),
	pages integer,
	price money,
	description varchar(256),
	publisher varchar(100)
);

create table chapter (
	id integer,
	number integer,
	title varchar(50),
	content varchar(1024)
);

create table author (
	name varchar(50),
	bio varchar(50),
	email varchar(50) primary key
);

create table popular_recipes (
	recipe_id varchar(20),
	ingredient_id varchar(20),
	downloaded integer,
	primary key (recipe_id, ingredient_id)
);

create table popular_books (
	book_title varchar(100),
	author_name varchar(50),
	number_sold integer,
	number_previewed integer,
	primary key (book_title, author_name)
);

create table book_details ( 
	id 
	rating decimal,
	language varchar(10),
	keywords text[], an array of unlimited-length strings
	date_published of type date
);

create table page (
	id integer PRIMARY KEY,
	content text,
	header varchar(20),
	footer varchar(20)
);

--select 
--	constraint_name, table_name, column_name
--from
--	information_schema.key_column_usage
--where 
--	table_name = 'author';

