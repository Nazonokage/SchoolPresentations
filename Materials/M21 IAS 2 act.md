# Disaster Simulation: The Cyber Resilience Drill

> **Course:** Information Assurance and Security  
> **Module:** 21 — Disaster Simulation  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Welcome, future security officers! Today, we put your theoretical knowledge to the ultimate test. We are conducting a **Cyber Resilience Drill**. 

In previous modules, we discussed Business Continuity and IT Disaster Recovery Plans (DRP). You learned how to create them, but today, you will prove that they actually work. 

**Quick Review:**
Before we begin, recall the core components of your DRP:
1.  Identify system activities.
2.  Identify potential hindrances.
3.  Determine maximum tolerable downtime.
4.  Establish recovery procedures (Backups, Version Control, etc.).

**Learning Targets:**
By the end of this module, you will be able to:
1.  Demonstrate that your project progress is being performed.
2.  Demonstrate that you can solve a simulated disaster within your project.
3.  Evaluate the effectiveness of your own Disaster Recovery Plan.

![Cyber Resilience Drill](https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### The Modern "Live-Fire" Simulation
In this modernized activity, your instructor will act as a **Threat Actor** (or "Disaster Agent"). They will intentionally simulate a catastrophic failure in your project environment to test your recovery capabilities.

> **Important Note:** This is a controlled simulation. It is designed to stress-test your documentation, your backups, and your ability to remain calm under pressure. It is not a punishment; it is a learning exercise.

**The Simulation Scenarios:**
Your instructor will choose one of the following realistic disaster scenarios to execute during the session:
1.  **Database Corruption:** A critical table is dropped, or the entire database is deleted.
2.  **Deleted Documentation:** Your project documentation (Word/PDF files) is removed from the local machine.
3.  **GitHub Repository Wipe:** The remote repository is pushed to empty, or the main branch is deleted.
4.  **Ransomware/File Lockout:** Files are encrypted or locked, rendering them inaccessible.
5.  **Code Deletion:** The source code folder (`htdocs`, `src`, or main project folder) is deleted.

### Your Role as the Defender
Before the simulation begins, you must demonstrate due diligence. You must **back up your files** and provide a copy to your instructor or store it in a secure, offsite location (like cloud storage). Then, the disaster strikes.

Once the disaster has occurred, you must:
1.  Assess the damage.
2.  Execute your **Disaster Recovery Plan**.
3.  Recover your data (Database, Code, Documentation).
4.  Document the process and your results.

---

## C. Analogies and Use Cases

### The "Fire Drill" Analogy
Think of this activity as a fire drill for your capstone project. You don't wait for a real fire to figure out where the exits are. You practice under controlled conditions. 

If you fail to recover during a drill, you learn valuable lessons without losing your actual work permanently. If you fail during a real disaster (like a final defense), you lose everything. This simulation ensures you are prepared for the worst.

### Real-World Use Case: Netflix's "Chaos Monkey"
Netflix famously invented a tool called **Chaos Monkey** that randomly terminates instances in their production environment. Why? To ensure that their engineers had built systems resilient enough to survive random failures without impacting the customer. This module is your "Chaos Monkey" moment. You are being forced to prove your system's resilience.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **Preparation is Key:** You cannot recover what you did not back up. Offsite and version-controlled backups are mandatory.
*   **Testing Validates the Plan:** A DRP that hasn't been tested is just a theoretical document. The simulation validates its practicality.
*   **Speed and Efficiency:** The time it takes to recover is critical. You must know your recovery steps by heart.
*   **Post-Mortem Analysis:** Even if you recover successfully, there is always room for improvement. Understanding *why* a failure happened is as important as fixing it.

### Frequently Asked Questions
**1. What if I fail to recover my data during the simulation?**
**A:** Do not panic. If you fail to recover, you will receive a below-passing grade for the drill, but you have an opportunity to pass by providing a written explanation of *why* your disaster recovery plan failed and what steps you will take to fix it. Failure is a learning opportunity here.

**2. Can I refuse to participate?**
**A:** No. This is a mandatory activity designed to prepare you for real-world IT scenarios. It tests your ability to handle pressure and technical challenges. 

**3. How do I prepare for the simulation?**
**A:** Follow the instructions carefully. Backup your database, code, and documentation. Give a copy to your teacher before the simulation begins. Verify that your backup works on a different computer. If your backup doesn't work, your recovery will fail.

---

## E. Guided Drills / Code Projects

### The Disaster Simulation Activity
**Project Overview:** 
You will undergo a controlled disaster scenario orchestrated by your instructor. You must successfully recover your capstone project data using your prepared Disaster Recovery Plan.

**Project Guidelines:**
*   **Format:** Individual Activity (Solo Work).
*   **Objective:** Recover from the simulated disaster and document the process.
*   **Submission:** A written report answering the post-simulation reflection questions.

**Step-by-Step Deliverable:**

**Phase 1: Preparation (Before the Drill)**
1.  **Backup:** Export your database, compress your codebase, and save your documentation.
2.  **Offsite Storage:** Upload your backups to a secure location (Google Drive, GitHub, or a physical external drive).
3.  **Verification:** Hand a copy of the backup to your instructor. *Do not skip this step.*
4.  **Test:** Restore a backup on a different computer to ensure the backup file is not corrupted.

**Phase 2: The Simulation (The Disaster)**
Your instructor will simulate one of the disaster scenarios listed in the Main Lesson. Observe what has happened to your project environment.

**Phase 3: The Recovery**
Execute your DRP. Restore your database, retrieve your code, and rebuild your documentation.

**Phase 4: Reporting (Submit this to your instructor)**
Answer the following questions comprehensively:

1.  **Describe thoroughly the disaster that you encountered.**
    *   *(What was the specific simulated disaster? Database deletion, code wipe, etc.)*
2.  **What were the targeted assets, describe them?**
    *   *(List the specific files, databases, or repositories that were affected.)*
3.  **What were your disaster recovery plans used?**
    *   *(Which backup strategy or version control method did you utilize to recover?)*
4.  **What were the steps of your disaster recovery plan?**
    *   *(Provide a step-by-step breakdown of what you did to restore your system.)*
5.  **How long did it take the group to recover, was it good enough?**
    *   *(Provide a time estimate. Evaluate if this downtime would be acceptable in a real business scenario.)*
6.  **What was your overall experience with the disaster?**
    *   *(Reflect on the stress, the process, and the outcome.)*
7.  **What improvements on your disaster recovery plan would you place?**
    *   *(Based on the drill, what changes would you make to your backup policy or DRP?)*
8.  **Explanation if you failed to recover from the disaster.**
    *   *(If you were unable to restore your data, explain exactly why the DRP failed. What broke? Was the backup corrupted? Was the process too slow?)*

---

## F. Skill-Building Check

### Post-Drill Self-Assessment

*After completing the simulation, rate your performance based on the following criteria. This will help you identify areas for improvement in your final project defense.*

| Assessment Criteria | Excellent (4) | Good (3) | Fair (2) | Needs Improvement (1) |
| :--- | :--- | :--- | :--- | :--- |
| **Backup Preparedness** | Had multiple, verified backups ready before the drill. | Had a backup, but it required minor troubleshooting. | Backup was outdated or missing a critical component. | No backup was available. |
| **Disaster Identification** | Immediately understood the disaster and its impact. | Took a moment to assess the situation but identified the problem. | Confused about what happened initially. | Panicked and could not identify the issue. |
| **Execution of DRP** | Followed the DRP flawlessly and recovered all data. | Recovered most data, but missed a minor step. | Recovered some data, but the process was messy. | Failed to recover data using the DRP. |
| **Downtime Minimization** | Recovered in under 10 minutes. | Recovered in under 30 minutes. | Recovered in 1-2 hours. | Downtime exceeded 2 hours or unrecovered. |
| **Documentation** | Reflection questions answered thoroughly with deep insights. | Questions answered adequately. | Answers were brief or lacked detail. | Questions were not answered. |

**Total Score:** _____ / 20

> **Final Reminder:** If you failed to recover, do not be discouraged. The purpose of this simulation is to find the flaws in your plan *before* the real world does. Document your failure honestly, learn from it, and improve your strategy for the final defense.