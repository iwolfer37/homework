-- Завдання 1

CREATE DATABASE my_first_db;

-- Завдання 2
CREATE TABLE student (
  id INT,
  name VARCHAR(255)
);

-- Завдання 3
CREATE TABLE employee (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  salary INT
);

-- Завдання 4
ALTER TABLE student ADD PRIMARY KEY (id);

-- Завдання 5
INSERT INTO student (id, name) VALUES (01, 'John');
INSERT INTO employee (id, name, salary) VALUES (01, 'John', 10000);
