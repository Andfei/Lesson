SELECT max(id) AS max_id FROM animal;
SELECT count(*) FROM animal WHERE type_animal LIKE 'собака%';
SELECT avg(weight) FROM animal WHERE type_animal LIKE 'собака%':
SELECT DISTINCT type_animal FROM animal;
SELECT * FROM animal WHERE name_animal='Вилли';
SELECT count(*) FROM animal WHERE type_animal='собака' AND sex='мужской';
SELECT count(*) FROM animal WHERE type_animal='собака' AND sex='женский';
SELECT DISTINCT * FROM animal WHERE type_animal='кот';
SELECT * FROM animal WHERE name_animal LIKE '%ик%';
UPDATE animal SET name_animal='монти' WHERE name_animal='бой' 