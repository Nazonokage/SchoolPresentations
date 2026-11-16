# Final Project Announcement: Securing Your Capstone

> **Course:** Information Assurance and Security  
> **Module:** 25 — Final Project: Securing Your Capstone  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Congratulations, students! You have reached the final module of this course. Throughout our journey, you have learned about risk management, secure SDLC, database security, encryption, and incident response. 

Today is not about learning new concepts. Today is about **synthesis**. You will apply everything you have learned to create a comprehensive **Security Document** for your ongoing capstone or project.

**The Goal:** You will produce a professional security document that encompasses all the topics in this course. This document will then be presented to at least one panelist with the intent of convincing them that these are the security features you are using and will use for your project.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Understand the objectives of the final security project.
2.  Demonstrate all accumulated knowledge from previous modules.

![Final Project Concept](https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### Project Requirements
Your final project is to create a single, cohesive **Security Document**. This document must apply the following elements, which we have covered throughout the course:

1.  **Disaster Recovery:** Identification of potential disasters and the corresponding recovery plans.
2.  **Key Personnel:** Identification of the roles and responsibilities of your team members.
3.  **Security Features:** Implementation and explanation of protection against XSS and SQL Injection.
4.  **Information Flow:** A secure information flow model, database security policy, and its implementation.
5.  **Version Control:** A strategy for secured versioning.
6.  **Data Protection:** The use of encryption for sensitive data (like passwords).

> **Important Note:** This document will be graded based on how well you integrate these concepts into a realistic, executable plan for your specific capstone project. It is not just about theoretical knowledge; it is about practical application.

### Required Documentation Format
To ensure a professional presentation, your final document must adhere to the following formatting guidelines:
*   **Margins:** Narrow Margins
*   **Line Spacing:** 1.5 spacing
*   **Font:** Calibri, Size 11

### Required Document Structure
Your final project documentation must be structured with the following chapters and subsections:

| Chapter | Section | Description |
| :--- | :--- | :--- |
| **I. Introduction** | **A. About the Project** | Describe the overall goal of the project (securing the capstone). |
| | **B. About the Capstone Project** | Describe the capstone project, its features, and its objectives. |
| | **C. About the Team Members** | Briefly describe the team members, advisers, and teachers, and their roles. |
| | **D. Team Member UAC & Authorization** | Enumerate the database access controls of your team members. |
| **II. Purpose of the Project** | | Explain the purpose of the project and how you are applying security principles. |
| **III. Security Features** | **A. Disaster Recovery Plans** | Describe all potential risks and the recovery plans for them. |
| | **B. XSS Protection** | Describe how you will protect your code against XSS attacks. |
| | **C. SQL Injection Protection** | Describe how you will protect your code against SQL Injection attacks. |
| | **D. Database Security Policy** | Describe your Database Security Policies. |
| | **E. Secure Information Flow Model** | Illustrate and explain the security of your information flow model (DFDs, Flow Charts, ERD). |
| | **F. Test Cases** | Provide initial test cases that will be used for testing your system. |
| | **G. Encryption** | Explain the encryption algorithm you will use for your project's passwords. |
| | **H. Secured Versioning** | Explain how you will use GitHub and provide your repository link for securing versions. |
| | **I. Securing SDLC** | Explain how you will secure your SDLC using a risk management framework. |
| **IV. Recommendations** | **A. Security Recommendations** | Include recommendations for future users of this project. |

---

## C. Analogies and Use Cases

### The "Security Consultant's Pitch" Analogy
Imagine you are an external security consultant hired by a major corporation. You have spent weeks auditing their infrastructure, identifying risks, and designing solutions. This final project document is your **Statement of Work (SOW)** and your **Final Report**. You are presenting this to the board of directors (your panelists) to convince them that your security architecture is sound, justified, and necessary for the business's survival.

### Real-World Use Case: Preparing for a Compliance Audit
In industries like finance or healthcare, companies must prove they are compliant with regulations (like PCI DSS or HIPAA). They compile a massive document called a "System Security Plan" (SSP). This SSP outlines exactly how they protect data, what happens during a disaster, who is responsible, and how they test their defenses. Your capstone security document is a scaled-down version of an SSP.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   This module is a **capstone project** that synthesizes all previous learning.
*   The deliverable is a **comprehensive Security Document** covering risk, recovery, and technical controls.
*   Documentation must follow strict formatting guidelines (Calibri 11, 1.5 spacing, narrow margins).
*   The document must be structured according to the 4 major chapters (Introduction, Purpose, Security Features, Recommendations).
*   This document will serve as the basis for your final project defense.

### Frequently Asked Questions
**1. How long should this security document be?**
**A:** There is no strict page count, but given the depth of the required sections (Disaster Recovery, XSS/SQLi, DFDs, Test Cases, Encryption, SDLC), a thorough document would likely be between 10 to 20 pages, depending on the complexity of your capstone project.

**2. Do I need to include actual code snippets in the Security Features section?**
**A:** It is highly recommended. For example, in the "Encryption" section, you can show a snippet of how you use `password_hash()` in PHP. In the "XSS Protection" section, show how you validate input.

**3. What if my team members are working on different parts?**
**A:** Even though this is a solo adaptation, if you are working in a group context, the "About the Team Members" section should reflect the real roles. For the solo version, describe your role as the sole developer and security architect.

**4. Can I reuse content from previous module activities?**
**A:** Absolutely! This document is the compilation of all your previous work. You should take the risk assessments, the DRP, the UAC policies, and the test cases you created in earlier modules and expand upon them to fit this final format.

---

## E. Guided Drills / Code Projects

### The Final Project Deliverable
**Project Overview:** 
You will compile your final Security Document for your capstone project.

**Project Guidelines:**
*   **Format:** Individual Activity (Solo Work).
*   **Objective:** Compile a comprehensive Security Document applying all course concepts.
*   **Submission:** A single document (Word/PDF) following the required structure and formatting.

**Step-by-Step Deliverable:**
Review the required chapters and ensure you have addressed every single point. 

1.  **Chapter I: Introduction** - Ensure you clearly define the scope of your capstone and introduce your team.
2.  **Chapter II: Purpose** - State clearly why security is essential for *this specific project*.
3.  **Chapter III: Security Features** - This is the core. Use subheadings for each feature. Include diagrams for your DFDs, ERDs, and Test Cases. 
4.  **Chapter IV: Recommendations** - Think about what a future developer would need to know to maintain your security posture. 

**Example Checklist before Submission:**

- [ ] Is the document formatted with Narrow Margins, 1.5 spacing, and Calibri 11?
- [ ] Does Chapter I include the Team Member UAC?
- [ ] Does Chapter III include a Disaster Recovery Plan?
- [ ] Does Chapter III include XSS and SQL Injection protection strategies?
- [ ] Does Chapter III include a Database Security Policy?
- [ ] Does Chapter III include a Secure Information Flow Model (diagrams)?
- [ ] Does Chapter III include Test Cases?
- [ ] Does Chapter III include the Encryption method used?
- [ ] Does Chapter III include a link to your GitHub repository?
- [ ] Does Chapter III include how you secured the SDLC?

---

## F. Skill-Building Check

### Final Project Self-Assessment Checklist
*Review this checklist before you submit your final project and begin your defense. Tick each box to confirm completion.*

| Requirement | Completed? | Notes |
| :--- | :--- | :--- |
| **Formatting:** Narrow Margins, 1.5 spacing, Calibri 11 applied. | ⬜ Yes / ⬜ No | |
| **Chapter I (A-D):** Introduction, About Capstone, Team Members, and UAC are complete. | ⬜ Yes / ⬜ No | |
| **Chapter II:** Purpose of the Project is clearly explained. | ⬜ Yes / ⬜ No | |
| **Chapter III (A):** Disaster Recovery Plan is outlined. | ⬜ Yes / ⬜ No | |
| **Chapter III (B):** XSS Protection strategy is described. | ⬜ Yes / ⬜ No | |
| **Chapter III (C):** SQL Injection Protection strategy is described. | ⬜ Yes / ⬜ No | |
| **Chapter III (D):** Database Security Policy is included. | ⬜ Yes / ⬜ No | |
| **Chapter III (E):** Secure Information Flow Model is illustrated and explained. | ⬜ Yes / ⬜ No | |
| **Chapter III (F):** Initial Test Cases are provided. | ⬜ Yes / ⬜ No | |
| **Chapter III (G):** Encryption algorithm is explained for passwords. | ⬜ Yes / ⬜ No | |
| **Chapter III (H):** Secured Versioning (GitHub repo link) is included. | ⬜ Yes / ⬜ No | |
| **Chapter III (I):** Securing SDLC with RMF is explained. | ⬜ Yes / ⬜ No | |
| **Chapter IV:** Security Recommendations for future users are provided. | ⬜ Yes / ⬜ No | |
| **Presentation:** Finalized slide deck ready and practiced. | ⬜ Yes / ⬜ No | |

> **Final Reminder:** Your project defense is not just about showing what you found, but convincing the panel that the organization will benefit from your security framework. Good luck, future security officers!