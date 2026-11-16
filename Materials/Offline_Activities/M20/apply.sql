-- Select your activity database in phpMyAdmin first.
-- Run each statement in order and capture required results before continuing.
-- Import starter.sql ONCE first. Do not run it again if its tables already exist.
SELECT customer_id,UPPER(TRIM(customer_name)) AS clean_name FROM customers;
SELECT order_id,order_date,DATE_ADD(order_date,INTERVAL 5 DAY) AS delivery_date FROM orders;
SELECT order_id,ROUND(quantity*unit_price,2) AS order_total FROM orders;
SELECT c.customer_id,c.customer_name,SUM(o.quantity*o.unit_price) AS total_sales
FROM customers c JOIN orders o ON c.customer_id=o.customer_id
GROUP BY c.customer_id,c.customer_name;
SELECT COUNT(*) AS order_count,SUM(quantity*unit_price) AS total_sales FROM orders;
