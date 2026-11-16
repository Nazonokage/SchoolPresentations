-- Import once into a NEW empty activity database. No database is created or dropped.
CREATE TABLE items (item_id INT PRIMARY KEY, item_name VARCHAR(60) NOT NULL, quantity INT NOT NULL, price DECIMAL(8,2) NOT NULL) ENGINE=InnoDB;
INSERT INTO items VALUES (1,'Rice meal',10,50.00),(2,'Noodles',8,35.00),(3,'Fruit cup',6,25.00);
