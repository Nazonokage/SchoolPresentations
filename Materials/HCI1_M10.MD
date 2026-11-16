# Basic HTML 3: Lists and Tables

---

## A. Lesson Preview & Review

Welcome to Module 10! In previous modules, we learned how to format text and add media. Now, we are going to learn how to organize information using **Lists** and **Tables**. 

Organizing data is crucial. Lists are used to group related pieces of information together so they are easy to read and understand. Tables are used to display large amounts of structured data neatly in rows and columns. 

**Learning Objectives:**
By the end of this module, you should be able to:
1.  Identify the different HTML list and table tags.
2.  Understand how to use HTML lists and table tags correctly.
3.  Create a sample web design using lists and tables.

> **Pro Tip (Modern Context):** In modern web development, HTML is used strictly for the **structure and meaning (semantics)** of the content. While older HTML versions used attributes to style lists (like changing bullet types) or tables (like adding borders), today we use **CSS** to handle all the visual styling. We use HTML lists and tables purely to tell the browser *what* the data is, not how it looks.

---

## B. Main Lesson

### Part 1: HTML Lists

There are three main types of lists in HTML. Each has a specific purpose and meaning.

#### 1. Unordered Lists (`<ul>`)
An unordered list is used to group a set of related items where the order **does not matter**. They are typically rendered as a bulleted list. 

*   *Example:* A grocery shopping list. It doesn't matter if you buy milk before bread.

**Syntax:**
You wrap the entire list in `<ul>` tags, and wrap each individual item in `<li>` (list item) tags.
```html
<ul>
  <li>milk</li>
  <li>bread</li>
  <li>butter</li>
  <li>coffee beans</li>
</ul>
```

#### 2. Ordered Lists (`<ol>`)
An ordered list is used when the sequence of items **is important**. They are typically rendered as a numbered list.

*   *Example:* A cooking recipe or step-by-step instructions. You cannot mix the ingredients after you bake the cake.

**Syntax:**
You wrap the list in `<ol>` tags, and use `<li>` for the items.
```html
<ol>
  <li>Gather ingredients</li>
  <li>Mix ingredients together</li>
  <li>Place ingredients in a baking dish</li>
  <li>Bake in oven for an hour</li>
  <li>Remove from oven</li>
</ol>
```
> **Historical Note:** In older HTML, you could use the `type` attribute on `<ol>` to change the numbering to letters (A, B, C) or Roman numerals (I, II, III). In modern development, you use CSS (`list-style-type`) to achieve this.

#### 3. Description Lists (`<dl>`)
A description list is used to display name/value pairs, such as terms and their definitions, or FAQ questions and answers. 

**Syntax:**
*   `<dl>`: The container for the whole list.
*   `<dt>`: The Description Term (the name or item).
*   `<dd>`: The Description Definition (the value or description).

```html
<dl>
  <dt>Coffee</dt>
  <dd>A beverage made from roasted, ground coffee beans.</dd>
  
  <dt>Espresso</dt>
  <dd>A concentrated form of coffee served in small, strong shots.</dd>
</dl>
```

---

### Part 2: HTML Tables

When building a project, you will sometimes need to display data visually in rows and columns. HTML tables are designed exactly for this—representing tabular data (like a spreadsheet).

> ⚠️ **Important Modern Warning:** In the early days of the web, designers used massive tables to create website layouts (e.g., putting a sidebar in one table cell and the main content in another). **Never do this today.** Tables are strictly for data (like schedules, pricing, or stats). For layout, use modern CSS (Grid or Flexbox).

#### Basic Table Structure
*   `<table>`: The main container for the table.
*   `<tr>`: Table Row. Defines a row in the table.
*   `<th>`: Table Header. Used for the top row to define column headings. Text inside `<th>` is bolded and centered by default.
*   `<td>`: Table Data. Defines a standard data cell.

**Code Example:**
```html
<table>
  <!-- First Row: Headers -->
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  
  <!-- Second Row: Data -->
  <tr>
    <td>March</td>
    <td>$200</td>
  </tr>
  
  <!-- Third Row: Data -->
  <tr>
    <td>April</td>
    <td>$300</td>
  </tr>
</table>
```

**Result:**
| Month | Savings |
| :--- | :--- |
| March | $200 |
| April | $300 |

> **Modern Accessibility Tip:** When using `<th>` tags, it is highly recommended to add the `scope` attribute for screen readers. For example, `<th scope="col">Month</th>` tells a screen reader that "Month" is the header for that entire column. 

---

## C. Analogies and Use Cases

### The Lists Analogy
*   **Unordered List (`<ul>`):** Think of a bucket of items you need to buy at the hardware store. The order doesn't matter, you just need all of them.
*   **Ordered List (`<ol>`):** Think of a recipe. You cannot bake the cake before you mix the batter. 
*   **Description List (`<dl>`):** Think of a dictionary. You have the word (Term) and the meaning (Definition).

### Use Case: Tabular Data vs. Layout
Imagine you are building a pricing page for a software company. You have three tiers: Basic, Pro, and Enterprise. You want to compare features side-by-side. A **Table** is perfect for this because it aligns the features horizontally, allowing users to easily compare the data. 
However, you wouldn't use a table to structure the header and footer of that webpage. You use CSS to position the header at the top and the footer at the bottom.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   HTML provides three lists: **Unordered** (bullets), **Ordered** (numbers), and **Description** (definitions).
*   Lists are nested: use `<li>` inside `<ul>` or `<ol>`.
*   Tables are built using `<table>`, `<tr>` (rows), `<th>` (headers), and `<td>` (data cells).
*   Never use tables for webpage layout; only use them for tabular data.

### Frequently Asked Questions

**Q: How do I make my table have borders? It looks invisible!**
**A:** By default, modern browsers render tables without borders. You must use CSS to add them. Add this to your `<style>` tag or CSS file: `table, th, td { border: 1px solid black; }`.

**Q: Can I put a list inside a table cell?**
**A:** Yes! You can put an `<ul>` or `<ol>` inside a `<td>` or `<th>` tag. This is great for listing multiple features within a single cell of a pricing table.

**Q: Why does my text in the table look squished together?**
**A:** You likely need to add cell padding. In CSS, you can use `padding: 10px;` on your `<td>` and `<th>` elements to give the text some breathing room.

---

## E. Guided Drills / Code Projects

### Exercise 1: Create Your Own Sample HTML
**Instructions:** Build an HTML page that uses both lists and tables.
1.  Create an `<h1>` title: "My Favorite Recipes".
2.  Create an **Unordered List** of your top 3 favorite foods.
3.  Create an **Ordered List** detailing the steps to make a sandwich.
4.  Create a **Table** with 2 columns: "Class" and "Grade". Add 3 rows of data.
5.  *Bonus:* Wrap the table in a `<style>` block and add a border to the table and cells so you can actually see it!

```html
<!-- Example to get you started -->
<!DOCTYPE html>
<html>
<head>
  <style>
    table, th, td {
      border: 1px solid black;
      border-collapse: collapse;
      padding: 5px;
    }
  </style>
</head>
<body>
  <h1>My Schedule</h1>
  <!-- Add your table here -->
</body>
</html>
```

---

## F. Skill-Building Check

*Test your understanding of the lists and tables covered in this module.*

1.  A block element used to create a table.
2.  Type of list to display items that should be in a specific order.
3.  Type of list to display name/value pairs such as terms and definitions.
4.  This tag defines the heading of the table.
5.  This tag is used to create table rows.
6.  It is the representation of data arranged in rows and columns.
7.  Type of list to group a set of related items in no particular order.
8.  These are used to group together related pieces of information so they are clearly associated with each other.
9.  The HTML tag to create a table.
10. The HTML tag used to create data cells.

<details>
<summary><strong>Click to reveal answers</strong></summary>

1. **table** (`<table>`)
2. **Ordered list** (`<ol>`)
3. **Description list** (`<dl>`)
4. **Table Header** (`<th>`)
5. **Table Row** (`<tr>`)
6. **Table**
7. **Unordered list** (`<ul>`)
8. **Lists**
9. **`<table>`**
10. **Table Data** (`<td>`)

</details>