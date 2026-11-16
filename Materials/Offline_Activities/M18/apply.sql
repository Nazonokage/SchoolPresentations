-- Select your activity database in phpMyAdmin first.
-- Run each statement in order and capture required results before continuing.
-- Import starter.sql ONCE first. Do not run it again if its tables already exist.
SELECT * FROM items;
INSERT INTO items VALUES (4,'Water',12,15.00);
SELECT * FROM items WHERE item_id=2;
UPDATE items SET quantity=20 WHERE item_id=2;
SELECT * FROM items WHERE item_id=2;
SELECT * FROM items WHERE item_id=3;
DELETE FROM items WHERE item_id=3;
SELECT * FROM items ORDER BY item_id;
SELECT SUM(quantity*price) AS stock_value FROM items;
