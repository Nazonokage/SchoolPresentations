# Business Continuity and IT Disaster Recovery Plan

> **Course:** Information Assurance and Security 2  
> **Module:** 4 — Business Continuity and IT Disaster Recovery Plan  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Welcome back, students! Today we are tackling a critical part of security where IT is heavily involved. Whether your system is already created and under maintenance, or still under construction, you must have a **Disaster Recovery Plan** in place. 

We will also discuss **Business Continuity**, which is the "bigger picture." It helps us understand how businesses continue to operate whenever a disaster occurs, ensuring that critical operations are not permanently halted.

**Quick Review Activity:**
Before we begin, let's test your understanding of risks and assets. 

*   **Give examples of a disaster in a general idea with the asset (e.g., Earthquakes on Office Computers):**
    1.  ___________________________
    2.  ___________________________
    3.  ___________________________
*   **Give examples of a disaster in an IT idea with the asset (e.g., Denial of Service on Website):**
    1.  ___________________________
    2.  ___________________________
    3.  ___________________________

**Learning Targets:**
By the end of this module, you will be able to:
1.  Describe an IT Disaster Recovery Plan.
2.  Identify Business Continuity overall.
3.  Create an IT Disaster Recovery Plan.

![Disaster Recovery Concept](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### What is an IT Disaster Recovery Plan?
**IT Disaster Recovery (IT DR) planning** anticipates technology downtime and creates contingencies and workarounds that mitigate against its potential consequences. 

*   *Example:* A live website suddenly has its server shut down. The main plan is obviously to find a way to restart the server, but a good plan is to have a **backup server** ready to run whenever the main server shuts down.

### Business Continuity vs. IT Disaster Recovery
While IT Disaster Recovery focuses specifically on restoring technology (servers, networks, databases), **Business Continuity** is the broader strategy. It ensures that the *entire business* can continue operating during and after a disaster—even if it means using manual processes or alternative workspaces until the technology is restored.

### Creating an IT Disaster Recovery Plan (During Live Usage)
This example explores the IT DRP during the **maintenance phase** of IT, meaning the system is already running and being used. *(We will explore an example during the development phase later in the course.)*

There are three main steps to creating an IT DRP:

| Step | Action | Focus |
| :--- | :--- | :--- |
| **Step 1** | **Identify the activities or actions of your System.** | Understand what needs to keep running. *Example: The website is running, and the server is running.* |
| **Step 2** | **Identify what issues or problems can hinder the activity.** | Pinpoint the vulnerabilities and threats. *Example: The server suddenly shuts down.* |
| **Step 3** | **Determine how long we can survive without the activity.** | Assess the cost of downtime and establish recovery time objectives (RTO). *Example: The website can be live for at least a week, but remember, it really depends on the system.* |

> **Pro Tip:** The importance of the system determines how costly it would be if it was hindered. Imagine Google being shut down for a month—it would be a huge problem for Google and its users. Therefore, Google's Step 3 would require near-instant recovery times.

---

## C. Analogies and Use Cases

### The "Hospital Power Grid" Analogy
Think of **Business Continuity** as the entire hospital's emergency preparedness plan. It covers everything from evacuating patients to setting up triage tents outside.
Think of **IT Disaster Recovery** as the hospital's backup power generator. If the main power goes out (the server crashes), the generator kicks in immediately to keep life-saving equipment (the critical systems) running. 
*   *Step 1:* Identify what needs power (Life support, MRI machines).
*   *Step 2:* Identify what can cause a power failure (Downed power lines, generator failure).
*   *Step 3:* Determine how long the hospital can survive without power (Even 5 minutes is too long for life support, so the generator must be instantaneous).

### Real-World Use Case: A Retail Store's Point-of-Sale (POS) System
A retail chain experiences a ransomware attack on their POS system.
*   **Business Continuity:** The store manager switches to manual credit card imprinters and paper receipts so customers can still buy products. The store remains open.
*   **IT Disaster Recovery:** The IT team isolates the infected server, restores the database from an offsite backup taken 24 hours earlier, and rebuilds the POS terminals. Within 4 hours, the digital POS is back online, and the manual records are entered into the system.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **IT Disaster Recovery Plan (IT DRP):** Focuses specifically on restoring technology infrastructure (servers, networks, data) after a disruption.
*   **Business Continuity:** The broader strategy ensuring the entire organization can continue its critical functions during and after a disaster.
*   **Three Steps of IT DRP:** 1. Identify system activities. 2. Identify potential hindrances. 3. Determine the maximum tolerable downtime.
*   **The Cost of Downtime:** The longer a critical system is down, the more it costs the organization (financially and reputationally).

### Frequently Asked Questions
**1. What is the main difference between Business Continuity and IT Disaster Recovery?**
**A:** Business Continuity is the "big picture" of how the entire company keeps running (e.g., relocating staff, using manual workarounds). IT Disaster Recovery is a subset that focuses purely on restoring the technology and data systems.

**2. How do we decide "how long we can survive without the activity"?**
**A:** This depends on the system's criticality. You must evaluate the financial impact, operational impact, and legal/regulatory impact of downtime. A hospital system might have a zero-tolerance policy (0 hours), while a blog might survive a week.

**3. Does an IT DRP only apply to live systems?**
**A:** No, an IT DRP should also apply to systems under construction or development. If a developer's laptop crashes and the source code isn't backed up, that's a disaster. We will cover development-phase DRP in a future module.

**4. Why do we need a backup server if we already have a main server?**
**A:** Redundancy. A backup server ensures that if the primary server suffers a hardware failure, cyberattack, or power outage, the service can be restored quickly, minimizing downtime and data loss.

---

## E. Guided Drills / Code Projects

### Solo Project: Drafting Your First IT DRP
**Project Overview:** 
For this module, you will create a draft of an IT Disaster Recovery Plan based on the scenario provided below. This is an individual activity to practice applying the 3 steps.

> *Note: This is a solo activity. You will act as the sole IT security consultant.*

**Project Scenario:**
You are the IT administrator for a local dental clinic. The clinic uses a cloud-based patient management system to store appointments, medical histories, and billing information. The system runs on a local server in the clinic, but it syncs to the cloud every night.

**Deliverable:**
Using the 3 steps discussed in the Main Lesson, draft a concise IT DRP for this clinic.

**1. Identify the activities or actions of the System:**
*   (What does the system do? e.g., Store patient records, process billing, schedule appointments.)

**2. Identify what issues or problems can hinder the activity:**
*   (What could go wrong? e.g., Server crash, internet outage, ransomware attack, power failure.)

**3. Determine how long we can survive without the activity:**
*   (How long can the clinic operate without this system? What is the financial/medical impact of downtime?)

**Draft your plan below:**

```json
// Example JSON representation of your IT DRP Draft
{
  "system_name": "Dental Clinic Patient Management System",
  "activities": [
    "Storing patient medical histories",
    "Scheduling appointments",
    "Processing billing and insurance claims"
  ],
  "potential_issues": [
    "Local server hardware failure",
    "Internet Service Provider (ISP) downtime preventing cloud sync",
    "Ransomware encrypting the local database"
  ],
  "maximum_tolerable_downtime": "4 hours during clinic hours. If downtime exceeds 4 hours, patient care is compromised, and billing cannot be processed.",
  "recovery_strategy": "Switch to manual paper-based scheduling and use the previous night's cloud backup to restore patient records on a backup laptop."
}
```

---

## F. Skill-Building Check

### Part 1: Multiple Choice

**1. What is the primary focus of an IT Disaster Recovery Plan?**
A. Ensuring the entire business can operate during a disaster.
B. Anticipating technology downtime and creating contingencies for IT systems.
C. Hiring new employees after a disaster.
D. Increasing the company's marketing budget.
**Correct Answer: B** (IT DRP focuses specifically on technology downtime and contingencies).

**2. In the 3-step IT DRP process, what is the goal of Step 3?**
A. Determine how long we can survive without the activity.
B. Identify what issues can hinder the activity.
C. Identify the activities of the system.
D. Install antivirus software.
**Correct Answer: A** (Step 3 is about assessing the maximum tolerable downtime).

**3. Why is a backup server considered a good IT DRP strategy for a live website?**
A. It makes the website load faster.
B. It allows the website to continue running if the main server shuts down.
C. It prevents all cyberattacks.
D. It reduces the cost of web hosting.
**Correct Answer: B** (A backup server provides redundancy and minimizes downtime).

**4. What is the difference between Business Continuity and IT Disaster Recovery?**
A. There is no difference; they are the same thing.
B. Business Continuity is the big picture of keeping the business running; IT DRP is specifically about restoring technology.
C. Business Continuity is only for large companies; IT DRP is for small businesses.
D. IT DRP is the big picture; Business Continuity is only for IT.
**Correct Answer: B** (Business Continuity is holistic; IT DRP is a technical subset).

### Part 2: Short Answer

**5. Why is it important to determine "how long we can survive without the activity" before a disaster happens?**
*Guidance:* Your answer should discuss how this step helps an organization prioritize their recovery efforts and allocate resources (budget, personnel) efficiently. If a system can only tolerate 1 hour of downtime, the organization knows they must invest in high-availability systems and instant failover. If it can survive a week, they can afford a slower, cheaper recovery process.