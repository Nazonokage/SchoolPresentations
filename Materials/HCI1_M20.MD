# Human Error and Safety Design

---

## A. Lesson Preview & Review

We all make mistakes. No matter how careful, diligent, or tech-savvy a user is, errors are inevitable. A simple typo, a mis-click on a mobile phone, or entering the wrong information into a form can lead to frustration—or worse, accidental financial loss. 

> **In a Nutshell:** You cannot trust users to always do the right thing. As a designer, your job is to assume human error will happen and build systems that **prevent, catch, or easily recover** from those mistakes.

**Learning Objectives:**
By the end of this module, you should be able to:
1. Identify what human error is and why safety design is crucial.
2. Understand the 9 concepts of designing for human error.
3. Modify web designs to minimize user errors.

---

## B. Main Lesson: 9 Ways to Design for Human Error

To err is human. Here is how to design web interfaces that act as a safety net for your users.

### 1. Clear Instructions
People often skip instructions because they assume they already know how to do a simple task. This assumption is the root of many errors. 
*   **Best Practice:** Put clear, concise instructions on any task more complex than a basic contact form. Use tooltips or inline help text to guide users right where they need it.

### 2. Clear Warnings
Users need to know the consequences of their actions. 
*   **Best Practice:** If an action is destructive (like deleting an account or formatting a drive), warn them clearly. However, beware of **alert fatigue**—if you warn users about *everything*, they will ignore *everything*. Reserve strong warnings for critical, irreversible actions.

### 3. White Space (Spacing)
Miss-clicks and "fat-finger" taps are incredibly common, especially on touch screens.
*   **Best Practice:** Give clickable elements breathing room. If a "Delete" button sits directly next to a "Save" button, a slight mis-tap can be disastrous. Add ample negative space between buttons with opposing actions.

### 4. Confirmation Dialogs
A confirmation dialog is that "Are you sure you want to do that?" pop-up. 
*   **Best Practice:** Use these for destructive actions. However, use them sparingly. For users who perform a repetitive task (like data entry), constant confirmation pop-ups become an annoying hindrance, leading to "dialog blindness" where users click "Yes" without even reading.

### 5. Form Validation
Preventing users from putting the wrong text in the wrong format is a powerful safety measure.
*   **Modern Update:** Instead of waiting until the user hits "Submit" to show all errors, use **Inline Validation**. Validate the field as the user types or when they leave the field (on blur). For example, changing the border to green when a valid email is entered, or red with an error message if the password is too short.

### 6. Clear Labels
Vague labels are a major source of form abandonment and errors. Worse is using industry jargon on a client-facing website.
*   **Modern Update:** Avoid "placeholder-only" labels. Placeholders (text that sits inside the input box) disappear once the user starts typing. If they get distracted, they forget what the field was for. Always use a persistent label above or beside the input field.

### 7. Use Both Color and Contrast
Relying solely on color to convey meaning (e.g., green = good, red = bad) is a mistake. 
*   **Best Practice:** Color-blind users may not be able to distinguish between red and green. Always pair color with **contrast, text, or icons**. For example, don't just turn a field red; add an error icon (!) and text that says "Invalid email format."

### 8. Make Changes Carefully
People operate on "autopilot" when performing familiar tasks. If you suddenly change the location of a menu item, users will click the wrong thing out of pure muscle memory.
*   **Modern Context:** This is related to **Jakob's Law**—users spend most of their time on *other* sites, so they expect yours to work the same way. If you must do a UI redesign, consider using "feature highlights" or onboarding tours to show users what has changed.

### 9. Undo Buttons Where Possible
The ultimate safety net is the ability to reverse a mistake.
*   **Best Practice:** Implement "Undo" functions for any action with permanent consequences. 
*   **Modern Standard:** The **"Snackbar" or "Toast" notification**. Think of how Gmail works: when you delete an email, a message pops up at the bottom saying "Conversation moved to Trash. Undo." This provides immediate error recovery without interrupting the user's flow.

![User Error](https://images.unsplash.com/photo-1516321497487-e288fb19713f?auto=format&fit=crop&w=800&q=80)
*Good design catches the user before they make a critical mistake.*

---

## C. Analogies and Use Cases

### The "Poka-Yoke" Analogy
In manufacturing and engineering, there is a Japanese concept called **Poka-Yoke** (pronounced *poh-kah yoh-kay*), which means "mistake-proofing." 
A classic example is a microwave: you cannot turn it on if the door is open. The design physically prevents you from making a mistake. In web design, disabling a "Submit" button until all required fields are filled out is a form of Poka-Yoke.

### Use Case: The Danger of the "Delete" Button
Imagine a backend dashboard where an admin manages user accounts. The "Edit Profile" and "Delete User" buttons are placed right next to each other. A user goes to edit a profile, mis-clicks, and permanently deletes the account. 
*   *Safety Design Fix:* Move the delete button to a separate "Danger Zone" at the bottom of the page, make it red, and require a confirmation dialog where they have to type "DELETE" to confirm.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   Assume users will make mistakes; design to prevent them.
*   Use **white space** and **clear labels** to prevent mis-clicks and confusion.
*   Use **warnings** and **confirmation dialogs** for destructive actions (but don't overuse them).
*   **Form validation** should guide users in real-time.
*   Always provide an **Undo** option (like Snackbar notifications) as a final safety net.

### Frequently Asked Questions

**Q: Why are confirmation dialogs sometimes bad?**
**A:** If you use them for every minor action, users develop "alert fatigue" and will automatically click "Yes" or "OK" without reading. This defeats the purpose of the safety check. Save them for high-stakes actions.

**Q: How do I make my error messages helpful?**
**A:** A bad error message says: "Error 404: Invalid input." A good error message says: "Please enter a valid email address (e.g., name@example.com)." Tell the user exactly what went wrong and how to fix it.

---

## E. Guided Drills / Design Activities

### Exercise 1: The Human Error Audit
**Instructions:** Find a website or app that you use regularly. Look for examples of good (or bad) error prevention. 
*   Find one example of **Form Validation**.
*   Find one example of an **Undo/Snackbar** feature.
*   Find one example where a user could easily make a mistake due to poor spacing or labeling.

---

## F. Skill-Building Check

*Write **TRUE** if the statement is correct. Otherwise, write **FALSE**.*

1.  Users will never make mistakes if they are ever caring, careful, and diligent.
2.  The key combination CTRL+Z is for UNDO.
3.  Form validation is a great way to guide the user in the right direction.
4.  The question "Are you sure you want to do that?" may manifest as a label in an app or website.
5.  Adding contrast to elements makes them clearly and easily distinguished from each other.

<details>
<summary><strong>Click to reveal answers</strong></summary>

1. **FALSE** *(Even the most careful users will make mistakes. Error prevention is a design responsibility).*
2. **TRUE**
3. **TRUE**
4. **FALSE** *(This manifests as a Confirmation Dialog, not a label).*
5. **TRUE**

</details>