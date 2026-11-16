-- Select your activity database in phpMyAdmin first.
-- Run each statement in order and capture required results before continuing.
-- Start in an EMPTY database. If you already built these tables through the UI, skip CREATE and INSERT steps already completed.
CREATE TABLE customers (customer_id INT PRIMARY KEY, customer_name VARCHAR(60) NOT NULL) ENGINE=InnoDB;
CREATE TABLE orders (
 order_id INT PRIMARY KEY, customer_id INT NOT NULL,
 order_date DATE, total DECIMAL(10,2),
 FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
) ENGINE=InnoDB;
INSERT INTO customers VALUES (1,'Ana'),(2,'Ben');
INSERT INTO orders VALUES (101,1,'2026-11-01',100.00),(102,1,'2026-11-02',50.00),(103,2,'2026-11-03',75.00);
SELECT c.customer_name,o.order_id,o.order_date,o.total
FROM customers c JOIN orders o ON c.customer_id=o.customer_id
ORDER BY o.order_id;
