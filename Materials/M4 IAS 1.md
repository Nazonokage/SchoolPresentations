# Risk Identification and Risk Assessment

> **Course:** Information Assurance and Security 1  
> **Module:** 4 — Risk Identification and Risk Assessment  
> **Learning Format:** Individual & Group Activities

---

## A. Lesson Preview & Review

Good day, future security officers! Today, we will discuss **Risk Identification** and **Risk Assessment**. Before we dive into the main lesson, let's clarify the fundamental difference between a *risk* and a *threat*.

*   **Risk:** Refers to the potential loss, damage, or destruction of assets, caused by a successful threat.
*   **Threat:** The entity or event that deals with the potential loss, damage, or destruction of assets. This is usually done by exploiting a vulnerability or weakness in security.

**Quick Review Exercise:**
Can you classify the following based on the definitions above?
*   **Super Typhoon:** This is a **Threat**. (It is the external event causing potential damage).
*   **Damage to Computer Lab:** This is a **Risk**. (It is the potential outcome or loss resulting from the typhoon).

> **Pro Tip:** Don't worry if you find this slightly confusing. The lines between threats and risks often blur in casual conversation. However, in a professional setting, understanding that a threat exploits a vulnerability to create a risk is crucial.

![Risk Assessment Concept](https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### Risk Identification
In Information Assurance and Security (IAS), we secure our assets using two primary approaches:
1.  **Risk Identification and Risk Assessment:** We focus on the potential negative outcomes first, then identify what could cause them.
2.  **Threat Identification and Risk Assessment:** We focus on the threats first, then assess the risks associated with them.

In this module, we focus on the first approach. **Risk Identification** is simply the process of finding out what can damage an organization. 

**Example:**
Consider an asset like a computer in a computer lab. What are the possible risks to this asset?
*   Being hacked (Cyber risk)
*   Physically destroyed (Physical risk)
*   Virus infected (Malware risk)
*   Getting wet (Environmental risk)
*   Burning (Environmental/fire risk)

### Risk Measurement (Likelihood and Severity)
Once you identify risks, you need to measure them to prioritize your response. This involves assessing two key factors:
1.  **Likelihood:** How probable is it that the risk will occur?
2.  **Severity (Impact):** How much damage will it cause if it happens?

> **Instructional Note:** The source material for Module 4 is relatively brief. To ensure adequate comprehension and practical application of these concepts, this section is expanded into a practical, hands-on activity below. It is highly recommended that this module be treated as a dedicated activity session to allow students to practice measuring likelihood and severity.

---

## C. Analogies and Use Cases

### The "Umbrella" Analogy
Imagine you are going outside.
*   **Threat:** Dark clouds and thunder (the external event).
*   **Vulnerability:** You don't have an umbrella (the weakness).
*   **Risk:** You get soaked and ruin your laptop (the potential loss).
*   **Risk Measurement:** If the weather forecast says 90% chance of rain (Likelihood) and you are carrying an expensive laptop (Severity), the risk is very high. You assess this and decide to stay inside.

### Real-World Use Case: E-Commerce Store
An online store has a customer database.
*   **Risk Identification:** The team identifies that the database could be breached, taken offline by a DDoS attack, or accidentally deleted.
*   **Risk Measurement:** They measure the *likelihood* of a breach (e.g., High, due to recent phishing attempts) and the *severity* (e.g., Critical, because it would cost millions in fines and lose customer trust). This measurement allows them to justify spending money on better firewalls and backups.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **Risk** is the potential for loss or damage, while a **Threat** is the event or entity that exploits a vulnerability to cause that risk.
*   **Risk Identification** is the process of discovering what could go wrong with an organization's assets.
*   **Risk Measurement** involves evaluating both the **likelihood** and the **severity** of identified risks.
*   Risks are dynamic. The likelihood and severity can change over time as the environment, technology, and threat landscape evolve.

### Frequently Asked Questions
**1. What is another term for risk assessment of severity and likelihood?**
**A:** Risk Measurement.

**2. Can the likelihood and severity change over time?**
**A:** Yes, it can. Sometimes, the risk even totally disappears (e.g., if a vulnerable software is retired or patched). Conversely, new threats can make a previously low risk suddenly very severe.

**3. How do I know which risks to prioritize?**
**A:** Prioritize risks that have the highest combination of likelihood and severity. These are the ones that pose the greatest immediate threat to your organization's critical assets.

**4. What is the difference between Risk Assessment and Threat Assessment?**
**A:** Risk Assessment focuses on the potential outcomes and vulnerabilities, whereas Threat Assessment focuses on the actors or events that might exploit those vulnerabilities. Both are valid frameworks for securing an organization.

**5. If I identify a risk but it has a low likelihood and low severity, do I ignore it?**
**A:** No, you don't ignore it entirely, but you might "accept" the risk. This means you acknowledge it exists but decide that the cost of mitigating it outweighs the potential damage. You should document it and monitor it periodically.

---

## E. Guided Drills / Code Projects

### Course Project: Risk Assessment Matrix
**Project Overview:** 
For Module 4, your group will apply the concepts of Risk Identification and Measurement to your ongoing project target (the business/organization you selected in Module 2). 

> *Note: This should be treated as a mandatory activity, as it forms the analytical backbone of your final defense. You are expected to produce a working document here.*

**Project Guidelines:**
*   **Group Size:** 3–5 members.
*   **Objective:** 
    1. Identify at least 5 risks associated with the assets of your chosen organization.
    2. Measure the likelihood and severity of each risk using a scale of 1 to 5 (1 = Very Low, 5 = Very High).
    3. Calculate a Risk Score (Likelihood x Severity) for each.
*   **Sample Project Title:** *Risk Assessment Matrix for a University Student Portal*

**Step-by-Step Deliverable for Module 4:**
1.  **Create a Table:** Set up a table with the columns: Asset, Risk, Likelihood (1-5), Severity (1-5), Risk Score, Priority.
2.  **Populate the Table:** Let's assume your asset is the "Student Portal Database." 
    *   *Risk:* Data breach via SQL Injection. 
    *   *Likelihood:* 4 (High, due to known vulnerabilities). 
    *   *Severity:* 5 (Critical, due to privacy laws). 
    *   *Score:* 20.
3.  **Analyze:** Based on the scores, rank the risks from highest to lowest.
4.  **Draft Recommendations:** For your top 2 highest-scoring risks, write a brief paragraph recommending how to mitigate them (e.g., "Implement parameterized queries and Web Application Firewalls to mitigate SQL Injection").

```json
// Example JSON representation of a Risk Assessment entry
{
  "asset": "Customer Database",
  "risk": "Unauthorized Access",
  "likelihood": 4,
  "severity": 5,
  "risk_score": 20,
  "priority": "High",
  "recommendation": "Implement Multi-Factor Authentication (MFA) and role-based access control."
}
```

---

## F. Skill-Building Check

### Part 1: Identification
*Fill in the blank with the correct term based on the definitions provided in this module.*

1.  ___________ refers to the potential loss, damage, or destruction of assets.
2.  ___________ is the process of finding out what can damage an organization's assets.
3.  ___________ is the term used for the risk assessment of severity and likelihood.
4.  A ___________ is the entity or event that exploits a vulnerability to cause harm.
5.  ___________ evaluates how probable it is that a risk will occur, while ___________ evaluates how much damage it will cause.

**Answers:**
1. **Risk**
2. **Risk Identification**
3. **Risk Measurement**
4. **Threat**
5. **Likelihood**, **Severity** (or Impact)

### Part 2: Check for Understanding (Short Answer)

**1. Why is it important to measure both the likelihood and the severity of a risk?**
*Guidance:* Measuring only one gives an incomplete picture. A highly severe risk that is extremely unlikely might not require immediate action, while a low-severity risk that happens every day (high likelihood) could accumulate significant damage over time. Measuring both allows an organization to prioritize its limited resources effectively.

**2. Explain how a "threat" differs from a "risk" using a real-world IT example.**
*Guidance:* A threat is the source of harm (e.g., a hacker group conducting a phishing campaign). A risk is the potential damage that threat could cause (e.g., the risk of the hacker successfully stealing employee credentials and accessing the payroll system). The threat is the *actor*, the risk is the *potential outcome*.

**3. If a company identifies a risk of "Server Room Flooding," what are the potential threats that could cause this risk?**
*Guidance:* Potential threats could include burst pipes, natural disasters (like a hurricane or heavy rains), or a malfunctioning fire sprinkler system. These are the events/entities that could trigger the risk of flooding.