# Secured Versioning with GitHub

> **Course:** Information Assurance and Security  
> **Module:** 19 — Secured Versioning  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Hello students! Today, we are continuing our discussion on backup policies and introducing a critical tool for managing code and databases: **Secured Versioning**. 

We will be using **GitHub**, a platform you may already be familiar with. In our previous modules, we discussed database backup policies using export and import. Today, we will improve upon that by learning where to store your databases and code properly, how to track changes made to them, and how to secure everything using GitHub's user access controls.

**Quick Review:**
Can you still recall what a database backup policy is? 
*   *Hint:* It involves creating regular copies of your database (e.g., weekly, or before major updates) and naming them consistently (e.g., `DBName-YYYY-MM-DD.sql`) to ensure data recovery.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Understand the importance of versioning and securing created and archived versions.
2.  Use versioning and GitHub.

![GitHub Concept](https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### What is Versioning?
Whenever someone creates a computer system, software, or database, changes are inevitable. **Versioning** is the practice of assigning a value to indicate a step or change in the evolution of the system.

*   *Example:* Microsoft released **Windows 8**. After user feedback (and some backlash), they made updates and released **Windows 8.1**. The change in the number indicates a new version. 
*   *In your Capstone:* As a developer, whatever you are creating now is not yet a "Version 1" because it is still in development. Once you are able to run your system, it can be considered **Version 0.2**. When you near your defense, it might be **Version 0.9**.

### The Problem with Manual Versioning
The main problem developers face with versioning is managing backups of each version, maintaining changelogs, and deciding on version naming conventions. This can take time and lead to **human errors** if not done properly.

### Presenting GitHub
**GitHub** can be considered a tool for **secured versioning**. It is a widely used web-based platform for version control and source code management. It provides a secure and collaborative environment for storing, managing, and versioning software code.

#### Functions of GitHub
Here are the key functions that make GitHub essential for developers:

| Function | Description |
| :--- | :--- |
| **1. Version Control** | GitHub utilizes the **Git** version control system. It tracks and manages changes to your codebase, ensuring every version is stored and can be easily accessed. It allows you to commit changes, create branches, and merge versions while maintaining a complete history. |
| **2. Access Control** | Offers robust access control features. Repository owners can define and manage access rights for individuals or teams. Access can be restricted to authorized personnel, preventing unauthorized access or tampering. |
| **3. Collaboration and Review** | Facilitates collaboration via pull requests, code reviews, and commenting. Multiple developers can work together, review code changes, and suggest improvements before merging into the main branch. Viewers can also see who edited specific lines of code. |
| **4. Security Features** | Incorporates security features to protect code versions. It supports secure communication protocols (HTTPS), provides two-factor authentication (2FA), and offers options for encryption. It also supports vulnerability scanning capabilities and integrations with security tools. |
| **5. Audit Trail and Logging** | Keeps a detailed audit trail of all activities and changes made to the repository. It