# Basic HTML: Structuring the Web

---

## A. Lesson Preview & Review

Welcome to Module 7! Up to now, we've focused on *designing* interfaces (UI/UX). Now, we are going to look at how those designs are actually built on the web. 

**What is HTML?**
**HTML (HyperText Markup Language)** is the standard code used to structure a web page and its content. Think of it as the "skeleton" of a website. It allows you to define paragraphs, bulleted lists, images, and data tables. HTML uses a series of **elements** (tags) to enclose, wrap, or annotate different parts of content to tell the browser how to display them.

> **Pro Tip (Modern Context):** Today, web development relies on three main languages working together:
> *   **HTML** provides the *structure* (the skeleton).
> *   **CSS** provides the *style* (the skin, colors, and layout).
> *   **JavaScript** provides the *behavior* (the muscles, interactivity).
> In this module, we focus entirely on the structure: HTML.

---

## B. Main Lesson

### 1. The Anatomy of an HTML Element
Let's look at a basic line of text and turn it into an HTML paragraph:

```html
<p>My cat is very grumpy</p>
```

Here is how that element is broken down:
*   **Opening tag:** `<p>` - Consists of the element name wrapped in **angle brackets**. It states where the element begins.
*   **Closing tag:** `</p>` - Same as the opening tag, but includes a forward slash `/`. It states where the element ends. *Forgetting this is a common beginner error!*
*   **Content:** `My cat is very grumpy` - The text or media inside the element.
*   **Element:** The combination of the opening tag, content, and closing tag.

#### What are Attributes?
Elements can also have **attributes**, which contain extra information about the element that you don't want to appear in the actual content.

```html
<p class="editor-note">My cat is very grumpy</p>
```
*   `class` is the **attribute name**.
*   `editor-note` is the **attribute value**.

**Rules for Attributes:**
1.  A space between it and the element name (or the previous attribute).
2.  The attribute name followed by an equals sign `=`.
3.  The attribute value wrapped by opening and closing quotation marks `""`.

---

### 2. The Basic HTML Document Structure
Every web page needs a specific skeleton to behave correctly. Here is the standard HTML5 boilerplate:

```html
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My test page</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="My test image">
  </body>
</html>
```

**Breakdown of the Document:**
*   `<!DOCTYPE html>`: A required preamble. In modern web development (HTML5), this simply tells the browser to render the page using standard modern rules.
*   `<html></html>`: The **root element**. It wraps all the content on the entire page. The `lang` attribute sets the primary language (important for screen readers).
*   `<head></head>`: A container for metadata (data about the page). It contains things like keywords for search engines, character sets, and links to CSS stylesheets. *It is not visible to the user.*
*   `<meta charset="utf-8">`: Tells the document to use the UTF-8 character set, which includes almost all characters from human languages. 
*   `<meta name="viewport" ...>`: Ensures the page renders at the width of the device's screen, preventing mobile browsers from shrinking the page.
*   `<title></title>`: Sets the title that appears in the browser tab or bookmark.
*   `<body></body>`: Contains *all* the content you want to show to web users (text, images, videos, etc.).

> **How to test this:** You can save the code above into a Notepad file, name it `index.html`, and double-click it to open it in your web browser!

---

### 3. HTML Text Formatting
HTML provides many tags to format text. These are divided into two main categories:
1.  **Physical tags:** Provide purely visual appearance (styling).
2.  **Logical tags:** Add logical or semantic value (meaning) to the text.

> **Modern Best Practice:** In modern web design, we strongly prefer **Logical tags**. Why? Because screen readers (used by visually impaired users) understand logical tags. Also, CSS should be used to handle most physical styling nowadays. 

Here is a breakdown of the tags covered in the module, plus modern context:

| Element | Category | Description | Modern Usage Note |
| :--- | :--- | :--- | :--- |
| `<b>` | Physical | Bolds text. | Used for visual offset without extra importance. |
| `<strong>` | **Logical** | Indicates strong importance. | **Prefer this.** Browsers render it bold, and screen readers emphasize it. |
| `<i>` | Physical | Italicizes text. | Used for visual offset (e.g., foreign words, thoughts). |
| `<em>` | **Logical** | Indicates emphasized stress. | **Prefer this.** Browsers render it italic, and screen readers emphasize it. |
| `<mark>` | Logical | Highlights text. | Great for search result highlighting. |
| `<u>` | Physical | Underlines text. | *Caution:* Users often confuse underlined text with hyperlinks. |
| `<tt>` | Physical | Teletype (monospaced font). | ⚠️ **Deprecated in HTML5.** Use CSS `font-family` instead. |
| `<strike>` | Physical | Strikethrough text. | ⚠️ **Deprecated in HTML5.** Use `<s>` or `<del>` instead. |
| `<del>` | Logical | Represents deleted text. | Renders with a strikethrough. Great for tracking document edits. |
| `<ins>` | Logical | Represents inserted text. | Often rendered with an underline. Pairs with `<del>`. |
| `<sup>` | Physical | Superscript (above line). | Great for exponents like \(E=mc^2\) or footnotes. |
| `<sub>` | Physical | Subscript (below line). | Great for chemical formulas like \(H_2O\). |
| `<big>` | Physical | Increases font size. | ⚠️ **Deprecated in HTML5.** Use CSS `font-size` instead. |
| `<small>` | Logical | Decreases font size. | Represents "side comments" or fine print (like copyright). |

#### Code Examples

**Bold & Strong:**
```html
<p><b>Write Your First Paragraph in bold text.</b></p>
<p><strong>This is an important content</strong>, and this is normal content.</p>
```

**Italic & Emphasis:**
```html
<p><i>Write Your First Paragraph in italic text.</i></p>
<p><em>This is an important content</em>, which displayed in italic font.</p>
```

**Highlight & Underline:**
```html
<h2>I want to put a <mark>Mark</mark> on your face</h2>
<p><u>Write Your First Paragraph in underlined text.</u></p>
```

**Subscript, Superscript, and More:**
```html
<p>Hello <sup>Write Your First Paragraph in superscript.</sup></p>
<p>Hello <sub>Write Your First Paragraph in subscript.</sub></p>
<p>Hello <del>Delete your first paragraph.</del> <ins>Write another paragraph.</ins></p>
<p>Hello <small>Write the paragraph in smaller font.</small></p>
```

> **Note on Headers:** You can make text bigger and more important by using header tags, `<h1>` through `<h6>`. `<h1>` is the most important (usually the main title), and `<h6>` is the least. Don't use them just to make text big; use them to structure your document hierarchy!

---

## C. Analogies and Use Cases

### The "House" Analogy
Building a website is like building a house:
*   **HTML** is the wooden frame, the bricks, and the floor plan. It defines where the walls (paragraphs) and doors (links) go.
*   **CSS** is the paint, wallpaper, and interior design. It makes the walls look pretty.
*   **JavaScript** is the electricity and plumbing. It makes the lights turn on when you flip a switch.

### Use Case: Why `<strong>` is better than `<b>`
Imagine a screen reader reading a webpage to a blind user. If the text says `<b>Warning: Do not enter</b>`, the screen reader just reads it in a normal voice. But if the text says `<strong>Warning: Do not enter</strong>`, the screen reader knows to change its tone, perhaps reading it louder or with emphasis. This is why **Logical tags** are crucial for accessibility!

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   HTML elements consist of an **opening tag**, **content**, and a **closing tag**.
*   The `<head>` contains metadata, while the `<body>` contains visible content.
*   **Logical tags** (`<strong>`, `<em>`, `<del>`) are preferred over **Physical tags** (`<b>`, `<i>`) for accessibility and modern web standards.
*   Many older styling tags like `<big>`, `<tt>`, and `<strike>` have been deprecated in HTML5 in favor of CSS.

### Frequently Asked Questions

**Q: What does "Deprecated" mean?**
**A:** It means the tag is obsolete. Browsers might still support it for older websites, but you shouldn't use it in new projects. Modern HTML5 relies on CSS for styling things like font size and type.

**Q: Why did my text not break into a new line when I hit "Enter" in my code?**
**A:** HTML ignores extra spaces and line breaks in the code. If you want to start a new paragraph, you must wrap it in `<p>` tags. If you just want a single line break, you use the `<br>` tag.

**Q: What is the `<head>` used for if we can't see it?**
**A:** The `<head>` is the "brain" of the page. It tells search engines what the page is about, it holds the title for the browser tab, and it links to the CSS files that make the page look good. 

---

## E. Guided Drills / Code Projects

### Exercise 1: Create Your Own Sample HTML
**Instructions:** Using a text editor (like Notepad, VS Code, or an online editor like CodePen), write a complete HTML document that includes:
1.  The `<!DOCTYPE html>` and basic document structure.
2.  A `<title>` in the head that says "My First Webpage".
3.  A main `<h1>` header with your name.
4.  A paragraph about yourself using `<strong>` for your major and `<em>` for your favorite hobby.
5.  A list of your top 3 favorite foods, using `<del>` on the one you hate and `<ins>` on a new one you want to try.
6.  A mathematical formula using `<sup>` (e.g., 10<sup>2</sup>).
7.  A chemical formula using `<sub>` (e.g., H<sub>2</sub>O).

*Save it as `index.html` and open it in your browser to see the result!*

---

## F. Skill-Building Check

*Test your understanding of basic HTML by identifying the tags described below.*

1.  This tag doesn't do much and is basically just needed to make sure your document behaves correctly (a required preamble).
2.  This element acts as a container for all the stuff you want to include on the HTML page that *isn't* the content you are showing to your page's viewers.
3.  This tag is used to put your font size smaller than the rest of the text.
4.  This means something is displayed half a character's height above the other characters.
5.  It is a tag that puts a line under your text.
6.  This sets the title of your page, which is the title that appears in the browser tab.
7.  This contains *all* the content that you want to show to web users when they visit your page.
8.  This tag is used to highlight text.
9.  This tag is used to increase the font size by one conventional unit (deprecated in HTML5).
10. This is a physical tag, which is used to bold the text written between it.

<details>
<summary><strong>Click to reveal answers</strong></summary>

1. `<!DOCTYPE html>`
2. `<head>`
3. `<small>`
4. `<sup>` (Superscript)
5. `<u>`
6. `<title>`
7. `<body>`
8. `<mark>`
9. `<big>`
10. `<b>`

</details>