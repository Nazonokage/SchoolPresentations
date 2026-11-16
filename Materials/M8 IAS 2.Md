# Software Development Security: SQL Injection

> **Course:** Information Assurance and Security  
> **Module:** 8 — Software Development Security: SQL Injection  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Welcome, students! Today, we are tackling one of the most critical web application vulnerabilities: **SQL Injection**. As a future IT developer or security professional, your systems must be immune to this attack. To do that, you must first know how to inject yourself. 

We will use **DVWA (Damn Vulnerable Web Application)** and **XAMPP** to perform this activity. You can find them in the resources for this class. 

**Learning Targets:**
By the end of this module, you will be able to:
1.  Understand what SQL Injection is.
2.  Understand how to defend against SQL Injection.

**Materials:**
*   Student Activity Sheet
*   Chrome (Browser)
*   XAMPP (Local Server)
*   DVWA (Vulnerable Web App)

![SQL Injection Concept](https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### What is SQL Injection?
**SQL Injection** is a code injection technique that might destroy your database. It is one of the most common web hacking techniques and involves the placement of malicious code in SQL statements via web page input.

Essentially, it is simply placing a SQL statement that will cut off the checking or `SELECT` part of a query and placing a true statement to access the database and security.

> **Pro Tip:** Keep a SQL injection cheat sheet handy. It will serve as a valuable reference when you are in the position of testing systems for SQL injections.

### Lab Setup Guide
To perform the hands-on activity, ensure you have XAMPP and DVWA installed.

1.  **Open XAMPP Control Panel:** Start both **Apache** and **MySQL**.
2.  **Open your browser:** Type in the address bar: `http://localhost/dvwa/`
3.  **Input your credentials:** Default username: `admin`, default password: `password`.
4.  **Set Security Level:** Click the DVWA Security button and set the security level to **low**, then press submit.
5.  **Navigate to SQL Injection:** Click the **SQL Injection** button from the choices on the left.
6.  **View Source:** You can click on the "View Source" button in the bottom right corner to show the codes used in submitting the User ID. 

### SQL Injection Trials

**Trial 1: Trying out a cut-off query**
*   **Input:** `1'`
*   **What Happened:** The query made an error. 
*   **Explanation:** The single quote (`'`) cuts off the `$query` in the SELECT statement, allowing you to place your own query.
*   *Source Code Context:* `$query = "SELECT first_name, last_name FROM users WHERE user_id = '$id';"`

**Trial 2: Commenting out the rest**
*   **Input:** `1' OR 1 = 1#`
*   **What Happened:** The query selects the previous query with the condition `1=1` (which is true), showing all user records.
*   **Explanation:** The `#` part of the SQL comments out everything on the right of the query. This means the last single quote is no longer queried. 
*   *Query Context:* `SELECT first_name, last_name FROM users WHERE user_id = '1' OR 1=1#';`

**Trial 3: Getting the table name where the users are located**
*   **Input:** `1' OR 1=1 UNION SELECT NULL, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES#`
*   **What Happened:** The query will show all the table names of the database, revealing the structure.
*   **Explanation:** The `UNION SELECT` statement combines the previous query with another query showing table names. Most importantly, we now know there is a table named `users`.

**Trial 4: Getting the column names from the TABLE users**
*   **Input:** `1' UNION SELECT 1, COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='users'#`
*   **What Happened:** This query lists all columns for the table `users`.
*   **Explanation:** We can now see the names of the columns we need, specifically `user` and `password`.

**Trial 5: Getting the users and their passwords from the TABLE users**
*   **Input:** `1' OR 1=1 UNION SELECT user, password from users#`
*   **What Happened:** This dumps all usernames and password hashes.
*   **Explanation:** In this case, the "surname" in the output are the **Hashed Passwords**, meaning they are still encrypted. We still have to decrypt it.

> **Bonus Activity: Decrypting the Hash**
> 1. Copy the hash code from the `surname` output (e.g., for the user `gordonb`).
> 2. Open the website: `md5online.org`.
> 3. Click decrypt on the top menu.
> 4. Paste the MD5 hash code and press decrypt. 
> *(This will reveal the plaintext password for that user).*

### Exercise 2: Defending Against SQL Injection

**1. Medium Difficulty Security**
*   **What changed:** The code uses `str_replace` to reduce the input of the attacker (removing `'`).
*   **Weakness:** It is still hackable by intercepting the submit command and changing the query inside, using a tool called **Burp Suite**. 

**2. High Difficulty Security**
*   **What changed:** The `$query` now includes `LIMIT 1`. 
*   **Impact:** This limits the results returned to one, making it harder for conventional scanning tools like `sqlmap` to detect patterns. However, manual injections can still bypass this.

**3. Impossible Difficulty Security**
*   **What changed:** It uses PHP Data Objects (PDO) technology to clear boundaries between code and data, effectively defending against SQL injection. It also adds an Anti-CSRF token mechanism.
*   **Result:** The injection attempts no longer work because the query results are limited, and the data is properly separated from the SQL code.

| Security Level | Defense Mechanism | Still Vulnerable? |
| :--- | :--- | :--- |
| **Low** | None. | Yes, easily exploitable. |
| **Medium** | `str_replace` to remove single quotes. | Yes, via Burp Suite interception. |
| **High** | `LIMIT 1` to limit results. | Yes, to manual advanced injections. |
| **Impossible** | PDO (Object-Oriented Data Access), Anti-CSRF Tokens. | No, robustly protected. |

---

## C. Analogies and Use Cases

### The "Fake ID" Analogy
Think of an SQL query as a bouncer asking a bouncer asking "What is your name?"
*   **Normal Input:** "John" -> The bouncer checks the list and lets John in.
*   **SQL Injection Input:** "John' OR 1=1#" -> The bouncer reads it as "Let John in, OR let everyone in because 1=1 is true, and ignore the rest of my instructions (#)". The attacker tricks the bouncer into letting everyone (the whole database) out.

### Real-World Use Case: The Retail Data Breach
Imagine a retail website that uses SQL to check customer login credentials. An attacker inputs `admin' --` into the username field. The SQL query becomes `SELECT * FROM users WHERE username = 'admin' --' AND password = '...'`. The `--` comments out the password check, allowing the attacker to log in as the admin without knowing the password. This is a classic example of SQL Injection leading to unauthorized access.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **SQL Injection** is a serious threat that can destroy databases and leak sensitive information.
*   It occurs when user input is incorrectly filtered for SQL statements.
*   Defending against SQL requires **Input Validation**, **Parameterized Queries**, and using modern **Frameworks**.
*   The "Impossible" security level in DVWA demonstrates how robust coding practices (like PDO and Anti-CSRF tokens) can completely mitigate this risk.

### Frequently Asked Questions
**1. Are these SQL injections still used?**
**A:** Yes, a lot of old systems are still used by some companies. SQL injections can still be very effective against them if they haven't been updated with modern security practices.

**2. Are there any other solutions to protecting against SQL injection?**
**A:** Yes, now we use frameworks that make our programming lives easier. These frameworks already include protection against SQL injection by default, provided you use their built-in database abstraction layers correctly.

**3. What is the primary takeaway for a developer?**
**A:** Never trust user input. Always sanitize and validate input, and use parameterized queries or prepared statements instead of concatenating strings to build SQL queries.

---

## E. Guided Drills / Code Projects

### Project Group Update: SQL Injection Defense Plan
**Project Overview:** 
With the added knowledge from this module, your group must draft a security recommendation for your capstone project based on SQL Injection vulnerabilities. 

**Activity Guidelines:**
*   **Format:** Individual or Group work (as instructed).
*   **Objective:** Write a draft of your SQL Injection defense strategy for your project's database.
*   **Submission:** Add this to your project documentation.

**Draft your plan below:**

> *Example Draft:*
> **SQL Injection Defense Plan for [Project Name]**
> *   **Defense 1: Prepared Statements.** We will use PDO (PHP Data Objects) with prepared statements for all database queries. This ensures that SQL code and user input are separated, preventing the injection of malicious commands.
> *   **Defense 2: Input Validation.** All user inputs (login forms, search bars, contact forms) will be validated on the server side. We will strictly define the expected data type (e.g., integers for IDs, alphanumeric for names).
> *   **Defense 3: Testing.** Before deployment, we will test our application using tools like Burp Suite to intercept requests and attempt basic injection payloads (e.g., `' OR 1=1#`) to ensure our defenses are working.

---

## F. Skill-Building Check

### Check for Understanding (25 mins Quiz)

**Let's check your understanding of SQL Injection. As a future IT professional:**

**1. Why do we need to be protected against SQL injection?**
*Guidance:* We need protection because SQL injection can lead to unauthorized access to sensitive data (like passwords and personal information), data corruption, database destruction, and even complete system compromise. It compromises the Confidentiality, Integrity, and Availability (CIA Triad) of the organization's data.

**2. How would we do it if we are a developer?**
*Guidance:* As a developer, I would use **Parameterized Queries** (Prepared Statements) which are built into modern frameworks. I would also implement strict **Input Validation** (whitelisting acceptable characters) and ensure that error messages do not reveal database structure information to potential attackers.

**3. How would we do it if we are a tester?**
*Guidance:* As a tester, I would use automated vulnerability scanners (like SQLMap) and manual testing techniques (like Burp Suite) to attempt injection attacks on forms, URL parameters, and cookies. I would test for error-based, union-based, and blind SQL injection vulnerabilities across all entry points.

**4. What is the purpose of the `#` symbol in the injection `1' OR 1=1#`?**
**Correct Answer:** The `#` symbol is used to comment out the rest of the SQL query. This prevents the database from throwing a syntax error due to the trailing single quote left over from the original query structure.