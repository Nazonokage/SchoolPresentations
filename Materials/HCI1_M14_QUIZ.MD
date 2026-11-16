# Comprehensive Assessment: HTML & Web Design

---

## A. Lesson Preview & Review

Welcome to your second major checkpoint! This assessment will test your knowledge of HTML structure, legacy frame tags, and the principles of good web design.

Before you begin, here is a quick recap of the key concepts you need to know:

*   **HTML Tags:** Remember the differences between structural tags (`<html>`, `<body>`), list tags (`<ul>`, `<ol>`, `<li>`), table tags (`<table>`, `<tr>`, `<th>`, `<td>`), and text formatting tags (`<em>`, `<mark>`, `<sup>`).
*   **Simplicity in Design:** When designing a website, you should limit your color palette to **less than 5 colors**, use a **maximum of 3 fonts**, and ensure high-quality **imagery**.
*   **Legacy Frames (`<frameset>`):** Though obsolete, remember that `<frameset>` replaces the `<body>` tag and uses attributes like `cols` and `rows` to divide the screen, while `<frame>` uses `src` to load the files.
*   **Web Design Principles:** Always keep in mind the 9 principles: Purpose, Simplicity, Navigation, F-Shaped Pattern, Visual Hierarchy, Content, Grid-Based Layout, Load Time, and Mobile Friendly.

> **Pro Tip:** For the coding section, remember that tables are built row by row (`<tr>`). Inside each row, you create the data cells (`<td>`). You will need to nest your code carefully.

---

## B. The Quiz

### Test I. Identification (10 pts)
*Identify what HTML tag is being described in each statement.*

1.  This is used to group a set of related items in no particular order.
2.  This tag wraps all the content on the entire page and is sometimes known as the root element.
3.  This tag sets the title of your page.
4.  This is a logical tag which is used to display content in italic.
5.  This tag is used to create table rows.
6.  This tag is used for the heading of the table.
7.  This contains all the content that you want to show to visitors of your web page.
8.  This tag is used to highlight text.
9.  This tag displays the content slightly above the normal line.
10. This tag is used to create frames.

### Test II. Enumeration (10 pts)

**1-3 Ways to achieve simplicity**
*   1. ________________________
*   2. ________________________
*   3. ________________________

**4-8 Attributes of a `<frameset>` tag** *(List any 5)*
*   4. ________________________
*   5. ________________________
*   6. ________________________
*   7. ________________________
*   8. ________________________

**9-10 Principles of good website design** *(List any 2)*
*   9. ________________________
*   10. ________________________

### Test III. HTML Coding (10 pts)
*Create HTML codes that will display a 10 x 10 multiplication table.*

*(Note: You can write the structural logic below, or write out the full code on a separate sheet.)*

```html
<!-- Write your multiplication table code here -->
```

---

## C. Answer Key

*Review your answers below. Don't peek until you've finished the quiz!*

<details>
<summary><strong>Click to reveal answers for Test I and II</strong></summary>

**Test I. Identification**
1.  **`<ul>`** (Unordered List)
2.  **`<html>`**
3.  **`<title>`**
4.  **`<em>`** (Emphasis)
5.  **`<tr>`** (Table Row)
6.  **`<th>`** (Table Header)
7.  **`<body>`**
8.  **`<mark>`**
9.  **`<sup>`** (Superscript)
10. **`<frameset>`**

**Test II. Enumeration**
**1-3 Ways to achieve simplicity** (Any order)
*   **Color** (Limiting to <5 colors)
*   **Type / Typography** (Limiting to max 3 fonts)
*   **Imagery** (Using high-quality, expressive visual aspects)

**4-8 Attributes of a `<frameset>` tag** (Any 5 of the following)
*   **`cols`**
*   **`rows`**
*   **`border`**
*   **`frameborder`**
*   **`framespacing`**
*   *(Note: Attributes like `src`, `name`, `noresize`, `scrolling` belong to the `<frame>` tag, not `<frameset>`, but depending on the strictness of the teacher, they might accept them.)*

**9-10 Principles of good website design** (Any 2 of the following)
*   **Website Purpose**
*   **Simplicity**
*   **Navigation**
*   **F-Shaped Pattern Reading**
*   **Visual Hierarchy**
*   **Content**
*   **Grid-Based Layout**
*   **Load Time**
*   **Mobile Friendly**

</details>

<details>
<summary><strong>Click to reveal an example Answer for Test III</strong></summary>

*To create a 10x10 multiplication table entirely manually in HTML without a server-side language like PHP or a client-side language like JavaScript would require writing 100 individual cells. For a written quiz, teachers are usually looking for the correct structural understanding.*

**Basic Structural Approach:**
You would need a `<table>`, 10 `<tr>` tags (for rows), and inside each row, 10 `<td>` tags (for columns). 

```html
<table border="1">
  <!-- Row 1 -->
  <tr>
    <td>1x1=1</td>
    <td>1x2=2</td>
    <!-- ... up to 1x10=10 ... -->
  </tr>
  <!-- Row 2 -->
  <tr>
    <td>2x1=2</td>
    <td>2x2=4</td>
    <!-- ... up to 2x10=20 ... -->
  </tr>
  <!-- ... Repeat for Rows 3 through 10 ... -->
</table>
```

**Advanced/Modern Approach (If the teacher allows basic scripting):**
If they expect a programmatic answer using JavaScript to generate the table:
```html
<!DOCTYPE html>
<html>
<body>
  <table border="1" id="multTable"></table>

  <script>
    let table = document.getElementById("multTable");
    for (let i = 1; i <= 10; i++) {
      let row = table.insertRow();
      for (let j = 1; j <= 10; j++) {
        let cell = row.insertCell();
        cell.innerHTML = i * j;
      }
    }
  </script>
</body>
</html>
```
</details>