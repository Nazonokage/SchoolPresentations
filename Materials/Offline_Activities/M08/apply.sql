-- Select your activity database in phpMyAdmin first.
-- Run each statement in order and capture required results before continuing.
-- Start in an EMPTY database. If you already built these tables through the UI, skip CREATE and INSERT steps already completed.
CREATE TABLE students (student_id INT PRIMARY KEY, student_name VARCHAR(60) NOT NULL) ENGINE=InnoDB;
CREATE TABLE courses (course_id INT PRIMARY KEY, course_name VARCHAR(60) NOT NULL) ENGINE=InnoDB;
INSERT INTO students VALUES (1,'Ana'),(2,'Ben'),(3,'Cara');
INSERT INTO courses VALUES (101,'Databases'),(102,'Programming');
CREATE TABLE enrollments (
 student_id INT, course_id INT,
 PRIMARY KEY(student_id,course_id),
 FOREIGN KEY(student_id) REFERENCES students(student_id),
 FOREIGN KEY(course_id) REFERENCES courses(course_id)
) ENGINE=InnoDB;
INSERT INTO enrollments VALUES (1,101),(1,102),(2,101),(3,102);
SELECT * FROM enrollments;
SHOW CREATE TABLE enrollments;
