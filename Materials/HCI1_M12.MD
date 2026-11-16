# Task-Centered Design: Building Software Around User Goals

---

## A. Lesson Preview & Review

Welcome to Module 12! So far, we've covered visual design, UI/UX principles, and basic HTML. Now, we are going to zoom out and look at the overarching methodology for creating software: **Task-Centered Design**.

> **In a Nutshell:** Task-Centered Design is a philosophy where the design process is entirely structured around the specific, real-world tasks that a user needs to accomplish. Instead of just adding cool features, you ask, "What is the user trying to get done, and how can we make that as smooth as possible?"

This approach sits under the umbrella of **Human-Centered Computing**. It recognizes that good HCI leads to better interactive systems. 

**Learning Objectives:**
By the end of this module, you should be able to:
1. Identify the concepts and 11 steps of task-centered design.
2. Understand how to execute a task-centered design process.
3. Create your own web task-centered design plan.

---

## B. Main Lesson: The 11 Steps of Task-Centered Design

The process is highly structured. It involves choosing specific tasks early on, using them to raise design issues, making decisions, and evaluating the design as it develops.

### 1. Figure Out Who's Going to Use the System to Do What
This is called **Task and User Analysis**. It’s not enough for a system to just "do what's needed." A successful system must merge smoothly into the user's existing workflow. 
*   It should request information in the order the user naturally receives it.
*   It should make it easy to correct frequent errors.
*   It must account for the user's background knowledge (e.g., Mac users expect standard cut/copy/paste functions). 
*   Less quantifiable factors like user confidence or willingness to learn new systems dictate how much feedback you need to provide.

### 2. Choose Representative Tasks for Task-Centered Design
After understanding the users, you need to pick 3-5 **representative tasks** that the system will be used to accomplish. These must be real tasks, not abstract concepts. 
*   *Example for a spreadsheet:* "Produce a salary budget for next year."
*   *Example for a comms program:* "Log into the office via modem."
These tasks should be a mix of simple and complex, and the design team should collect the actual materials needed to do them to ensure complete coverage of the system's functionality.

### 3. "Plagiarize" (Reuse Good Design)
We don't mean literally stealing copyrighted code. We mean **do not reinvent the wheel**. Find existing interfaces that work well for users and build those paradigms into your system. 
*   If users are familiar with a spreadsheet layout, make your data entry screen look like a spreadsheet. 
*   If you are building a spell checker, look at how Microsoft Word's spell checker works and copy its button placement and menu naming. Using existing paradigms makes the system quicker to build and much easier for users to learn.

### 4. Rough Out the Design
Get the design out of your head and onto **paper**. 
*   **Do not program it yet.** Coding too early commits you to specific decisions before you've thought them through.
*   Discuss features with your team. If someone proposes a feature, ask: *Which of our representative tasks supports this?* If it doesn't support a real task, discard it.

### 5. Think About It
Just like aviation engineers run simulations before building a jet, interface designers must analyze the design before building it. Two structured methods for this are:
*   **GOMS Analysis:** (Goals, Operators, Methods, Selection rules). This involves counting keystrokes and mental operations to estimate task times and identify steps that take too long.
*   **Cognitive Walkthrough:** Analyzing the interface specifically to spot places where users might make mistakes.

### 6. Create a Mock-Up or Prototype
Build something concrete to show users. 
*   Start with **paper sketches** where a user "steps through" a task. This is cheap and reveals hidden misunderstandings.
*   Move to digital prototyping tools.
*   **Wizard of Oz technique:** If the underlying backend system isn't built yet, a human can sit behind a screen and manually respond to the user's actions to simulate a working system!

### 7. Test the Design with Users
No matter how much analysis you do, problems will only appear when real users interact with it.
*   Test with people whose background matches your target audience.
*   Ask them to perform the representative tasks.
*   Crucially, ask them to **"think aloud"** (say what they are looking at and feeling). Document the time taken, errors made, and their verbalized confusion.

### 8. Iterate
**The purpose of testing is not to prove the interface works; it is to find what needs to be improved.** 
*   Balance the cost of fixing a problem against its severity.
*   Revise the interface and test again. 
*   Be careful: fixing a menu for one task might break it for another task. Iteration stops when specific usability objectives are met.

### 9. Build the Design
Now you code. The key guideline here is to **build for change**.
*   If you used a prototyping system, transition to a proper development environment.
*   Don't hardcode parameters (like menu sizes or colors). 
*   Write modular code. If a specialized menu needs to be replaced with a generic function later, modular code makes that change trivial. 

### 10. Track the Design
Interface designers must not be isolated from users after the product launches. 
*   Rotate designers onto the customer hotline.
*   Hold user group meetings.
*   This ensures continued awareness of real user needs and may reveal new market opportunities for future updates.

### 11. Change the Design
In today's market, software that doesn't get updated will become obsolete within a few years. 
*   Tasks change. Users gain new skills. New hardware emerges.
*   Designers must stay abreast of these changes and update the design not just to fix problems, but to seize new opportunities. 

---

## C. Analogies and Use Cases

### The Custom Kitchen Analogy
Imagine an architect designing a custom kitchen.
*   **Task Analysis (Step 1):** They don't just ask "what color cabinets do you like?" They ask, "Who cooks? Do you bake a lot? Are you left-handed?" 
*   **Representative Tasks (Step 2):** "Making a Thanksgiving turkey" and "Quickly grabbing a midnight snack."
*   **Rough Design (Step 4):** They sketch out the triangle between the sink, fridge, and stove on paper.
*   **Iterate (Step 8):** The homeowner realizes in the mockup that the oven door opens into the main walkway. They change the design *before* the contractor builds it.

### Use Case: The Fred Stroller Scenario
Look at the exercise in the module. Fred is a slow typist who wants to buy a red JPG stroller. A task-centered design would focus on minimizing his typing (maybe by offering large, clickable category buttons instead of a text search) and clearly showing him the total cost before he triggers the invoice. 

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   Task-Centered Design focuses on real tasks, not abstract features.
*   It heavily emphasizes **planning on paper** and using cheap prototypes before committing to code.
*   "Plagiarizing" (reusing) existing design patterns makes your app easier to learn.
*   **Testing and Iterating** are the most critical steps—designers must watch real users struggle and then fix it.

### Frequently Asked Questions

**Q: What does GOMS stand for?**
**A:** **G**oals, **O**perators, **M**ethods, **S**election rules. It's a modeling technique used to predict how long it takes a user to perform a task by counting the mental and physical steps (keystrokes, mouse movements).

**Q: What is the "Wizard of Oz" prototyping technique?**
**A:** It's when you have a fully designed user interface (the front end), but the back end isn't built. When a user clicks a button or searches for an item, a human "wizard" behind the curtain manually processes the request and sends the response back to the user's screen.

**Q: Why shouldn't I just start coding right away?**
**A:** Because coding is expensive and rigid. If you spend weeks coding a complex menu system and then discover during testing that users hate it, you have to throw away weeks of work. If you discover that from a paper sketch, you just draw a new sketch.

---

## E. Guided Drills / Design Activities

### Exercise 1: Task-Centered Design Ordering
**Instructions:** Read the scenario below and arrange the tasks in the correct chronological order (1-10) based on how a user would interact with the system.

**Scenario:** Fred Johnson wants to buy a red JPG stroller. He is a first-time customer, types slowly with one finger, and lives on Dear Bottom Avenue NW.

*   [ ] Fred enters the store
*   [ ] Fred looks at the computer
*   [ ] Fred moves to the phone field
*   [ ] Fred enters his name in the computer
*   [ ] Fred fills in the phone, postal code, province, and city
*   [ ] Fred enters his delivery address
*   [ ] Fred looks for a catalog
*   [ ] Fred enters his credit card info
*   [ ] Fred finds the red JPG stroller in the catalog
*   [ ] Fred enters the item number for the JPG red stroller
*   [ ] Fred selects the name field
*   [ ] Fred selects a quantity of the JPG stroller
*   [ ] Fred clicks trigger invoice (PF5)
*   [ ] Fred types his name
*   [ ] Fred sees the cost per item and total
*   [ ] Fred enters the cost of the JPG stroller
*   [ ] Fred goes to the sales counter, pays, and gets the item
*   [ ] Fred uses the stroller immediately
*   [ ] Fred sees the balance he owes

<details>
<summary><strong>Click to reveal correct order</strong></summary>
*(Note: Based on the module's provided answers, here is the sequence)*

1. Fred enters the store
2. Fred looks at the computer
3. Fred selects the name field
4. Fred types his name
5. Fred moves to the phone field
6. Fred fills in the phone, postal code, province, and city
7. Fred enters a date
8. Fred enters his delivery address
9. Fred enters his credit card info
10. Fred looks for a catalog
11. Fred finds the red JPG stroller in the catalog
12. Fred enters the item number for the JPG red stroller
13. Fred enters the cost of the JPG stroller
14. Fred selects a quantity of the JPG stroller
15. Fred clicks trigger invoice (PF5)
16. Fred sees the cost per item and total
17. Fred sees the balance he owes
18. Fred goes to the sales counter, pays, and gets the item
19. Fred uses the stroller immediately
</details>

---

## F. Skill-Building Check

*Test your understanding of Task-Centered Design.*

**Part 1: Identification**
1.  In this task-centered design step, the aim is to start building the interface based on the created prototype.
2.  In this task-centered design step, the designer starts building something more concrete that can be shown to users and that can act as a more detailed description for further work.
3.  It is an approach to interface design that is structured around specific tasks that the user wants to accomplish with the system.
4.  In this task-centered design step, the rough description of the design should be put on paper.
5.  This will allow you to estimate task times and identify tasks that take too many steps.

**Part 2: Multiple Choice**
6.  What will happen to a system that does not serve its purpose?
    *   A. It will prosper
    *   B. It will survive
    *   C. It will be revised
    *   D. It will fail
7.  UIMS means?
    *   A. User Interface Management System
    *   B. User Integrated Management System
    *   C. User Interface Measurable System
    *   D. User Integrated Measurable System
8.  A technique used to spot places in the design where users might make mistakes.
    *   A. GOMS
    *   B. UIMS
    *   C. Iteration
    *   D. Cognitive walkthrough
9.  What is the reason why software becomes obsolete as years pass?
    *   A. Trends
    *   B. Tasks and users both change
    *   C. System life span
    *   D. User needs
10. What is the purpose of testing?
    *   A. To satisfy the user needs
    *   B. To avoid problems in the future
    *   C. To improve the system
    *   D. To debug the system

<details>
<summary><strong>Click to reveal answers</strong></summary>

**Part 1: Identification**
1. **Build the design** (or Step 9)
2. **Create a mock-up or prototype** (or Step 6)
3. **Task-centered design**
4. **Rough out the design** (or Step 4)
5. **GOMS analysis**

**Part 2: Multiple Choice**
6. **D. It will fail** *(If it doesn't do what's needed, it fails).*
7. **A. User Interface Management System**
8. **D. Cognitive walkthrough** *(GOMS is for time estimation, not specifically spotting errors).*
9. **B. Tasks and users both change** *(The module states: "Tasks and users both change. Work patterns change because of the product itself...")*
10. **C. To improve the system** *(The module explicitly states: "The purpose of testing is not to prove the interface, but to improve it.")*

</details>