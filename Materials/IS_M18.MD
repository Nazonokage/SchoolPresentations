# Basic SQL: Data Manipulation Language (DML)

> **Learning Objectives:**
> By the end of this lesson, you will be able to:
> *   Discuss the Data Manipulation Language (DML) and its associated commands.
> *   Contrast the different comparison and logical operators used in a query.
> *   Apply `INSERT`, `UPDATE`, and `DELETE` commands to perform basic CRUD (Create, Read, Update, Delete) operations.
> *   Understand modern data safety practices including **Soft Deletes** and **Prepared Statements**.

---

## A. Lesson Preview & Review

Welcome, students! Today we are diving into **Data Manipulation Language (DML)**. While Data Definition Language (DDL) builds the structure of our database (the tables), DML is how we actually interact with the data inside those tables. 

We will cover the four fundamental operations—often called **CRUD**: Create (`INSERT`), Read (`SELECT`), Update (`UPDATE`), and Delete (`DELETE`). We will also explore how to filter data using comparison and logical operators to find exactly what you need. Let's get started!

![SQL Data Manipulation Concept](https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&q=80&w=1200)

---

## B. Main Lesson

### 1. What is DML?
**Data Manipulation Language (DML)** is a subset of SQL commands used to manage and manipulate the data *within* existing database objects. DML commands do not change the structure of the database; they only change the rows of data.

The most commonly used DML commands are:
*   **`SELECT`**: Retrieves data from one or more tables.
*   **`INSERT`**: Adds new records into a table.
*   **`UPDATE`**: Modifies existing records in a table.
*   **`DELETE`**: Removes records from a table.

> **Modern Update: UPSERT (Merge)**
> Modern databases often support an `UPSERT` operation (e.g., `INSERT ... ON CONFLICT DO UPDATE` in PostgreSQL or `INSERT ... ON DUPLICATE KEY UPDATE` in MySQL). This allows you to insert a new row, but if a row with the same primary key already exists, it updates that row instead of throwing an error. 

### 2. Comparison and Logical Operators
To query or modify specific rows, we use operators to filter the data. 

#### Comparison Operators (Compare a column to a value)
| Operator | Description | Example |
| :--- | :--- | :--- |
| **`=`** | Equal to | `WHERE department = 'IT'` |
| **`>`** | Greater than | `WHERE salary > 50000` |
| **`<`** | Less than | `WHERE age < 30` |
| **`>=`** | Greater than or equal to | `WHERE experience >= 5` |
| **`<=`** | Less than or equal to | `WHERE price <= 100` |
| **`<>` or `!=`** | Not equal to | `WHERE status <> 'Inactive'` |

#### Logical Operators (Combine multiple conditions)
| Operator | Description | Example |
| :--- | :--- | :--- |
| **`AND`** | True if *both* conditions are true | `WHERE dept = 'IT' AND salary > 50000` |
| **`OR`** | True if *at least one* condition is true | `WHERE dept = 'IT' OR dept = 'HR'` |
| **`NOT`** | Reverses the boolean value of a condition | `WHERE NOT dept = 'IT'` |
| **`IN`** | True if the value matches any in a list | `WHERE dept IN ('IT', 'HR', 'Sales')` |
| **`BETWEEN`** | True if the value is within a range | `WHERE salary BETWEEN 40000 AND 60000` |

---

### 3. Performing CRUD Operations (DML Syntax)

#### A. INSERT (Create)
Used to add new rows to a table.
```sql
INSERT INTO table_name (column1, column2, column3)
VALUES ('value1', 'value2', 'value3');
```
*Example:* Adding a new customer.
```sql
INSERT INTO customers (name, email)
VALUES ('John Smith', 'johnsmith@example.com');
```

#### B. UPDATE (Modify)
Used to change existing data. **Always use a `WHERE` clause** unless you intend to update every row in the table!
```sql
UPDATE table_name
SET column1 = 'new_value1', column2 = 'new_value2'
WHERE some_column = some_value;
```
*Example:* Changing a customer's email address.
```sql
UPDATE customers
SET email = 'jsmith@example.com'
WHERE name = 'John Smith';
```

#### C. DELETE (Remove)
Used to remove rows from a table. **Always use a `WHERE` clause** to prevent deleting the entire table's data!
```sql
DELETE FROM table_name
WHERE some_column = some_value;
```
*Example:* Removing a customer.
```sql
DELETE FROM customers
WHERE name = 'John Smith';
```

> **Pro Tip: Modern Best Practice - Soft Deletes**
> In modern application development, running a hard `DELETE` (physically removing the row) is often discouraged because it destroys historical data and breaks foreign key relationships. Instead, developers use **Soft Deletes**. This involves having an `is_deleted` or `deleted_at` column. 
> *   *Instead of:* `DELETE FROM users WHERE id = 1;`
> *   *We do:* `UPDATE users SET deleted_at = CURRENT_TIMESTAMP WHERE id = 1;`
> This keeps the data for auditing and allows for easy recovery if a user is deleted by mistake.

---

## C. Analogies and Use Cases

### The Spreadsheet Analogy
*   **INSERT** is adding a new row at the bottom of your Excel sheet.
*   **SELECT** is using the filter feature to only show rows where the "Department" is "IT".
*   **UPDATE** is clicking a cell and typing a new value over the old one.
*   **DELETE** is highlighting a row, right-clicking, and selecting "Delete Row."

### Real-World Use Case: E-Commerce Inventory Management
An online store uses DML constantly. 
*   When a customer buys a shirt, an `INSERT` statement creates a new order record.
*   An `UPDATE` statement decreases the `quantity_in_stock` by 1.
*   If a customer cancels their order, instead of a `DELETE` (which might ruin financial reporting), a `UPDATE` statement sets the order status to `Cancelled` (Soft Delete).

> **Important Note on Security (SQL Injection)**
> In the real world, you rarely write raw `INSERT` or `UPDATE` queries with string concatenation (like `WHERE name = 'John Smith'`). If you do this in a web application (e.g., PHP, Python), malicious users can inject SQL code. Always use **Prepared Statements** (parameterized queries) provided by your database driver to separate the SQL code from the user data.

---

## D. Lesson Wrap-Up / FAQs

### Summary
**DML** is how we manipulate the actual data within our database tables using **CRUD** operations (`INSERT`, `UPDATE`, `DELETE`, and `SELECT`). We use **comparison** operators (like `=`, `>`, `<`) and **logical** operators (like `AND`, `OR`, `IN`, `BETWEEN`) to filter exactly which rows are affected by our queries. Always exercise caution with `UPDATE` and `DELETE` to avoid accidental data loss.

### Frequently Asked Questions (FAQs)

**Q: What happens if I run a `DELETE` command without a `WHERE` clause?**
**A:** It will delete **every single row** in the table, leaving an empty table structure. Use extreme caution and always back up data before running queries on production databases.

**Q: What is the difference between `DELETE` and `TRUNCATE`?**
**A:** `DELETE` is a DML command; it removes rows one by one, can be filtered with a `WHERE` clause, and can be rolled back (if wrapped in a transaction). `TRUNCATE` is a DDL command; it quickly removes all rows at once, cannot be filtered, and usually cannot be rolled back.

**Q: What does `MERGE` do?**
**A:** The `MERGE` statement (also known as UPSERT) allows you to insert new data or update existing data based on a specified condition. It's highly useful for synchronizing data between two tables.

---

## E. Guided Drills / Code Projects

### Exercise: Manage a Products Table

**Task:** You are managing a database for an electronics store. Use the following `products` table to practice your DML skills.

| product_id | product_name | price | quantity | supplier |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Pen | 2.50 | 100 | A |
| 2 | Pencil | 1.50 | 200 | B |
| 3 | Notebook | 5.00 | 50 | A |
| 4 | Eraser | 0.50 | 500 | B |
| 5 | Ruler | 1.00 | 300 | A |

**Questions:**
1.  Write a query to retrieve all products with a price greater than 2.00.
2.  Write a query to increase the price of all products by 10%.
3.  Write a query to delete all products with a quantity less than 100.
4.  Write a query to retrieve all products supplied by 'A' and order the results by `product_name` ascending.
5.  Write a query to retrieve the average price of all products.

**Solutions:**
```sql
-- 1. Retrieve products > 2.00
SELECT * FROM products WHERE price > 2.00;

-- 2. Increase price by 10%
UPDATE products SET price = price * 1.1;

-- 3. Delete products with quantity < 100
DELETE FROM products WHERE quantity < 100;

-- 4. Retrieve Supplier A, ordered by name
SELECT * FROM products WHERE supplier = 'A' ORDER BY product_name ASC;

-- 5. Average price
SELECT AVG(price) FROM products;
```

---

## F. Skill-Building Check

### Part 1: Fill in the Blanks
*Complete the statement with the correct DML command.*

1.  The command used to insert data into a table is **`INSERT`**.
2.  The command used to update data in a table is **`UPDATE`**.
3.  The command used to delete data from a table is **`DELETE`**.
4.  The command used to retrieve data from a table is **`SELECT`**.
5.  The DDL command used to create a table is **`CREATE`**.

### Part 2: Multiple Choice
*Identify the best answer from the following questions.*

**1. Which SQL operator is used to check if a value falls within a specific range?**
a) `IN`
b) `BETWEEN`
c) `LIKE`
d) `AND`
> **Correct Answer: b.** `BETWEEN` checks if a value is within a range (inclusive).

**2. What is the primary risk of running an `UPDATE` command without a `WHERE` clause?**
a) The database will crash.
b) It will update every row in the table.
c) It will delete the table.
d) It will throw a syntax error.
> **Correct Answer: b.** Without a `WHERE` clause, the database engine applies the update to all existing rows.

**3. Which logical operator requires *both* conditions to be true for the row to be included in the result?**
a) `OR`
b) `NOT`
c) `AND`
d) `IN`
> **Correct Answer: c.** `AND` requires both sides of the condition to evaluate to true.

**4. (Modern Practice) Instead of physically deleting a record, modern applications often use a "Soft Delete". How is this typically implemented?**
a) Moving the record to a different database.
b) Using an `UPDATE` statement to change a status column (e.g., `is_deleted = true`).
c) Using the `DROP` command.
d) Encrypting the row.
> **Correct Answer: b.** Soft deletes mark a row as inactive rather than removing the data entirely, preserving history.