# Infosec Case Analysis: Securing the Software Development Life Cycle

> **Course:** Information Assurance and Security  
> **Module:** 23 — Infosec Case Analysis: Securing SDLC  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Hello students! Today, we are putting our knowledge of the **Software Development Life Cycle (SDLC)** to the test through a real-world case analysis. 

Your goal is to read and understand this case study with your group (or individually, as adapted for this assignment). We will focus on identifying the specific issues that arose from failing to secure the SDLC from the very beginning.

**Quick Review: The 5 Phases of SDLC**
Before we begin, can you enumerate and describe the phases?
1.  **Planning:** Requirements gathering and goal setting.
2.  **Design:** Architecture, database design, and prototyping.
3.  **Implementation:** Writing the code.
4.  **Testing:** Verifying the system against requirements.
5.  **Deployment and Maintenance:** Releasing and maintaining the system.

![SDLC Phases](https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### Case Study Narrative: SDLC Chaos

**The Team and the Project:**
The case revolves around a development team named **NinjaCoders**. The team consisted of 2 Project Managers (one focused on code, one on client communication), 3 Developers, 2 Testers, and 1 Designer. All members were experts in their fields. 

They were tasked with developing a **School System** (finance, grading, enrollment, and LMS) for an offshore client. The budget was **18 million pesos**, and the timeline was **1 year**. The client had high faith in the team, but the team had **no dedicated Security Manager** to oversee the SDLC.

**The Initial Phases:**
*   **Planning:** The Planning phase was seamless, even with time zone differences causing slight communication delays. The team created reports, updates, and initial tests for the client.
*   **Design:** The Design phase finished on time, leaving a small buffer for the developers.

**The Problem:**
Midway through the **Development (Implementation) phase**, the client realized they needed to change some core requirements. This meant changing things that were established back in the **Planning phase**. 

The team split the developers into two groups, and the Project Manager joined the dev team to handle the changes. However, the changes involved the **actual core process** of the system, halting the main development. They had to perform three rounds of major overtime to catch up.

**The End of Development:**
Nearing the Testing and Deployment phase, the team was **2 months late**, costing both the developers and the client money. Just before finishing, the client requested more changes. Although minor, it added to the timeline. Ultimately, the project took an **extra 5 months** to finish. The remaining project budget was down to **11 million pesos**. 

**Post-Deployment:**
Today, the system is considered unfinished. It required constant updates and fixes due to poor detailed requirements from the client. During the **COVID-19 pandemic**, the system became obsolete, and the client abandoned it entirely, switching to a different system.

### Analysis: What Went Wrong?
The case highlights the severe consequences of improper SDLC management, particularly the failure to integrate **Risk Management and Security** into every phase.

| SDLC Phase | What Happened | The Root Cause |
| :--- | :--- | :--- |
| **Planning** | Missed critical requirements that only surfaced during implementation. | Poor requirements gathering and lack of risk assessment for scope creep. |
| **Design** | Finished on time, but was based on incomplete requirements. | Lack of traceability between design and future change requests. |
| **Implementation** | Mid-development changes broke the core process, causing massive delays. | Absence of a formal Change Management process and Security/Architectural oversight. |
| **Testing** | Inconsistencies between requirements, test cases, and code. | Test cases were not updated when changes were requested. |
| **Deployment** | System unfinished, buggy, and eventually abandoned. | High technical debt and failure to plan for long-term maintenance or external disruptions (COVID). |

---

## C. Analogies and Use Cases

### The "Building Construction" Analogy
Imagine hiring a construction team to build a 10-story building.
*   You spend months on the **Planning** and **Design** phases, agreeing on the blueprints.
*   Halfway through construction (**Implementation**), you decide you want to add a swimming pool on the roof. 
*   The construction team agrees and starts pouring concrete for the pool, but they don't reinforce the foundation.
*   By the time they reach the **Testing** phase, they realize the building is sagging. They spend months adding supports (overtime).
*   The building is finally "finished" but leaks, and the client refuses to move in. The construction company loses money and reputation.

### Real-World Use Case: Scope Creep in Software
The "NinjaCoders" case is a textbook example of **Scope Creep**. In the real world, if a client requests a change after the design is frozen, it should go through a formal **Change Control Board (CCB)**. The CCB evaluates the impact on the timeline and budget. If the client wants the change, they must pay for the extended timeline. Without a Security Manager or strict Project Management, the team absorbed the costs, leading to the project's failure.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **Requirements must be thorough.** Missing requirements in the Planning phase cause catastrophic delays later.
*   **Change Management is vital.** Accepting major changes mid-development without adjusting the timeline or budget is a recipe for failure.
*   **The Cost of Poor Security/Architecture.** Without a Security Manager or a proper architectural review, core processes are disrupted, leading to technical debt and unusable systems.
*   **External factors (COVID-19).** Systems that are not built with resilience and adaptability in mind will quickly become obsolete when business environments change.

### Frequently Asked Questions
**1. Is this a true story?**
**A:** Yes. This case study was based on the real-world experience of the module writer. However, a lot of details were changed and omitted for simplicity's sake to fit within the scope of this lesson.

**2. What is the most critical failure point in this case?**
**A:** The failure to secure the **Planning phase**. By not capturing all requirements and failing to establish a robust change management process, the team set themselves up for failure in the Implementation and Testing phases.

**3. Why didn't the 2 Project Managers prevent this?**
**A:** Having 2 Project Managers (one for code, one for client communication) can be an advantage, but it can also cause a disconnect. The client-facing PM may have agreed to changes without fully understanding the technical impact on the code, and the code-focused PM may have struggled to push back against the client's demands without a unified strategy.

---

## E. Guided Drills / Code Projects

### Solo Project Update: Applying Lessons Learned
**Project Overview:** 
For Module 23, you will use the knowledge from this case study to improve the security and stability of your own capstone project. Look at what made the "NinjaCoders" fail and implement security measures to prevent those mistakes in your project.

> *Note: This was originally designed as a group activity. We are adapting it as a **solo activity**. You will act as the sole risk manager and developer for this assignment.*

**Project Guidelines:**
*   **Format:** Individual work.
*   **Objective:** Draft a "Lessons Learned" policy or plan for your capstone based on the failures of the NinjaCoders.
*   **Submission:** Add this to your ongoing project documentation.

**Step-by-Step Deliverable:**
Write a reflection document answering the following prompts:

1.  **Change Management Policy:** Draft a short policy outlining how you will handle client/stakeholder change requests during the Implementation phase of your capstone. (Hint: Will you stop development? Will you re-estimate the timeline?)
2.  **Security Oversight:** Since you don't have a dedicated Security Manager, what role will you play to ensure security is embedded in every SDLC phase? 
3.  **Documentation Strategy:** How will you ensure your test cases and documentation are updated when changes occur, preventing the "inconsistencies" the NinjaCoders faced?

**Draft your plan below:**

> *Example Draft:*
> **Capstone SDLC Risk Mitigation Plan**
> *   **Change Management:** All change requests after the Design phase must go through a written assessment. I will assess the impact on the timeline and code. If it's a major change, I will document the delay rather than doing unrecorded overtime.
> *   **Security Oversight:** I will act as the "Security Champion" for the project. I will personally review every pull request on GitHub for SQL injection or XSS vulnerabilities before merging.
> *   **Documentation:** I will maintain a single source of truth for requirements. If a change is accepted, the first step is updating the test cases *before* writing the new code.

---

## F. Skill-Building Check

### Check for Understanding (25 mins Quiz)

*Answer the following questions with the best of your abilities. You can answer them individually.*

**1. Was there an advantage to having 2 project managers? Explain.**
*Guidance:* Having 2 project managers can be an advantage because it allows for the division of labor: one focuses on technical execution and code, while the other focuses on client communication and expectations. This prevents one person from being overwhelmed. However, as seen in the case, it can also lead to misalignment if the client-facing PM promises changes without consulting the technical PM on the feasibility and timeline implications.

**2. Do you think it would have been helpful to have a Security Officer managing the SDLC? Explain.**
*Guidance:* Absolutely. A Security Officer (or Security Manager) would have ensured that secure coding practices were followed from the start. More importantly, they would have enforced a rigorous change management process, assessing the security risks and architectural impacts of the client's mid-development requests. They act as the voice of reason, preventing knee-jerk reactions that break the system.

**3. What part of the SDLC do you think the team failed? Explain.**
*Guidance:* The team failed primarily in the **Planning Phase** by not gathering comprehensive, future-proof requirements. They also failed in the **Implementation Phase** by mishandling the change requests (scope creep) and failing to adjust their timeline. Finally, they failed in **Testing** by not updating the test cases to match the new requirements, leading to a low-quality product.

**4. During the Planning phase, there were a lot of things the client failed to mention that were only brought up during the development phase. List down all possible risks that the developers can encounter during the planning phase.**
*Guidance:*
1.  **Scope Creep:** The client changes their mind or remembers new requirements late in the game.
2.  **Misaligned Expectations:** The client and developers have a different vision of the final product.
3.  **Budget Miscalculation:** Underestimating the resources needed due to missing requirements.
4.  **Timeline Overruns:** The initial 1-year timeline becomes impossible to meet.
5.  **Communication Breakdowns:** Offshore clients may have language or time zone barriers that lead to misunderstandings.

**5. During the Development phase, there were a lot of changes requested by the client. Would you have accepted the changes and proceeded with the development? Or do you have a better option? Explain.**
*Guidance:* I would not have accepted the changes outright without a formal assessment. A better option would be to implement a **Change Control Process**. I would evaluate the requested changes, determine their impact on the timeline and budget, and present this assessment to the client. I would then negotiate a contract amendment for the additional time and cost, or put the changes on hold for a future version (v2.0) to protect the core system's integrity.

**6. What have you learned about this Case Analysis?**
*Guidance:* I learned that software development is highly sensitive to changes in the early phases. A flawless Planning phase is critical, and a lack of a dedicated Security/Architectural oversight role leaves the project vulnerable to scope creep. It is better to negotiate a realistic timeline upfront than to promise an impossible deadline and fail, losing both money and reputation.

**7. What will you change in the current setup of the team? What do you recommend for the team to make the project more successful?**
*Guidance:* I would change the team setup by adding a dedicated **Security Officer** or **Systems Architect** to oversee the SDLC and manage risk. I would also implement a formal **Change Management Policy**. For the project to be successful, requirements gathering must be exhaustive, and any changes after the Design freeze must trigger a re-evaluation of the timeline, budget, and security implications.