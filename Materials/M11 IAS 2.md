# Database Security and Integrity: DB Access Controls

> **Course:** Information Assurance and Security  
> **Module:** 11 — Database Security and Integrity: DB Access Controls  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Hello students! Today, we are enhancing our knowledge with **Database (DB) Access Controls**. This module is about going in-depth into changing and configuring your database access controls for your capstone project.

**Quick Review:**
Before we dive into configuration, let's recall what database access controls are. Essentially, they are the rules and privileges that determine what actions a specific user can perform on the database. 

**Learning Targets:**
By the end of this module, you will be able to:
1.  Understand Database Access Controls.
2.  Configure your DB access controls.

> **Goal:** By the end of this module, you should have updated your privileges in your database for your project(s).

![Database Access Control](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### Locating Database Access Controls
Let's start by locating where you can manage the access controls in your database. Using **MySQL** as our example (since it is the most common), you can find the privileges of all **USERS** in the **User Accounts Tab** in your localhost. 

*   **Best Practice:** It is ideal to have passwords for your database users, especially the `root` username. This ensures only authorized users can access your databases.
*   **Creating Users:** You are free to create your own user accounts in localhost MySQL. Ideally, it is recommended to have **multiple users with different privileges**. 

**Example Role Definitions:**
*   **Project Manager:** Can have all privileges except ADMINISTRATION privileges.
*   **Senior Developer:** Has all DATA query privileges.
*   **Junior Developer:** Has only SELECT from DATA Query privilege.
*   **Designers:** Have some privileges from DATA and STRUCTURE.

### MySQL Privilege Groups
Understanding the different privilege groups is crucial for assigning the right access levels.

| Privilege Group | Scope | Common Privileges | Assigned To |
| :--- | :--- | :--- | :--- |
| **Data** | Rows within database tables. | `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `FILE` | Developers who need to work with content but shouldn't alter the table design. |
| **Structure** | The entire structure of database tables (Columns). | `CREATE`, `ALTER`, `INDEX`, `DROP`, `CREATE VIEW`, `TRIGGER` | Project Managers and Designers who control the database design. |
| **Administration** | User accounts and the whole MySQL server. | `GRANT`, `SUPER`, `PROCESS`, `RELOAD`, `SHUTDOWN`, `CREATE USER` | Software Architects, Database Administrators (DBAs), and some Project Managers. |
| **Resource Limits** | Controls the volume of operations. | `MAX QUERIES PER HOUR`, `MAX UPDATES PER HOUR`, `MAX CONNECTIONS PER HOUR` | Used to prevent buffer overflows and system overload. |

### Sample User Access Controls in a Project Database
Here is a sample of how User Access Controls might be set up for a project database named `Project`:

| User Name | Host Name | Password | Global Privileges |
| :--- | :--- | :--- | :--- |
| `Designer1` | `%` | Yes | SELECT, INSERT, UPDATE, DELETE, FILE, CREATE TEMPORARY TABLES, CREATE VIEW, EVENT, TRIGGER, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EXECUTE |
| `Developer1` | `%` | Yes | SELECT, INSERT, UPDATE, DELETE, FILE |
| `Tester` | `%` | Yes | SELECT, INSERT, UPDATE, DELETE, FILE |
| `projectmanager1` | `%` | Yes | SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, FILE, INDEX, ALTER, CREATE TEMPORARY TABLES, CREATE VIEW, EVENT, TRIGGER, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EXECUTE |
| `root` | `localhost` | No | ALL PRIVILEGES |

> **Note:** The `pma` user (phpMyAdmin) typically has a `USAGE` privilege, meaning it can connect to the database but has no specific permissions unless explicitly granted.

---

## C. Analogies and Use Cases

### The "Restaurant Kitchen" Analogy
Think of your database as a high-end restaurant kitchen.
*   **Root / Admin (Owner):** Has the keys to the building, hires and fires staff, and can change the entire menu.
*   **Project Manager (Head Chef):** Can create new recipes, design the menu layout (Structure), and cook the food (Data). However, they cannot hire or fire staff (Administration).
*   **Senior Developer (Line Cook):** Can cook any dish on the menu, modify recipes (Data), but cannot redesign the kitchen or change the menu structure.
*   **Junior Developer (Prep Cook):** Can only read the recipes (`SELECT`) to prepare ingredients. They cannot change the recipes or invent new dishes.
*   **Resource Limits (Kitchen Timers):** The kitchen manager limits how many dishes can be cooked per hour to ensure the kitchen doesn't get overwhelmed (buffer overflow). 

### Real-World Use Case: A University Grading System
A university uses a database to store student grades.
*   **System Admin (Root):** Configures the database, sets up server backups, and creates user accounts for the semester.
*   **Registrar (Project Manager):** Has the ability to create new tables for a new semester, modify the table structure to add new grading criteria, and view all student data.
*   **Teacher (Developer):** Can `SELECT` (view) student names, and `UPDATE` (edit) grades for the specific subjects they teach. They cannot drop the table or change the schema.
*   **Student (Tester/Viewer):** Can only `SELECT` (view) their own grades. They cannot edit them.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **Database Access Controls** are essential for the Principle of Least Privilege—giving users only the access they need to do their job.
*   **Data Privileges** control row-level operations (`SELECT`, `INSERT`, `UPDATE`, `DELETE`).
*   **Structure Privileges** control table-level operations (`CREATE`, `ALTER`, `DROP`).
*   **Administration Privileges** control the server and user accounts.
*   **Resource Limits** prevent a single user from overwhelming the database with too many queries or updates.
*   Always assign strong passwords to database users, especially `root`.

### Frequently Asked Questions
**1. Are there other user access controls for other types of databases?**
**A:** Yes. The concept of User Access Controls exists in all database systems, including **SQL, MariaDB, PostgreSQL, Oracle, and even NoSQL databases** like MongoDB. While the specific names of the privileges might differ, the core concept of limiting access based on roles remains the same. 

**2. What happens if a Junior Developer tries to run a DELETE query?**
**A:** The database will reject the query and return a permission denied error. The Junior Developer only has `SELECT` privileges, so they cannot delete or modify data.

**3. Why is it dangerous to let the `root` user have a blank password?**
**A:** A blank password means anyone who can access the network or local machine can log in as the `root` user. The `root` user has `ALL PRIVILEGES`, meaning an attacker could instantly drop the entire database, steal all data, or create malicious backdoor accounts.

**4. What is the purpose of the Resource Limits privilege?**
**A:** Resource limits are used to prevent performance degradation and Denial of Service (DoS) conditions. By setting a `MAX QUERIES PER HOUR`, you prevent a runaway script or a malicious user from consuming all server resources and crashing the database.

---

## E. Guided Drills / Code Projects

### Solo Project Update: Configuring User Access Controls
**Project Overview:** 
For Module 11, you will expand your ongoing project by creating and configuring **User Access Controls** for your database. 

> *Note: This was originally designed as a group activity. We are adapting it as a **solo activity**. You will act as the sole database administrator for this assignment.*

**Project Guidelines:**
*   **Format:** Individual work.
*   **Objective:** Create a set of User Access Controls for your project's database. Include your teacher as a user with full access to the database (for grading purposes).
*   **Submission:** Include a screenshot of your User Accounts tab in your project documentation.

**Step-by-Step Deliverable (SQL Example):**
Use the following SQL commands as a guide to create your users and assign privileges. *Replace the placeholder names with your specific roles.*

```sql
-- 1. Create the users
CREATE USER 'projectmanager1'@'localhost' IDENTIFIED BY 'StrongPassword123!';
CREATE USER 'developer1'@'localhost' IDENTIFIED BY 'SecurePass456!';
CREATE USER 'tester1'@'localhost' IDENTIFIED BY 'TestPass789!';

-- 2. Grant Data & Structure privileges to Project Manager
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, INDEX ON Project.* TO 'projectmanager1'@'localhost';

-- 3. Grant Data privileges to Developer
GRANT SELECT, INSERT, UPDATE, DELETE ON Project.* TO 'developer1'@'localhost';

-- 4. Grant only SELECT privileges to Tester
GRANT SELECT ON Project.* TO 'tester1'@'localhost';

-- 5. Apply the changes
FLUSH PRIVILEGES;
```

**Draft your own User Access Controls below:**

| User Name | Role / Description | Assigned Privileges | Host Name |
| :--- | :--- | :--- | :--- |
| `projectmanager1` | Manager of the project | SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER... | `localhost` |
| `developer1` | Senior Developer | SELECT, INSERT, UPDATE, DELETE | `localhost` |
| `tester1` | QA Tester | SELECT | `localhost` |
| `[Your Name]` | Lead Consultant/Teacher | ALL PRIVILEGES | `localhost` |

---

## F. Skill-Building Check

### Check for Understanding (25 mins Quiz)

*Answer the following questions with the best of your abilities.*

**1. What is the importance of having User Access Controls for Database Security?**
*Guidance:* User Access Controls are crucial because they enforce the **Principle of Least Privilege**. They ensure that users only have the permissions necessary to perform their specific job functions. This prevents accidental or malicious data loss (e.g., a junior developer dropping a table) and limits the damage if an account is compromised. It also protects the integrity and confidentiality of the data.

**2. Multiple Choice: Which privilege group is responsible for row-level operations like selecting and updating data?**
A. Structure
B. Administration
C. Data
D. Resource Limits
**Correct Answer: C** (Data privileges manage rows, whereas Structure manages the table schema, and Administration manages users/servers).

**3. Multiple Choice: What is the primary purpose of setting a MAX QUERIES PER HOUR resource limit?**
A. To make the database faster.
B. To prevent buffer overflows and system overload from excessive queries.
C. To charge users for their database usage.
D. To ensure all users get equal time.
**Correct Answer: B** (Resource limits act as a safety valve to prevent a single user or script from consuming all server resources).

**4. True or False: A Junior Developer should be given ALL PRIVILEGES so they can learn how to manage the database.**
**Correct Answer: False** (Junior developers should only be given `SELECT` privileges according to the module. Giving them ALL PRIVILEGES violates the Principle of Least Privilege and poses a major security risk).

**5. Short Answer: If a Designer needs to add a new column to a table, which privilege group must they have access to?**
**Correct Answer:** The **Structure** privilege group. Actions like `ALTER`, `CREATE`, and `INDEX` fall under the Structure group, which controls the columns and relationships of the database tables.