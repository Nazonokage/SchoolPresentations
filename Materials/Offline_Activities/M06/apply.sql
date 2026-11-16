-- Select your activity database in phpMyAdmin first.
-- Run each statement in order and capture required results before continuing.
-- Start in an EMPTY database. If you already built these tables through the UI, skip CREATE and INSERT steps already completed.
CREATE TABLE items (item_id INT PRIMARY KEY, item_name VARCHAR(60), quantity INT, price DECIMAL(8,2)) ENGINE=InnoDB;
INSERT INTO items VALUES (1,'Pen',10,10.00),(2,'Notebook',8,35.00),(3,'Pencil',6,8.00),(4,'Eraser',12,5.00),(5,'Folder',5,12.00);
SELECT * FROM items WHERE item_id=1;
UPDATE items SET quantity=15 WHERE item_id=1;
SELECT * FROM items WHERE item_id=1;
SELECT item_name, quantity, price, quantity * price AS stock_value
FROM items ORDER BY stock_value DESC;
