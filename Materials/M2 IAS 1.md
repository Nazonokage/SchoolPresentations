# Introduction to Information Assurance and Security (IAS)

> **Course:** Information Assurance and Security 1  
> **Module:** 2 — Introduction to IAS  
> **Learning Format:** Individual & Group Activities

---

## A. Lesson Preview & Review

Welcome to Module 2 of Information Assurance and Security! 

In today's world, technology is woven into every aspect of our daily lives—from the moment we wake up to alarms, to checking the news on our phones, to working, learning, and communicating with loved ones. As future IT professionals, it is your job to secure these technologies so that our daily routines remain undisturbed. 

The constant emergence of cyber vulnerabilities demands robust countermeasures. This module introduces you to the foundational concepts of Information Assurance (IAS), the evolving threat landscape, and the preliminary requirements for your course project.

**Learning Targets:**
By the end of this module, you will be able to:
1. Describe information assurance and security, and threats.
2. Identify different kinds of security threats.
3. Discuss the importance of knowing security threats.
4. Discuss the preliminaries about the project for the subject.

![Cybersecurity concept](https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### Core Concepts of Information Assurance
**Information Assurance (IA)** is defined as the set of measures intended to protect and defend information and information systems by ensuring their **availability, integrity, authentication, confidentiality, and non-repudiation**. 

It is the practice of:
*   Assuring information.
*   Managing risks related to the use, processing, storage, and transmission of information or data.
*   Protecting the systems and processes used for those purposes.

### The Importance of Information Assurance
The invention and widespread usage of computers gave rise to new requirements for safeguarding data transfers among networked computer systems. 

*   **Computer Security:** Initially, "computer security" focused on stand-alone computer security. However, it was unable to safeguard data during processing, storing, or transmission across systems.
*   **Information Security:** This realization gave rise to "information security," expanding the mission of "information protection."
*   **Information Assurance (IA):** IA evolved to safeguard information during transmission, processing, or storage within intricate and/or scattered computer networks. IA incorporates dynamic information protection techniques that can identify assaults and enable a defense against them.

> **Pro Tip:** Information Assurance professionals consider corporate governance concerns including privacy, regulatory compliance, audits, business continuity, and disaster recovery. IA is viewed as the business result of information risk management and as a superset of information security.

### The Information Assurance Process
The IA process follows a structured, cyclical approach to managing risks:

1.  **Enumeration and Classification:** Identify and classify the information assets to be protected.
2.  **Risk Assessment:** Perform a risk assessment for those assets.
3.  **Vulnerability Identification:** Determine vulnerabilities in the information assets to enumerate the threats capable of exploiting them.
4.  **Probability Assessment:** Consider the probability of a threat exploiting a vulnerability in an asset.
5.  **Impact Assessment:** Evaluate the impact of a threat exploiting a vulnerability, usually measured in terms of cost to the asset's stakeholders.
6.  **Total Risk Calculation:** The sum of the products of the threats' impact and the probability of their occurring is the total risk to the information asset.

```text
[Enumeration] --> [Risk Assessment] --> [Vulnerabilities] --> [Probability] --> [Impact] --> [Total Risk]
```

### Five Information Assurance Pillars
These pillars serve as the fundamental cornerstones for guaranteeing confidence and integrity in information systems.

| Pillar | Definition | Focus Areas |
| :--- | :--- | :--- |
| **Integrity** | Protecting against improper information modification or damage. | Non-repudiation and authenticity. |
| **Confidentiality** | Preserving authorized restrictions on access and disclosure. | Personal privacy and proprietary information. |
| **Availability** | Ensuring timely and reliable access to and use of information. | System uptime and reliability. |
| **Authentication** | Verifying the identity of a user, process, or device. | Access control and identity verification. |
| **Non-repudiation** | Ensuring that a party cannot deny the authenticity of their signature or message. | Proof of origin and delivery. |

### Information Assurance Strategy
To effectively implement IA, organizations should adopt a multi-layered strategy:
1.  Cyber security awareness and education.
2.  Strong cryptography.
3.  Good security-enabled commercial information technology.
4.  An enabling global Security Management Infrastructure.
5.  A civil defense infrastructure equipped with attack sensing, warning capability, and a coordinated response mechanism.

### Information Security vs. Information Assurance

**Information Security** (sometimes shortened to "InfoSec") is the practice of defending information from unauthorized access, use, disclosure, disruption, modification, perusal, inspection, recording, or destruction. It is the state of being protected against the unauthorized use of information.

There are **two major aspects** of Information Security:

1.  **IT Security (Computer Security):** Information security applied to technology, most often some form of a computer system.
2.  **Information Assurance:** The act of ensuring that data is not lost when critical issues arise. These issues include natural disasters, computer/server malfunction, physical theft, or any instance where data has the potential of being lost.

### Understanding Security Threats
A **Threat** is a malicious act that aims to corrupt or steal data, or disrupt an organization's systems or the entire organization. 

Common security threats range from insider threats to advanced persistent threats. If an organization's internal security team is not informed and prepared, these risks could bring the organization to its knees.

#### Top 10 Security Threats (2022 Landscape)

1.  **Social Engineering:** An attack vector that focuses on interpersonal interactions. It frequently entails persuading people to disregard security norms and best practices to gain illegal access to systems, networks, or physical locations. 
    *   *Statistic:* 85% of all data breaches involve human interaction (Verizon DBIR).
2.  **Third-Party Exposure:** Damages alleged by clients or other third parties for which the policyholder firm may be liable. Hackers penetrate a client's computer system and use the information found there to launch attacks.
    *   *Example:* A 2021 breach at a third-party contractor, Socialarks, leaked personal data from over 214 million Facebook, Instagram, and LinkedIn accounts.
3.  **Configuration Mistakes:** Even very effective security systems almost always have a flaw in the installation or configuration. 
    *   *Statistic:* Rapid7 found vulnerable misconfigurations in 80% of external penetration tests, rising to 96% when the attacker had inside system access.
4.  **Poor Cyber Hygiene:** Customary routines and behaviors involving the use of technology, such as avoiding open WiFi networks and using a VPN or multi-factor authentication (MFA).
    *   *Statistic:* Nearly 60% of organizations rely on human memory to manage passwords, and 42% use sticky notes. 54% of IT professionals do not require MFA for company accounts.
5.  **Cloud Vulnerabilities:** Contrary to popular belief, cloud vulnerabilities have increased 150% over the past five years (IBM). Over 90% of the 29,000 breaches examined in Verizon's DBIR were due to web app breaches.
6.  **Mobile Device Vulnerabilities:** The COVID-19 epidemic resulted in an increase in mobile device usage and remote work, leading to an uptick in BYOD (Bring Your Own Device) policies.
    *   *Statistic:* 46% of companies experienced a security incident involving a malicious mobile application downloaded by an employee (Check Point).
7.  **Internet of Things (IoT):** A system of interrelated computing devices, mechanical and digital machines, objects, animals, or people provided with unique identifiers (UIDs) and the ability to transfer data over a network without requiring human-to-human or human-to-computer interaction.
    *   *Statistic:* Over 1.5 billion breaches occurred between January and June of 2021 as attacks on smart devices increased sharply.
8.  **Ransomware:** A subset of malware that locks the data on a victim's computer using encryption and demands payment before the data is unlocked.
    *   *Impact:* 66% of companies suffered significant revenue loss, and 29% were forced to remove jobs following an attack (Cybereason).
9.  **Poor Data Management:** Consumer-generated data doubles every four years, but more than half of it is never used or evaluated. Data becomes exposed to cyber attacks as a result of confusion caused by mountains of excess data.
    *   *Example:* In 2018, Aetna was ordered to pay $17 million after mailing sensitive health information in the wrong type of envelope.
10. **Inadequate Post-Attack Procedures:** After a cyberattack, security flaws need to be fixed right away.
    *   *Statistic:* 80% of victims that paid the ransom reported that they quickly came under another attack. 60% of cyber attacks could have been avoided if a patch had been issued (Cybereason).

![Threat landscape](https://images.unsplash.com/photo-1563206767-5b1d972b9c9a?auto=format&fit=crop&w=1200&q=80)

---

## C. Analogies and Use Cases

### The Smart Home Analogy
Think of an organization's IT infrastructure as a "Smart Home." 
*   **Availability** is ensuring the electricity and internet stay on so you can use your devices.
*   **Integrity** is ensuring no one breaks down your doors or messes with your smart locks.
*   **Confidentiality** is ensuring the curtains are drawn so outsiders can't see inside.
*   **Authentication** is using your fingerprint or keycode to unlock the front door.
*   **Non-repudiation** is the security camera footage that proves who entered and exited, meaning no one can deny they were there.

If a burglar tricks you into opening the door by pretending to be a delivery driver, that is **Social Engineering** (exploiting human trust rather than breaking the lock).

### Real-World Use Cases
1.  **Healthcare Industry:** A hospital relies heavily on Information Assurance to protect patient records (Confidentiality) while ensuring doctors can access critical life-saving data instantly during an emergency (Availability). A ransomware attack on a hospital is a perfect example of a threat that exploits poor post-attack procedures and causes massive disruption.
2.  **E-Commerce:** An online store must safeguard customer credit card information. They rely on strong cryptography and compliance with PCI DSS standards. If they suffer a third-party exposure, they risk massive reputational damage and regulatory fines.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **Information Assurance (IA)** goes beyond just securing data; it encompasses risk management, business continuity, and disaster recovery.
*   The **Five Pillars** of IA are Availability, Integrity, Authentication, Confidentiality, and Non-repudiation.
*   The **IA Process** is a cyclical risk assessment model that starts with asset enumeration and ends with calculating total risk.
*   **Human error** (Social Engineering, Poor Cyber Hygiene) is the root cause of the vast majority of data breaches (85%).
*   **Cyber threats** evolve constantly. Organizations must maintain vigilance, patch systems promptly, and foster a culture of security awareness.

### Frequently Asked Questions
**1. What is the main difference between Information Security and Information Assurance?**
While Information Security focuses primarily on protecting data from unauthorized access (IT Security), Information Assurance is broader. IA ensures data is not lost when critical issues arise, such as natural disasters, server malfunctions, or physical theft. IA is a superset of Information Security.

**2. Why is Social Engineering considered so dangerous?**
Social Engineering is dangerous because it relies on human error rather than technical vulnerabilities. Cybercriminals find it easier to trick an employee into revealing credentials than to hack through a sophisticated firewall. 

**3. What is the "CIA Triad" and how does it relate to IA?**
The CIA Triad stands for Confidentiality, Integrity, and Availability. It is a fundamental model in InfoSec. Information Assurance incorporates the CIA Triad but adds two additional pillars: Authentication and Non-repudiation.

**4. How can organizations protect themselves against Ransomware?**
Organizations can mitigate ransomware risks by conducting regular data backups, keeping systems patched, implementing Multi-Factor Authentication (MFA), and conducting continuous cybersecurity awareness training for employees.

---

## E. Guided Drills / Code Projects

### Course Project: Application of Information Security in a Business
**Project Overview:** 
For this module, you will begin a continuous group project where you apply the principles of Information Assurance and Security to an existing business (preferably one you or a group member are affiliated with, such as a school, local shop, or family business).

**Project Guidelines:**
*   **Group Size:** 3–5 members.
*   **Method of Updating:** The project will be updated for every lesson/module. You can update it anytime as you learn new concepts.
*   **Objective:** 
    1. Identify the threats and assets of the chosen business.
    2. Assess risks and scale their likelihood and impact.
    3. Provide recommendations and conclusions for the client.
*   **Sample Project Title:** *Application of Information Security in School Management*
*   **Milestones:** 
    *   **Pre-Defense:** During the second half of the term.
    *   **Final Defense:** At the end of the term. You will need to convince the panel (your teacher) that the organization needs your IAS recommendations.

**Step-by-Step Deliverable for Module 2:**
1.  **Form your group** (3-5 members).
2.  **Choose a business** you are familiar with.
3.  **Draft an Asset Inventory:** List 3-5 critical information assets (e.g., customer database, student records, payroll system).
4.  **Identify Top Threats:** Based on the "Top 10 Security Threats" discussed in this module, identify which 3 are most likely to affect your chosen business. Justify your answer.

---

## F. Skill-Building Check

### Part 1: Identification
*Fill in the blank with the correct term based on the definitions provided in this module.*

1.  ___________ it covers protecting against improper information modification or damage, and includes ensuring information non-repudiation and authenticity.
2.  ___________ It is considered as malicious acts, to corrupt or steal data or disrupt an organization's systems or the entire organization.
3.  ___________ it is to preserve authorized restrictions on access and disclosure, including means for protecting personal privacy and proprietary information.
4.  ___________ it is the set of measures intended to protect and defend information and information systems by ensuring their availability, integrity, authentication, confidentiality, and non-repudiation.
5.  ___________ it is to ensure timely and reliable access to and use of information.

**Answers:**
1. **Integrity** 
2. **Threat** 
3. **Confidentiality** 
4. **Information Assurance** 
5. **Availability**

### Part 2: Check for Understanding (Essay)

**1. In any organization, why do we need IAS?**
*Guidance:* Your answer should discuss the reliance on technology in daily operations, the need to protect data from unauthorized access, the importance of maintaining business continuity (availability), and the necessity of managing evolving cyber vulnerabilities to prevent financial loss, reputational damage, and operational disruption.

**2. Explain Social Engineering, and provide an example based on your understanding/experience.**
*Guidance:* Social Engineering is a non-technical attack vector that relies on human interaction and psychological manipulation to trick individuals into breaking security protocols. Examples could include phishing emails, pretexting (pretending to be an IT support technician to get a password), or baiting (leaving a malware-infected USB drive in a parking lot).