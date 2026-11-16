-- Import once into a NEW empty activity database. No database is created or dropped.
CREATE TABLE order_lines_raw (order_id INT,customer_id INT,customer_name VARCHAR(60),product_id INT,product_name VARCHAR(60),quantity INT,unit_price DECIMAL(8,2)) ENGINE=InnoDB;
INSERT INTO order_lines_raw VALUES (1,1,'Ana',1,'Pen',2,2.00),(1,1,'Ana',2,'Notebook',1,5.00),(2,2,'Ben',1,'Pen',1,2.00);
