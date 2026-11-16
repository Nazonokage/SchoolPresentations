-- Select your activity database in phpMyAdmin first.
-- Run each statement in order and capture required results before continuing.
-- Import starter.sql ONCE first. Do not run it again if its tables already exist.
CREATE VIEW customer_spending AS
SELECT c.customer_id,c.customer_name,SUM(o.quantity*o.unit_price) AS total_spent
FROM customers c JOIN orders o ON c.customer_id=o.customer_id
GROUP BY c.customer_id,c.customer_name;
SELECT * FROM customer_spending;
EXPLAIN SELECT * FROM customers WHERE email='alex1@example.test';
CREATE INDEX idx_customer_email ON customers(email);
SHOW INDEX FROM customers;
EXPLAIN SELECT * FROM customers WHERE email='alex1@example.test';
