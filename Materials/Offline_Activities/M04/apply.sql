-- Select your activity database in phpMyAdmin first.
-- Run each statement in order and capture required results before continuing.
-- Start in an EMPTY database. If you already built these tables through the UI, skip CREATE and INSERT steps already completed.
CREATE TABLE items (
 item_id INT PRIMARY KEY,
 item_name VARCHAR(60) NOT NULL,
 quantity INT NOT NULL,
 price DECIMAL(8,2) NOT NULL
) ENGINE=InnoDB;
INSERT INTO items VALUES
 (1,'Rice meal',10,50.00),
 (2,'Noodles',8,35.00),
 (3,'Fruit cup',6,25.00);
INSERT INTO items VALUES (4,'Water',12,15.00);
SHOW CREATE TABLE items;
SELECT * FROM items;
