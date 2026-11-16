# Applying the Risk Management Framework: Prioritizing Risks and the Risk Matrix

> **Course:** Information Assurance and Security  
> **Module:** 6 — Apply Risk Management Framework (Step 1)  
> **Learning Format:** Individual & Group Activities

---

## A. Lesson Preview & Review

Good day, future security officers! Today, we are diving into the **first step of the Risk Management Framework (RMF)**: Categorizing Information Systems (Prioritizing Risks). 

Before we get started, let's quickly review the 6 steps of the RMF we learned in the previous module:
1.  Categorize Information Systems
2.  Select Security Controls
3.  Implement Security Controls
4.  Assess Security Controls
5.  Authorize Information Systems
6.  Monitor Security Controls

In previous modules, we learned how to identify risks and measure their **likelihood** and **severity**. Now, we will improve upon that by applying the **Risk Matrix** to determine which risks we need to prioritize first.

![Risk Prioritization Concept](https://images.unsplash.com/photo-1507925921958-8a62f3d1a50d?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### Prioritizing the Risks
We already know how to scale the likelihood and impact of a risk. Now, with those scales, we can prioritize which risks should be placed first in our Risk Management Framework. 

When prioritizing importance, organizations can use:
*   **Numerical Scales:** Priority 1, 2, 3, 4, 5 (where 1 is highest priority).
*   **Descriptive Scales:** Least important, Less important, Important, More important, Most important.

The method used depends on the organization and how easily it is understood by both the executives and the security team.

In general, the risk with the most severe impact and the highest likelihood is the most important. But what if a risk has a 5 in impact but only a 4 in likelihood? Or a 4 in impact and a 5 in likelihood? How do we determine its exact priority? For that, we need the **Risk Matrix**.

### The Basic Risk Matrix
A risk matrix is a 5x5 table where the severity (impact) and likelihood meet to determine the importance of the risk. 

> **Pro Tip:** In this basic matrix, we can see that if a risk has a 4 likelihood and 5 impact, or 4 impact and 5 likelihood, it has a priority of **most importance**. The same goes for a 5, 5 scale. **As long as there is a 5 in either impact or likelihood, it is automatically a most important priority.**

| | Impact 1 | Impact 2 | Impact 3 | Impact 4 | Impact 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Likelihood 5** | Less Important | Important | More Important | Most Important | Most Important |
| **Likelihood 4** | Least Important | Less Important | Important | More Important | Most Important |
| **Likelihood 3** | Least Important | Less Important | Important | More Important | More Important |
| **Likelihood 2** | Least Important | Least Important | Less Important | Important | More Important |
| **Likelihood 1** | Least Important | Least Important | Least Important | Important | Important |

*   *1 = Least likely or lowest severity*
*   *5 = Highest likely to occur or highest severity*

If a risk has a 3 impact and 3 likelihood scale, we determine it as simply an **Important** priority. A 3,4 or 4,4 scale is a **More Important** priority. So, the exact categorization depends on the risks you identified and scaled.

### Understanding Risk Appetite
You must take note that **for every organization, there are different risk matrices**. This is where **Risk Appetite** comes in.

**Risk Appetite** is the attitude of an organization toward its risks. It determines what and how much risk an organization can take. 

*   **Call Center Example (Conservative Appetite):** A call center has very few "Most Important" priorities. In their risk matrix, perhaps they only focus on a **5 impact, with 4 likelihood** as "most important." A 4 impact and 5 likelihood might only be a "More Important" priority for them.
*   **Hospital Example (Aggressive/Critical Appetite):** A hospital considers anything within a **4 impact and 5 likelihood** an "most important" priority because patient safety is critical.

In your project, you must identify the risk matrix that fits your chosen organization, or create your own based on their specific needs. Usually, a basic risk matrix is enough, and adjustments can be made later.

#### Sample Risk Matrix in Other Industries: Call Center
Notice how the "Most Important" (darkest) zones are smaller compared to the basic matrix, reflecting a different risk appetite.

| | Impact 1 | Impact 2 | Impact 3 | Impact 4 | Impact 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Likelihood 5** | Less Important | Important | More Important | Most Important | Most Important |
| **Likelihood 4** | Least Important | Less Important | Important | More Important | More Important |
| **Likelihood 3** | Least Important | Less Important | Important | More Important | More Important |
| **Likelihood 2** | Least Important | Least Important | Less Important | Important | More Important |
| **Likelihood 1** | Least Important | Least Important | Least Important | Less Important | Important |

#### Sample Risk Matrix in Other Industries: Hospital
Notice how the "Most Important" (darkest) zones are larger, reflecting the hospital's low tolerance for risk regarding patient safety.

| | Impact 1 | Impact 2 | Impact 3 | Impact 4 | Impact 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Likelihood 5** | Important | More Important | Most Important | Most Important | Most Important |
| **Likelihood 4** | Less Important | Important | Important | More Important | Most Important |
| **Likelihood 3** | Less Important | Less Important | Important | More Important | Most Important |
| **Likelihood 2** | Least Important | Less Important | Important | More Important | Most Important |
| **Likelihood 1** | Least Important | Least Important | Less Important | Important | Most Important |

---

## C. Analogies and Use Cases

### The "Speed Limit" Analogy
Think of **Risk Appetite** as a driver's tolerance for speed.
*   A **race car driver** (High Risk Appetite) has a risk matrix where driving 100 mph on a straight road is "Low Priority" (acceptable).
*   A **school bus driver** (Low Risk Appetite) has a risk matrix where driving 100 mph is "Most Important" (unacceptable).
The risk (speeding) is the same, but the organizational context changes the priority level.

### Real-World Use Case: E-Commerce vs. Healthcare
*   **E-Commerce:** If their website goes down for 2 hours, they lose sales. However, they might categorize this as a "More Important" risk rather than "Most Important" because they can recover and customers will likely return.
*   **Healthcare:** If a hospital's patient monitoring system goes down for 2 hours, lives are at risk. This would immediately be categorized as a "Most Important" risk. The *likelihood* and *impact* scales are the same, but the **Risk Appetite** shifts the priority.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **Step 1 of RMF** involves categorizing information systems by prioritizing risks.
*   A **Risk Matrix** is a 5x5 grid that maps Likelihood against Impact to determine priority.
*   In a basic matrix, any risk with a score of **5 in either impact or likelihood** is automatically a "Most Important" priority.
*   **Risk Appetite** is the organization's attitude toward risk. It dictates how the risk matrix is structured and which risks are considered "Most Important."
*   Risk matrices are not universal; they vary by organization and industry.

### Frequently Asked Questions
**1. Can the risk matrix change?**
**A:** Yes, it can. But it doesn't change very often. Usually, it changes whenever the first RMF is completed, and it requires adjustments based on the new reality.

**2. Why do risk matrices differ from every organization and industry?**
**A:** Because every organization has a different **Risk Appetite**. A hospital prioritizes patient safety (high impact), while a call center prioritizes uptime for customer service. What is "Most Important" to one might be "Less Important" to another.

**3. How do I know if my organization has a high or low risk appetite?**
**A:** Look at their business model. If they are highly regulated or deal with sensitive data (like healthcare or finance), they typically have a low risk appetite (meaning they consider more risks as "Most Important"). If they are a fast-paced startup, they might have a higher risk appetite.

**4. What should I do if I don't know my organization's risk appetite?**
**A:** Start with a basic risk matrix. As you monitor and assess the controls (Steps 4 and 6 of the RMF), you will learn more about their tolerance levels and can adjust the matrix accordingly.

**5. Does a "Most Important" priority mean I have to fix it immediately?**
**A:** Yes. "Most Important" risks are the ones that require immediate attention and resources. You will select and implement controls for these first.

---

## E. Guided Drills / Code Projects

### Course Project: Drafting Your Risk Matrix
**Project Overview:** 
For Module 6, your group will create a draft of your own **Risk Matrix** for your Project Document. You will update your Risk Management Framework table from the previous module and now determine the priority (Step 1: Categorizing) using your new matrix.

**Project Guidelines:**
*   **Group Size:** 3–5 members.
*   **Objective:** Apply the Risk Matrix to prioritize the risks you identified in Modules 4 and 5.
*   **Submission:** Add this draft to your ongoing project documentation.

**Step-by-Step Deliverable:**
1.  **Review your identified risks** from Module 5 (e.g., Flooding, Hacking, Hardware Failure).
2.  **Create a Risk Matrix.** You can use the basic matrix provided in this module, or adjust it based on the perceived **Risk Appetite** of your chosen organization. 
3.  **Determine the Priority.** For each risk, assign a Likelihood (1-5) and Impact (1-5) score based on your previous assessment. 
4.  **Map it.** Use your matrix to find the exact priority level (e.g., Least Important, Important, Most Important).
5.  **Fill in the table below** (continue on a separate sheet if needed):

| Risk | Likelihood (1-5) | Impact (1-5) | Priority Level (from Matrix) |
| :--- | :--- | :--- | :--- |
| *Example: Database Hacking* | *4* | *5* | *Most Important* |
| *Example: Server Room Flooding* | *2* | *4* | *Important* |
| | | | |
| | | | |
| | | | |

> *Note: You will use this categorized list in the next module to start selecting security controls (Step 2 of the RMF).*

---

## F. Skill-Building Check

### Part 1: Short Essay

**1. Explain why risk matrices differ from every organization, and industry.**
*Guidance:* Your answer should discuss the concept of **Risk Appetite**. Explain that different organizations have different tolerances for risk based on their industry, regulatory environment, and business model. For example, a hospital has a lower tolerance for risks affecting patient safety, making its "Most Important" zone larger than a call center's, which might tolerate more downtime.

### Part 2: Multiple Choice

**2. In a basic risk matrix, what combination of likelihood and impact automatically qualifies a risk as "Most Important"?**
A. 3 likelihood, 3 impact
B. 4 likelihood, 4 impact
C. 5 likelihood, 2 impact
D. 2 likelihood, 5 impact
**Correct Answer: C and D** (As long as there is a 5 in *either* impact or likelihood, it is automatically a most important priority). *Note: Option D also has a 5 in impact. Option C has a 5 in likelihood.*

**3. What does "Risk Appetite" refer to?**
A. The amount of food a security team consumes during a breach.
B. The organization's attitude toward risk and how much risk it is willing to take.
C. The specific security controls an organization chooses to implement.
D. The financial cost of a security breach.
**Correct Answer: B** (Risk Appetite defines the organization's tolerance for risk).

**4. If an organization has a risk with a likelihood of 4 and an impact of 4, how would this typically be categorized in a basic matrix?**
A. Least Important
B. Less Important
C. More Important
D. Most Important
**Correct Answer: C** (While it is high, without a 5 in either category, it falls into the "More Important" category in a basic matrix).

**5. Why is it important to prioritize risks in Step 1 of the RMF?**
A. To ensure you spend the most money on the most expensive controls.
B. To identify which risks need immediate attention and resources first.
C. To avoid having to monitor the risks later.
D. To make the Risk Matrix look more complicated.
**Correct Answer: B** (Prioritization ensures that limited resources are allocated to the most critical risks first).