# Risk Management: Identification, Assessment, and Treatment

> **Course:** Information Assurance and Security 2  
> **Module:** 2 — Risk Management Fundamentals  
> **Learning Format:** Individual & Group Activities

---

## A. Lesson Preview & Review

Welcome to Information Assurance and Security 2! In the world of computer security—whether during operations, software development, or system usage—risks will always exist, no matter how secure your systems appear to be. 

Today, we will revisit and deepen our understanding of **Risk Management**. We will break down the five-step process of managing risks, starting from identifying assets and vulnerabilities to communicating with executives and re-evaluating our strategies.

**Key Definition:**
*   **Risk:** Potential events that can occur and disrupt, corrupt, or destroy operations in a given situation.

![Risk Management Concept](https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### Step 1: Identification
Our goal in this step is to identify the **assets, vulnerabilities, threats, and controls** of our organization. By identifying these, we can easily understand the risks associated with our operations or software development.

**1. Identifying Assets**
We look at what we **own** in our organization or software development.
*   *Examples:* Data, Computers, Servers, Office Space, and Intellectual Property.
*   *Software Development Focus:* Intellectual property is considered the main asset. This includes your code, design, process, artwork, menu styles, etc.

**2. Identifying Vulnerabilities**
We look at the **weaknesses** in our operations, organization, or software development. Regardless of how good your operations are, there will always be weaknesses.
*   *Company Vulnerabilities:* Few to no CCTVs, no proper locks, no backup power.
*   *Developer Vulnerabilities:* Obsolete programming languages, older encryption (e.g., MD5 or SHA1), older development software, no backup storage or recovery.
*   *Security Officer Vulnerabilities:* Obsolete software, security systems, or methods.

> **Pro Tip:** You may think these vulnerabilities are small (like using older encryption), but if you use older technology, it is highly probable that attackers already know how to decrypt your security.

**3. Identifying Threats**
We look at the scenarios or events that can **attack** the organization or software development directly or indirectly.
*   *Indirect Threats:* Viruses, accidents, forces of nature (earthquakes, tsunamis).
*   *Direct Threats:* Hackers and thieves.

**4. Identifying Controls**
We look at our organization's assets and the vulnerabilities that were given **fixes or protection**. This is done by looking at the risks we have already managed and improving upon them.
*   *Example:* If we find out that the number one cause of data accidents is a specific group of employees from a department, we simply deny them access to that data. We then assess if this solution hinders the overall operations of the organization.

### Step 2: Assessing
In this step, we use a generalized idea to assess things. We determine the **probability or likelihood** that the risk will occur, and then determine the **severity, impact, or cost** that the risk can do. 

The higher the likelihood and impact, the more damaging the risk. The more damaging the risk, the more reason to focus on mitigating or removing it. You can use a **Risk Matrix** to understand this further.

![Risk Matrix Example](https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80)

### Step 3: Treatment
When treating your risks, it is about the way we control them. There are 5 primary methods for risk treatment:

| Treatment Method | Description | Example |
| :--- | :--- | :--- |
| **1. Remediation** | Completely removing the risk. Normally this is impossible, because to remove the risk entirely, it needs to remove the asset itself (which is not ideal). | Eliminating a vulnerable software entirely. |
| **2. Reduction** | If the risk cannot be remediated, you can at least reduce or mitigate it. | If a fire occurs, it can be reduced by doing fire drills and adding fire extinguishers. |
| **3. Transfer** | Transferring the cost of the risk to a third party. | Purchasing insurance or transferring liability to a parent company. |
| **4. Accept** | You should always avoid this unless it is unavoidable. Some very little accidents or risks can still happen and are unavoidable. | Accepting the risk of a minor power flicker because backup generators are too expensive. |
| **5. Avoid** | The highest goal in risk treatment. This is by entirely avoiding the risk, which is also rare in organizations. | Shutting down a dangerous project entirely. |

### Step 4: Communication
The 4th step is about communicating with the people in charge of the organization. Their final decision is usually what must be followed. After presenting the risks, how they are assessed, and how they will be treated, the higher-ups or owners/stakeholders of the organization will decide if they wish to treat the risks.

### Step 5: Re-identification or Rinse-and-Repeat
The 5th step is repeating the risk management process again. This way, you can re-evaluate existing risks, regardless of the treatment placed on them. 
*   *Example:* You managed to completely avoid an Operating System Risk by using a Linux operating system. But after a while, employees are unaware of how to use Linux, causing delays and setbacks. You must reassess and treat the new risk (usability) that emerged.

### IT Development
These 5 steps of risk management can be applied in software development. For every step of your Software Development Life Cycle (SDLC), there are risks that can be encountered, and these risks must undergo the risk management process.

---

## C. Analogies and Use Cases

### The "Home Security Audit" Analogy
Think of Risk Management as a home security audit:
*   **Assets:** Your family, jewelry, TV, and computers.
*   **Vulnerabilities:** A broken window lock, an old alarm system, or a dark backyard.
*   **Threats:** Burglars (Direct) or a tree falling on the roof (Indirect).
*   **Controls:** Installing a new deadbolt, adding motion-sensor lights.
*   **Treatment Options:**
    *   *Reduction:* Adding a security camera to deter thieves.
    *   *Transfer:* Buying homeowners insurance.
    *   *Accept:* Deciding not to reinforce the garage door because you park outside anyway.

### Real-World Use Case: Software Development Cycle
A development team is building a new banking app.
1.  **Identification:** They identify the codebase (Asset), a lack of input validation (Vulnerability), SQL Injection (Threat), and a Web Application Firewall (Control).
2.  **Assessment:** They score the SQL Injection risk as High Likelihood and Catastrophic Impact.
3.  **Treatment:** They choose **Reduction** by implementing parameterized queries and hiring a penetration tester.
4.  **Communication:** They present the cost of the penetration tester to the CFO, who approves the budget.
5.  **Re-identification:** Six months later, a new hacking technique emerges. They restart the process to assess if their current controls are still sufficient.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   Risk Management is a cyclical, 5-step process: Identification, Assessing, Treatment, Communication, and Re-identification.
*   Assets are what you own; Vulnerabilities are your weaknesses; Threats are the attackers; Controls are your protections.
*   The 5 Risk Treatment Options are Remediation, Reduction, Transfer, Accept, and Avoid.
*   The Risk Management process is never truly finished; it must be continuously repeated to address new and changing risks.

### Frequently Asked Questions
**1. Is it possible to remove all risks?**
**A:** No, it is actually impossible to remove all risks. The idea is to minimize them so that there can be no huge damage to the organization. 

**2. Are all risk management processes 5 steps?**
**A:** The 5-step process presented in this module is the most generalized way of performing risk management. It is an excellent template if you have a small organization or project that requires risk management. Larger frameworks (like the NIST RMF) break these steps down into more granular sub-steps.

---

## E. Guided Drills / Code Projects

### Project Activity: Capstone Risk Management Exercise
**Activity Announcement:** 
This is a practical group update. You are required to apply the 5-step Risk Management process to a specific, realistic scenario. 

**Scenario:**
Your group is developing a Capstone Project. The risk is that **you won't be able to finish the capstone 2 because your developer is unavailable in the development phase.** 

**Instructions:**
Write a 5-step risk management plan to address this specific scenario. You can use the template below to structure your draft. You can apply this draft to your actual IAS 2 project.

1.  **Identification:** (Identify the assets, vulnerabilities, threats, and existing controls in this scenario.)
2.  **Assessing:** (Determine the likelihood and impact of the developer being unavailable.)
3.  **Treatment:** (Choose one of the 5 treatment options: Remediation, Reduction, Transfer, Accept, or Avoid.)
4.  **Communication:** (How will you communicate this risk and your proposed treatment to your group leader/instructor?)
5.  **Re-identification:** (How will you monitor the situation and adjust your plan if the developer returns, or if they don't?)

**Draft your plan below:**

---

## F. Skill-Building Check

### Check for Understanding (5 mins Quiz)

*Answer the following questions based on this module.*

**1. Enumerate the 5 steps in risk management.**
*Answer:* 
1. Identification
2. Assessing
3. Treatment
4. Communication
5. Re-identification (or Rinse-and-Repeat)

**2. What are the 2 factors determining the overall risk?**
*Answer:* 
1. Probability / Likelihood (How likely is it to occur?)
2. Severity / Impact / Cost (How much damage will it cause?)

**3. What are the ways in identifying risks?**
*Answer:* By identifying the following elements:
1. Assets (What we own)
2. Vulnerabilities (Our weaknesses)
3. Threats (Who or what can attack us)
4. Controls (The fixes or protections we already have)