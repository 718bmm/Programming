-- SELECT avg(LifeExpectancy) from Country

-- where LifeExpectancy IS NOT NULL;





-- 66.486036036036

-- select avg(LifeExpectancy) from Country;



 

-- select min(age) from people;

-- select max(age) from people;

 



-- select round(avg(age), 2) as 'Средний возраст' from people

--  30;

-- select round(avg(age), 2) as 'Средний возраст' from people

--  40;

-- select round(avg(age), 2) as 'Средний возраст' from people

--  60;





-- SELECT state_code, avg(age) FROM people

-- GROUP BY state_code

-- ORDER BY state_code;



-- SELECT city, avg(age) FROM people

-- GROUP BY city

-- ORDER BY city;





-- SELECT from city, state_code, avg(age) FROM people

-- where city like 'B%'

-- GROUP BY 1

-- ORDER BY 1

-- LIMIT 10;

-- 

-- SELECT city, state_code, av(age) as Age, sum(quiz_points) as Total_Points FROM people

-- GROUP BY 1

-- HAVING sum(quiz_points) &gt; 100

-- ORDER BY 1;









--### Queries

-- Вывести названия всех стран из таблицы country (имена стран не должны повторятся)

-- Вывести на экран все страны из континента Asia из таблицы country

-- Вывести на экран столбцы: Name, Continent, IndepYear, где IndepYear наступило после 1990 года сортированные от убыванию из таблицы country.

-- Вывести на экран первые 10 строк где IndepYear не Null и Population в диапазоне от 15000 до 24318000 из таблицы country

-- Вывести на экран столбцы: Name, HeadOfState с искусственным полем 'Форма управления', которое может иметь три значения: 

-- когда GovernmentForm равен Republic - 'Республика'

-- когда GovernmentForm равен Monarchy - 'Монархния'

-- когда GovernmentForm равен Federal Republic - 'Федерация'

-- для остальных случаев - 'Иные виды правления'







-- SELECT DISTINCT Name FROM Country ORDER BY Name;





-- SELECT Name FROM Country

-- WHERE Continent = 'Asia';





-- SELECT Name, Continent, IndepYear FROM Country

-- WHERE IndepYear &gt; 1990

-- ORDER BY desc;





-- select Name from Country

-- where (IndepYear is not NULL) AND

-- (Population BETWEEN 15000 and 24318000)

-- limit 10;

























--### Aggregate funcs

-- получить сумму населения из таблицы Country

-- родолжения жизни (LifeExpectancy) из таблицы Country

-- продолжения жизни для каждого континента из таблицы Country

-- из таблицы City и сортировать по убыванию	

	

	

	

	

	

	

	

	
