-- Select your activity database in phpMyAdmin first.
-- Run each statement in order and capture required results before continuing.
-- Start in an EMPTY database. If you already built these tables through the UI, skip CREATE and INSERT steps already completed.
CREATE TABLE members (member_id INT PRIMARY KEY, member_name VARCHAR(60) NOT NULL) ENGINE=InnoDB;
CREATE TABLE books (book_id INT PRIMARY KEY, title VARCHAR(100) NOT NULL) ENGINE=InnoDB;
CREATE TABLE loans (
 loan_id INT PRIMARY KEY, member_id INT NOT NULL, book_id INT NOT NULL,
 loan_date DATE, return_date DATE NULL,
 FOREIGN KEY(member_id) REFERENCES members(member_id),
 FOREIGN KEY(book_id) REFERENCES books(book_id)
) ENGINE=InnoDB;
INSERT INTO members VALUES (1,'Ana'),(2,'Ben');
INSERT INTO books VALUES (1,'Database Basics'),(2,'Programming Basics'),(3,'Web Design');
INSERT INTO loans VALUES (101,1,1,'2026-11-01',NULL),(102,2,2,'2026-11-02',NULL),(103,1,3,'2026-10-20','2026-10-27');
SELECT m.member_name,b.title,l.loan_date
FROM loans l JOIN members m ON l.member_id=m.member_id
JOIN books b ON l.book_id=b.book_id
WHERE l.return_date IS NULL;
SHOW CREATE TABLE loans;
