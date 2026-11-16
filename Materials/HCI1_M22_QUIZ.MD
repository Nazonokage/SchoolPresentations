# Comprehensive Assessment: Design, Accessibility, and Responsive Web

---

## A. Lesson Preview & Review

Welcome to your third major checkpoint! This assessment covers the core concepts from Modules 15 through 21. Before you begin, let's do a quick recap of the critical topics:

*   **User-Centered Design (UCD):** Designing based on the specific needs, contexts, and feedback of the end-users.
*   **Universal Design & Accessibility:** Creating environments (physical or digital) that are usable by all people, regardless of age, size, or ability. We covered the **POUR** framework (Perceivable, Operable, Understandable, Robust) and the importance of **Assistive Technologies** (AT) like screen readers.
*   **Human Error & Safety Design:** Building systems that prevent mistakes (form validation, clear labels) and allow for recovery (undo buttons, confirmation dialogs).
*   **Evaluating Design Quality:** The 5 pillars are **Strategy** (business goals), **Usability** (ease of use), **Style** (aesthetics/brand), **Content** (readability), and **Search Optimization** (SEO).
*   **Responsive Design:** Using fluid grids, flexible images (like the `<picture>` tag), and media queries to ensure a website looks good on all devices.

> **Pro Tip:** For Test III, remember that responsive design doesn't just mean making things smaller; it means re-arranging them so they fit the screen. CSS `flex-wrap` or `@media` queries are your best friends here.

---

## B. The Quiz

### Test I. Identification (10 pts)
*Identify what's described/defined in each statement.*

1.  It is the design and composition of an environment so that it can be accessed, understood, and used to the greatest extent possible by all people regardless of their age, size, ability, or disability.
2.  This website design quality is defined by the question "Who is my target audience, and how does the design consider them?"
3.  This tag allows you to define different images for different browser window sizes.
4.  This design quality enables a person with a disability afforded the opportunity to acquire the same information, engage in the same interactions.
5.  This design is useful and marketable to people with diverse abilities.
6.  The key combination "CTRL-Z" is used for this purpose.
7.  This refers to practical considerations of what goes into good website design, such as speed, user-friendliness, security, technical details like sitemaps, etc.
8.  It is a form of assistive technology software that enables access to a computer, and to identify and interpret what is being displayed on the computer screen using text-to-speech.
9.  The P in POUR stands for ______.
10. This website design quality is alluded to by the question "Are the text big enough?"

### Test II. Acronyms (10 pts)
*Provide the complete meaning of each given acronym.*

1.  POUR: ________________________
2.  UI: ________________________
3.  UX: ________________________
4.  vw: ________________________
5.  GUI: ________________________
6.  SVGs: ________________________
7.  UDC: ________________________
8.  AT: ________________________
9.  HTML: ________________________
10. URL: ________________________

### Test III. HTML Code (10 pts)
*Write HTML codes to create a responsive design that divides the page into three columns.*

```html
<!-- Write your code here -->
```

---

## C. Answer Key

*Review your answers below. Don't peek until you've finished the quiz!*

<details>
<summary><strong>Click to reveal answers for Test I and II</strong></summary>

**Test I. Identification**
1.  **Universal Design**
2.  **Strategy**
3.  **`<picture>`** (or `<picture>` element)
4.  **Accessibility**
5.  **Equitable Use** (Universal Design Principle #1)
6.  **Undo** (or error recovery)
7.  **Usability**
8.  **Screen Reader**
9.  **Perceivable**
10. **Content**

**Test II. Acronyms**
1.  **POUR:** Perceivable, Operable, Understandable, Robust
2.  **UI:** User Interface
3.  **UX:** User Experience
4.  **vw:** Viewport Width
5.  **GUI:** Graphical User Interface
6.  **SVGs:** Scalable Vector Graphics
7.  **UDC:** Universal Design (and Accessibility) / User-Centered Design *(Note: In the context of Module 19, it specifically stood for Universal Design, though UCD is usually User-Centered Design).*
8.  **AT:** Assistive Technology
9.  **HTML:** HyperText Markup Language
10. **URL:** Uniform Resource Locator

</details>

<details>
<summary><strong>Click to reveal a sample answer for Test III</strong></summary>

*There are multiple ways to create a 3-column responsive layout. Here are the two most common approaches (Classic Media Query vs. Modern Flexbox). For full points, the code should show the structure and how it adapts (e.g., stacking on mobile).*

**Approach 1: Modern CSS Flexbox (Recommended)**
```html
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  .container {
    display: flex;
    flex-wrap: wrap; /* Allows columns to stack on smaller screens */
  }
  .column {
    flex: 1; /* Each column takes equal space */
    min-width: 250px; /* Breaks to a new line if screen is smaller than 250px */
    padding: 15px;
    box-sizing: border-box;
    border: 1px solid #ccc;
  }
</style>
</head>
<body>

<div class="container">
  <div class="column">Column 1</div>
  <div class="column">Column 2</div>
  <div class="column">Column 3</div>
</div>

</body>
</html>
```

**Approach 2: Classic CSS Media Query (Based on Module 18)**
```html
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  .col {
    float: left;
    width: 33.33%; /* Three equal columns by default */
    padding: 10px;
    box-sizing: border-box;
  }
  
  /* Breakpoint for mobile devices */
  @media screen and (max-width: 768px) {
    .col {
      width: 100%; /* Stacks vertically on smaller screens */
      float: none;
    }
  }
</style>
</head>
<body>

<div class="col" style="background-color:#aaa;">Column 1</div>
<div class="col" style="background-color:#bbb;">Column 2</div>
<div class="col" style="background-color:#ccc;">Column 3</div>

</body>
</html>
```
</details>