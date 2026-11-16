# Basic HTML 2: Marquee and Multimedia

---

## A. Lesson Preview & Review

Welcome to Module 8! In the previous module, we learned how to structure text using basic HTML tags. Now, we are going to add some movement and media to our web pages.

**Learning Objectives:**
By the end of this module, you should be able to:
1. Identify HTML marquee tags and media tags.
2. Understand how to use HTML marquee and media insertion tags.
3. Create a sample web design using marquee and media tags.

> **Pro Tip (Modern Context):** The tags we are about to learn—specifically `<marquee>` and `<embed>`—are considered **legacy or deprecated** features in modern web development. However, learning them helps you understand the history of the web and how to read older code. I have included modern best practices alongside the historical ones so you know how these effects are achieved today!

---

## B. Main Lesson

### 1. The `<marquee>` Tag
The HTML `<marquee>` tag was historically used to define a scrolling text area in an HTML document that moves across the page in a horizontal or vertical direction. By default, text will scroll from right to left. 

> ⚠️ **Important Modern Warning:** The `<marquee>` tag has been **deprecated in HTML5**. This means it is obsolete and should no longer be used in modern web design. It is widely considered bad practice due to accessibility issues (it can be hard for users with cognitive disabilities to read) and because it gives the user no control over the movement. Today, similar scrolling effects are created using **CSS Animations**.

**Historical Syntax:**
```html
<body>
  <marquee direction="down" height="100" width="200" bgcolor="white">Scrolling text</marquee>
</body>
```

#### `<marquee>` Tag Attributes
Even though it's deprecated, you might see these in older code. Here are the key attributes:

| Attribute | Description |
| :--- | :--- |
| `width` | Specifies the width of the marquee (e.g., 10 or 20%). |
| `height` | Specifies the height of the marquee (e.g., 10 or 20%). |
| `direction` | Specifies the direction to scroll: `up`, `down`, `left`, or `right`. |
| `behavior` | Specifies the type of scrolling: `scroll` (default), `slide`, or `alternate`. |
| `scrolldelay` | How long to delay between each jump (in milliseconds). |
| `scrollamount` | The speed of the marquee text. |
| `loop` | How many times to loop. Default is `INFINITE` (endless loop). |
| `bgcolor` | Background color (using a color name or hex value). |
| `hspace` | Horizontal space around the marquee. |
| `vspace` | Vertical space around the marquee. |

---

### 2. Embedding Multimedia (`<embed>`)
Sometimes you need to add music or video to your web page. Historically, the easiest way to do this was using the `<embed>` tag. This tag causes the browser to include controls for the multimedia automatically (if the browser supports the media type).

It was often paired with the `<noembed>` tag, which provided fallback content for older browsers that didn't recognize the `<embed>` tag (like displaying an image instead).

> ⚠️ **Important Modern Warning:** The `<embed>` tag is still technically supported, but it is largely obsolete for audio and video. Most modern browsers no longer support the old plugins it relied on (like Flash). Today, HTML5 provides the much better `<video>` and `<audio>` tags.

**Historical Syntax:**
```html
<body>
  <embed src="your-file.mid" width="100%" height="60">
    <noembed><img src="yourimage.gif" alt="Alternative Media"></noembed>
  </embed>
</body>
```

#### `<embed>` Tag Attributes

| Attribute | Description |
| :--- | :--- |
| `align` | Determines how to align the object (`center`, `left`, or `right`). |
| `autostart` | Boolean attribute indicating if media should start automatically (true/false). |
| `loop` | Specifies if the sound should play continuously (true/false or a number). |
| `playcount` | The number of times to play the sound (alternative to loop). |
| `hidden` | Specifies if the multimedia object should be hidden from the page. |
| `width` / `height` | Dimensions of the object in pixels. |
| `name` | A name used to reference the object. |
| `src` | The URL or file path of the object to be embedded. |
| `volume` | Controls the volume of the sound (from 0 to 100). |

#### Supported Video Types (Historically)
The module originally listed older file types: `.swf` (Flash), `.avi`, `.mov` (QuickTime), and `.mpeg`. 
*   *Modern Note:* Flash (`.swf`) is completely dead and unsupported by all modern browsers. Today, the web standard for video is **`.mp4`** (H.264) and **`.webm`**.

### 💡 How We Do It Today (Modern HTML5)
Instead of `<embed>`, modern developers use the `<video>` and `<audio>` tags, which don't require third-party plugins.

**Modern Video Example:**
```html
<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
  Your browser does not support the video tag.
</video>
```

> **File Path Tip:** When embedding multimedia, ensure the file path in your `src` attribute exactly matches where the file is saved relative to your HTML file. If they are in the same folder, you just need the file name (e.g., `src="myvideo.mp4"`).

---

## C. Analogies and Use Cases

### The Marquee Analogy
Think of the `<marquee>` tag like the scrolling text ticker at the bottom of a news broadcast (like a stock market ticker). It’s great for grabbing attention, but it’s a terrible way to read a long paragraph because you have to chase the text with your eyes. This is exactly why modern UX designers avoid it!

### The `<embed>` vs `<video>` Analogy
Using `<embed>` is like needing a special adapter to plug an old VCR into a modern smart TV. It might work, but it's clunky and relies on outdated technology. Using `<video>` is like streaming directly through a smart TV—it's built-in, standard, and works perfectly.

### Use Case: Why Accessibility Matters
Imagine a user with a visual impairment using a screen reader. A `<marquee>` tag constantly moves, making it very difficult for screen readers to parse the text. Modern CSS animations allow designers to pause or stop movement, ensuring equal access to information for everyone.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   The `<marquee>` tag creates scrolling text, but it is **deprecated** and replaced by CSS.
*   The `<embed>` tag was used to add multimedia but has largely been replaced by HTML5 `<video>` and `<audio>` tags.
*   Always use the `<noembed>` (or fallback text inside a `<video>` tag) to provide alternatives if the media fails to load.
*   The `src` attribute is crucial for telling the browser where to find your media files.

### Frequently Asked Questions

**Q: Can I still use `<marquee>` for a fun retro effect on my website?**
**A:** You can, because most browsers still keep it around for backwards compatibility. However, it is generally frowned upon in professional development. If you want a scrolling effect today, you should use CSS `@keyframes` animations.

**Q: My embedded video isn't playing. What went wrong?**
**A:** This is almost always a file path issue. Check your `src` attribute. If your HTML file is on your desktop and your video is in a folder called "media", your code should look like `src="media/video.mp4"`.

---

## E. Guided Drills / Code Projects

### Exercise 1: Create Your Own Sample HTML
**Instructions:** Create an HTML file that practices the concepts from this module. 
1. Add a `<marquee>` tag with some text (e.g., "Welcome to my retro website!"). Set it to scroll from right to left.
2. Change the `bgcolor` of the marquee.
3. Add an `<embed>` tag (you can use a public URL or a local file).
4. Below that, implement a **Modern HTML5 Video** using the `<video>` tag with the `controls` attribute.

*Bonus:* Try adding the `loop="infinite"` attribute to the marquee to see it scroll forever.

---

## F. Skill-Building Check

*Test your understanding of the tags and attributes covered in this module.*

1.  This specifies the direction in which the marquee should scroll.
2.  It is used to reference the object.
3.  It defines a scrolling text area in the HTML document that moves across the page.
4.  It refers to Apple's QuickTime Movie format.
5.  It references the URL of the object to be embedded.
6.  It specifies the number of times to play the sound.
7.  This specifies the number of times to loop your marquee.
8.  This specifies the type of scrolling of the marquee (e.g., scroll, slide, alternate).
9.  This specifies background color in terms of color name or color hex value.
10. It controls the volume of the sound.

<details>
<summary><strong>Click to reveal answers</strong></summary>

1. **direction**
2. **name** (Attribute in `<embed>`)
3. **`<marquee>`** (or marquee tag)
4. **`.mov`** files
5. **src**
6. **playcount**
7. **loop**
8. **behavior**
9. **bgcolor**
10. **volume**

</details>