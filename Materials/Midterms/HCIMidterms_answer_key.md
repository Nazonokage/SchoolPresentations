# Answer Key — HCI2 (IT103) Midterm Periodical Exam
**Total Items: 48 | Total Points: 60**

---


## I. Multiple Choice (Items 1–20, 1 pt each)

| # | Ans |
|---|-----|
| 1 | B   |
| 2 | D   |
| 3 | C   |
| 4 | B   |
| 5 | C   |

| 6 | C   |
| 7 | B   |
| 8 | C   |
| 9 | B   |
| 10 | B  |

| 11 | B  |
| 12 | B  |
| 13 | B  |
| 14 | B  |
| 15 | C  |

| 16 | D  |
| 17 | C  |
| 18 | B  |
| 19 | B  |
| 20 | B  |

---

## II. Identification (Items 21–30, 1 pt each, situational)

21. **Live collection** — HTMLCollection auto-updates as the DOM changes, so its length grows mid-loop.
22. **Failed to null-check** the result of `querySelector()` before using it.
23. **`forEach()`** — NodeLists have a native `forEach()` method.
24. A **`#text` (whitespace) node**; should have used **`firstElementChild`** instead of `firstChild`.
25. **`addEventListener()`** — it attaches handlers without overwriting existing ones and allows multiple handlers on the same event.
26. **Event delegation** — attach one listener to the parent container and check `event.target` inside it.
27. **AmbientLightSensor**; requires the **`ambient-light-sensor`** permission policy.
28. **sessionStorage** — cleared automatically when the tab/session closes.
29. **HttpOnly** — blocks JavaScript from reading the cookie via `document.cookie`.
30. `fetch()` only rejects on **network failures**, not on HTTP error statuses like 404/500; the developer should check **`response.ok`** and throw an error manually.

*Grading note: accept close paraphrases that name the same concept/method.*

---

## III. Enumeration (Items 31–40, 1 pt each — any order within a group unless noted)

**31–33 (in order required):**
31. Create (`document.createElement`)
32. Configure (set innerHTML / className / style / attributes)
33. Attach (`appendChild` to a parent)

**34–37 (any 4, order not required):**
34. Parent Node
35. Child Node
36. Sibling Nodes
37. Ancestors *(or Descendants — accept either)*

**38–40 (order not required):**
38. HttpOnly
39. Secure
40. SameSite

---

## IV. Guess the Output (Items 41–45, 1 pt each — must match exactly)

**41.**
```
3
```
*(The loop runs 3 times, creating and appending 3 `<div>` circles into `#shapes`.)*

**42.**
```
1
3
```
*(`children` counts only the `<p>`; `childNodes` also counts the two whitespace `#text` nodes.)*

**43.**
```
[object Object]
```
*(`JSON.stringify()` was not used before storing the object.)*

**44.**
```
Hello!
```
*(Calling `.click()` triggers the click event, which runs the listener function.)*

**45.**
```
A
B
C
```
*(`fetch()` is asynchronous, so synchronous code — A, B — runs before the resolved `.then()` callback — C.)*

---

## V. Coding Problems (Items 46–48, 5 pts each)

Grade holistically. Suggested rubric per item (5 pts):
- **2 pts** — correct core logic/structure (e.g., loop + createElement, correct fetch chain, correct storage calls)
- **1 pt** — correct selectors/element references (`#circleContainer`, `#theme-btn`, etc.)
- **1 pt** — correct method usage (`appendChild`, `.style` properties, `localStorage.setItem`/`getItem`, `.json()`)
- **1 pt** — completeness (all 3 circles created / toggle works both ways / `.catch()` present)

### 46. Circle Generator (DOM Creation Loop)
Reference solution:
```html
<div id="circleContainer"></div>

<script>
const container = document.getElementById("circleContainer");
const colors = ["red", "green", "blue"];

for (let i = 0; i < 3; i++) {
  const circle = document.createElement("div");
  circle.style.width = "50px";
  circle.style.height = "50px";
  circle.style.borderRadius = "50%";
  circle.style.backgroundColor = colors[i];
  circle.style.display = "inline-block";
  circle.style.margin = "5px";
  container.appendChild(circle);
}
</script>
```
Key things to look for: a loop that runs exactly 3 times; `document.createElement("div")` used inside the loop; `borderRadius = "50%"` plus equal width/height to form a circle; a `backgroundColor` set; each circle appended to `#circleContainer` with `appendChild()`. (Coloring each circle differently is a nice-to-have, not required.)

### 47. Theme Toggle with localStorage
Reference solution:
```javascript
const savedTheme = localStorage.getItem("appTheme") || "light";
document.body.className = savedTheme;

document.getElementById("theme-btn").addEventListener("click", function () {
  const newTheme = document.body.className === "light" ? "dark" : "light";
  document.body.className = newTheme;
  localStorage.setItem("appTheme", newTheme);
});
```
Key things to look for: default fallback to `"light"` with `||`; `getItem`/`setItem` used correctly (no `JSON.stringify` needed since it's a plain string); toggle logic is correct both ways.

### 48. Fetching Users with fetch()
Reference solution:
```javascript
function fetchUsers() {
  fetch("https://api.example.com/users")
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log(data);
    })
    .catch(function (error) {
      console.error(error);
    });
}
```
Key things to look for: `return response.json()` inside the first `.then()` (not just calling it without returning); `console.log(data)` in the second `.then()`; a `.catch()` at the end. Checking `response.ok` / throwing a manual error is a bonus, not required at this difficulty level.

---
*End of Answer Key*
