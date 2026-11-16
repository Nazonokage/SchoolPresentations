# Basic HTML 4: HTML Frames (Legacy Features)

---

## A. Lesson Preview & Review

Welcome to Module 11! In this lesson, we are going to look at **HTML Frames**. 

Historically, HTML frames were used to divide a browser window into multiple, independent sections (rows and columns). Each section (frame) could load a completely separate HTML document at the same time. The collection of these frames was called a **frameset**.

> **⚠️ CRITICAL MODERN WARNING:** The `<frameset>` and `<frame>` tags we are about to discuss are **completely obsolete and deprecated in HTML5**. Modern web browsers barely support them, and they are considered terrible practice for layout, accessibility, and mobile responsiveness. 
> 
> *Why learn them?* You may encounter them in legacy enterprise systems or older websites. However, **never use them for new projects**. I have included modern alternatives at the end of the lesson to show you how this is actually done today!

**Learning Objectives:**
By the end of this module, you should be able to:
1. Identify HTML frame tags.
2. Understand how to use HTML frame tags in legacy systems.
3. Create a sample web design using frame tags.

---

## B. Main Lesson

### 1. The Disadvantages of Frames
Even when frames were popular, they had massive drawbacks. This is why they were removed from the modern web standard:
*   **Mobile Devices:** Small screens cannot handle dividing the screen into multiple frames.
*   **Screen Resolutions:** Pages looked wildly different on different monitors.
*   **Broken Navigation:** The browser's "Back" button often behaved unpredictably.
*   **Browser Support:** Not all browsers supported them well.

*(Modern Context: They also break SEO, ruin bookmarking because the URL doesn't change, and make it impossible for screen readers to navigate the page).*

### 2. Creating Frames
Instead of using the `<body>` tag, a framed page used the `<frameset>` tag. 

*   The `<frameset>` tag defines how to divide the window (using the `rows` or `cols` attributes).
*   The `<frame>` tag is placed inside the `<frameset>` to indicate which HTML document should open in that specific section (using the `src` attribute).

#### The `<frameset>` Tag Attributes

| Attribute | Description |
| :--- | :--- |
| **`cols`** | Specifies the number and size of columns. You can use pixels (`"100, 500"`), percentages (`"10%, 80%"`), or wildcards (`"10%, *"`). |
| **`rows`** | Specifies the number and size of rows. Works exactly like `cols` but for horizontal sections. |
| **`border`** | Width of the border between frames in pixels (e.g., `border="5"`). `0` means no border. |
| **`frameborder`** | Whether a 3D border should be displayed (`1` for yes, `0` for no). |
| **`framespacing`** | The amount of empty space between frames. |

#### The `<frame>` Tag Attributes

| Attribute | Description |
| :--- | :--- |
| **`src`** | The URL or file path of the HTML document to load inside the frame. |
| **`name`** | Gives the frame a name (e.g., `name="main_content"`). This is crucial if you want a link in one frame to load a page in another frame. |
| **`frameborder`** | Overrides the frameset border setting for this specific frame (`1` or `0`). |
| **`marginwidth`** | Space between the left/right of the frame's borders and its content. |
| **`marginheight`** | Space between the top/bottom of the frame's borders and its content. |
| **`noresize`** | By default, users can drag borders to resize frames. Adding this attribute (`noresize="noresize"`) locks the size. |
| **`scrolling`** | Controls scrollbars: `"yes"`, `"no"`, or `"auto"`. |
| **`longdesc`** | A link to a page containing a detailed description of the frame's content (an old accessibility attempt). |

### 3. Code Examples

**Example 1: Creating Vertical Frames**
This layout creates three vertical columns. The middle column takes up 50% of the screen.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Vertical Frames</title>
</head>
<frameset cols="25%, 50%, 25%">
  <frame src="left_menu.html">
  <frame src="main_content.html">
  <frame src="right_sidebar.html">
</frameset>
</html>
```
*Note: There is no `<body>` tag in a frameset document!*

**Example 2: Creating Horizontal Frames**
This layout stacks three rows. The `name` attributes are added so links can target them later.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Horizontal Frames</title>
</head>
<frameset rows="30%, 40%, 30%">
  <frame name="top" src="header.html">
  <frame name="main" src="content.html">
  <frame name="bottom" src="footer.html">
</frameset>
</html>
```

---

### 💡 How We Do It Today: Modern Alternatives

Since `<frameset>` is dead, how do we achieve similar layouts or embed content today?

#### 1. For Layouts (Sidebar + Main Content)
We use **CSS Grid** or **CSS Flexbox**. This is much cleaner, highly responsive for mobile devices, and doesn't require separate HTML files for the menu and content.

```html
<!-- Modern Layout Approach -->
<body style="display: flex;">
  <nav style="width: 25%;">Sidebar Menu</nav>
  <main style="width: 75%;">Main Content</main>
</body>
```

#### 2. For Embedding External Content (`<iframe>`)
If you need to embed a YouTube video, a Google Map, or a specific widget into your page, you use the **`<iframe>` (Inline Frame)** tag. 

**Do not confuse `<frame>` (legacy layout) with `<iframe>` (modern embedding).**

```html
<!-- Modern Embedding with iframe -->
<iframe 
  width="560" 
  height="315" 
  src="https://www.youtube.com/embed/dQw4w9WgXcQ" 
  title="YouTube video player" 
  frameborder="0" 
  allowfullscreen>
</iframe>
```

---

## C. Analogies and Use Cases

### The Picture-in-Picture Analogy
Imagine watching a TV with a Picture-in-Picture feature. You have the main broadcast on the big screen, and a smaller news ticker or sports score in the corner. 
*   **Legacy `<frameset>`:** Forcing the *entire* browser window to act like a TV split into 3 equal channels playing simultaneously, all controlled by one remote.
*   **Modern `<iframe>`:** Placing a small TV (a YouTube video) inside your living room (your web page). The rest of your page functions normally around it.

### Use Case: Why Frames Broke the Web
Imagine you are browsing a site with a left frame menu and a right frame content area. You click "About Us" in the left menu. The right frame loads the new page. However, look at the URL bar at the top of the browser—it hasn't changed! 
If you try to bookmark the page, or copy/paste the link to a friend, it will just load the homepage again because the URL doesn't track the state of the individual frames. This is a massive UX failure.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   Framesets replace the `<body>` tag to divide a browser window into `rows` and `cols`.
*   The `<frame>` tag loads individual HTML files into those sections.
*   Frames are **deprecated** and obsolete. 
*   Modern layout is done with CSS (Grid/Flexbox).
*   Modern embedding of content is done with `<iframe>`.

### Frequently Asked Questions

**Q: Can I still use `<frameset>` if I want to?**
**A:** You can write the code, but the browser might ignore it, render it weirdly, or it will break completely on a mobile phone. It is highly recommended to learn CSS Flexbox or Grid instead.

**Q: What is the difference between `<frame>` and `<iframe>`?**
**A:** `<frame>` was used exclusively inside a `<frameset>` to build the main layout of a webpage (now obsolete). An `<iframe>` (Inline Frame) is used *inside* a normal `<body>` tag to embed a piece of external content (like a map or video) within a standard webpage.

**Q: Why does the `name` attribute matter in a `<frame>`?**
**A:** In a legacy frameset, you could make a link in the left menu open in the right frame by using the `target` attribute: `<a href="page.html" target="main_frame">`. The `name` attribute was required to identify the target frame.

---

## E. Guided Drills / Code Projects

### Exercise 1: Legacy vs. Modern
**Instructions:**
1.  Create a legacy `<frameset>` that divides the screen horizontally into two rows: 20% and 80%. Name the top frame "header" and the bottom frame "main". (Note: You will need to create dummy files like `header.html` and `main.html` in the same folder to see it work).
2.  **Challenge:** Recreate that exact same 20/80 layout using CSS Flexbox in a standard `<body>` tag without using frames. 

*Modern Flexbox Solution for the challenge:*
```html
<body style="margin: 0; display: flex; flex-direction: column; height: 100vh;">
  <header style="height: 20%; background-color: #ccc;">Header Content</header>
  <main style="height: 80%; background-color: #eee;">Main Content</main>
</body>
```

---

## F. Skill-Building Check

*Test your understanding of legacy frames and modern attributes.*

1.  This attribute controls the appearance of the scrollbars that appear on the frame.
2.  These are used to divide your browser window into multiple sections.
3.  This attribute allows you to give a name to a frame.
4.  This attribute specifies the width of the border of each frame in pixels.
5.  This attribute allows you to specify the height of the space between the top and bottom of the frame's borders and its contents.
6.  This attribute works just like the `cols` attribute and takes the same values.
7.  This attribute specifies whether a three-dimensional border should be displayed between frames.
8.  Defines how to divide the window into frames.
9.  This attribute specifies the amount of space between frames in a frameset.
10. This attribute prevents a user from being able to resize a frame.

<details>
<summary><strong>Click to reveal answers</strong></summary>

1. **scrolling**
2. **Frames** (or `<frameset>`)
3. **name**
4. **border**
5. **marginheight**
6. **rows**
7. **frameborder**
8. **`<frameset>`** (or the `cols`/`rows` attributes)
9. **framespacing**
10. **noresize**

</details>