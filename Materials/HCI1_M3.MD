# Interaction Design 2: UI Rules, Principles, and Usability

---

## A. Lesson Preview & Review

Welcome to the next stage of Interaction Design! In our previous module, we explored the core foundations of HCI. Now, we are going to dive into the practical guidelines that make interfaces truly usable.

**The Core Philosophy:** 
To deliver impressive user interfaces, we must remember one golden truth: **Users are humans.** Humans have needs, require comfort, and have a limited mental capacity for processing information. HCI starts with understanding the problems users face and designing systems that support their natural activities.

**Learning Objectives:**
By the end of this module, you should be able to:
1. Identify key design rules and principles for User Interfaces (UI).
2. Understand how Interaction Design directly affects user usability.
3. Create simple, interactive designs following these guidelines.

> **Pro Tip:** As you read through the rules below, think about your favorite apps. Do they follow these guidelines? Do they break them? Recognizing good and bad design in the wild is the first step to becoming a great designer.

---

## B. Main Lesson

### The 8 Golden Rules of User Interface Design

When creating or updating products, keep these fundamental guidelines in mind to ensure a seamless user experience.

**1. Make user interfaces consistent**
Consistency breeds familiarity. Use similar design patterns, identical terminology in prompts, and homogeneous menus and screens throughout your interface. If a "Submit" button is green on one page, it shouldn't be blue on the next.

**2. Allow users to navigate easily via shortcuts**
While beginners need clear navigation, expert users who frequent your site need to move quickly. Provide keyboard shortcuts (like `Ctrl + C` to copy and `Ctrl + V` to paste) and quick-access features to speed up their workflow.

**3. Provide informative feedback**
Always tell the user what is happening. If a user is creating a password, don't just say "invalid." Use a visual strength meter (like the one used by Dropbox) or clear text to show exactly what is required and how strong their current input is.

![Dropbox Password Strength](https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?auto=format&fit=crop&w=800&q=80)
*A good UI uses visual cues (like a progress bar) to provide immediate feedback on password strength.*

**4. Design dialogs to yield closure**
Sequences of actions should have a clear beginning, middle, and end. When a user finishes a task (like placing an order), give them a clear confirmation screen (e.g., a "Thank You" page with a summary). This provides satisfaction, a sense of relief, and drops contingency plans from their mind.

**5. Prevent errors as much as possible**
Make the UI foolproof. Instead of letting a user make a mistake and then showing an error, prevent the mistake from happening. For example, grey out menu items that aren't available, or restrict users from typing letters into a phone number field. If an error *does* happen, offer a clear explanation and an easy solution.

**6. Allow users ways to reverse their actions easily**
Users make mistakes. Having a clear "Undo," "Redo," or "Back" button relieves anxiety and encourages users to explore unfamiliar features. If someone adds the wrong item to a form, let them go back one step without having to start the entire process over.

**7. Support internal locus of control**
Users want to feel in control of the system. A classic example is the "Are you sure you want to exit without saving?" prompt in Microsoft Office. It makes the user feel in charge and prevents accidental data loss.

**8. Minimize memory load**
Don't make users remember things from one screen to the next. Minimize **cognitive load** by letting the computer do the remembering. For example, don't make users re-enter their personal information every time they buy something—use autofill. Always choose **recognition over recall**.

---

### The 6 Key UI Design Principles

Beyond the golden rules, these six principles form the backbone of great UI design:

*   **Clarity:** Navigation must be intuitive. Users should easily understand the purpose of each element. Use highly visible buttons and ask yourself, "Is it clear and easy to understand what this does?"
*   **Familiarity:** Users spend most of their time on *other* websites. They prefer your site to work the same way as the ones they already know. They expect menus at the top, and they expect the `<Back>` button to take them to the previous step, not the homepage. Familiarity reduces the learning curve and increases user retention.
*   **Hierarchy:** Arrange visual elements to show their level of importance. Guide the user's eye to the most important information first using **color, size, and fonts**. 
*   **Negative Space:** Give elements room to breathe. Don't cram everything together. **Negative space** makes important elements pop and stand out. (Think of it like social distancing for your UI elements).
*   **Flexibility:** Design for everyone—from the novice using an old laptop to the expert using the latest iPad. Provide **accelerators** (like shortcuts or advanced filters) for power users, while keeping the interface learnable for beginners.
*   **User Control:** Provide clearly marked "emergency exits" for users who accidentally click into an unwanted state. Support undo/redo and give users different options to navigate back a step.

---

### Essential GUI Guidelines

When designing Graphical User Interfaces, follow these technical guidelines to ensure a smooth experience:

*   **Predictability:** Common elements should perform predictably (e.g., pinch-to-zoom). Form should always follow function.
*   **Discoverability:** Clearly label icons. Use well-indicated affordances (like shadows on buttons) so users know they are clickable.
*   **Simplicity:** Keep interfaces simple by including only elements that serve the user's purpose. Aim for an "invisible" feel where the tool gets out of the way.
*   **Alignment & Readability:** Respect the user's eye. Use proper alignment (edge alignment is usually better than center alignment), color, contrast, and typography to guide scanning. 
*   **Efficiency:** Minimize the number of actions needed to perform a task. Focus on one chief function per page and use **progressive disclosure** (revealing complex options only when needed).
*   **Proximity:** Put controls near the objects they control (e.g., a "Submit" button right next to the form).
*   **Avoid Dark Patterns:** Beware of manipulative designs, such as hard-to-see pre-filled checkboxes or sneaking items into a user's cart. Maintain brand trust through honesty.

![Sephora Website Layout](https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=800&q=80)
*The Sephora website uses strong familiarity (standard top navigation) and clear hierarchy (large promotional banners).*

---

## C. Analogies and Use Cases

### Analogy: The "Undo" Button is a Safety Net
Imagine walking a tightrope. If there was no net below you, you would walk incredibly slowly, paralyzed by the fear of falling. If there is a net, you walk confidently and quickly. The "Undo" feature or a "Clear Exit" button is the safety net of your UI. It allows users to explore and learn without the fear of breaking something.

### Use Case: Minimizing Memory Load in E-Commerce
Imagine an online store that requires you to type in your shipping address, then re-type your billing address, and then re-type your name for the credit card—even though they are all the same. This causes extreme frustration and **cognitive load**. A well-designed system will have a simple checkbox: *"Billing address is the same as shipping address."* This demonstrates Rule #8 (Minimize Memory Load) perfectly.

### Use Case: Progressive Disclosure in Settings
When you open a new mobile app's settings, you usually see basic options like "Notifications" and "Profile." You don't immediately see complex developer options or detailed privacy configurations. This is **progressive disclosure**—keeping the interface simple (Principle: Clarity) and only revealing advanced options when the user clicks into a specific category.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **Consistency** and **Familiarity** make users feel at home.
*   **Feedback** and **Closure** keep users informed and satisfied.
*   **Preventing errors** (and allowing users to easily undo them) creates a safe environment for exploration.
*   Great UI uses **hierarchy** and **negative space** to guide the user's eye naturally.
*   A good system accommodates both novices and experts through **flexibility**.

### Frequently Asked Questions

**Q: What is "Cognitive Load"?**
**A:** Cognitive load is the amount of mental effort being used in the working memory. In UI design, minimizing cognitive load means not asking users to remember information from previous screens, use complex jargon, or navigate through cluttered layouts.

**Q: What is an "Affordance"?**
**A:** An affordance is a visual cue that tells a user how an object should be used. For example, a button with a drop shadow looks like a physical object that can be pressed. A text field with a blinking cursor affords typing.

**Q: What are "Dark Patterns"?**
**A:** Dark patterns are UI design tricks used to manipulate users into doing things they don't intend to do—like signing up for a subscription they didn't ask for, or making the "unsubscribe" button hidden and tiny.

---

## E. Guided Drills / Design Activities

### Activity 1: The Good vs. Bad Website Audit
Visit 3 websites you frequently use. Evaluate them against the rules we just learned. Write down your findings.

| Website/App | Verdict (Good/Bad) | Why? (Which rule/principle applies?) |
| :--- | :--- | :--- |
| *e.g., Amazon* | Good | Strong **familiarity** (top navigation) and **feedback** (order confirmation pages). |
| *[Your Website 1]* | | |
| *[Your Website 2]* | | |

### Activity 2: UI Pattern Identification
Look at a popular app on your phone. Try to identify where the designer used the following principles:
1.  Where is the **Negative Space**? Is it cluttered or clean?
2.  Find an example of **Hierarchy**. What is the biggest, boldest text on the screen?
3.  Find an example of **Flexibility**. Are there shortcuts, filters, or advanced search options?
4.  Find an example of **User Control**. Is there a clear "Back" or "Cancel" button?

---

## F. Skill-Building Check

*Test your understanding by matching the scenario to the correct UI Rule or Principle.*

1.  Enlarging a title on a webpage to make it the first thing the user sees. 
2.  Ensuring all pages on a website use the exact same color palette and font styles.
3.  Providing a "Cancel Order" button during the checkout process.
4.  Using a standard top-navigation menu layout that users instantly recognize.
5.  Showing a success message with a checkmark after a user successfully submits a contact form.
6.  A pop-up message suggesting a strong password when a user types a weak one.

<details>
<summary><strong>Click to reveal answers</strong></summary>

1. **Hierarchy** (or Visual Hierarchy)
2. **Consistency** (Make user interfaces consistent)
3. **User Control** (or Allow users to reverse their actions)
4. **Familiarity**
5. **Design dialog to yield closure** (or Provide informative feedback)
6. **Provide informative feedback** (or Prevent errors)

</details>