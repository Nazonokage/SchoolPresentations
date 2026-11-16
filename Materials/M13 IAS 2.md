# Database Security and Integrity: Authorization, Auditing, and Control

> **Course:** Information Assurance and Security  
> **Module:** 13 — Database Security and Integrity: Authorization, Auditing and Control  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Hello students! Today, we are adding crucial topics to improve your knowledge of database security. This will be helpful for your capstone or projects, but overall, this is what is used in organizations with massive databases that adhere to international standards like ISO.

**Quick Review:**
Before we dive into today's topic, can you recall what a **DB Access Policy** is? 
*   *Hint:* It is the set of rules and regulations determining how a database should be accessed, updated, edited, or changed. 

**Learning Targets:**
By the end of this module, you will be able to:
1.  Understand the importance of having **Authorization** in databases.
2.  Understand the importance of **Auditing** a database.

![Database Security Concept](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### Authorization and Control
**Authorization** is a privilege provided by the Database Administrator (DBA). Users—whether developers, clients, or other stakeholders—can only view the contents they are authorized to access. The rest of the database is out of bounds to them.

> **Important Note:** Database Authorization differs from database to database, and from company to company. It depends on whether the database was purposely designed for them or if it is a general-use database like MySQL. In this module, we will explore the general authorization concepts of a database.

#### Levels of Database Authorization
Authorization has multiple levels. Below is an example of a database management system authorization table for a company that develops systems.

| Authorization Level | Capabilities | Example Users |
| :--- | :--- | :--- |
| **Database Administrators** | Have full control of the system. | Highest administrators in the department where databases are managed. (e.g., IT Department Chief, IT Security Chief) |
| **Database Managers** | Only manage the databases they created or were given. | Project Managers of a development team. |
| **Database Designers** | With permission given by the managers, they are provided some capabilities, but it depends on the managers or administrators. | Lower-level positions in a company that have access to the database, but cannot do anything without explicit authorization from positions above. |
| **Database Viewers** | Only able to view the system. | Members of the company with sufficient access to view the system (e.g., HR Supervisor, Finance Officer, Stockholders, Auditors). |

#### Mapping to Key Personnel in Software Development
During the development of a system, specific key personnel are assigned these authorization levels within the **Database Management System (DBMS)** (e.g., MySQL, Microsoft SQL, PostgreSQL), *not* the actual database used by the developed system.

*   **Project Managers** → Given the **Database Managers** role.
*   **Designers** → Given the **Database Designers** role.
*   **Coders** → Given the **Database Designers** role, but with **limited access**.
*   **Testers** → Given the **Database Designers** role, but with **limited access**.
*   **Potential Users** → Given the **Database Viewers** role.

> **Note:** These key personnel are limited to systems development. In a broader organizational context, "Key Personnel" involves a lot more people.

### Database Auditing
The main reason organizations perform **database auditing** is to track the use of database records and the authority of those who have access to them. 

*   **What can be tracked?** It is possible to keep track of every action in a database, including:
    *   Which database object or data record was accessed.
    *   Who performed the action.
    *   When it occurred.

#### Importance of Auditing
Databases, after a few years of use, undergo many changes: change of positions, change of access, new hires, and new training. This means there is a high chance that someone will have access to the database that is not supposed to be there. Regular auditing catches these discrepancies.

**1. Maintain Data Quality**
Whether you run a tiny business or a giant corporation, precise audience targeting builds trust with customers. Success depends on having accurate and up-to-date information about your customers. Auditing ensures the data remains reliable.

**2. Compliance with Data Privacy & Protection Regulations**
Publishers and advertisers must keep data privacy compliance in mind in today's digital world. As a result of database audits, you'll be able to take advantage of new business prospects knowing that your organization is adhering to regulations.

**3. Reducing Security Risks**
It is impossible to exaggerate the importance of security to user trust and customer relationships. Regular database audits mean you're less likely to be attacked or caught off guard by a security breach.

#### Who performs Database Auditing?
Usually, it is performed by **IT Security Officers** and **Database Administrators**. Sometimes, when there are a lot of changes in the database, a fresh series of database authorizations is created, adhering to the changes and adjusting the access of each user.

#### How to perform Database Auditing?
Database auditing involves checking each and every part of the databases, and who has access to them. If you have hundreds of databases, it will take some time to check all of the authorization levels in those databases and the people who were given those authorizations.

---

## C. Analogies and Use Cases

### The "Library" Analogy
Think of a database as a massive library.
*   **Database Administrator (Head Librarian):** Has the keys to every room, decides which books to buy, and hires staff.
*   **Database Manager (Section Head):** Manages only the specific section they are assigned to (e.g., History). They can add books to their section but can't access the Rare Books room.
*   **Database Designer (Shelf Stocker):** Can arrange books on shelves and add new ones, but only if the Section Head gives them permission. They cannot restructure the library layout.
*   **Database Viewer (Library Patron):** Can read the books on the shelf, but cannot take them home, change their order, or add new ones.
*   **Auditing (Library Inventory):** The Head Librarian periodically checks the catalog to ensure no unauthorized person has a key to the rare books room and that all books are accounted for.

### Real-World Use Case: An E-Commerce Platform
An online store uses a database to store customer orders, payment info, and inventory.
*   **Without Authorization:** A temporary holiday hire has the same database access as the Lead Developer. They could accidentally (or maliciously) drop a table containing customer orders.
*   **With Authorization:** The temporary hire is given a **Viewer** role. They can look up orders to help customers, but they cannot modify the database structure or delete records.
*   **Auditing:** A year later, an audit reveals that a former employee still has an active admin account. The auditor immediately flags this, preventing a potential major data breach.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **Authorization** is the process of granting specific privileges to users based on their role (Administrator, Manager, Designer, Viewer).
*   **Database Auditing** tracks who accessed what data and when, providing accountability.
*   Auditing is crucial for **maintaining data quality**, **ensuring regulatory compliance**, and **reducing security risks**.
*   Audits should be performed regularly by IT Security Officers and DBAs.
*   The authorization levels for a DBMS (used for development) are distinct from the authorization levels of the final software product.

### Frequently Asked Questions
**1. Are there other levels of authorization?**
**A:** Yes. For other types of database management systems, and for some companies, they have different levels of authorization. Some have a "Super Admin" level, others have highly granular custom roles, etc. The levels presented here are the most common general categories.

**2. Why is a "Database Viewer" role given to auditors and stockholders?**
**A:** Auditors need to view the data to verify compliance and financial accuracy without the ability to alter or delete the records (which would compromise integrity). Stockholders may need to view high-level reports to make business decisions.

**3. What is the main difference between a Database Manager and a Database Administrator?**
**A:** A **Database Administrator** has full control over the entire database system, including creating and deleting databases. A **Database Manager** only manages the specific databases they created or were assigned to.

**4. How often should a database be audited?**
**A:** There is no fixed schedule, but it should be done regularly, especially when there are major changes in personnel, company structure, or after a significant security incident. Many organizations do it quarterly or annually.

---

## E. Guided Drills / Code Projects

### Solo Project Update: Creating an Authorization Matrix
**Project Overview:** 
For Module 13, you will expand your ongoing project by creating an Authorization and Control plan for your chosen system's database. 

> *Note: This was originally designed as a group activity. We are adapting it as a **solo activity**. You will act as the sole Database Administrator for your assignment.*

**Project Guidelines:**
*   **Format:** Individual work.
*   **Objective:** Draft a simple authorization level plan for your database. Assign roles and access levels to your "team" (even if you are working alone, imagine the roles needed for your project).
*   **Submission:** Add this to your ongoing project documentation.

**Step-by-Step Deliverable (SQL Example):**
Use the following SQL commands as a guide to create your users and assign privileges. *Replace the placeholder names with your specific roles.*

```sql
-- 1. Create the users
CREATE USER 'projectmanager1'@'localhost' IDENTIFIED BY 'StrongPassword123!';
CREATE USER 'lead_developer'@'localhost' IDENTIFIED BY 'SecurePass456!';
CREATE USER 'tester'@'localhost' IDENTIFIED BY 'TestPass789!';

-- 2. Assign Authorization Levels
-- Administrator: Full privileges
GRANT ALL PRIVILEGES ON *.* TO 'projectmanager1'@'localhost' WITH GRANT OPTION;

-- Manager: Database specific privileges
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, INDEX ON project_db.* TO 'lead_developer'@'localhost';

-- Designer/Viewer: Limited Access (Read-only for testers)
GRANT SELECT ON project_db.* TO 'tester'@'localhost';

-- 3. Apply the changes
FLUSH PRIVILEGES;
```

**Draft your Authorization Matrix below:**

| Role / User | Authorization Level | Assigned Privileges | Justification |
| :--- | :--- | :--- | :--- |
| `projectmanager1` | Database Administrator | ALL PRIVILEGES | Needs full control to manage the entire DBMS and user accounts. |
| `lead_developer` | Database Manager | SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER | Needs to build and structure the database tables. |
| `tester` | Database Viewer | SELECT | Only needs to view data to test functionality; cannot edit. |
| `[Your Advisor/Teacher]` | Database Administrator | ALL PRIVILEGES | Must be included for grading and oversight. |

---

## F. Skill-Building Check

### Check for Understanding (10 mins Quiz)

*Answer the questions with the best of your abilities.*

**1. Enumerate at least 2 potential risks that can be encountered if database auditing is not performed.**
*Guidance:* 
1.  **Insider Threats / Access Creep:** Former employees or employees who have changed roles may retain access privileges they no longer need, creating a massive security hole.
2.  **Data Quality Degradation:** Without auditing, errors, inconsistencies, or outdated information can accumulate in the database, leading to poor business decisions and loss of customer trust.
3.  **Non-compliance:** Failing to audit can result in non-compliance with data privacy regulations (like GDPR or the Data Privacy Act), leading to heavy fines and legal repercussions.

**2. What is the difference between a Database Manager and a Database Designer?**
**Correct Answer:** A **Database Manager** has the authority to manage entire databases they created or were assigned. A **Database Designer** only has some capabilities (like creating tables or modifying schemas) but must have explicit permission from the Managers or Administrators to perform those actions.

**3. Multiple Choice: Which of the following is the primary purpose of database auditing?**
A. To make the database run faster.
B. To track the use of database records and the authority of those who access them.
C. To update the database software.
D. To hire new database administrators.
**Correct Answer: B** (Auditing is about tracking access, changes, and ensuring accountability).

**4. True or False: The "Database Viewer" role is usually given to users who need to edit database records.**
**Correct Answer: False** (Database Viewers only have read-only access; they cannot edit records).

**5. Short Answer: Why is it important to regularly perform database auditing even after a few years of usage?**
**Correct Answer:** Over time, organizations experience turnover, role changes, new hires, and new training. These changes often result in access rights becoming misaligned. Regular auditing ensures that only current, authorized personnel have access to specific data, reducing the risk of unauthorized access or data breaches.