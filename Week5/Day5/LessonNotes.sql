-- Parent table: colors
CREATE TABLE colors (
    color_id SERIAL PRIMARY KEY,
    name TEXT
);
-- Child table: cars with ON DELETE RESTRICT
CREATE TABLE cars (
    car_id SERIAL PRIMARY KEY,
    car_color INTEGER REFERENCES colors(color_id) ON DELETE RESTRICT,
    car_name TEXT
);
-- Insert into colors
INSERT INTO colors (name) VALUES
('red'),
('blue'),
('yellow'),
('pink');
-- Insert into cars
INSERT INTO cars (car_color, car_name) VALUES
(1, 'Ferrari'),
(2, 'Ford'),
(3, 'BMW'),      -- yellow
(4, 'Bugatti');  -- pink
DELETE FROM colors WHERE name = 'yellow';  -- blocked if "BMW" still exists
DROP TABLE IF EXISTS cars;

