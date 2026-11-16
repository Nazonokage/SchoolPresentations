-- Select your activity database in phpMyAdmin first.
-- Run each statement in order and capture required results before continuing.
-- Import starter.sql ONCE first. Do not run it again if its tables already exist.
CREATE TABLE customers (customer_id INT PRIMARY KEY, customer_name VARCHAR(60)) ENGINE=InnoDB;
CREATE TABLE products (product_id INT PRIMARY KEY, product_name VARCHAR(60)) ENGINE=InnoDB;
CREATE TABLE orders (order_id INT PRIMARY KEY, customer_id INT NOT NULL,
 FOREIGN KEY(customer_id) REFERENCES customers(customer_id)) ENGINE=InnoDB;
CREATE TABLE order_items (order_id INT, product_id INT, quantity INT, unit_price DECIMAL(8,2),
 PRIMARY KEY(order_id,product_id),
 FOREIGN KEY(order_id) REFERENCES orders(order_id),
 FOREIGN KEY(product_id) REFERENCES products(product_id)) ENGINE=InnoDB;
INSERT INTO customers SELECT DISTINCT customer_id,customer_name FROM order_lines_raw;
INSERT INTO products SELECT DISTINCT product_id,product_name FROM order_lines_raw;
INSERT INTO orders SELECT DISTINCT order_id,customer_id FROM order_lines_raw;
INSERT INTO order_items SELECT order_id,product_id,quantity,unit_price FROM order_lines_raw;
SELECT o.order_id,c.customer_id,c.customer_name,p.product_id,p.product_name,i.quantity,i.unit_price
FROM order_items i JOIN orders o ON i.order_id=o.order_id
JOIN customers c ON o.customer_id=c.customer_id
JOIN products p ON i.product_id=p.product_id ORDER BY o.order_id,p.product_id;
SELECT order_id,SUM(quantity*unit_price) AS order_total
FROM order_items GROUP BY order_id;
