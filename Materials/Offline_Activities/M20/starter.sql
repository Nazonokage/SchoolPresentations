-- Import once into a NEW empty activity database. No database is created or dropped.
CREATE TABLE customers (customer_id INT PRIMARY KEY, customer_name VARCHAR(60) NOT NULL, email VARCHAR(100)) ENGINE=InnoDB;
CREATE TABLE orders (order_id INT PRIMARY KEY, customer_id INT NOT NULL, order_date DATE, quantity INT NOT NULL, unit_price DECIMAL(8,2) NOT NULL, FOREIGN KEY(customer_id) REFERENCES customers(customer_id)) ENGINE=InnoDB;
INSERT INTO customers VALUES (1,'  Alex Cruz  ','alex1@example.test'),(2,'  Alex Cruz  ','alex2@example.test');
INSERT INTO orders VALUES (101,1,'2026-11-01',2,50.00),(102,1,'2026-11-02',1,50.00),(103,2,'2026-11-03',3,25.00);
