Here is a simplified, three-part practical review and assessment based on the SQL commands covered in the module.

---

## Part 1: Lesson Recap & Review

Before starting the practical quiz, quickly review these essential SQL concepts:

*   **DDL (Data Definition Language):** Commands like `CREATE DATABASE` and `CREATE TABLE` define the structure of your data. Remember to specify data types (e.g., `INT`, `VARCHAR`, `DECIMAL`).
*   **DML (Data Manipulation Language):** Commands like `INSERT`, `UPDATE`, and `DELETE` manage the actual data inside the table.
*   **DQL (Data Query Language):** The `SELECT` command retrieves data. You can use it with:
    *   `WHERE` to filter specific rows.
    *   `COUNT()` to count rows.
    *   `SUM()` to add up values (you can do math inside it, like `quantity * price`).
    *   `ORDER BY` to sort results (use `ASC` for ascending, `DESC` for descending).
*   **Best Practice:** Always preview your data with a `SELECT` statement before running an `UPDATE` or `DELETE` to prevent accidental data loss!

---

## Part 2: Practical Quiz

**Instructions:** Carefully write the SQL command to complete each of the following tasks. *(2 points per correct task)*

1.  Create a new database called `shopping_cart`.
2.  Create a table called `items` within the `shopping_cart` database with the following columns:
    *   `id` (integer, primary key)
    *   `name` (varchar)
    *   `quantity` (integer)
    *   `price` (decimal)
3.  Use the `INSERT` command to add the following items to the `items` table:
    *   (1, 'Apple', 10, 0.99)
    *   (2, 'Banana', 5, 0.59)
    *   (3, 'Cherries', 15, 2.99)
4.  Use the `UPDATE` command to change the quantity of Banana to **20**.
5.  Use the `DELETE` command to remove Cherries from the table.
6.  Use the `SELECT` command with a `WHERE` clause to retrieve all items with a price greater than $1.00.
7.  Use the `COUNT` function to retrieve the number of items currently in the `items` table.
8.  Use the `SUM` function to calculate the total value of all items in the `items` table (Total Value = Quantity × Price).
9.  Use the `ORDER BY` clause to sort all items in the `items` table by price in ascending order.
10. Use the `SELECT *` command to view the final contents of the `items` table and verify that the changes made using `INSERT`, `UPDATE`, and `DELETE` have been applied correctly.

---

## Part 3: Answer Key

1.  **Create Database:**
    ```sql
    CREATE DATABASE shopping_cart;
    USE shopping_cart; -- (Important to select the DB before creating tables)
    ```

2.  **Create Table:**
    ```sql
    CREATE TABLE items (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        quantity INT,
        price DECIMAL(10, 2)
    );
    ```

3.  **Insert Data:**
    ```sql
    INSERT INTO items (id, name, quantity, price) 
    VALUES 
        (1, 'Apple', 10, 0.99),
        (2, 'Banana', 5, 0.59),
        (3, 'Cherries', 15, 2.99);
    ```

4.  **Update Data:**
    ```sql
    UPDATE items 
    SET quantity = 20 
    WHERE name = 'Banana';
    ```

5.  **Delete Data:**
    ```sql
    DELETE FROM items 
    WHERE name = 'Cherries';
    ```

6.  **Select with WHERE:**
    ```sql
    SELECT * FROM items 
    WHERE price > 1.00;
    ```

7.  **Count Items:**
    ```sql
    SELECT COUNT(*) FROM items;
    ```

8.  **Sum Total Value:**
    ```sql
    SELECT SUM(quantity * price) AS total_value FROM items;
    ```

9.  **Order By Price:**
    ```sql
    SELECT * FROM items 
    ORDER BY price ASC;
    ```

10. **Verify Final State:**
    ```sql
    SELECT * FROM items;
    ```