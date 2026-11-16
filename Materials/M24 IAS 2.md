# Introduction to Cyberforensics and IAS in Other Industries

> **Course:** Information Assurance and Security  
> **Module:** 24 — Introduction to Cyberforensics and IAS in Other Industries  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Congratulations, students! We are nearing the end of our journey through Information Assurance and Security. Today, we venture into a fascinating and highly relevant field: **Cyberforensics**. 

We will explore how technology has become a critical component in gathering evidence and solving crimes. We will also touch on how IAS principles apply to industries far beyond software development, and we will discuss the important role of **Ethical Hacking**.

**Quick Review:**
Before we dive into the main lesson, what are your thoughts about Ethical Hacking? 
*   *Hint:* Think back to our modules on SQL Injection and XSS. Those techniques aren't just for attackers; they are used by ethical hackers to test system defenses *before* a real attack occurs.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Understand the concept of cyberforensics.
2.  Understand how IAS operates in industries outside of IT.
3.  Explain the importance of Ethical Hacking.

![Cyberforensics Concept](https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### What is Cyberforensics?
Crime has existed since ancient times, and technology has helped us reduce and solve crimes. **Cyberforensics** is the application of technology to investigate and solve digital crimes. It involves recovering, analyzing, and preserving digital evidence from devices and networks.

#### 1. Data Recovery
When we talk about recovery of files, we mean data that has been completely deleted from devices like smartphones, computers, or even the internet (using tools like the Wayback Machine). 

*   **Why it matters:** Criminals often delete incriminating evidence like social media posts, text messages, or call logs. However, most suspects are unaware that these files are often recoverable. This makes digital forensics a powerful tool for law enforcement.
*   **Tools used by law enforcement:**
    *   AccessData
    *   Magnet Forensics
    *   BlackBag Technologies
    *   *Note: These tools are highly powerful and expensive, usually only affordable by law enforcement agencies.*

#### 2. Tracking and Tracing
Did you know your phone is almost always connected to the internet or cellular network, even if GPS is turned off? As long as your phone is connected to any cell network, it can receive signals, and **you can be tracked and traced**.

*   **How it works:** Investigators obtain the phone's cell activity and history. They can also use **triangulation**—using other cellular devices near a crime scene to pinpoint the location of a suspect's device. If the suspect's device is within the triangulated area, it can be used as evidence placing them at the scene.

#### 3. Data Privacy vs. Investigation
You might be thinking, "Doesn't the Data Privacy Act protect us?" Yes, it does. However, if you voluntarily surrender your devices for searching, the investigative team has the right to search them. Furthermore, even if you don't surrender your device, law enforcement can issue a **search warrant** to legally obtain and search your devices.

### IAS in Other Industries
We have used the term "organization" a lot in this course. This is because IAS is applicable in a lot of industries, not just IT or software development. 

*   Think of any company or business—almost all of them rely on technology to improve operations, and with that, they all need IAS.
*   Risk management, threat identification, and disaster recovery are universal needs.
*   This is why Information Security jobs are considered some of the highest-paid jobs in the world.

### Ethical Hacking
We have been discussing SQL Injection, XSS, and automated testing throughout this course. You may not have realized it, but these are actually forms of **Ethical Hacking**.

*   **Purpose:** The main purpose of ethical hacking is to test the security of systems *before* they are deployed for use.
*   **Difference from Malicious Hacking:** Ethical hacking varies from traditional hacking in that it is an **allowed activity** by the developers and users of the system, done for the sake of knowing if there are vulnerabilities that need to be fixed.

> **Pro Tip:** Always ensure you have explicit written permission before performing any security testing. Unauthorized testing, even with good intentions, is illegal.

---

## C. Analogies and Use Cases

### The "Digital Crime Scene" Analogy
Think of a cyberforensic investigator as a detective at a physical crime scene. 
*   A burglar might wipe their fingerprints off a doorknob (deleting a file), but investigators can still find DNA or fibers (recovering metadata or deleted files from a hard drive). 
*   The burglar might park their car down the street to avoid detection (turning off GPS), but traffic cameras or witnesses (cell tower triangulation) can still place them at the scene. 

### Real-World Use Case: Solving a Robbery with Cell Data
A bank is robbed. The suspect claims they were miles away at the time of the crime. However, cyberforensics investigators obtain a warrant for the suspect's cell phone records. They use **triangulation** from three nearby cell towers to prove that the suspect's phone was within 50 meters of the bank at the exact time of the robbery. The digital footprint left by the phone became the key evidence that led to a conviction.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **Cyberforensics** uses technology to recover deleted data and track digital footprints to solve crimes.
*   **Data Recovery** and **Tracking/Triangulation** are powerful tools used by law enforcement.
*   **Data Privacy** is important, but law enforcement can bypass it with a search warrant or voluntary surrender of devices.
*   **IAS applies to all industries**, not just IT, making security professionals highly valuable.
*   **Ethical Hacking** involves using hacking techniques (like SQLi and XSS) with authorized permission to test and improve security.

### Frequently Asked Questions
**1. Are there other cyberforensic acts done for identifying criminals?**
**A:** Yes, there are many. Investigators can track IP addresses, website accesses, email headers, and even use advanced malware analysis to trace attackers. Cyberforensics is a broad field; you just have to know how to use the tools.

**2. Can my phone be tracked if I turn off GPS?**
**A:** Yes. As long as your phone is connected to a cellular network (to make calls or send texts), the network can estimate your location based on your proximity to cell towers.

**3. What is the difference between a white-hat and a black-hat hacker?**
**A:** A white-hat hacker (ethical hacker) has explicit authorization to test systems and reports vulnerabilities so they can be fixed. A black-hat hacker acts without authorization for personal gain or malicious intent.

**4. How do I protect myself from cyberforensics if I am innocent?**
**A:** You don't need to "protect" yourself, but you should be aware that digital footprints are permanent. Always practice good cyber hygiene and avoid engaging in illegal activities online.

---

## E. Guided Drills / Code Projects

### Solo Project Update: Authorization of Ethical Hacking
**Project Overview:** 
For Module 24, you will update your ongoing capstone project documentation to explicitly state that the security testing performed (XSS, SQL Injection) was authorized and ethical.

> *Note: This was originally designed as a group activity. We are adapting it as a **solo activity**. You will act as the sole developer and security tester for this assignment.*

**Project Guidelines:**
*   **Format:** Individual work.
*   **Objective:** Create a formal "Authorization of Testing" statement or section in your project document. This protects you and ensures clear ethical boundaries.
*   **Submission:** Add this to your project documentation.

**Step-by-Step Deliverable:**
Draft a statement in your project documentation that includes the following elements:

1.  **Acknowledgment:** State that XSS and SQL Injection testing was included in your development process.
2.  **Statement of Authorization:** Explicitly mention that these tests were allowed and authorized by your adviser and teacher.
3.  **Scope of Testing:** Briefly describe what was tested (e.g., login forms, search fields).
4.  **Ethical Declaration:** Affirm that the testing was done solely to identify and fix vulnerabilities, not to exploit the system maliciously.

**Draft your statement below:**

> *Example Draft:*
> **Authorization of Security Testing**
> During the development of this capstone project, security testing was conducted using techniques such as Cross-Site Scripting (XSS) and SQL Injection. These tests were performed with the full knowledge and explicit authorization of the project adviser and course instructor. The purpose of this testing was strictly for educational and defensive purposes, to identify and mitigate potential vulnerabilities within the system before deployment. No unauthorized access or malicious exploitation was performed.

---

## F. Skill-Building Check

### Check for Understanding (10 mins Quiz)

*Answer the following questions with the best of your abilities.*

**1. How are we able to perform cyberforensics if there is a data privacy act?**
*Guidance:* Cyberforensics can be performed despite the Data Privacy Act through legal means. The law allows for the investigation of crimes if a **search warrant** is issued by a court. Additionally, if a suspect voluntarily surrenders their device, the data privacy protection is waived for that investigation. The Data Privacy Act protects law-abiding citizens but does not shield criminals from the lawful collection of evidence.

**2. Give an example and describe how IAS can be used for your school's assets.**
*Guidance:* (Example) A school has a database of student grades, financial records, and employee data. IAS can be applied by implementing **Role-Based Access Control (RBAC)** so only authorized staff can view grades, and encryption for financial records. Furthermore, the school should have a **Disaster Recovery Plan** for their servers in case of a flood or fire. Cyberforensics could also be used to track down the source if a student's grade was tampered with digitally.

**3. Multiple Choice: Which of the following is a tool used by law enforcement for data recovery?**
A. Photoshop
B. Magnet Forensics
C. Google Drive
D. Microsoft Word
**Correct Answer: B** (Magnet Forensics is a specialized digital forensics tool).

**4. True or False: Ethical hacking involves unauthorized access to a system to test its security.**
**Correct Answer: False** (Ethical hacking requires explicit authorization. Unauthorized access is illegal, regardless of intent).