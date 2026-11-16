-- Select your activity database in phpMyAdmin first.
-- Run each statement in order and capture required results before continuing.
-- Start in an EMPTY database. If you already built these tables through the UI, skip CREATE and INSERT steps already completed.
CREATE TABLE employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(60) NOT NULL, email VARCHAR(100) UNIQUE) ENGINE=InnoDB;
INSERT INTO employees VALUES (1,'Ana','ana@example.test'),(2,'Ben','ben@example.test');
ALTER TABLE employees ADD salary DECIMAL(10,2) NOT NULL DEFAULT 0;
UPDATE employees SET salary=20000 WHERE employee_id=1;
UPDATE employees SET salary=25000 WHERE employee_id=2;
INSERT INTO employees VALUES (3,'Cara','cara@example.test',22000);
SHOW CREATE TABLE employees;
SELECT * FROM employees;
