# Integration of Risk Management in Software Development Life Cycle

> **Course:** Information Assurance and Security  
> **Module:** 22 — Integration of Risk Management in SDLC  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Hello students! Today, we are combining two critical concepts: the **Software Development Life Cycle (SDLC)** and **Risk Management**. 

Can you still remember your Risk Management lessons from your previous module? How about the SDLC from your IT Project Management subject? 

**Quick Review: The 5 Phases of SDLC**
1.  **Planning:** Gathering requirements, setting goals, and defining the project scope.
2.  **Design:** Creating the structure, prototypes, and architecture of the system.
3.  **Implementation:** Writing the actual code.
4.  **Testing:** Verifying that the system works as intended.
5.  **Deployment and Maintenance:** Releasing the system and providing ongoing support.

**Our Goal Today:**
Our goal is to secure each and every one of these phases. Security cannot be an afterthought added at the end. It must be built into every step. 

> **Important Note:** Just as every organization has its own way of doing things, securing the SDLC differs across companies. For example, Agile Development has a different security process than traditional Waterfall. The concepts we discuss today are the most universal and common ways to secure the SDLC.

![Secure SDLC Concept](https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### Phase 1: Planning
In the Planning phase, the idea is to gather as many requirements as possible from the client or product owner. 

**What is done:**
*   Discuss what system the client wants.
*   Set goals and objectives (Who are the users? What platform will it run on?).
*   Plan the tools, software, and hardware to be used.
*   Document everything.

**How to Secure it:**
The most important part is securing the **requirements** and the **assets** involved in the project.
*   Secure the intellectual property (IP) of the system to be developed.
*   Secure the documents to be used.
*   Secure the tools, software, and hardware to be used.
*   Secure the documentation and its updates.
*   Secure the storage where the system will be built (e.g., GitHub).

### Phase 2: Design
The design phase focuses on the structure of the system, from creating prototypes or visual models to the actual design structure and relationship of the Classes, and most importantly, the **databases**.

**What is done:**
*   Create Database and Entity Relationship Diagrams (ERD).
*   Create Class Diagrams.
*   Create Flow Charts.
*   Create Data Flow Diagrams (DFD).
*   Prototyping.

**How to Secure it:**
Here, we apply previous lessons to secure the design.
*   Securing the Database from SQL injections and other threats.
*   Securing the Data Flows between entities.
*   Securing the Documents.
*   Securing the Connections/Network between the database, system, storage, computers, and users.
*   Preparing the Encryption technology to be used.
*   Securing your versioning (using GitHub).

### Phase 3: Implementation
In the Implementation phase, this is where we perform our coding. We basically follow the design and requirements to code the system.

**How to Secure it:**
*   The codes must be immune to injections such as SQL injections and XSS injections.
*   The Encryption of user credentials and information.
*   Secure the codes from vulnerabilities or backdoors.
*   Secure the versioning for every update done with the codes.

### Phase 4: Testing
During testing, we use test cases that were created to test every possible combination or action within the system, making sure it will not cause any errors or, worse, create vulnerabilities.

**How to Secure it:**
*   Securing the test cases.
*   Securing the automation process of the testing, if automated testing will be used.
*   Securing the codes/system that are ready for deployment.
*   Securing that the system adheres to the requirements of the client.

### Phase 5: Deployment and Maintenance
In the deployment phase, the focus is deploying the system, checking once more if the system is complete, and deploying it. We also proceed to maintenance, where we maintain the system for updates and changes depending on the contract with the clients.

**How to Secure it:**
*   Securing the requirements of the client adheres to the system.
*   Securing the versioning for future updates or patches requested by the client or created by the developers for detecting issues.
*   Securing the documentation for future purposes and copyright.

### Benefits of Securing SDLC
*   **Reduced Costs:** By identifying potential security risks early, we can avoid them, thus removing the costs of risks occurring later.
*   **Improves Development:** It improves the quality of the future development life cycle since you learn from the previous project (both from securing and from the development strategies).
*   **Better Security:** Overall, it simply reduces the risks and attacks that can cause organizational issues.

### Applying Risk Management
In applying Risk Management to the SDLC, you should refer to your previous lessons on the 6-step Risk Management Framework (RMF). You must apply all 6 steps of the RMF for *each* of the 5 phases of the SDLC. 

*   Step 1: Categorize Information Systems
*   Step 2: Select Security Controls
*   Step 3: Implement Security Controls
*   Step 4: Assess Security Controls
*   Step 5: Authorize Information Systems
*   Step 6: Monitor Security Controls

> **Pro Tip:** It will be a repetitive task, applying the RMF to all 5 phases, but this is exactly how security is created—through relentless repetition and evaluation.

---

## C. Analogies and Use Cases

### The "Building a Secure House" Analogy
Think of the SDLC as building a house.
*   **Planning:** You decide to build a house with a safe room. You plan to buy high-quality locks (Security requirement).
*   **Design:** The architect draws the blueprints showing where the reinforced doors and alarm systems will go (Design security).
*   **Implementation:** The builders install the reinforced doors and wire the alarm system while building the walls (Coding securely).
*   **Testing:** You test the alarm system and try to break down the doors (Penetration testing).
*   **Deployment & Maintenance:** You move in, but you regularly change the alarm codes and upgrade the locks as new lock-picking techniques are discovered (Maintenance & Monitoring).

If you wait until the house is built to think about the safe room, it is incredibly expensive and difficult to add.

### Real-World Use Case: A Fintech App
A company is building a mobile banking app.
*   During **Planning**, they decide that user data must be encrypted at rest and in transit.
*   During **Design**, they architect the database using an ERD, ensuring PII (Personally Identifiable Information) is stored in a separate, isolated table.
*   During **Implementation**, developers use parameterized queries to prevent SQL Injection.
*   During **Testing**, the QA team runs automated security scans and manual penetration tests.
*   During **Deployment**, they ensure the production server is hardened and monitor logs for suspicious activity.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **Security is not a phase; it's a mindset.** It must be integrated into every phase of the SDLC.
*   **Planning** requires securing requirements and tools. **Design** requires securing architecture and data flows. **Implementation** requires secure coding. **Testing** requires secure test cases. **Deployment** requires secure versioning and patching.
*   The **6 Steps of the Risk Management Framework** must be applied to *each* of the 5 SDLC phases.
*   Securing the SDLC reduces costs, improves development quality, and provides better overall security.

### Frequently Asked Questions
**1. Are there other ways in securing SDLC?**
**A:** Yes. The approach presented here is the universal, foundational way. However, companies may have different methodologies. For example, a company using Agile might use "Security Sprints" or "Threat Modeling" workshops in every iteration, while a company using DevOps might automate security checks in their CI/CD pipeline. The core concepts remain the same.

**2. Why do I need to apply the RMF to every phase of the SDLC?**
**A:** Because risks change at every phase. A risk in the Planning phase (e.g., a misaligned requirement) is different from a risk in the Implementation phase (e.g., an SQL injection vulnerability). Applying RMF continuously ensures no gap is left unaddressed.

**3. What is the difference between securing the SDLC and regular SDLC?**
**A:** Regular SDLC focuses on delivering the software on time and within budget. Secure SDLC (SSDLC) adds security checkpoints and activities to every phase to ensure the final product is not vulnerable to attacks. 

---

## E. Guided Drills / Code Projects

### Solo Project Update: Final Integration
**Project Overview:** 
This is your final project update for Information Assurance and Security. You will apply the Risk Management Framework (RMF) for each step of your project's SDLC.

> *Note: This was originally designed as a group activity. We are adapting it as a **solo activity**. You will act as the sole security consultant applying RMF to your project.*

**Project Guidelines:**
*   **Format:** Individual work.
*   **Objective:** Create a comprehensive matrix or document that applies the 6 RMF steps to each of the 5 SDLC phases for your capstone.
*   **Submission:** Add this to your final project documentation.

**Step-by-Step Deliverable:**
Create a table or write a structured document that maps the RMF to the SDLC. For each phase (Planning, Design, Implementation, Testing, Deployment), list the specific security measures you applied based on the RMF.

**Draft your integration plan below:**

| SDLC Phase | Step 1: Categorize | Step 2: Select | Step 3: Implement | Step 4: Assess | Step 5: Authorize | Step 6: Monitor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Planning** | Identify requirements and assets. | Select secure tools and storage (GitHub). | Set up private repos, MFA. | Check if tools meet security needs. | Get client sign-off on security plan. | Monitor for new threats. |
| **2. Design** | Identify sensitive data (PII). | Select encryption (AES-256). | Design ERD with isolated tables. | Review design for vulnerabilities. | Approval of DB schema. | Monitor access logs. |
| **3. Implementation** | Categorize code modules. | Select secure coding standards. | Code with parameterized queries. | Code review and SAST. | Merge into main branch. | Monitor for zero-days. |
| **4. Testing** | Identify critical test cases. | Select automated tools. | Run OWASP ZAP/Burp Suite. | Verify fixes for reported bugs. | Sign-off on release candidate. | Monitor QA metrics. |
| **5. Deployment** | Categorize production assets. | Select server hardening scripts. | Deploy with HTTPS. | Conduct final pen test. | Exec sign-off for go-live. | Monitor server health and logs. |

*(You can elaborate on these points in your project document to meet the specific needs of your capstone).*

---

## F. Skill-Building Check

### Check for Understanding (25 mins Quiz)

*Answer the questions with the best of your abilities.*

**1. Create a checklist of the listed security details for each phase of the SDLC, and check if you have applied those security details. You can use the given above from the Content of the modules.**

**Phase 1: Planning**
*   [ ] Intellectual Property of the system secured.
*   [ ] Project documents secured.
*   [ ] Tools, software, and hardware secured.
*   [ ] Documentation and updates secured.
*   [ ] Storage location (e.g., GitHub) secured.

**Phase 2: Design**
*   [ ] Database secured from SQL injections.
*   [ ] Data Flows secured.
*   [ ] Documents secured.
*   [ ] Connections/Network secured.
*   [ ] Encryption technology prepared.
*   [ ] Versioning secured.

**Phase 3: Implementation**
*   [ ] Codes immune to SQL injections and XSS.
*   [ ] User credentials and information encrypted.
*   [ ] Codes secured from vulnerabilities/backdoors.
*   [ ] Versioning for updates secured.

**Phase 4: Testing**
*   [ ] Test cases secured.
*   [ ] Automation process secured.
*   [ ] Codes ready for deployment secured.
*   [ ] System adheres to client requirements.

**Phase 5: Deployment and Maintenance**
*   [ ] Client requirements adhered to.
*   [ ] Future updates/patches secured.
*   [ ] Documentation for future purposes and copyright secured.

**2. Multiple Choice: Why is it important to apply Risk Management at every phase of the SDLC?**
A. To make the project take longer.
B. Because risks change at every phase, and early identification reduces costs.
C. To ensure the developers have more paperwork.
D. Because the client asked for it.
**Correct Answer: B** (Early identification of risks in the SDLC drastically reduces the cost and effort of fixing them later).

**3. True or False: Securing the SDLC is a one-time task done during the Testing phase.**
**Correct Answer: False** (Security must be integrated into *all* phases, from Planning to Deployment and Maintenance).

**4. Short Answer: What is the primary benefit of securing the SDLC?**
**Correct Answer:** The primary benefits are **Reduced Costs** (identifying risks early is cheaper than fixing them later), **Improved Development** (learning from previous projects), and **Better Security** (reducing the overall risks and attacks that can cause organizational issues).