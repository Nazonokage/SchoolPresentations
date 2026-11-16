# Database Security and Integrity: Policies for DB Security

> **Course:** Information Assurance and Security  
> **Module:** 10 — Database Security and Integrity: Policies for DB Security  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Hello students! Today we are tackling the policies for **Database (DB) Security**. This is the first part of Database Security and Integrity. 

**Quick Scenario:** Imagine if someone deleted the database of your school, changed the database of your bank account, or perhaps deleted the database of your project right before you were set to present and defend it. What would happen? 

This situation is exactly why we need strict **Database Security Policies**. These involve rules and regulations on how the database should be accessed, updated, edited, or changed. 

> **Important Note:** The policies discussed here are not the absolute *only* policies that exist. This is a sample set of universally applicable policies. Some companies have their own specific database policies that must be followed.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Understand the importance of having DB Security Policies.
2.  Create Policies for your DB Security for your capstone or project.

![Database Security Concept](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

A secure database is not just about technical firewalls; it is about establishing clear, enforceable rules. Here are the 7 essential Database Security Policies every organization should implement.

### 1. Database Password Policy
Do you recall setting up your local database connection? Often, users use `root` as the username and leave the password blank (`""`). This means the root username has no password, and **everyone** can access it.

*   **Rule:** It is important to have a password, especially on your `root` username. If the database is shared between multiple users and multiple computers (like on a server), it is extremely important to have different usernames and passwords for any database they access.
*   **Why?** This prevents accidental deletion or unauthorized changes by coworkers. 
*   **Additional Rule:** Implement a "change password" policy, where users must change their passwords regularly.

### 2. DB Access Controls Policy
It is ideal to have limited controls or privileges for specific users of the database. 

*   *Example:* A `projectmanager1` user might have complete access to the database to do their job, but they do *not* have the privilege to create new user accounts. 
*   *Example:* The `root` user has all privileges.
*   *Recommendation:* Create specific roles (like `designer1`) who are allowed to create and insert data, but cannot edit or delete it. They must rely on the `projectmanager1` to perform those higher-level actions.

### 3. Database Backup Policy
It is ideal to back up your database in a regular fashion. 
*   If your project is a 1-year project, back up once every 2 weeks or month.
*   Additionally, perform a backup every time you update the structure of your database.
*   **How to do it:** To create a backup, you simply need to **export** the database. To restore a backup, you **import** it. 
*   **Naming Convention:** When backing up, the system creates an `.sql` file. It is ideal to name it with a standard naming convention. 
    *   *Example:* `DBName-YYYY-MM-DD` (e.g., `CapstoneDB-2026-09-13.sql`).

### 4. Recovery Policy
It is ideal to have rules in recovering your database from a backup. 
*   Sometimes there are moments in development where you need to apply a backup. Performing a backup without the proper authorization can lead to changes that the project manager or designer might not be aware of.
*   *Compatibility Risk:* If other developers have proceeded with the development and created codes for the latest version of the database, restoring an older backup might cause incompatibility. 
*   *Rule:* The developer should always be aware that there will be a backup recovery.

### 5. Encrypted Password Policy
It is ideal to have your passwords in the database **encrypted**. This way, not even the developers can see the passwords written by the users, nor can potential hackers.

| State | Username | Password |
| :--- | :--- | :--- |
| **NOT ENCRYPTED** | `admin` | `password` |
| **ENCRYPTED (MD5)** | `admin` | `5f4dcc3b5aa765d61d8327deb882cf99` |

> *This is an MD5 Encryption, a very basic encryption. We will be using more powerful encryption (like AES 256) in the future.*

### 6. Database Update and Revision Policy
Change happens frequently in software development. This is why we must have a record of the changes we perform. 
*   The usual way to record changes is through **changelogs** (a list of things that changed with each update).
*   This keeps track of what changed. If you wish to revert a change, you also must revert the changelogs.
*   *Example:* Initially, the password was not encrypted. On the next update, it is now encrypted. This must be documented.

### 7. Archiving Policy
Deleting rows on a database table is not ideal. The correct way is **archiving**. 
*   **How:** Create a boolean column on your database named `archived`.
*   **Logic:** It should either be `true` or `1` (archived), or `false` or `0` (active).
*   **Querying:** To make sure you only get the data that is not archived, you can always query: `WHERE archived = 0`.

### Example of a Simple Database Policy
Here is a comprehensive example of what a 1-page database policy document might look like:

1.  **Database accounts must have passwords**
    *   Passwords must be 10 characters at least.
    *   Passwords must have at least 1 uppercase and 1 lowercase.
    *   Passwords must have at least 1 symbol and 2 numbers.
2.  **Database must have user controls or privileges**
    *   A project manager has all controls and privileges to their projects except making, editing, and deleting accounts.
    *   Developers require designer or project manager's authorization to make changes to the database.
3.  **Backup Regularly**
    *   Backup the database every week.
    *   Backup the database every time a change will be implemented.
    *   Name the backup with this format: `DatabaseName-Year-Month-Day`.
    *   Store backup SQLs on a GitHub repository, secure server, or Google Drive.
4.  **Recovery Policy**
    *   Recovery can only be performed if the project manager and designer are present at the same time.
5.  **Encryption**
    *   All password fields within the created databases must be AES 256.
6.  **Update Policy**
    *   Create changelogs before implementing an update to the database.
    *   Create changelogs before reverting a database version to the previous version.
7.  **Archiving Policy**
    *   Archive the fields rather than deleting.

---

## C. Analogies and Use Cases

### The "Bank Vault" Analogy
Think of your database as a bank vault.
*   **Password Policy:** Only the bank manager (root) has the master key, and it's locked away. Tellers (users) have their own unique keys.
*   **Access Control:** A teller can deposit money (insert) and check balances (select), but they cannot change the interest rates (alter schema) or hire new tellers (create accounts).
*   **Backup & Recovery:** The bank makes a daily copy of all the ledger books and stores them in a fireproof safe. If the bank burns down, they can rebuild the ledger from yesterday's backup.
*   **Archiving:** Instead of shredding old transaction receipts, the bank puts them in a filing cabinet in the basement (`archived = 1`). They only look at the active drawer (`archived = 0`) for daily business.
*   **Encryption:** The vault stores the money in a locked box (encrypted). Even if someone breaks into the vault, they can't use the money without the decryption key.

### Real-World Use Case: A Healthcare Database
A hospital database stores patient records. 
*   If the `root` password is blank, a malicious actor could drop the entire patient table, causing massive disruption.
*   If a nurse's account is compromised, the hacker could view the data (because nurses need view access). However, due to **Access Controls**, they cannot delete the patient records or alter the database schema.
*   If a ransomware attack encrypts the hospital's servers, the hospital relies on their **Backup Policy** to restore patient records from an offsite, secure backup taken 2 hours prior.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **Database Security Policies** are rules that regulate how the database is accessed, updated, and managed.
*   The **Root Password** should never be blank. Always use strong, unique passwords for all database users.
*   **Access Controls** ensure users only have the privileges necessary to do their jobs (Principle of Least Privilege).
*   **Backups** must be done regularly and named using a standard convention (e.g., `DBName-YYYY-MM-DD`).
*   Passwords must be **encrypted** (e.g., MD5, AES 256) before storing them in the database.
*   Use **Archiving** (`archived = 0/1`) instead of deleting rows to preserve data history.

### Frequently Asked Questions
**1. Are there other policies regarding databases?**
**A:** Yes, there are plenty more policies. The policies discussed here are a baseline. The specific policies depend on the database used (NoSQL vs SQL) and the specific needs and compliance requirements of the company.

**2. What are the dangers of not changing the password of your root user in MySQL?**
**A:** If the `root` password is left blank (default), anyone with access to the network or local machine can log in as the root user. The root user has `ALL PRIVILEGES`. This means an attacker could drop tables, delete data, create backdoor accounts, or steal sensitive information instantly.

**3. Why is MD5 considered "basic" encryption for passwords?**
**A:** MD5 is a fast hashing algorithm. Because it is fast, hackers can use brute-force or rainbow tables to crack MD5 hashes quickly. Modern standards recommend stronger, slower hashing algorithms like bcrypt or Argon2, or encrypting the data with AES-256.

**4. Is it better to delete a user's data or archive it?**
**A:** Archiving is better. Deleting data is irreversible. If a user asks to be "deleted" or if data becomes outdated, archiving keeps the record for auditing, legal, or historical purposes while hiding it from active use.

---

## E. Guided Drills / Code Projects

### Solo Project Update: Drafting Your Database Policy
**Project Overview:** 
For Module 10, you will expand your ongoing project by creating your own **Database Security Policy** document. 

> *Note: This was originally designed as a group activity. We are adapting it as a **solo activity**. You will act as the sole database administrator/security consultant for your project.*

**Project Guidelines:**
*   **Format:** Individual work.
*   **Objective:** Create a 1-page Database Policy document for your capstone or ongoing project. 
*   **Formatting Requirements:** Arial 12 pt, Double Spaced.
*   **Submission:** Add this to your ongoing project documentation.

**Step-by-Step Deliverable:**
Review the 7 policies discussed in this module. Write a draft of your own Database Policy. You can add as many policies as you believe will help your project. Ensure you address the following:

1.  **Password Requirements:** (e.g., Minimum length, complexity).
2.  **Access Controls:** (Who gets what level of access? e.g., Admin, Developer, Designer).
3.  **Backup Schedule & Naming:** (How often? What format? Where stored?).
4.  **Recovery Authorization:** (Who must be present to restore a backup?).
5.  **Encryption:** (What algorithm will be used for passwords?).
6.  **Update/Revision:** (Will you use changelogs?).
7.  **Archiving:** (How will you handle data deletion?).

**Draft your policy below:**

```markdown
# Database Security Policy for [Project Name]

## 1. Password Policy
*   All database accounts must have a strong password (min. 12 chars, 1 upper, 1 lower, 1 symbol, 2 numbers).
*   The `root` account password must be changed from the default.
*   Passwords must be rotated every 90 days.

## 2. Access Control Policy
*   **Level 4 (Admin):** Full access, including creating users and altering tables.
*   **Level 3 (Project Manager):** Full access to project data, can create tables but cannot drop the database or manage users.
*   **Level 2 (Developer):** Can insert, update, and select data. Cannot drop tables or manage users.
*   **Level 1 (Viewer):** Can only select (view) data.

## 3. Backup Policy
*   Full database backups will be performed every Friday at 11:59 PM.
*   An additional backup will be performed before any major schema changes.
*   Backup naming convention: `ProjectName-YYYY-MM-DD.sql`.
*   Backups will be stored securely on Google Drive.

## 4. Recovery Policy
*   Database recovery can only be performed with the explicit authorization of the Project Manager and the Lead Developer.

## 5. Encryption Policy
*   All user passwords must be encrypted using AES-256 before insertion into the database. Plaintext passwords are strictly prohibited.

## 6. Update and Revision Policy
*   Changelogs must be created and committed to the version control system before any database update is applied.

## 7. Archiving Policy
*   Data will never be physically deleted. An `archived` boolean column (0 = active, 1 = archived) will be used. Active queries must filter by `archived = 0`.
```

---

## F. Skill-Building Check

### Check for Understanding (25 mins Quiz)

*Answer the following questions with the best of your abilities.*

**1. What is the importance of having a Database Security Policy?**
*Guidance:* A Database Security Policy is crucial because it establishes the rules and regulations for how data is accessed, modified, and protected. It prevents unauthorized access, data loss, and accidental deletion. It ensures accountability (who did what), maintains data integrity, and protects the confidentiality of sensitive information.

**2. What are the dangers of not changing the password of your root user in MySQL?**
*Guidance:* Leaving the root password blank is extremely dangerous because the root user has `ALL PRIVILEGES`. Anyone can access the database, delete all tables (`DROP TABLE`), steal sensitive data, or create unauthorized user accounts. It is a critical vulnerability that can lead to total database compromise.

**3. Multiple Choice: Which policy involves creating a boolean column to mark data as inactive instead of deleting it?**
A. Backup Policy
B. Access Control Policy
C. Archiving Policy
D. Recovery Policy
**Correct Answer: C** (Archiving Policy uses a boolean column to mark records as inactive rather than physically deleting them).

**4. True or False: It is acceptable to restore a database backup at any time without notifying the development team.**
**Correct Answer: False** (A Recovery Policy should require proper authorization and notification because restoring an older backup can break newly written code that relies on the latest database structure).

**5. In the context of Database Security, why is MD5 considered a weak encryption method for passwords?**
**Correct Answer:** MD5 is considered weak because it is a fast hashing algorithm. Attackers can use high-speed computers and rainbow tables to easily crack MD5 hashes. It is recommended to use stronger algorithms like AES-256 or bcrypt for password storage.