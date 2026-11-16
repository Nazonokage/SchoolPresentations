# Attack and Defense Methods

> **Course:** Information Assurance and Security  
> **Module:** 8 — Attack and Defense Methods  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Welcome to the most exciting part of Information Assurance! Today, we will discuss the various **attacks** you might encounter and, most importantly, how to **defend** against them. 

We will cover the theoretical landscape of cyber threats, but rest assured, we will not be performing any actual attacks in this module. Our focus is on understanding the tactics used by adversaries so we can build better defenses.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Differentiate **Attacks** from **Threats**.
2.  Describe different types of **IAS Attacks**.
3.  Describe how to **defend** against IAS Attacks.

![Cybersecurity Attack and Defense](https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### Threats vs. Attacks
These two terms are often used interchangeably, but they have distinct meanings in Information Assurance.

*   **Threat:** A category of objects, persons, or other entities that **presents a danger to an asset**. Threats are always present and can be purposeful or undirected.
    *   *Example:* Hackers purposely threaten unprotected information systems, while severe storms incidentally threaten buildings and their contents.
*   **Attack:** An intentional or unintentional act that can cause damage to or otherwise compromise information and/or the systems that support it.

### Classifying Attacks
Attacks can be categorized in several ways:

| Classification | Description | Examples |
| :--- | :--- | :--- |
| **Active vs. Passive** | **Active:** Directly changing or modifying sensitive information not intended for the attacker's use.<br>**Passive:** Casually reading or observing sensitive information not intended for the attacker's use. | *Active:* Changing a grade in a school database.<br>*Passive:* Shoulder surfing to read a password. |
| **Intentional vs. Unintentional** | **Intentional:** A deliberate act by a malicious actor.<br>**Unintentional:** Accidental actions or natural events that cause damage. | *Intentional:* A hacker breaking into a system.<br>*Unintentional:* A lightning strike causing a fire in a server room. |
| **Direct vs. Indirect** | **Direct:** The attack originates from the threat itself.<br>**Indirect:** The attack originates from a compromised system or resource that is malfunctioning or working under the control of a threat. | *Direct:* A hacker using a personal computer to break into a system.<br>*Indirect:* A hacker compromising a system and using it to attack other systems (e.g., a botnet). |

### Intentional Information Security Attacks and Threats
When we think of information security attacks, hacking usually comes to mind. However, there are many specific types of intentional attacks:

*   **Password Attack:** Attempting to access a user's account or device by determining the target's password. This can be done through social engineering (scams), hacking a password database, guessing, brute force, or using a computer to input all possible passwords.
*   **Cross-Site Scripting (XSS):** Performed by placing malicious scripts in reliable websites, mainly in the HTML part of the sites.
    *   *How it works:* An attacker sends a script-injected link to a victim. When the victim clicks it and loads the legitimate website, the browser executes the malicious script, sending private data back to the attacker.
*   **Internet of Things (IoT) Attacks:** Exploiting the convenience of interconnected devices. *Real-life example:* Linking a bank account to an e-commerce platform, creating a vulnerability if the platform is breached (this has happened before).
*   **Malware:** Viruses, worms, and trojans. This is the most common IAS threat and the primary reason we have anti-virus software.
*   **Phishing:** A type of scam where millions of emails or text messages are sent to unsuspecting users, often asking them to update their profile on a website, thereby capturing their credentials.
*   **Zero-day Exploit:** Occurs when there is new software. Because new software hasn't been tested against hackers and attacks, it is easily attacked before a patch is released.

### Unintentional Information Security Attacks and Threats
Not all threats are malicious. Many come from accidents or environmental factors:

*   **Coding Errors:** Mistakes made by developers, such as forgetting to add important validation in the code.
*   **Admin Errors:** Errors from administrators or even regular users where they accidentally modify data or information.
*   **Natural Disasters:** Storms, earthquakes, floods, etc.
*   **Power Supply Loss:** Brownouts or blackouts.
*   **ISP Issues:** Faulty telecommunications causing loss of communication or work.
*   **Peripheral Devices:** A device such as a monitor or cellphone can be viewed in a peripheral view (shoulder surfing), allowing people to exploit sensitive info like passwords.
*   **Server Issues:** Errors that can happen in servers, causing them to malfunction or stop.

### Database Security Attacks
*   **SQL Injection:** A type of attack involving entering "invalid" information into software that uses SQL. From there, attackers can manipulate or even destroy the data within. *(More in-depth database security will be covered in IAS 2).*

### Network Security Attacks
*   **Denial-of-Service (DoS) Attack:** A type of attack where attackers **flood the system, server, or network**, causing it to fail from overprocessing the requests. This can cause loss of data and a stop in operations.
*   **Man-in-the-Middle (MitM) Attack:** Occurs when an attacker **intercepts communications** between devices. They put themselves in between (such as on a router or switch) and can receive and send information/data from the connected devices.

### Information Security Defenses
Now that we know the attacks, let's discuss how to secure our systems.

#### Defenses for Intentional Attacks
*   **Intrusion Detection System (IDS):** Software that monitors activities within your network and systems. It can automatically stop attacks or warn officers. Used against DoS and MitM attacks.
*   **Information Security Management System (ISMS):** Like an IDS, but on a larger scale. It tracks employee activities and can create risk assessments.
*   **Anti-Virus:** Software that focuses on preventing and removing malware.
*   **Firewalls:** Systems that are crucial to a network, preventing malicious hackers from accessing the network or devices.
*   **Software Updates:** Patches for software to remove faults, removing zero-day exploits.
*   **SQL Injection Defense:** Requires learning SQL Injection itself and how to protect against it. (More in IAS 2).

#### Defenses for Unintentional Attacks
*   **Training and Awareness:** Train employees/users on how to properly protect accounts through simulations/exercises or seminars. This can also lessen admin errors and peripheral device issues.
*   **Natural Disasters:** We cannot avoid these, but careful planning and proper safety measures can reduce damage to almost negligible. Use fire drills, training, proper placement of tools/equipment, and place electrical machines on a higher floor to avoid flood damage.
*   **Power Supply Loss / ISP Loss / Server Issues:** Fix these by having generators for power, a backup ISP if available, and proper server usage with regular backups.

---

## C. Analogies and Use Cases

### The "High-Security Vault" Analogy
Imagine a bank's high-security vault.
*   **Threat:** A skilled group of robbers (intentional) or a massive earthquake (unintentional).
*   **Attack:** The robbers drilling the lock (Active/Direct) or an employee accidentally leaving the vault door open (Unintentional).
*   **Defense:** Armed guards (IDS), reinforced steel walls (Firewalls), and earthquake-proof foundations (Disaster planning).

### Real-World Use Case: The Coffee Shop with Public Wi-Fi
A local coffee shop offers free Wi-Fi to customers.
*   *Risk Identified (from previous module):* Customer data interception.
*   *Type of Attack:* **Man-in-the-Middle (MitM)**. An attacker sits in the coffee shop, sets up a fake Wi-Fi hotspot named "CoffeeShop_Free_WiFi," and intercepts all traffic.
*   *Defense:* The coffee shop implements a **Firewall** and uses strong encryption (WPA3) for their actual network. They also post signs advising customers to use a **VPN** (Virtual Private Network). Furthermore, they train their baristas to spot suspicious individuals who might be physically tampering with the router.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **Threats** are potential dangers; **Attacks** are the actual acts that cause harm.
*   Attacks can be **Active/Passive**, **Intentional/Unintentional**, or **Direct/Indirect**.
*   Common intentional attacks include **Malware, Phishing, SQL Injection, XSS, and DoS**.
*   Unintentional threats include **Natural Disasters, Power Loss, and Human Error**.
*   A robust defense strategy requires a combination of **Technical Controls** (Firewalls, IDS, Antivirus), **Administrative Controls** (Training, Policies), and **Physical Controls** (Equipment placement).

### Frequently Asked Questions
**1. What is the main difference between a threat and an attack?**
**A:** A threat is the *source* of potential danger (e.g., a hacker, a storm). An attack is the *action* that exploits a vulnerability to cause damage (e.g., a hacker breaking in, a storm flooding a server room).

**2. Why are unintentional attacks important to consider?**
**A:** Unintentional attacks (like coding errors or natural disasters) can cause just as much damage as intentional attacks. They are often overlooked, making them a critical blind spot for organizations.

**3. How do firewalls and IDS differ in their defense?**
**A:** A firewall acts like a security guard at the door, blocking unauthorized traffic based on predefined rules. An IDS acts like a security camera, monitoring the network for suspicious activity and alerting the security team if something looks wrong.

**4. What is a Zero-day exploit?**
**A:** A Zero-day exploit is an attack that targets a newly discovered vulnerability in software that the vendor has not yet patched. Since there is no "day zero" patch available, it is highly dangerous.

**5. Can we stop all attacks?**
**A:** No. It is impossible to stop all attacks, especially unintentional ones like natural disasters. The goal of Information Assurance is not to achieve perfect security, but to *manage risk* and ensure that the organization can recover quickly from any attack that occurs.

---

## E. Guided Drills / Code Projects

### Solo Project: Attack-Defense Mapping
**Project Overview:** 
For Module 8, you will expand your ongoing project by mapping specific **Attacks** and **Defenses** to the risks you identified in Module 7. 

> *Note: While this was originally designed as a group discussion, we are adapting it as a **solo activity**. You will act as the sole security consultant for this assignment.*

**Project Guidelines:**
*   **Format:** Individual work.
*   **Objective:** For every risk in your Module 7 table, identify the type of attack and propose a specific defense.
*   **Submission:** Add this mapping to your ongoing project documentation.

**Step-by-Step Deliverable:**
1.  **Review your Risk Matrix** from Module 7 (e.g., Flooding, Hacking, Hardware Failure).
2.  **Classify the Attack** (e.g., Active/Passive, Intentional/Unintentional).
3.  **Propose a Defense** based on the defenses discussed in this module (IDS, Firewall, Training, etc.).
4.  **Fill in the table below** (continue on a separate sheet if needed):

| Risk (from Module 7) | Type of Attack (Active/Passive, Intentional/Unintentional) | Proposed Defense |
| :--- | :--- | :--- |
| *Example: Server Room Flooding* | *Unintentional* | *Physical: Place server on a higher floor, install water sensors.* |
| *Example: Database Hacking* | *Active, Intentional* | *Technical: Firewall, IDS, Software Updates. Administrative: Training.* |
| *Example: Employee Data Leak* | *Passive, Unintentional* | *Administrative: Training and Awareness, ISMS monitoring.* |
| *Your Risk 1* | | |
| *Your Risk 2* | | |
| *Your Risk 3* | | |

---

## F. Skill-Building Check

### Part 1: Identification
*Identify the correct term based on the definitions provided.*

1.  Refers to computer viruses, worms, and trojans. 
    **Answer: Malware**
2.  An act of sending out multiple scam emails and text messages.
    **Answer: Phishing**
3.  A part of a network securing against unauthorized access.
    **Answer: Firewall**
4.  A type of attack flooding the system with multiple requests, causing crashes.
    **Answer: Denial-of-Service (DoS)**
5.  This is a system that monitors and detects unauthorized access to your network and systems.
    **Answer: Intrusion Detection System (IDS)**

### Part 2: Multiple Choice

**6. What type of attack involves modifying or changing sensitive information not intended for the attacker's use?**
A. Passive Attack
B. Active Attack
C. Indirect Attack
D. Unintentional Attack
**Correct Answer: B** (Active attacks involve modification, while passive attacks involve reading/observing).

**7. Which of the following is an example of an Unintentional Information Security Threat?**
A. A hacker deploying ransomware.
B. A phishing email.
C. A power supply loss (brownout).
D. A SQL Injection attack.
**Correct Answer: C** (Power loss is an unintentional environmental threat. The others are intentional attacks).

**8. What does a Man-in-the-Middle (MitM) attack do?**
A. Floods a system with requests to crash it.
B. Places malicious scripts on reliable websites.
C. Intercepts communications between devices to receive and send data.
D. Guesses a user's password through brute force.
**Correct Answer: C** (MitM places the attacker in the middle of a communication stream).

**9. Which defense mechanism is specifically designed to monitor and detect unauthorized access, and can automatically stop an attack?**
A. Anti-virus
B. Intrusion Detection System (IDS)
C. Firewall
D. Software Update
**Correct Answer: B** (An IDS monitors and detects, whereas a firewall primarily blocks).

**10. Why are new software applications particularly vulnerable to Zero-day exploits?**
A. They are too expensive to secure.
B. They haven't been tested against hackers, so vulnerabilities are unknown.
C. They are not compatible with firewalls.
D. They require too much training to use.
**Correct Answer: B** (A zero-day exploit targets a vulnerability that is unknown to the software vendor, hence "zero days" of warning).