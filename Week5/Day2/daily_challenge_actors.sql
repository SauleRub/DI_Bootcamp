SELECT COUNT(*) FROM actor; -- 200

INSERT INTO actor (first_name, last_name)
VALUES (NULL, NULL); -- Error

INSERT INTO actor (first_name, last_name)
VALUES ('Saule', 'Rubinshtein');

SELECT COUNT(*) FROM actor; -- 201


