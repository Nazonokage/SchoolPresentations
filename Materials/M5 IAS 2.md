# Infosec Case Analysis: Disaster Recovery

> **Course:** Information Assurance and Security  
> **Module:** 5 — Infosec Case Analysis: Disaster Recovery  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Welcome back, students! Today, we are putting your knowledge to the test with one of the most important case analyses in this subject. Your goal is to read, understand, and dissect a real-world inspired scenario involving a cloud service provider and its business partners. 

This case study focuses on the **Deep Cloud Services Disaster**. We will explore the complex web of relationships between a cloud provider, a software development company, and their mutual clients, and analyze how one flawed disaster recovery plan led to the downfall of both businesses.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Explore an existing Case Analysis about Disaster Recovery.
2.  Identify issues with some Disaster Recovery Plans.
3.  Explain your thoughts regarding the given case.

**Quick Review:**
Before we begin, can you recall the three main steps in creating an IT Disaster Recovery Plan? 
1.  Identify the activities of the system.
2.  Identify what issues or problems can hinder the activity.
3.  Determine how long we can survive without the activity.

![Cloud Computing Disaster Concept](https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### Case Study: Deep Cloud Services Disaster

**Introduction to the Players:**
**Deep Cloud Services (DCS)** is a small cloud computing provider based in the UK, akin to Amazon Web Services or Google Cloud, but smaller. They are famous for providing cloud services to companies that develop systems. Their main client is a multinational systems development company we will call **IT Corp**. 

IT Corp creates software and websites for various industries, including **schools, stores, and banks**. 

**The Relationship Web:**
IT Corp uses DCS's cloud servers for their development environment. Additionally, IT Corp *recommends* DCS to their clients. This means the end clients (the banks, stores, and schools) are also using DCS's cloud infrastructure.

> *Graphical Overview:*
> DCS (Cloud Provider) → provides services to → IT Corp (Developer) → develops systems for → Schools, Stores, Banks.

**The Problem:**
DCS's security team is small and focused primarily on serving *systems development* companies (like IT Corp). However, because IT Corp's clients (the end-users) also use DCS, DCS is now exposed to threats from *banks, schools, and retail stores*. 

The DCS security officer raised a critical concern: They are not equipped to handle a breach or disaster originating from a client's client. The chief security officer, recognizing the immense risk, resigned because the owners accepted the risk in pursuit of greater income.

**The Solution: Client Targeted Disaster Recovery Plan**
To address the glaring liability issue, the DCS owners tasked their security officers to create a Disaster Recovery Plan. The key plan they created was the **Client Targeted Disaster Recovery Plan**.

The logic of this plan was liability shifting:
*   If a client's client (e.g., a school) causes a breach, the one who will be liable is the **company that created the software** (IT Corp).
*   *Step 1:* Assuring the DCS Cloud server is live and secure.
*   *Step 2:* If a hacking or attack comes from a Client's Client (i.e., IT Corp), it will not affect DCS.
*   *Step 3:* DCS is not responsible; the responsibility lies within IT Corp.
*   *Step 4:* IT Corp will pay for the damages caused by the attack.

**The Disaster:**
A bug or vulnerability in one of the IT Corp systems sold to a store gave attackers access to the cloud servers of DCS. This damaged, stole, and corrupted the data of the companies whose systems were on the vulnerable server. 

**The Aftermath:**
DCS enacted their Disaster Recovery Plan, blaming IT Corp. However, IT Corp argued that they assumed DCS was secure based on their marketing. This led to a series of lawsuits and problems for both companies. Even if DCS was "correct" legally, IT Corp was unable to pay DCS for the damages because they were also facing massive issues with their own clients.

Ultimately, this legal and financial battle led to the **closure of both DCS and IT Corp**. Their clients were forced to migrate to other systems provided by other companies.

---

## C. Analogies and Use Cases

### The "Landlord and Tenant" Analogy
Imagine DCS is a landlord renting out secure storage units. IT Corp is a business that rents a unit to store goods for its own customers (schools, stores). 
*   IT Corp accidentally leaves a toxic chemical in the unit, which explodes and damages the entire building. 
*   The landlord (DCS) says, "It's your fault, you pay for the damages."
*   IT Corp says, "You advertised the building as safe, you should have contained the explosion."
*   Both end up bankrupt because the damages are too high for either to pay, and the landlord's insurance didn't cover this specific scenario.

### Real-World Use Case: The Target Data Breach (2013)
This case study mirrors real-life supply chain attacks. In the Target breach, hackers stole credentials from an HVAC vendor (a third party) to access Target's internal network. The vendor had legitimate access, but poor security hygiene. Target faced massive fines and reputation damage, while the vendor faced lawsuits. It highlights that when you connect to a third party, you inherit their vulnerabilities—and their clients' vulnerabilities.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **Supply Chain Risk:** Organizations inherit the risks of their vendors, and sometimes their vendor's vendors.
*   **Liability vs. Security:** A Disaster Recovery Plan cannot just be a legal liability shield. If the technical security is flawed, no amount of legal paperwork will prevent data destruction or business collapse.
*   **Risk Acceptance:** The owners of DCS accepted the risk of expanding to untrusted clients. When the risk materialized, it resulted in total business failure.
*   **The End Result:** Overconfidence in a legal document (the DRP) without proper technical safeguards is fatal.

### Frequently Asked Questions
**1. Is this a true story?**
**A:** No, this is a fictionalized case study based on real cases involving companies and disaster recovery plans that failed. It serves as an educational example of supply chain vulnerabilities.

**2. What other stories exist with real-life disasters?**
**A:** There are several IT disasters that involve loss of life or massive financial ruin:
*   **Therac-25:** A radiation therapy computer that had a software bug causing massive radiation overdoses.
*   **The Challenger Disaster:** A space rocket disaster caused by a failure in the O-rings, exacerbated by communication and management failures.
*   **Therac-25 is a prime example of how software errors can have fatal consequences.**

**3. Why didn't the Client Targeted Disaster Recovery Plan work?**
**A:** Because it focused on shifting *financial liability* rather than preventing or mitigating the actual *technical disaster*. When the disaster occurred, IT Corp couldn't pay the damages, so DCS still suffered the consequences of the data breach.

---

## E. Guided Drills / Code Projects

### Project Update: Building Your Own DRP
**Project Overview:** 
With the added knowledge from this case study, you need to include a disaster recovery plan in your ongoing project documentation. Think about the vulnerabilities exposed in the DCS case study and how you would prevent them in your own system.

**Activity Guidelines:**
*   **Format:** Individual work.
*   **Objective:** Draft at least 2 Disaster Recovery Plans that you found missing or inadequately handled in the DCS case. 
*   **Submission:** Add this to your "Recommendations" or "Disaster Recovery" section in your project document.

**Draft your plans below:**

> *Example Draft:*
> **1. Multi-Factor Authentication (MFA) for Third-Party Access:**
> *   *Risk Addressed:* A client's client compromising the core infrastructure.
> *   *Plan:* Implement mandatory MFA for all administrative and developer access to the cloud environment. This prevents attackers from using a single compromised credential from the vendor to access the main cloud servers.
>
> **2. Redundant Data Backups with Immutable Storage:**
> *   *Risk Addressed:* Data destruction and corruption by attackers.
> *   *Plan:* Implement a 3-2-1 backup strategy (3 copies of data, 2 different media types, 1 offsite). Ensure that one copy is immutable (cannot be deleted or altered) to prevent attackers from encrypting or destroying the backups during a breach.

---

## F. Skill-Building Check

### Case Analysis Quiz (25 mins)

*Based on the case study, answer the following questions to the best of your abilities.*

**1. Enumerate 5 possible threats and risks that DCS can encounter.**
*Guidance:*
1. Data breaches from an end-client's poor security.
2. Legal liability lawsuits from data loss.
3. Financial insolvency due to payouts.
4. Reputation damage causing client loss.
5. Internal mismanagement or insider threats.

**2. What do you think of DCS's Disaster Recovery Plan?**
*Guidance:* The plan is deeply flawed. It focuses on legal liability shifting rather than technical disaster prevention and mitigation. A DRP should ensure business continuity and data recovery, not just blame the client.

**3. Imagine that DCS has sufficient resources. Create at least 2 or 3 Disaster Recovery Plans that can help them against the disaster they encountered.**
*Guidance:*
1. **Network Segmentation:** Isolate client environments from each other so a compromise in one doesn't affect others.
2. **Continuous Monitoring:** Implement an Intrusion Detection System (IDS) to monitor cross-client traffic.
3. **Vendor Security Audits:** Mandate that clients like IT Corp must adhere to strict security standards before integrating with DCS.

**4. Do you think what the chief officer did, leaving DCS, was the correct decision? Explain.**
*Guidance:* Yes. The chief security officer identified a massive, unmitigated risk that the owners were willingly ignoring for profit. Leaving protects their professional integrity and career, as they cannot effectively do their job without executive support.

**5. What have you learned about this Case Analysis?**
*Guidance:* I learned that security is a shared responsibility across the supply chain. An organization cannot rely solely on legal contracts to protect its data. Technical safeguards and thorough risk assessments of third parties are essential for survival.

**6. Do you think the idea of using a disaster recovery plan for their situation is correct, or do you think they should have opted to improve their security? Explain.**
*Guidance:* They should have opted to improve their security first. A Disaster Recovery Plan is what you use *after* a disaster happens. It is not a preventative measure. They should have invested in better security (like MFA and segmentation) to *prevent* the attack, rather than relying on a DRP to clean up the mess and assign blame.