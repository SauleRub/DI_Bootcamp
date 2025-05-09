-- Daily SQL Puzzle: Table Relationships and NULL Behavior
-- Assumptions and expected outputs written in comments before each query

-- Step 1: Create tables
CREATE TABLE FirstTab (
    id INTEGER,
    name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5, 'Pawan'),
(6, 'Sharlee'),
(7, 'Krish'),
(NULL, 'Avtaar');

SELECT * FROM FirstTab;

CREATE TABLE SecondTab (
    id INTEGER
);

INSERT INTO SecondTab VALUES
(5),
(NULL);

SELECT * FROM SecondTab;

-- Q1: Expected output = 0
-- NOT IN (NULL) always returns unknown → nothing matches
SELECT COUNT(*) AS Q1_Result
FROM FirstTab AS ft
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab WHERE id IS NULL
);

-- Q2: Expected output = 2 (id = 6, 7 match; NULL ignored)
SELECT COUNT(*) AS Q2_Result
FROM FirstTab AS ft
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab WHERE id = 5
);

-- Q3: Expected output = 0 (NOT IN with NULL returns nothing)
SELECT COUNT(*) AS Q3_Result
FROM FirstTab AS ft
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab
);

-- Q4: Expected output = 2 (same logic as Q2)
SELECT COUNT(*) AS Q4_Result
FROM FirstTab AS ft
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab WHERE id IS NOT NULL
);