# Database Programming in Practice: Local Environments, DDL, and PHP Integration

> **Learning Objectives:**
> By the end of this lesson, you will be able to:
> *   Explain the differences between traditional local development stacks (like XAMPP) and modern containerized environments (like Docker).
> *   Discuss and apply Data Definition Language (DDL) commands including `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, and `RENAME`.
> *   Enforce data integrity using SQL constraints.
> *   Connect a PHP application to a MySQL database securely using modern **PDO (PHP Data Objects)** with prepared statements.

---

## A. Lesson Preview & Review

Welcome students! Today, we are bridging the gap between database theory and practical web development. We will cover how to configure a local environment to run MySQL, use SQL commands to define the structure of your database (DDL), and utilize PHP to connect to and interact with your database.

While traditional tools like **XAMPP** are excellent for beginners, modern engineering demands consistency and scalability. We will also explore how **Docker** has become the industry standard for replicating production-like environments locally.

![XAMPP vs Docker Development Environment](https://images.unsplash.com/photo-1607799279861-4dd421887fb3?auto=format&fit=crop&q=80&w=1200)

---

## B. Main Lesson

### 1. Local Development Environments: XAMPP vs. Docker

**XAMPP** is a popular open-source package that provides a local web server environment. It stands for Cross-Platform (X), Apache (A), MariaDB (M), PHP (P), and Perl (P). It is beginner-friendly and comes with a control panel to start and stop services.

However, as projects grow more complex, XAMPP faces limitations:
*   **Lack of Isolation:** One global PHP/MySQL version affects all projects.
*   **Environment Inconsistency:** It runs directly on your OS, which can lead to "works on my machine" issues when deploying to production.

> **Modern Update: Docker for PHP Development**
> **Docker** has become the standard for modern development. It packages your entire stack (PHP, MySQL, Nginx) into isolated containers. 
> *   **Consistency:** The exact environment runs locally, on staging, and in production.
> *   **Isolation:** You can run different PHP versions for different projects simultaneously.
> *   **Infrastructure as Code:** A `docker-compose.yml` file defines the setup, making it reproducible for the whole team.
> 
> **Beginner Recommendation:** Start with XAMPP to learn the basics of Apache and MySQL. Transition to Docker or tools like **Local** once you begin collaborating or deploying production applications.

### 2. Data Definition Language (DDL)

**DDL** is the subset of SQL used to define and modify the structure of database objects (tables, views, indexes). DDL statements are executed immediately and cannot be rolled back.

| DDL Command | Purpose |
| :--- | :--- |
| **`CREATE`** | Creates a new database, table, or view. |
| **`ALTER`** | Modifies an existing database object (e.g., adding a column). |
| **`DROP`** | Deletes an existing object and its data entirely. |
| **`TRUNCATE`** | Removes all data from a table but preserves its structure. |
| **`RENAME`** | Renames an existing database object. |
| **`CREATE INDEX`** | Creates an index on a table to improve query performance. |
| **`CREATE VIEW`** | Creates a virtual table based on a `SELECT` statement. |

#### DDL Code Examples

```sql
-- CREATE: Define a new table with constraints
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    hire_date DATE NOT NULL
);

-- ALTER: Add a new column to the existing table
ALTER TABLE employees
ADD salary DECIMAL(10, 2) NOT NULL;

-- TRUNCATE: Empty the table but keep the structure
TRUNCATE TABLE employees;

-- DROP: Delete the table and all its data
DROP TABLE employees;
```

> **Note:** `DROP` removes the table definition and data. `TRUNCATE` removes only the data, keeping the table structure intact.

### 3. SQL Constraints in Practice

Constraints enforce rules to ensure data accuracy and reliability.

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    -- FOREIGN KEY: Ensures customer_id exists in the customers table
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

### 4. Modern PHP Database Connection (PDO)

Historically, PHP used the `mysql_*` functions, which were removed in PHP 7.0 due to severe security vulnerabilities. Today, the standard is **PDO (PHP Data Objects)** or **MySQLi**.

**Why PDO?**
*   **Database Agnostic:** PDO works with over 12 different database systems.
*   **Security:** It supports **prepared statements**, which prevent SQL injection attacks.
*   **Error Handling:** It uses exceptions, making debugging easier.

> **Modern Security Best Practices:**
> *   **Never hardcode credentials:** Use environment variables (`getenv()`) or a `.env` file for database passwords.
> *   **Set Character Set:** Specify `charset=utf8mb4` in the DSN string to support full Unicode, including emojis.
> *   **Enable Exception Mode:** Set `PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION` to catch errors.
> *   **Use Prepared Statements:** Never concatenate user input directly into SQL queries.

#### Modern PDO Connection Example

```php
<?php
// 1. Read credentials securely from environment variables
$host = getenv('DB_HOST') ?: '127.0.0.1';
$db   = getenv('DB_NAME') ?: 'mydb';
$user = getenv('DB_USER') ?: 'root';
$pass = getenv('DB_PASS') ?: '';
$charset = 'utf8mb4';

// 2. Construct the Data Source Name (DSN)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

// 3. Set PDO options (Error handling, fetch mode)
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false, // Use real prepared statements
];

try {
    // 4. Create the PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);
    echo "Connected successfully to the database!";
    
    // Example of a safe prepared statement
    $stmt = $pdo->prepare('SELECT * FROM employees WHERE email = :email');
    $stmt->execute(['email' => 'john@example.com']);
    $user = $stmt->fetch();
    
} catch (\PDOException $e) {
    // 5. Handle connection errors gracefully
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}
?>
```

---

## C. Analogies and Use Cases

### The Blueprint vs. The Building Code
*   **DDL** is like the architectural blueprint and building code. It defines the rooms (`CREATE TABLE`), adds walls (`ALTER TABLE`), or demolishes the structure (`DROP TABLE`).
*   **Constraints** are the physical safety rails and load-bearing walls. They ensure the building doesn't collapse (e.g., a `NOT NULL` constraint ensures no empty rooms).

### The Secure Delivery Service (PDO)
Using `mysql_*` is like sending a postcard with your bank details written on the back—anyone can read it. Using **PDO with Prepared Statements** is like putting your message in a locked armored truck. The SQL and the data are kept separate, so even if the data contains malicious code (SQL injection), it cannot affect the database.

---

## D. Lesson Wrap-Up / FAQs

### Summary
In this lesson, we transitioned from theory to practice. We explored how to set up a local environment using **XAMPP** for beginners or **Docker** for production parity. We learned that **DDL** commands manage database structure and **constraints** enforce data integrity. Finally, we established that modern PHP applications must use **PDO with prepared statements** and environment variables to ensure secure and scalable database connections.

### Frequently Asked Questions (FAQs)

**Q: What is the difference between DROP and TRUNCATE?**
**A:** `DROP` deletes the entire table (structure and data). `TRUNCATE` deletes all data but preserves the table structure, indexes, and columns.

**Q: Can I undo a DDL command?**
**A:** Most DDL commands (like `DROP` and `TRUNCATE`) are irreversible and cause immediate data loss. For `ALTER`, it is crucial to back up the database before making changes.

**Q: Why is MySQLi considered less flexible than PDO?**
**A:** MySQLi only works with MySQL databases. PDO provides a unified API for 12+ different database systems, making it easier to migrate to PostgreSQL or SQLite without rewriting connection logic.

**Q: How do I handle passwords for users?**
**A:** Never store plain text passwords. Use PHP's `password_hash()` function with `PASSWORD_ARGON2ID` or `PASSWORD_DEFAULT` (Bcrypt) to securely hash passwords before storing them in the database.

---

## E. Guided Drills / Code Projects

### Exercise: Secure Database Setup

**Task:** Create a PHP script that connects to a MySQL database and retrieves data safely.

1.  **Create the Table (DDL):**
    ```sql
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(100) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```
2.  **Insert a User (PHP with Prepared Statement):**
    ```php
    <?php
    // Assume $pdo is your connection from the example above
    $email = 'student@example.com';
    $password = 'super_secret_password';
    
    // Hash the password securely
    $hash = password_hash($password, PASSWORD_ARGON2ID);
    
    $stmt = $pdo->prepare('INSERT INTO users (email, password_hash) VALUES (:email, :hash)');
    $stmt->execute(['email' => $email, 'hash' => $hash]);
    echo "User created successfully!";
    ?>
    ```
3.  **Retrieve the User:**
    ```php
    <?php
    $stmt = $pdo->prepare('SELECT * FROM users WHERE email = :email');
    $stmt->execute(['email' => 'student@example.com']);
    $user = $stmt->fetch();
    
    // Verify a password against the stored hash
    if ($user && password_verify('super_secret_password', $user['password_hash'])) {
        echo "Login successful!";
    }
    ?>
    ```

---

## F. Skill-Building Check

### Part 1: Fill in the Blanks
*Complete the statement with the correct term.*

1.  **XAMPP** is an open-source software package that provides a local web server environment (Apache, MariaDB, PHP, Perl).
2.  **MySQL** is a relational database management system (RDBMS) widely used for web applications.
3.  The main **DDL** commands are: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, and `RENAME`.
4.  To access the MySQL command line client, type the command `mysql -u root`.
5.  One of the ways to connect to a MySQL database using PHP is by using the **PDO** function or by using MySQLi.

### Part 2: Multiple Choice
*Identify the best answer.*

**1. Which DDL command is used to remove all data from a table but keep the table structure intact?**
a) DROP
b) DELETE
c) TRUNCATE
d) ALTER
> **Correct Answer: c.** `TRUNCATE` empties the table but preserves the structure.

**2. What is the primary advantage of using PDO over MySQLi?**
a) PDO is faster.
b) PDO supports multiple database systems (not just MySQL).
c) PDO does not require prepared statements.
d) PDO is built into older PHP versions.
> **Correct Answer: b.** PDO provides a uniform interface for 12+ different databases.

**3. Which PDO option ensures that database errors are thrown as exceptions?**
a) `PDO::ATTR_DEFAULT_FETCH_MODE`
b) `PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION`
c) `PDO::ATTR_EMULATE_PREPARES => false`
d) `PDO::ATTR_CASE`
> **Correct Answer: b.** This option enables exception-based error handling.

**4. In modern PHP development, where should database credentials be stored?**
a) Hardcoded in the PHP file.
b) In a public GitHub repository.
c) In environment variables or a `.env` file.
d) In a text file on the desktop.
> **Correct Answer: c.** Credentials should never be committed to source code. Environment variables are the standard.