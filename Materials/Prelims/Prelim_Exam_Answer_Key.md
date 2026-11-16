# 🔑 PRELIM EXAM — Answer Key
**Web Systems | Node.js Foundations**
> Instructor copy — do not distribute

---

## PART I — Multiple Choice (30 pts)

```markdown
| # | Answer |
|:-:|--------|
| 1  | **c) const** |
| 2  | **c) "object"** |
| 3  | **b) true** |
| 4  | **c) .map()** |
| 5  | **b) Compares value AND type** |
| 6  | **b) A function that remembers variables from its outer scope even after that scope has finished** |
| 7  | **c) NaN** |
| 8  | **b) Compiles JavaScript to machine code** |
| 9  | **b) It uses a single-threaded, non-blocking event loop** |
| 10 | **c) fs** |

| 11 | **c) The path to the node executable** |
| 12 | **c) path** |
| 13 | **c) const d = await fs.promises.readFile("x.txt", "utf8")** |
| 14 | **c) index.js** |
| 15 | **b) It builds correct paths for the current OS — avoiding / vs \\ issues** |
| 16 | **b) ^1.2.3** |
| 17 | **c) dependencies are needed at runtime; devDependencies are only needed during development** |
| 18 | **c) async/await** |
| 19 | **b) Between each phase, before the next phase starts** |
| 20 | **c) process.nextTick(fn)** |

| 21 | **c) 0** |
| 22 | **b) An expected failure such as a missing file or invalid input** |
| 23 | **b) A safety net — not a substitute for proper try/catch handling** |
| 24 | **b) They get committed to version control and exposed; use environment variables instead** |
| 25 | **b) 403** |
| 26 | **c) 422** |
| 27 | **b) An object that emits named events and lets listeners register for them** |
| 28 | **b) Streams process data in chunks — memory stays flat regardless of file size** |
| 29 | **d) Transform** |
| 30 | **b) Connects a readable stream output directly into a writable stream** |
```
---

## PART II — Identification (10 pts)

### Items 31–33 — Guess the Output

**31.**
```
Hello, Node!
```
> `makeGreeter("Hello")` returns a closure that captures `greeting = "Hello"`. Calling `hello("Node")` fills in `name`, and the template literal produces `Hello, Node!`.

**32.**
```
{"message":"pong"}
```
> Both conditions match (`GET` + `/ping`), so the server sends status 200 with `JSON.stringify({ message: "pong" })` as the response body.

**33.**
```
Connected to server
```
> `Promise.resolve("Connected to server")` resolves immediately. `await` unwraps the value into `msg`, and `console.log(msg)` prints it.

---

### Items 34–40 — Short Identification

| # | Answer |
|---|--------|
| 34 | `process` |
| 35 | `devDependencies` |
| 36 | Closure |
| 37 | Programmer error |
| 38 | `~` (tilde) |
| 39 | `events` |
| 40 | `403` |

---

## PART III — GET or POST? (6 pts)

| # | Answer | Reason |
|---|--------|--------|
| 41 | **POST** | Submitting credentials — data goes in the request body; changes server state |
| 42 | **GET** | Fetching a list — read-only, idempotent, no body |
| 43 | **POST** | Creating a resource — sends a body; calling twice creates two users (not idempotent) |
| 44 | **GET** | Fetching a specific record by ID — read-only |
| 45 | **POST** | Submitting data to be saved — changes server state |
| 46 | **GET** | Requesting information — read-only, no side effects |

---

## PART IV — Coding Problems (9 pts)

---

### Problem 1 — Closure / Function Factory (3 pts)

**What a correct answer demonstrates:**
- `makeLogger` accepts `prefix` and **returns** an inner function (closure)
- The inner function accepts `message` and calls `console.log` formatted as `[PREFIX] message`
- The outer `prefix` variable is still accessible inside the returned function after `makeLogger` has finished — this is the closure behavior

**Reference implementation:**
```js
function makeLogger(prefix) {
  return function(message) {
    console.log(`[${prefix}] ${message}`);
  };
}

const warn = makeLogger("WARN");
warn("Disk space low");   // [WARN] Disk space low
```

**Scoring guide:**
- 1 pt — `makeLogger` returns a function (closure structure correct)
- 1 pt — Inner function accepts `message` and logs with the correct `[PREFIX] message` format
- 1 pt — Correct invocation shown or implied; expected output matches

**Common mistakes:** Logging inside `makeLogger` itself instead of the returned function; not returning the inner function; template literal syntax errors.

---

### Problem 2 — Raw HTTP Server (3 pts)

**What a correct answer demonstrates:**
- Requires `http`; creates a server with `http.createServer((req, res) => { ... })`
- Checks **both** `req.method === 'GET'` **and** `req.url === '/status'`
- On match → `res.writeHead(200, { 'Content-Type': 'application/json' })` then `res.end(JSON.stringify({ status: 'ok' }))`
- On no match → `res.writeHead(404)` then `res.end(JSON.stringify({ error: 'Not found' }))`
- Calls `server.listen(port)`

**Reference implementation:**
```js
const http = require('http');

const server = http.createServer((req, res) => {
  if (req.method === 'GET' && req.url === '/status') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'ok' }));
  } else {
    res.writeHead(404);
    res.end(JSON.stringify({ error: 'Not found' }));
  }
});

server.listen(3000);
```

**Scoring guide:**
- 1 pt — Server created with `http.createServer`; `server.listen()` called
- 1 pt — Correct conditional on both `req.method` and `req.url`; 200 response with JSON body
- 1 pt — 404 fallback with JSON error body; `Content-Type` header set on the success response

**Common mistakes:** Using `==` instead of `===`; missing `res.end()` (response hangs); forgetting `JSON.stringify`; no else/fallback for the 404 case.

---

### Problem 3 — Async/Await + Error Handling (3 pts)

**What a correct answer demonstrates:**
- Function declared with the `async` keyword
- `await fs.promises.readFile(filename, 'utf8')` used inside a `try` block; result stored in a variable
- On success: `console.log(data)` (or whatever the variable is named)
- In `catch(err)`: logs exactly `"Could not read file: " + err.message` — the format matters
- The function is called with `'config.txt'` after it is declared

**Reference implementation:**
```js
const fs = require('fs');

async function readConfig(filename) {
  try {
    const data = await fs.promises.readFile(filename, 'utf8');
    console.log(data);
  } catch (err) {
    console.error('Could not read file: ' + err.message);
  }
}

readConfig('config.txt');
```

**Scoring guide:**
- 1 pt — `async` function declared; `await` used correctly inside `try`
- 1 pt — File read with `fs.promises.readFile`; result logged on success
- 1 pt — `catch(err)` block logs the exact format: `"Could not read file: <err.message>"`

**Common mistakes:** Forgetting `async` keyword (makes `await` a syntax error); using callback-style `fs.readFile` inside an async function; missing `'utf8'` encoding; error message format doesn't match the spec; function never called at the end.

---

*Good luck sa checking! 🍀*
