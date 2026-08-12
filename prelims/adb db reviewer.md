# Complete Summary: MySQL, WAMP, PHP & Database Management

## 📚 **Module Overview**

This comprehensive learning path covers everything from setting up your local development environment to mastering advanced database operations with MySQL and PHP.

---

## 🖥️ **Part 1: Environment Setup (WAMP Server)**

### **What is WAMP?**
WAMP = **Windows** + **Apache** + **MySQL** + **PHP**
- A complete local server stack for Windows development
- Provides everything needed to run PHP applications and MySQL databases locally

### **Installation Steps:**
1. Download WAMP from [wampserver.aviatechno.net](http://wampserver.aviatechno.net)
2. Run the installer and choose installation folder (default: `C:\wamp64\`)
3. Launch WAMP and wait for the icon to turn **green** (indicates all services are running)
4. Access via `http://localhost/`

### **Key Directories:**
```
C:\wamp64\www\          → Place your PHP files here
C:\wamp64\bin\mysql\    → MySQL binaries
C:\wamp64\logs\         → Error logs for troubleshooting
```

### **Important WAMP Shortcuts:**
- **Restart All Services**: Right-click tray icon → Restart All Services
- **phpMyAdmin**: Click tray icon → phpMyAdmin (visual database management)
- **Localhost**: Click tray icon → localhost (opens `http://localhost/`)

---

## 🗄️ **Part 2: MySQL Fundamentals**

### **What is SQL?**
**Structured Query Language** - the standard language for relational databases.

**Three Main Sub-languages:**

| Category | Commands | Purpose |
|----------|----------|---------|
| **DDL** (Data Definition) | CREATE, ALTER, DROP | Defines database structure |
| **DML** (Data Manipulation) | INSERT, UPDATE, DELETE | Manages data |
| **DCL** (Data Control) | GRANT, REVOKE, DENY | Controls permissions |

### **MySQL Terminal Commands:**

```sql
-- Connect to MySQL
mysql -u root -p

-- Show databases
SHOW DATABASES;

-- Use a database
USE database_name;

-- Show tables
SHOW TABLES;

-- Describe a table
DESCRIBE table_name;

-- Exit
EXIT;
```

### **MySQL Server Startup (via Command Line):**
```cmd
cd C:\wamp64\bin\mysql\mysql8.4.7\bin
.\mysqld.exe --console  (Window 1 - keep running)
.\mysql.exe -u root -p  (Window 2 - run queries)
```

---

## 📊 **Part 3: Data Definition Language (DDL)**

### **Creating Databases:**
```sql
CREATE DATABASE dbLending;
USE dbLending;
```

### **Creating Tables:**
```sql
CREATE TABLE CUSTOMERS (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    PRIMARY KEY (CustomerID)
);

CREATE TABLE ORDERS (
    OrderID INT AUTO_INCREMENT,
    OrderDate DATE NOT NULL,
    Amount DECIMAL(10,2) NOT NULL,
    CustomerID INT,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES CUSTOMERS(CustomerID)
);
```

### **Key Constraints:**

| Constraint | Purpose |
|------------|---------|
| **PRIMARY KEY** | Uniquely identifies each row |
| **FOREIGN KEY** | Links to primary key in another table |
| **NOT NULL** | Column cannot be empty |
| **UNIQUE** | No duplicate values allowed |
| **DEFAULT** | Provides fallback value |
| **CHECK** | Values must satisfy condition |

### **Altering Tables:**
```sql
-- Add column
ALTER TABLE CUSTOMERS ADD Phone VARCHAR(20);

-- Modify column type
ALTER TABLE CUSTOMERS MODIFY Phone VARCHAR(30);

-- Drop column
ALTER TABLE CUSTOMERS DROP COLUMN Phone;

-- Drop table (DANGER - irreversible!)
DROP TABLE ORDERS;
```

---

## ✏️ **Part 4: Data Manipulation Language (DML)**

### **INSERT - Adding Data:**
```sql
-- Insert specific columns
INSERT INTO CUSTOMERS (FirstName, LastName, Email)
VALUES ('Juan', 'Dela Cruz', 'juan@email.com');

-- Insert all columns (values must match order)
INSERT INTO CUST VALUES (150, 'Soriano', 'Ken', '', 8221.00, 7500.00);
```

### **SELECT - Reading Data:**
```sql
-- Get all columns
SELECT * FROM CUSTOMERS;

-- Get specific columns
SELECT FirstName, LastName FROM CUSTOMERS;

-- Filter with WHERE
SELECT * FROM CUSTOMERS WHERE CustomerID = 1;

-- Pattern matching
SELECT * FROM CUST WHERE Branch LIKE '%up%';

-- Range queries
SELECT CustID, CONCAT(FName, ' ', LName) AS FullName, Balance 
FROM CUST 
WHERE Balance BETWEEN 5000 AND 8000;
```

### **UPDATE - Modifying Data:**
```sql
UPDATE CUSTOMERS 
SET Email = 'newemail@example.com' 
WHERE CustomerID = 1;

UPDATE CUST 
SET Branch = 'Dagupan City' 
WHERE CustID = 142;
```
⚠️ **Warning:** Always use `WHERE` clause! Without it, ALL rows are updated.

### **DELETE - Removing Data:**
```sql
DELETE FROM CUSTOMERS WHERE CustomerID = 3;

DELETE FROM CUST WHERE Branch LIKE 'A%A';
```
⚠️ **Warning:** Always use `WHERE` clause! Without it, ALL rows are deleted.

---

## 🔗 **Part 5: SQL JOINs**

### **Why JOIN?**
- Combines data from multiple tables
- Eliminates data duplication
- Enables complex queries across related data

### **JOIN Types with Venn Diagrams:**

| JOIN Type | Description | Use Case |
|-----------|-------------|----------|
| **INNER JOIN** | Only matching rows | When you need data from both tables |
| **LEFT JOIN** | All from left + matches | When you need all records from main table |
| **RIGHT JOIN** | All from right + matches | Opposite of LEFT JOIN |
| **FULL OUTER JOIN** | All rows from both tables | When you need everything |

### **INNER JOIN Example:**
```sql
SELECT customers.name, orders.date, orders.total_amount
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id;
```

### **JOIN with PHP:**
```php
$sql = "SELECT Users.name, Orders.order_date, Orders.total_amount
        FROM Users
        INNER JOIN Orders
        ON Users.user_id = Orders.user_id";

$result = mysqli_query($conn, $sql);
while ($row = mysqli_fetch_assoc($result)) {
    echo "Name: " . $row["name"] . "<br>";
}
```

---

## 🔐 **Part 6: Data Control Language (DCL)**

### **GRANT - Giving Permissions:**
```sql
-- Grant SELECT and INSERT privileges
GRANT SELECT, INSERT ON employees TO 'user1'@'localhost';

-- Grant ALL privileges
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';
```

### **REVOKE - Removing Permissions:**
```sql
-- Remove SELECT and INSERT
REVOKE SELECT, INSERT ON employees FROM 'user1'@'localhost';

-- Remove ALL privileges
REVOKE ALL PRIVILEGES ON *.* FROM 'user1'@'localhost';
```

### **DENY - Explicitly Forbidding:**
```sql
-- Deny DELETE (overrides any GRANT)
DENY DELETE ON employees TO 'user1'@'localhost';

-- Check current grants
SHOW GRANTS FOR 'user1'@'localhost';
```

### **DCL in PHP:**
```php
$sql = "GRANT SELECT, INSERT ON employees TO 'user1'@'localhost'";
mysqli_query($conn, $sql);
```

---

## 🐘 **Part 7: CRUD Operations in PHP**

### **The 4 CRUD Operations:**

| Operation | SQL Command | PHP Implementation |
|-----------|-------------|-------------------|
| **Create** | INSERT | `mysqli_query($conn, $sql)` |
| **Read** | SELECT | `mysqli_fetch_assoc($result)` |
| **Update** | UPDATE | `mysqli_query($conn, $sql)` |
| **Delete** | DELETE | `mysqli_query($conn, $sql)` |

### **Database Connection (mysqli):**
```php
$conn = mysqli_connect("localhost", "root", "", "database_name");
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
```

### **Secure Connection (PDO):**
```php
$pdo = new PDO("mysql:host=localhost;dbname=database_name", "root", "");
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
```

### **CREATE (INSERT):**
```php
// Simple (insecure - SQL injection risk)
$sql = "INSERT INTO users (name, email) VALUES ('$name', '$email')";

// Secure (prepared statement)
$sql = "INSERT INTO users (name, email) VALUES (:name, :email)";
$stmt = $pdo->prepare($sql);
$stmt->execute([':name' => $name, ':email' => $email]);
```

### **READ (SELECT):**
```php
$sql = "SELECT * FROM users";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    while ($row = mysqli_fetch_assoc($result)) {
        echo "ID: " . $row["id"] . " - Name: " . $row["name"] . "<br>";
    }
}
```

### **UPDATE:**
```php
$sql = "UPDATE users SET name='$name' WHERE id=$id";
mysqli_query($conn, $sql);
```

### **DELETE:**
```php
$sql = "DELETE FROM users WHERE id=$id";
mysqli_query($conn, $sql);
```

### **Checking Results:**
```php
if (mysqli_affected_rows($conn) > 0) {
    echo "Operation successful!";
} else {
    echo "Error: " . mysqli_error($conn);
}
```

---

## 💾 **Part 8: Backup & Recovery**

### **Why Backup Matters:**
1. **Data Protection** - Guards against hardware failure, human error
2. **Business Continuity** - Minimizes downtime
3. **Disaster Recovery** - Enables recovery from catastrophic events
4. **Compliance** - Meets regulatory requirements
5. **Peace of Mind** - System reliability

### **Backup Methods:**

#### **1. PHP Backup using mysqli:**
```php
function backupDatabase($connection, $database) {
    $backupFile = "backup_" . date("Ymd_His") . ".sql";
    
    // Get tables
    $result = mysqli_query($connection, "SHOW TABLES");
    
    // Export structure and data
    foreach ($tables as $table) {
        $sql = "SHOW CREATE TABLE $table";
        $result = mysqli_query($connection, $sql);
        fwrite($handle, $row[1] . ";\n\n");
        
        $sql = "SELECT * FROM $table";
        $result = mysqli_query($connection, $sql);
        while ($row = mysqli_fetch_assoc($result)) {
            $values = implode("\", \"", array_map("addslashes", $row));
            fwrite($handle, "INSERT INTO $table VALUES (\"$values\");\n");
        }
    }
}
```

#### **2. Command-line Backup (mysqldump):**
```bash
mysqldump --host=localhost --user=root --password= database_name > backup.sql
```

#### **3. Recovery using mysql:**
```bash
mysql --host=localhost --user=root --password= database_name < backup.sql
```

### **PHP Recovery Script:**
```php
function recoverDatabase($connection, $database, $backupFile) {
    $sql = file_get_contents($backupFile);
    $queries = explode(";\n", $sql);
    
    foreach ($queries as $query) {
        $query = trim($query);
        if (!empty($query)) {
            mysqli_query($connection, $query);
        }
    }
    echo "Database recovery successful.";
}
```

### **Backup Best Practices:**
- Schedule regular backups
- Keep backups **off-site**
- Test your backups by performing **test restores**
- Define **Recovery Point Objective (RPO)**
- Use **automated** backup scripts

---

## 🔧 **Part 9: Common Troubleshooting**

### **WAMP Issues:**

| Problem | Solution |
|---------|----------|
| **Orange icon** | Port 80/443 in use; change Apache port in httpd.conf |
| **Red icon** | Check error logs in `wamp64/logs/` |
| **MySQL won't start** | Check if port 3306 is in use |
| **"Access denied"** | Check your username/password (default: root / no password) |

### **PHP/MySQL Errors:**
```php
// Always check for errors
if (!mysqli_query($conn, $sql)) {
    echo "Error: " . mysqli_error($conn);
}

// Check affected rows
if (mysqli_affected_rows($conn) > 0) {
    echo "Operation successful!";
}
```

---

## 📝 **Key Takeaways**

### **Database Design Principles:**
1. **Normalize** your data to avoid duplication
2. Use **Primary Keys** to uniquely identify rows
3. Use **Foreign Keys** to maintain referential integrity
4. Always define **appropriate data types**
5. Use **constraints** to enforce data rules

### **Security Best Practices:**
1. Never store passwords in plain text (use hashing)
2. Always use **prepared statements** to prevent SQL injection
3. Use **GRANT/REVOKE** to control access
4. Validate all user input
5. Use **htmlspecialchars()** to prevent XSS

### **PHP Best Practices:**
1. Use **PDO** or **mysqli** for database connections
2. Always check for errors
3. Close database connections when done
4. Store database credentials in a separate config file
5. Use **modular code** (separate connection logic)

---

## 🎓 **Module Completion Checklist**

- [ ] WAMP installed and running (green icon)
- [ ] Can access phpMyAdmin
- [ ] Know basic MySQL terminal commands
- [ ] Can CREATE databases and tables
- [ ] Understand PRIMARY KEY and FOREIGN KEY
- [ ] Can INSERT, SELECT, UPDATE, DELETE data
- [ ] Can perform INNER JOIN queries
- [ ] Can GRANT and REVOKE permissions
- [ ] Can connect PHP to MySQL (mysqli/PDO)
- [ ] Can perform CRUD operations in PHP
- [ ] Can create database backups
- [ ] Can restore from backups
- [ ] Understand security best practices

---

> **💡 Final Tip:** Practice is the key to mastery. Set up a local environment, create sample databases, and build small projects to reinforce these concepts. The journey from beginner to proficient database developer is built on consistent, hands-on practice!