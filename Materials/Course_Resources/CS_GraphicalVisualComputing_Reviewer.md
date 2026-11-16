# 📚 CS Graphical Visual Computing — Reviewer

> Covers: HTML/CSS/JS Basics · Web Design Principles · The 12 Principles of Animation · Wireframes & Mockups

---

## 1. What is Graphic Visual Computing?

Graphic Visual Computing is the field that deals with the creation, manipulation, and representation of visual content using computers. It bridges design and programming — from structuring web content with HTML, styling it with CSS, making it interactive with JavaScript, to applying animation principles and design workflows (wireframes → mockups → prototypes).

---

## 2. HTML — The Skeleton of the Web

**HTML (HyperText Markup Language)** is the structure of a web page. Think of it as the skeleton of a building — it gives the page its bones but no styling.

### 2.1 Basic Document Structure

Every HTML file follows this structure:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <!-- Visible content goes here -->
  </body>
</html>
```

| Tag | Purpose |
|-----|---------|
| `<!DOCTYPE html>` | Declares the document as HTML5 |
| `<html>` | Root element of the page |
| `<head>` | Meta-information (title, styles, scripts) |
| `<body>` | All visible content displayed on the page |

> **Rule:** Every opening tag must have a closing tag — `<p>...</p>` — except self-closing ones like `<img>`.

### 2.2 Essential HTML Tags

| Tag | Description | Example |
|-----|-------------|---------|
| `<h1>` – `<h6>` | Headings (h1 = largest) | `<h1>Title</h1>` |
| `<p>` | Paragraph | `<p>Hello world</p>` |
| `<ul>` + `<li>` | Unordered list + list items | `<ul><li>Egg</li></ul>` |
| `<a href="...">` | Hyperlink | `<a href="https://google.com">Go</a>` |
| `<img src="...">` | Image (self-closing) | `<img src="dog.jpg">` |
| `<table>`, `<tr>`, `<td>` | Table, row, cell | Used for tabular data |
| `<div>` | Generic container/box | Used extensively for layout |
| `<form>`, `<input>` | User input form | Captures data from user |

### 2.3 Attributes

Attributes add extra functionality to tags.

```html
<a href="https://google.com">Click here</a>
<img src="photo.jpg" alt="A photo">
<input type="text" name="username" placeholder="Enter name">
```

- `href` — destination URL for links
- `src` — source path for images/scripts
- `id` — unique identifier for an element
- `class` — reusable identifier for styling
- `placeholder` — hint text inside input fields

---

## 3. CSS — The Visual Styling Layer

**CSS (Cascading Style Sheets)** controls the presentation and layout of HTML. It determines colors, fonts, spacing, and positioning.

### 3.1 Three Ways to Add CSS

| Method | How | Best For |
|--------|-----|----------|
| **Inline** | `style` attribute on the element | Quick, one-off styling |
| **Internal** | `<style>` tag inside `<head>` | Single-page styling |
| **External** | Separate `.css` file via `<link>` | Best practice — reusable across pages |

```html
<!-- External (Best Practice) -->
<link rel="stylesheet" href="style.css">
```

### 3.2 CSS Syntax

```css
selector {
  property: value;
}
```

Example:
```css
p {
  color: white;
  background-color: blue;
  font-size: 16px;
}
```

### 3.3 Common CSS Properties

| Property | Description | Example Value |
|----------|-------------|---------------|
| `color` | Text color | `white`, `#FF0000` |
| `background` / `background-color` | Element background | `blue`, `url("img.jpg")` |
| `font-size` | Text size | `30px`, `2em` |
| `font-style` | Italic or normal | `italic`, `normal` |
| `width` / `height` | Element size | `100px`, `50%`, `auto` |
| `border` | Outline around element | `2px solid red` |
| `margin` | Space **outside** the element | `10px` |
| `padding` | Space **inside** the border | `20px` |

### 3.4 Selectors: IDs vs Classes

| Selector | Syntax | Rule |
|----------|--------|------|
| **ID** (`#`) | `#box` | Unique — use once per page |
| **Class** (`.`) | `.box` | Reusable — apply to many elements |

```css
#unique-box { background-color: yellow; }  /* ID */
.shared-card { border: 1px solid gray; }   /* Class */
```

### 3.5 The CSS Box Model

Every HTML element is a rectangular box with four layers:

```
┌──────────────────────┐
│        Margin        │  ← Space outside the border
│  ┌────────────────┐  │
│  │    Border      │  │  ← The visible edge
│  │  ┌──────────┐  │  │
│  │  │ Padding  │  │  │  ← Space inside the border
│  │  │ ┌──────┐ │  │  │
│  │  │ │Content│ │  │  │  ← Text, image, etc.
│  │  │ └──────┘ │  │  │
│  │  └──────────┘  │  │
│  └────────────────┘  │
└──────────────────────┘
```

### 3.6 Layout: Float & Position

| Property | Value | Effect |
|----------|-------|--------|
| `float` | `left` / `right` | Places elements side-by-side horizontally |
| `position` | `static` | Default — normal page flow |
| `position` | `relative` | Offset from its normal position |
| `position` | `absolute` | Placed relative to nearest positioned ancestor using `top/left/right/bottom` |

---

## 4. JavaScript — Adding Interactivity

**JavaScript** makes pages dynamic and interactive. It runs in the browser and responds to user actions.

### 4.1 Adding JavaScript

```html
<!-- Internal -->
<script> console.log("Hello!"); </script>

<!-- External -->
<script src="script.js"></script>
```

### 4.2 Core Concepts

#### Variables
```javascript
var number = 10;       // Number
var name = "Hello";    // String
var isRad = true;      // Boolean
```

#### DOM Manipulation
```javascript
document.getElementById("box").innerHTML = "Hello there!";
```

#### Conditionals
```javascript
if (number === 10) {
  console.log("Yeah buddy!");
} else {
  console.log("Nope.");
}
```

#### Loops
```javascript
for (var i = 0; i < 10; i++) {
  console.log(i);  // Prints 0–9
}
```

#### Arrays
```javascript
var groceries = ["milk", "eggs", "cheese"];
for (var i = 0; i < groceries.length; i++) {
  console.log(groceries[i]);
}
```

#### Functions
```javascript
function listGroceries() {
  // reusable block of code
}
listGroceries(); // call the function
```

#### Event Listeners
```javascript
document.getElementById("box").addEventListener("click", function() {
  alert("I got clicked!");
});
```

---

## 5. Wireframes & Mockups

Wireframes and mockups are critical steps in the **design workflow** of any visual computing or web project. They come before any code is written.

### 5.1 The Design Workflow

```
Idea → Wireframe → Mockup → Prototype → Final Product
```

### 5.2 Wireframe

A **wireframe** is a low-fidelity, skeletal blueprint of a webpage or application. It focuses purely on **layout and structure** — no colors, no real fonts, no images.

**Key characteristics:**
- Black-and-white or grayscale
- Uses placeholder boxes (e.g., "IMAGE HERE"), dummy text, and basic shapes
- Represents content hierarchy and navigation flow
- Created with tools like Figma, Balsamiq, pen & paper, or even HTML `<div>` boxes

**Purpose:**
- Plan where elements go (header, nav, content, footer)
- Get feedback on layout early — before investing time in visuals
- Acts as a communication tool between designer and developer

**Example elements in a wireframe:**
- `[LOGO]` box in top-left
- Navigation bar as a horizontal strip
- Hero banner as a large rectangle with "HEADLINE TEXT"
- Content cards as equal-width boxes in a grid

### 5.3 Mockup

A **mockup** is a high-fidelity, static representation of the final design. It looks like the real product but is **not interactive**.

**Key characteristics:**
- Full colors, typography, icons, and images
- Pixel-accurate layout matching the intended final design
- Created with tools like Figma, Adobe XD, Sketch, or Photoshop
- Still static — clicking buttons does nothing

**Purpose:**
- Show stakeholders exactly how the product will look
- Finalize the visual identity (color palette, spacing, brand)
- Used as a reference when writing actual HTML/CSS

### 5.4 Wireframe vs Mockup vs Prototype

| | Wireframe | Mockup | Prototype |
|--|-----------|--------|-----------|
| **Fidelity** | Low | High | High |
| **Colors/fonts** | No | Yes | Yes |
| **Interactive** | No | No | Yes |
| **Purpose** | Layout planning | Visual design | User testing |
| **Stage** | Early | Middle | Late |
| **Tool examples** | Balsamiq, paper | Figma, Adobe XD | Figma, HTML/CSS/JS |

### 5.5 Why This Matters in Graphic Visual Computing

In GVC, the wireframe-to-mockup pipeline teaches you to:

- **Separate concerns** — structure (HTML) vs. style (CSS) mirrors the wireframe vs. mockup distinction
- **Think visually before coding** — fewer rewrites, cleaner output
- **Apply visual hierarchy** — headings (`<h1>`–`<h6>`), spacing (margin/padding), and layout (float/position) all come from design decisions made at the wireframe stage

---

## 6. The 12 Principles of Animation

Originally formulated by Disney animators Frank Thomas and Ollie Johnston, these principles apply to all motion — including web transitions, UI micro-interactions, CSS keyframes, and game engines.

### 6.1 All 12 Principles at a Glance

| # | Principle | Core Idea |
|---|-----------|-----------|
| 1 | **Squash & Stretch** | Gives objects the illusion of weight and flexibility |
| 2 | **Anticipation** | A smaller, opposite movement before the main action |
| 3 | **Staging** | Present one clear idea at a time |
| 4 | **Straight Ahead & Pose to Pose** | Two animation workflows — spontaneous vs. planned |
| 5 | **Follow Through & Overlapping Action** | Different body parts stop at different times |
| 6 | **Slow In & Slow Out** | Objects accelerate and decelerate naturally |
| 7 | **Arcs** | Almost all living motion follows a curved path |
| 8 | **Secondary Action** | Supporting motion that adds richness without competing |
| 9 | **Timing** | Number of frames = speed = emotional meaning |
| 10 | **Exaggeration** | Push past realism to read clearly on screen |
| 11 | **Solid Drawing** | Characters must feel like they exist in 3D space |
| 12 | **Appeal** | Characters should be pleasant and interesting to watch |

### 6.2 Deep Dive: Key Principles

#### 1. Squash & Stretch
The most important principle. An object **squashes** flat on impact and **stretches** long mid-air.
- **Rule:** Volume stays constant. If it stretches taller, it must get thinner.
- In CSS: achieved via `scaleX()` / `scaleY()` transforms

#### 2. Anticipation
A wind-up before the main action. Prepares the viewer's eyes.
- Character crouches **before** jumping
- Fist pulls back **before** swinging
- Without it: action feels robotic or sudden

#### 3. Staging
Present one clear focal point. Silhouette should read instantly, even in shadow.
- Too much happening at once kills staging.
- In web UI: one primary call-to-action per screen

#### 5. Follow Through & Overlapping Action
- **Follow Through:** Loose parts (hair, coat) keep moving briefly after the body stops.
- **Overlapping Action:** Different body parts move on slightly offset timing.

#### 6. Slow In & Slow Out
Real objects don't snap to full speed instantly — they ease in and ease out.
- More frames near the **start and end** of movement, fewer in the middle
- This is exactly what CSS easing curves (`ease-in`, `ease-out`, `ease-in-out`) do

#### 9. Timing
Speed = emotional meaning:
- **Fast** → light, urgent, comedic (slap, jump scare)
- **Slow** → heavy, deliberate, powerful (slow nod, heavy door)

#### 10. Exaggeration
Push a pose or action further than real life. It's not about being unrealistic — it's about **amplifying the essence** so it reads clearly (wide-eyed shock, deep crouch before a jump).

### 6.3 The Mental Model Chain

```
GIVES IT WEIGHT       → Squash & Stretch
PREPARES THE EYE      → Anticipation + Staging
FEELS PHYSICAL        → Arcs + Slow In/Out + Follow Through
ADDS RICHNESS         → Secondary Action + Timing + Exaggeration
SELLS THE ILLUSION    → Solid Drawing + Appeal + Straight Ahead/Pose to Pose
```

### 6.4 Animation Principles in Web/UI Context

| Principle | Web/UI Application |
|-----------|-------------------|
| Slow In & Slow Out | CSS `ease-in-out` transitions |
| Anticipation | Button "press down" before triggering action |
| Follow Through | Dropdown slides slightly past then snaps back |
| Staging | One modal/alert at a time, clear focal point |
| Secondary Action | Icon wiggle alongside a primary button press |
| Squash & Stretch | Bouncy loading indicators, elastic UI elements |

---

## 7. Quick-Reference: HTML Tags Cheat Sheet

```html
<!-- Structure -->
<!DOCTYPE html>  <html>  <head>  <body>

<!-- Content -->
<h1>–<h6>   Headings
<p>          Paragraph
<a href="">  Link
<img src="">  Image (self-closing)
<ul><li>     Unordered list + items

<!-- Layout -->
<div>        Generic container
<table><tr><td>  Table structure

<!-- Forms -->
<form>  <input type="text">  <button>
```

---

## 8. Quick-Reference: CSS Cheat Sheet

```css
/* Selectors */
p       { }   /* element */
#id     { }   /* ID — unique */
.class  { }   /* class — reusable */

/* Box Model */
margin: 10px;   /* outside */
padding: 10px;  /* inside */
border: 2px solid red;

/* Layout */
float: left;
position: absolute;
top: 0; left: 0;

/* Typography */
font-size: 16px;
font-style: italic;
color: white;
```

---

## 9. Quick-Reference: JavaScript Cheat Sheet

```javascript
// Variables
var x = 10;
var name = "hello";

// DOM
document.getElementById("id").innerHTML = "text";

// Conditionals
if (x === 10) { } else { }

// Loops
for (var i = 0; i < arr.length; i++) { }

// Functions
function myFunc() { }
myFunc();

// Events
element.addEventListener("click", function() { });
```

---

## 10. Sample Quiz Questions

### Multiple Choice

**Q1.** Which HTML tag creates the largest heading?
- A) `<h6>`  B) `<h1>` ✅  C) `<head>`  D) `<title>`

**Q2.** Which CSS selector targets an element with `id="box"`?
- A) `.box`  B) `box`  C) `#box` ✅  D) `*box`

**Q3.** Which animation principle describes easing (slow start and end)?
- A) Anticipation  B) Arcs  C) Slow In & Slow Out ✅  D) Squash & Stretch

**Q4.** A wireframe is best described as:
- A) A fully interactive prototype  B) A high-fidelity color design  C) A low-fidelity layout blueprint ✅  D) The final HTML/CSS code

**Q5.** What does the CSS `margin` property control?
- A) Space inside the border  B) Space outside the border ✅  C) Text color  D) Border thickness

### Identification

**Q6.** This animation principle involves parts of the body (like hair or a coat) continuing to move after the main body has stopped. → **Follow Through**

**Q7.** The design artifact that looks exactly like the final product but has no interactive functionality. → **Mockup**

**Q8.** The CSS property that stacks elements horizontally. → **float**

**Q9.** The Disney principle that says volume must stay constant when a character deforms. → **Squash & Stretch**

**Q10.** The three ways to include CSS in an HTML document. → **Inline, Internal, External**

---

## 11. The 13 Principles of Good Design

> *"Thirteen principles that explain why some pages feel effortless to use — and why others feel off, even when you can't say exactly why."*

These are the visual and UX design principles that guide how any interface — webpage, app, poster — should be structured and styled.

### 11.1 All 13 Principles at a Glance

| # | Principle | Core Idea |
|---|-----------|-----------|
| 1 | **Visual Hierarchy** | Guide the eye to what matters most, in order |
| 2 | **Balance** | Distribute visual weight so the layout doesn't feel lopsided |
| 3 | **Contrast** | Differences in color, size, or weight that create emphasis |
| 4 | **Alignment** | Every element lines up with something else — nothing sits randomly |
| 5 | **Proximity** | Related items sit close; unrelated items get space between them |
| 6 | **Repetition** | Reuse colors, fonts, and button styles consistently throughout |
| 7 | **White Space** | Generous empty space improves readability and feels premium |
| 8 | **Typography** | Type carries tone before anyone reads a single word |
| 9 | **Color** | Pick a primary, an accent, and neutrals — keep them in proportion |
| 10 | **Grid Systems** | Invisible column-based skeleton for consistent spacing and alignment |
| 11 | **Responsive Design** | A design must adapt gracefully across phone, tablet, and desktop |
| 12 | **Usability / UX** | People shouldn't have to "learn" your site — it should just make sense |
| 13 | **Accessibility** | If it only works for some users, it isn't finished |

### 11.2 Deep Dive: Key Principles

#### 1. Visual Hierarchy
- **Bigger = more important.** Headlines dwarf body text on purpose.
- **Bold/bright = grabs attention first**, before anything else.
- In left-to-right cultures, the **top-left** is usually seen first.
- Elements set apart from the rest feel more significant.

#### 2. Balance
Two types:
- **Symmetrical** — mirrored layout, same weight on each side. Feels formal and trustworthy.
- **Asymmetrical** — different elements with similar visual "weight" that balance each other. Feels modern and dynamic.

#### 3 & 4. Contrast & Alignment
- **Contrast** — the difference between elements (color, size, shape, weight) that creates emphasis. It's why a button doesn't get lost in a wall of text.
- **Alignment** — every element should line up with something else. Good alignment creates invisible lines that make a page feel clean and organized.

#### 5 & 6. Proximity & Repetition
- **Proximity** — related items sit close together; unrelated items get space. Tells users what belongs together without labels or borders.
- **Repetition** — reuse colors, fonts, button styles, and spacing. Once someone learns how one button works, every button should work the same way.

#### 7. White Space
Beginners fear empty space and rush to fill it — don't. Generous white space:
- Improves readability and focus
- Is the fastest way to make a design feel **premium**

#### 8. Typography Rules
- No more than **2–3 fonts** per site
- A clear **type scale**: H1 > H2 > H3 > body
- **Line-height & letter-spacing** affect readability
- **Serif** = traditional/editorial; **Sans-serif** = modern/clean

#### 9. Color — The 60-30-10 Rule
| Proportion | Role | Example |
|------------|------|---------|
| **60%** | Dominant/neutral | Background, large areas |
| **30%** | Secondary | Sidebar, cards |
| **10%** | Accent | Buttons, highlights, CTAs |

> Accessible contrast: text must stand clearly apart from its background — for **everyone**, not just some.

#### 10. Grid Systems
Sites are built on invisible grid systems — commonly **12 columns** — to keep spacing and alignment consistent everywhere.
- Every element snaps to a column
- Nothing feels randomly placed, even across very different pages
- Think of it as **graph paper** beneath the design

#### 11. Responsive Design
A design must adapt gracefully across phone, tablet, and desktop. This is **non-negotiable today**, not a nice-to-have.

#### 12. Usability / UX Basics
| Rule | What it means |
|------|---------------|
| **Clear navigation** | Users always know where they are and how to get back |
| **Obvious CTAs** | Buttons look clickable; same action always looks the same |
| **Fast load times** | Every second of delay costs attention — and trust |
| **Predictable** | Interactions behave the way people already expect them to |

#### 13. Accessibility
Not an extra feature — a baseline.
- **Color contrast** — text needs to stand out from its background
- **Readable size** — font sizes that don't force anyone to squint
- **Alt text** — every image gets a text description for screen readers
- **Keyboard access** — every element reachable without a mouse

### 11.3 The Mental Model Chain

```
TELLS THE EYE WHERE TO LOOK    → Visual Hierarchy
MAKES IT FEEL STABLE           → Balance + Alignment
MAKES IT EASY TO SCAN          → Contrast + Repetition
MAKES IT EASY TO UNDERSTAND    → White Space + Proximity
THE TOOLS YOU EXECUTE WITH     → Typography · Color · Grids
MAKES IT WORK FOR EVERYONE     → Usability + Accessibility + Responsive Design
```

### 11.4 Design Principles vs. Animation Principles — Quick Comparison

| | Design Principles | Animation Principles |
|--|-------------------|---------------------|
| **Focus** | Static layouts & visual feel | Motion & movement |
| **Goal** | Guide the eye, create clarity | Make motion feel alive and believable |
| **Key shared idea** | Hierarchy & staging | Staging & timing |
| **Tool** | CSS, grid, typography | CSS keyframes, transitions |

---

## 12. Updated Sample Quiz Questions

*(Added from Design Principles)*

**Q11.** Which design principle explains why a button stands out from surrounding text?
- A) Proximity  B) Repetition  C) Contrast ✅  D) White Space

**Q12.** The 60-30-10 rule applies to which design principle?
- A) Typography  B) Grid Systems  C) Color ✅  D) Alignment

**Q13.** What does "proximity" tell the viewer about grouped elements?
- A) They are different  B) They belong together ✅  C) They are decorative  D) They should be read last

**Q14.** Which principle states that every element should line up with something else on the page?
→ **Alignment**

**Q15.** Name the two types of balance used in visual design.
→ **Symmetrical and Asymmetrical**

---

*Reviewer compiled from: Module 02 – 12 Principles of Animation, Web Design Crash Course (HTML/CSS/JS), Design Fundamentals Field Guide – 13 Principles of Good Design, and supplementary notes on Wireframes & Mockups.*
