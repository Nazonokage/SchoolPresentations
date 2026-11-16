# 📚 DOM & Modern Web APIs — Complete Reviewer

## Module 10–15: HCI2 — Human-Computer Interaction 2

---

## 🎯 PART 1: THE DOM (Document Object Model)

### What is the DOM?

> **Definition:** When a web page loads, the browser creates a **Document Object Model (DOM)** — a standard object model and programming interface for HTML. It represents the page as a **tree of objects**, where each node is an element, attribute, or piece of text.

| Concept | Description |
|---------|-------------|
| **HTML** | Static markup text — the blueprint |
| **DOM** | Browser's **live, in-memory** object representation — the built structure |
| **HTML DOM** | Defines HTML elements as objects with **properties, methods, and events** |

### W3C DOM Standard — 3 Parts

1. **Core DOM** — Standard model for all document types
2. **XML DOM** — Standard model for XML documents
3. **HTML DOM** — Defines HTML elements as objects with properties, methods, and events

---

## 🔍 PART 2: SELECTION METHODS

### Older Methods (Return HTMLCollections — LIVE)

| Method | Returns | Nature |
|--------|---------|--------|
| `document.getElementById(id)` | Single element | ✗ Not a collection |
| `document.getElementsByClassName(name)` | HTMLCollection | 🔴 **LIVE** |
| `document.getElementsByTagName(name)` | HTMLCollection | 🔴 **LIVE** |
| `element.children` | HTMLCollection | 🔴 **LIVE** |

### Modern Methods (Return NodeLists)

| Method | Returns | Nature |
|--------|---------|--------|
| `document.querySelector(selector)` | First matching Element | ✗ Not a collection |
| `document.querySelectorAll(selector)` | **Static NodeList** | 📸 **STATIC** |

**CRITICAL:** `querySelector` returns `null` if no match — always **null-check**!

```javascript
// COMPOUND SELECTORS — powerful CSS-style selection
const featuredCards = document.querySelectorAll(".card.featured");  // both classes
const allCards = document.querySelectorAll(".card, .featured");     // either class (OR)
const directChildren = document.querySelectorAll(".card > p");      // direct child
const requiredInputs = document.querySelectorAll("input[required]");// attribute selector
```

---

## 📋 PART 3: HTMLCollection vs NodeList

### Comparison Table

| Feature | HTMLCollection | NodeList |
|---------|---------------|----------|
| **Returned by** | `getByTagName`, `getByClass`, `children` | `querySelectorAll`, `childNodes` |
| **Node types** | HTML **elements only** | Any node type (elements, text, comments) |
| **Access** | By index `[0]` OR named item `["id"]` | By index `[0]` only |
| **forEach()** | ❌ **Not built-in** | ✅ **Native** |
| **Nature** | 🔴 **Always LIVE** | 📸 Usually **STATIC** |

### Live vs Static — Why It Matters

| Live Collection (HTMLCollection) | Static Collection (querySelectorAll) |
|-----------------------------------|--------------------------------------|
| Like a **live security camera feed** | Like a **photograph/snapshot** |
| Auto-updates when DOM changes | Never updates after query |
| Indexes shift mid-loop — **dangerous** | Safe to iterate |
| Prefer `querySelectorAll` in modern code | Use with `forEach()` directly |

### Iteration Strategies

```javascript
// ── 1. NodeList → native .forEach() ──
document.querySelectorAll(".item").forEach((item, index) => {
  item.style.color = "blue";
});

// ── 2. HTMLCollection → classic for loop ──
const boxes = document.getElementsByClassName("box");
for (let i = 0; i < boxes.length; i++) {
  boxes[i].style.backgroundColor = "gray";
}

// ── 3. Array.from() → unlocks filter/map/reduce ──
const arr = Array.from(document.getElementsByTagName("p"));
arr.filter(p => p.textContent.length > 50)
   .forEach(p => p.style.fontWeight = "bold");

// ── 4. Spread syntax (alternative) ──
const arr2 = [...document.querySelectorAll(".item")];
```

---

## 🧬 PART 4: DOM RELATIONSHIPS & TRAVERSAL

### Relationship Terminology

| Term | Definition |
|------|------------|
| **Parent Node** | The node **immediately above** a given node |
| **Child Node** | Any node **directly underneath** a parent |
| **Sibling Nodes** | Nodes sharing the **same direct parent** |
| **Ancestors** | All nodes above (parents, grandparents, etc.) |
| **Descendants** | All nodes below (children, grandchildren, etc.) |

### Navigation Properties

| Property | Description | Returns |
|----------|-------------|---------|
| `parentNode` / `parentElement` | Direct parent | Node / Element |
| `children` ✅ | HTML element children only (excludes #text) | HTMLCollection |
| `childNodes` | All children including text & whitespace | NodeList |
| `firstElementChild` ✅ | First HTML element child | Element |
| `lastElementChild` ✅ | Last HTML element child | Element |
| `nextElementSibling` ✅ | Next sibling HTML element | Element / `null` |
| `previousElementSibling` ✅ | Previous sibling HTML element | Element / `null` |

⚠️ **#text node trap:** `childNodes`, `firstChild`, and `lastChild` include whitespace from HTML indentation. Always use **Element variants** (`children`, `firstElementChild`, etc.)!

---

## ✏️ PART 5: MANIPULATION — ADDING, CHANGING, REMOVING

### 3-Step createElement Workflow

```
1. CREATE  → document.createElement("div")
2. CONFIGURE → set innerHTML, className, style, attributes
3. ATTACH  → parent.appendChild(newEl)
```

> Until Step 3, the element exists **only in memory** — invisible on the page.

### Manipulation Methods

| Method | What It Does |
|--------|--------------|
| `element.innerHTML = val` | Replaces inner HTML content |
| `element.style.property = val` | Changes CSS style (camelCase) |
| `element.setAttribute(attr, val)` | Sets an attribute explicitly |
| `parent.appendChild(node)` | Adds node as **last child** |
| `parent.insertBefore(new, ref)` | Inserts **before** reference sibling |
| `parent.removeChild(child)` | Removes a child node |
| `element.remove()` | Modern self-removal shorthand |
| `parent.replaceChild(new, old)` | Replaces existing child |
| `node.cloneNode(true)` | Deep clone (includes all children) |

```javascript
// Changing content
const el = document.getElementById("welcome-msg");
el.innerHTML = "Hello, World!";
el.style.color = "white";
el.style.backgroundColor = "darkred";

// Adding elements
const newPara = document.createElement("p");
newPara.innerHTML = "Added by JavaScript!";
document.getElementById("container").appendChild(newPara);

// Removing elements (modern)
const oldEl = document.getElementById("old-notice");
oldEl.remove();  // simpler than parentNode.removeChild()
```

---

## 🎯 PART 6: EVENT LISTENERS

### What Is an Event Listener?

> A **procedure in JavaScript that waits for a specific event to occur** — such as a user clicking the mouse or pressing a key.

### Syntax

```javascript
element.addEventListener(event, function, useCapture);
```

| Parameter | Description | Required? |
|-----------|-------------|-----------|
| **event** | Type of event (e.g., `"click"`, `"keydown"`) | ✅ Required |
| **function** | Callback function that runs when event occurs | ✅ Required |
| **useCapture** | Boolean: `false` (bubbling, default) or `true` (capturing) | Optional |

### Common Event Types

| Event | Description |
|-------|-------------|
| `"click"` | Mouse click |
| `"dblclick"` | Double click |
| `"mousedown"` / `"mouseup"` | Mouse pressed / released |
| `"keydown"` / `"keyup"` | Key pressed / released |
| `"submit"` | Form submitted |
| `"input"` | Input value changed |
| `"mouseover"` | Mouse enters element |
| `"load"` | Page/resource loaded |

### Key Benefits of addEventListener()

- ✅ Attaches handlers **without overwriting** existing handlers
- ✅ Add **multiple handlers** of the same type to one element
- ✅ Works on **any DOM object** (window, document, element)
- ✅ Keeps JavaScript **separated from HTML markup**
- ✅ Easier to **control event bubbling**
- ✅ Can be removed with `removeEventListener()`

### Named vs Anonymous Functions

```javascript
// ── Named function (can be removed) ──
document.getElementById("Btn").addEventListener("click", displayDate);
function displayDate() { alert("Clicked!"); }
// Later: removeEventListener("click", displayDate);

// ── Anonymous function (cannot be removed) ──
document.getElementById("Btn").addEventListener("click", function() {
  alert("Clicked!");
});
```

### Event Bubbling vs Capturing

```
         ┌─────────────┐
         │   Window    │  ← Capturing phase (top → down)
         │  Document   │
         │    html     │
         │    body     │  ← Bubbling phase (bottom → up)
         │  Target     │
         └─────────────┘
```

- **Bubbling (default, `false`):** Event travels **up** from target → ancestors
- **Capturing (`true`):** Event travels **down** from root → target

### Event Delegation Pattern

```javascript
// ONE listener on the parent handles ALL child events — even dynamically added ones
container.addEventListener("click", function(event) {
  if (event.target.classList.contains("delete-btn")) {
    event.target.parentElement.remove();
  }
});
```

---

## 🧩 PART 7: WIDGETS

### What Is a Widget?

> A **lightweight software application** designed to perform a **single, specific task** — operating independently and making it reusable across different platforms.

### Three Key Characteristics

| Trait | Description |
|-------|-------------|
| ⚡ **Lightweight** | Minimal byte size, executes quickly |
| 🎯 **Single-Purpose** | One focused utility task |
| 🔌 **Loose Coupling** | Operates independently, highly reusable |

### Types of Widgets

| Type | Examples |
|------|----------|
| **Desktop** | macOS Dashboard, Windows Sidebar gadgets |
| **Web** | Live chat modules, countdown timers, weather embeds |
| **Mobile** | Home screen interactive components |

---

## 📷 PART 8: WEB SENSORS (Generic Sensor API)

### Why Permission Policies?

Sensor data can reveal sensitive information about:
- User **movement** and location patterns
- **Environment** conditions (light, magnetic fields)
- Device **orientation** and physical gestures

### Sensor API Reference

| Sensor API | Permission Policy | Use Case |
|------------|-------------------|----------|
| **AbsoluteOrientationSensor** | accelerometer, gyroscope, magnetometer | AR, navigation compasses |
| **Accelerometer** | accelerometer | Shake gestures, motion detection |
| **AmbientLightSensor** | ambient-light-sensor | Auto dark/light UI theming |
| **GravitySensor** | accelerometer | Device tilt relative to Earth |
| **Gyroscope** | gyroscope | Angular velocity, gaming controls |
| **LinearAccelerationSensor** | accelerometer | Linear motion (no gravity) |
| **Magnetometer** | magnetometer | Magnetic field strength |
| **RelativeOrientationSensor** | accelerometer, gyroscope | VR headsets, 3D rotation |

---

## 📦 PART 9: QRIOUS — QR CODE GENERATOR

### Import QRious via CDN

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/qrious/4.0.2/qrious.min.js"></script>
```

### QRious() Options

| Option | Type | Description |
|--------|------|-------------|
| `value` | String | The text or URL to encode |
| `size` | Number | Width/height in pixels (e.g., 400) |
| `level` | String | Error correction: `'L'` (7%), `'M'` (15%), `'Q'` (25%), `'H'` (30%) |

### Complete QR Code Generator

```javascript
function generateQRCode() {
  // Step 1: Get user input
  const value = document.getElementById('qr-code-value').value;
  
  // Step 2: Configure options
  const options = {
    value: value,
    size: 400,
    level: 'H'  // High error correction = 30% resilience
  };
  
  // Step 3: Create QRious instance
  const qrCode = new QRious(options);
  
  // Step 4: Convert to Data URL (Base64 image)
  const qrCodeImage = qrCode.toDataURL();
  
  // Step 5: Inject into <img> src
  document.getElementById('qr-code-image').src = qrCodeImage;
}
```

### What is a Data URL?

A Data URL embeds image data directly as a **Base64-encoded string** inside the `src` attribute:

```
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...
```

**Benefits:** No file saved to disk — browser renders it as a full image immediately.

---

## ⚡ PART 10: MODERN WEB APIS

### Synchronous vs Asynchronous

| Feature | Synchronous | Asynchronous |
|---------|-------------|--------------|
| **Execution** | Line-by-line, sequential | Non-blocking, runs in background |
| **UI Responsiveness** | Freezes during long tasks | Remains responsive |
| **Use Cases** | Math logic, local data | Network requests, hardware access |

> ⚠️ JavaScript is **single-threaded** — synchronous operations that block for 3+ seconds completely lock the browser.

---

## 🌐 PART 11: FETCH API & AJAX

### The fetch() Promise Chain

```javascript
fetch('https://api.example.com/data')
  .then(function(response) {
    // ⚠️ fetch() only rejects on NETWORK failures — NOT on 404/500
    if (!response.ok) {
      throw new Error('HTTP Error: ' + response.status);
    }
    return response.json();  // Returns another Promise
  })
  .then(function(data) {
    console.log('Data:', data);  // Parsed JS object
  })
  .catch(function(error) {
    console.error('Error:', error);  // Network failure OR thrown error
  });
```

### Promise Lifecycle

```
      ┌─────────────────────────────────────────┐
      │                                         │
      ▼                                         │
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   PENDING   │───▶│  FULFILLED  │    │  REJECTED   │
│  (waiting)  │    │  (success)  │    │  (failure)  │
└─────────────┘    └─────────────┘    └─────────────┘
      │                   │                   │
      │              .then()              .catch()
```

### Common Promise Mistakes

| Mistake | Why It Breaks |
|---------|---------------|
| Missing `.catch()` | Unhandled rejections fail silently |
| Not returning `response.json()` | Breaks the Promise chain |
| Treating first `.then()` as the data | It's the **Response** object, not the data |
| Assuming 404/500 rejects | They DON'T — check `response.ok` |

---

## 📷 PART 12: DEVICE APIS — getUserMedia()

### How getUserMedia() Works

```javascript
navigator.mediaDevices.getUserMedia({ video: true, audio: false })
  .then(function(stream) {
    const videoElement = document.querySelector('video');
    videoElement.srcObject = stream;  // Attach live stream
  })
  .catch(function(error) {
    console.error('Camera access denied:', error);
  });
```

### Key Points

| Requirement | Description |
|-------------|-------------|
| **Constraints** | `{ video: true, audio: false }` |
| **Returns** | `Promise<MediaStream>` |
| **Permission** | Browser shows a pop-up — user must approve |
| **Security** | Requires **HTTPS** or **localhost** (fails on plain HTTP) |

### Server vs Device APIs

| Feature | Server APIs (fetch()) | Device APIs (getUserMedia()) |
|---------|-----------------------|------------------------------|
| **Data Source** | Remote web server | Local hardware (camera, mic) |
| **Permissions** | CORS | Browser pop-up approval |
| **Security** | HTTP or HTTPS | HTTPS or localhost only |
| **Data Format** | JSON, XML, text | MediaStream binary stream |
| **Returns** | `Promise<Response>` | `Promise<MediaStream>` |

---

## 💾 PART 13: CLIENT-SIDE STORAGE

### Storage Comparison

| Feature | localStorage | sessionStorage | Cookies |
|---------|--------------|----------------|---------|
| **Capacity** | ~5–10 MB | ~5 MB | ~4 KB |
| **Expires** | Permanent (until cleared) | Tab/session close | Configurable date |
| **Sent to server** | Never | Never | Automatically with every request |
| **Scope** | All tabs, same origin | Current tab only | Configurable domain/path |
| **Best for** | User prefs, themes, drafts | Temp form data, wizards | Auth tokens, session IDs |

### localStorage Methods

```javascript
// ── Basic CRUD ──
localStorage.setItem('theme', 'dark');
const theme = localStorage.getItem('theme');  // "dark"
localStorage.removeItem('theme');
localStorage.clear();  // Clears ALL

// ── Storing Objects (MUST use JSON.stringify) ──
const user = { name: 'Alex', role: 'Developer' };
localStorage.setItem('user', JSON.stringify(user));

// ── Reading Objects (MUST use JSON.parse) ──
const storedUser = JSON.parse(localStorage.getItem('user'));
console.log(storedUser.name);  // "Alex"

// ⚠️ WITHOUT JSON.stringify → "[object Object]" — useless!
```

### Analogies

| Storage Type | Analogy |
|--------------|---------|
| **localStorage** | Home bookshelf — stays forever until you remove it |
| **sessionStorage** | Hotel notepad — cleared when you check out (close tab) |

---

## 🔒 PART 14: COOKIE SECURITY FLAGS

### Security Flags

| Flag | What It Blocks | Effect |
|------|---------------|--------|
| **HttpOnly** | XSS (Cross-Site Scripting) | JavaScript cannot read via `document.cookie` |
| **Secure** | Network interception / MITM | Cookie only sent over HTTPS |
| **SameSite=Strict** | CSRF (Cross-Site Request Forgery) | Cookie never sent on cross-origin requests |
| **SameSite=Lax** | CSRF (safer) | Allows safe cross-site navigation |
| **SameSite=None** | Unrestricted | Requires `Secure` flag as well |

### Cookie Flag Summary

```
Set-Cookie: sessionId=abc123; HttpOnly; Secure; SameSite=Strict
```

| Flag | Purpose |
|------|---------|
| **HttpOnly** | Prevents XSS token theft |
| **Secure** | Prevents MITM interception |
| **SameSite** | Prevents CSRF attacks |

---

## 🧪 PART 15: SKILL-BUILDING DRILLS

### Drill 1: Task List Manager

```javascript
// ── Complete task manager combining all DOM pillars ──
const input = document.querySelector("#taskInput");
const addBtn = document.querySelector("#addBtn");
const container = document.querySelector("#taskList");

// 1. Event: Add Task
addBtn.addEventListener("click", function() {
  const taskText = input.value.trim();
  if (taskText === "") { alert("Enter a valid task!"); return; }

  // 2. Manipulation: Create → Configure → Append
  const row = document.createElement("div");
  row.className = "task-row";
  row.innerHTML = `<span>${taskText}</span> <button class="delete-btn">✕</button>`;
  container.appendChild(row);
  input.value = "";
});

// 3. Event Delegation: Delete via parentElement
container.addEventListener("click", function(event) {
  if (event.target.classList.contains("delete-btn")) {
    event.target.parentElement.remove();
  }
});
```

### Drill 2: Camera + Storage Demo

```javascript
// ── Theme persistence with localStorage ──
const savedTheme = localStorage.getItem('appTheme') || 'light';
document.body.className = savedTheme;

document.getElementById('theme-btn').addEventListener('click', function() {
  const newTheme = document.body.className === 'light' ? 'dark' : 'light';
  document.body.className = newTheme;
  localStorage.setItem('appTheme', newTheme);
});

// ── Camera access with getUserMedia ──
document.getElementById('cam-btn').addEventListener('click', function() {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(stream) {
      document.querySelector('video').srcObject = stream;
    })
    .catch(function() {
      alert('Could not access camera.');
    });
});

// ── Canvas snapshot ──
document.getElementById('snap-btn').addEventListener('click', function() {
  const canvas = document.getElementById('snapshot');
  canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
});
```

---

## 🚨 PART 16: COMMON PITFALLS & GOLDEN RULES

### Golden Rules

| Rule | Why |
|------|-----|
| ✅ Prefer `children` over `childNodes` | `childNodes` includes #text whitespace nodes |
| ✅ `querySelector` returns `null` — always null-check | Prevents "cannot read property of null" errors |
| ✅ `nextElementSibling` returns `null` — guard before use | Prevents errors on last element |
| ✅ Live collections shift mid-loop — convert or iterate in reverse | Prevents skipped elements |
| ✅ `addEventListener` stacks — `onclick=` overwrites | Use `addEventListener` for multiple handlers |
| ✅ `createElement` alone is invisible — must `appendChild` | Element exists only in memory |
| ✅ Always check `response.ok` in fetch | 404/500 do NOT reject the Promise |
| ✅ Always add `.catch()` to Promises | Unhandled rejections fail silently |
| ✅ Always `JSON.stringify()` before storing objects | localStorage only stores strings |
| ✅ Always `JSON.parse()` when reading objects back | Otherwise you get `"[object Object]"` |
| ✅ getUserMedia() needs HTTPS | Fails on plain HTTP sites |
| ✅ Never store tokens in localStorage | Vulnerable to XSS — use HttpOnly cookies |

### The #text Node Trap

```html
<!-- HTML with indentation -->
<div>
  <p>Hello</p>
</div>
```

```javascript
const div = document.querySelector('div');
console.log(div.childNodes);        // [ #text, <p>, #text ] ← includes whitespace!
console.log(div.children);          // [ <p> ]              ← elements only ✅
console.log(div.firstChild);        // #text                ← whitespace!
console.log(div.firstElementChild); // <p>                  ← correct ✅
```

---

## 📝 QUICK REFERENCE CARD

### Selection Quick Guide

| Need | Use |
|------|-----|
| Single element by ID | `getElementById(id)` or `querySelector("#id")` |
| First CSS match | `querySelector(selector)` |
| All CSS matches | `querySelectorAll(selector)` → NodeList with forEach |
| By class name | `getElementsByClassName(name)` → live HTMLCollection |
| By tag name | `getElementsByTagName(tag)` → live HTMLCollection |
| Element children only | `element.children` → live HTMLCollection |

### Collection Quick Guide

| Type | forEach? | Live? | Convert to Array |
|------|----------|-------|------------------|
| **HTMLCollection** | ❌ No | 🔴 Live | `Array.from(col)` or `[...col]` |
| **NodeList (querySelectorAll)** | ✅ Yes | 📸 Static | `Array.from(list)` or `[...list]` |
| **NodeList (childNodes)** | ✅ Yes | 🔴 Live | `Array.from(list)` |

### Event Listener Quick Guide

| Need | Code |
|------|------|
| Add listener | `element.addEventListener("click", function)` |
| Remove listener | `element.removeEventListener("click", namedFunction)` |
| Stop propagation | `event.stopPropagation()` |
| Prevent default | `event.preventDefault()` |
| Event delegation | `parent.addEventListener("click", function(e) { if (e.target.matches(".btn")) { ... } })` |

### Storage Quick Guide

| Need | Code |
|------|------|
| Store string | `localStorage.setItem("key", "value")` |
| Read string | `localStorage.getItem("key")` |
| Store object | `localStorage.setItem("key", JSON.stringify(obj))` |
| Read object | `JSON.parse(localStorage.getItem("key"))` |
| Remove item | `localStorage.removeItem("key")` |
| Clear all | `localStorage.clear()` |

---

> **💡 Final Thought:** The DOM is a tree. Master the tree — master the web. Every selection, traversal, event, and manipulation is just a predictable move on that tree. Go build something great! 🚀