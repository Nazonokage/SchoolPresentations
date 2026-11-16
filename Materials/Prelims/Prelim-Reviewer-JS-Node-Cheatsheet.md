
# 📘 PRELIM REVIEWER — JavaScript & Node.js Foundations
### Covers: Wk1–6 (Node Internals → Core Modules → HTTP/Streams → Docker Intro)

---

## PART 0 — JavaScript Basics Cheat Sheet
*(quick refresher before diving into Node-specific stuff)*

### Variables
```js
var a = 1;    // function-scoped, hoisted, avoid using
let b = 2;    // block-scoped, can reassign
const c = 3;  // block-scoped, cannot reassign (but object/array contents CAN change)
```

### Data Types
| Type | Example |
|---|---|
| Number | `42`, `3.14` |
| String | `"hello"`, `` `template ${literal}` `` |
| Boolean | `true`, `false` |
| Null | `null` (intentional empty value) |
| Undefined | `undefined` (declared, not assigned) |
| Object | `{ key: "value" }` |
| Array | `[1, 2, 3]` |
| Symbol / BigInt | rare, know they exist |

`typeof` checks type. `===` compares value **and** type (always prefer this over `==`).

### Functions
```js
function add(a, b) { return a + b; }         // declaration (hoisted)
const add = function(a, b) { return a + b; } // expression
const add = (a, b) => a + b;                 // arrow function (no own `this`)
```

### Arrays — common methods
| Method | Does |
|---|---|
| `.map()` | transforms each item, returns new array |
| `.filter()` | keeps items matching a condition |
| `.reduce()` | folds array into single value |
| `.forEach()` | loops, no return value |
| `.find()` | returns first match |
| `.includes()` | true/false if value exists |
| `.push()` / `.pop()` | add/remove from end |
| `.shift()` / `.unshift()` | remove/add from start |

### Objects
```js
const user = { name: "Ana", age: 20 };
const { name, age } = user;          // destructuring
const user2 = { ...user, age: 21 };  // spread — shallow copy + override
```

### Closures
A function "remembers" the variables from where it was created, even after that outer function has finished running.
```js
function counter() {
  let count = 0;
  return () => ++count;
}
const inc = counter();
inc(); // 1
inc(); // 2
```
This is the backbone of things like private state, `useState` in React later, and module patterns.

### Callbacks → Promises → Async/Await
```js
// 1. Callback style
fs.readFile("file.txt", (err, data) => { ... });

// 2. Promise style
fs.promises.readFile("file.txt").then(data => { ... }).catch(err => { ... });

// 3. Async/await (cleanest, sits on top of Promises)
async function readIt() {
  try {
    const data = await fs.promises.readFile("file.txt");
  } catch (err) {
    console.error(err);
  }
}
```
**Key rule:** `await` only works inside an `async` function. `await` pauses that function (not the whole program) until the Promise resolves or rejects.

### Truthy / Falsy (quick gotcha list)
Falsy: `false, 0, "", null, undefined, NaN` — everything else is truthy (yes, even `"0"` and `[]`).

---

## PART 1 — Node.js Internals (Week 1 Recap)

- **V8**: Google's JS engine (also powers Chrome). Compiles JS to machine code.
- **Event Loop**: Node is single-threaded but non-blocking — I/O is handed off, and callbacks are queued to run when ready. This is *why* Node is fast at handling many concurrent connections without spawning threads per request.
- **npm**: Node Package Manager. `npm install`, `npm init`, `package.json`, `package-lock.json`.
- **Core modules**: built into Node, no install needed (`fs`, `path`, `http`, `events`, etc.) — `require('fs')` just works.

---

## PART 2 — Core Modules (Week 2)

### `fs` (File System)
```js
// Callback style
fs.readFile('data.txt', 'utf8', (err, data) => { ... });

// Promise style (preferred)
const fs = require('fs').promises;
const data = await fs.readFile('data.txt', 'utf8');
await fs.writeFile('out.txt', data);
```

### `path`
```js
path.join(__dirname, 'files', 'a.txt');  // safe cross-platform path building
path.resolve('a.txt');                    // absolute path
path.extname('a.txt');                    // '.txt'
path.basename('/a/b/c.txt');              // 'c.txt'
```
**Why it matters:** hardcoding `/` breaks on Windows. `path.join` always does it correctly for the OS running the code.

### `package.json` essentials
```json
{
  "name": "log-parser",
  "version": "1.0.0",
  "scripts": { "start": "node index.js" },
  "dependencies": { "dotenv": "^16.0.0" }
}
```
- `dependencies` vs `devDependencies`
- Semver: `^1.2.3` (minor/patch updates ok), `~1.2.3` (patch updates only), `1.2.3` (exact)
- `npm run <script>` executes anything under `"scripts"`

---

## PART 3 — Event Loop, `process`, Error Handling (Week 3)

### Event Loop Phases (simplified order)
```
timers → pending callbacks → poll → check → close callbacks
```
- **Microtasks** (Promises, `process.nextTick`) run **between** each phase, before moving on.
- `setTimeout(fn, 0)` vs `setImmediate(fn)` vs `process.nextTick(fn)` — nextTick runs soonest, then microtasks, then timers/immediate.

### `process`
```js
process.argv;        // CLI arguments array
process.env.MY_VAR;  // environment variables
process.cwd();        // current working directory
process.exit(1);      // exit with non-zero = failure signal
```
Exit code `0` = success, anything else = failure. Matters later for CI/CD and Docker healthchecks.

### Error Handling
```js
class ValidationError extends Error {
  constructor(msg) {
    super(msg);
    this.name = 'ValidationError';
  }
}

try {
  if (!input) throw new ValidationError('Input required');
} catch (err) {
  console.error(err.message);
}
```
- **Operational errors** (bad input, missing file) → expected, handle gracefully.
- **Programmer errors** (bugs, typos) → should crash loudly in dev, get fixed.
- `process.on('uncaughtException', ...)` and `process.on('unhandledRejection', ...)` are a **safety net**, never a primary strategy — don't rely on them to "handle" errors.

---

## PART 4 — `http` Module, EventEmitter, Streams (Week 4)

### Raw HTTP Server (no Express)
```js
const http = require('http');

const server = http.createServer((req, res) => {
  if (req.url === '/summary' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ lines: 100 }));
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

server.listen(3000);
```
This is literally what Express does for you under the hood — routing, headers, status codes, all by hand here.

### EventEmitter
```js
const { EventEmitter } = require('events');
const emitter = new EventEmitter();

emitter.on('received', (order) => console.log('Got order:', order));
emitter.emit('received', { id: 1 });
```
`http.Server` itself is an EventEmitter — that's why `server.on('request', ...)` works.

### Streams
| Type | Direction |
|---|---|
| Readable | source you read from (e.g., file read stream) |
| Writable | destination you write to (e.g., file write stream, HTTP response) |
| Duplex | both read and write |
| Transform | reads, modifies, writes (e.g., uppercase converter) |

```js
fs.createReadStream('big.log').pipe(fs.createWriteStream('copy.log'));
```
**Why streams matter:** loading a huge file with `readFile` loads it *entirely* into memory. Streams process it in small chunks — memory stays flat regardless of file size.

### Common HTTP Status Codes
Grouped by first digit — the digit alone tells you the *category* even before you know the exact code.

| Range | Category | Meaning |
|---|---|---|
| 1xx | Informational | request received, still processing |
| 2xx | Success | request worked |
| 3xx | Redirection | client must go somewhere else |
| 4xx | Client Error | *you* (the request) messed up |
| 5xx | Server Error | the *server* messed up |

**The ones you'll actually use constantly:**

| Code | Name | When |
|---|---|---|
| `200` | OK | Successful GET/PUT/PATCH — "here's your data" |
| `201` | Created | Successful POST that created a new resource |
| `204` | No Content | Success, but nothing to send back (common on DELETE) |
| `301` | Moved Permanently | Resource has a new permanent URL |
| `304` | Not Modified | Cached version is still valid, don't re-send |
| `400` | Bad Request | Malformed request (missing/invalid fields) |
| `401` | Unauthorized | Not logged in / missing or invalid credentials |
| `403` | Forbidden | Logged in, but not allowed to access this |
| `404` | Not Found | Route/resource doesn't exist |
| `409` | Conflict | e.g., trying to create a duplicate (email already registered) |
| `422` | Unprocessable Entity | Valid request format, but fails validation rules |
| `500` | Internal Server Error | Unhandled exception / bug on the server |
| `503` | Service Unavailable | Server is down/overloaded (e.g., DB connection failed) |

```js
// Example: matching status codes to outcomes
if (!user) {
  res.writeHead(404, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ error: 'User not found' }));
} else {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify(user));
}
```
**Memory trick:** 2 = good, 4 = your fault, 5 = server's fault.

### GET vs POST
| | GET | POST |
|---|---|---|
| **Purpose** | Retrieve/read data | Create or submit data |
| **Data location** | In the URL (query string, e.g. `?id=5`) | In the request **body** |
| **Visible in URL?** | Yes — shows up in browser history, logs, bookmarks | No — hidden from the URL |
| **Idempotent?**† | Yes — calling it many times has the same effect as once | No — calling it twice can create two resources |
| **Cacheable?** | Yes, by default | No, not by default |
| **Has a body?** | Conventionally no | Yes, always |
| **Typical use** | `GET /users/5` → fetch user 5 | `POST /users` → create a new user |

† **Idempotent** = doing it once or ten times leaves the system in the same state. `GET /users/5` always just *reads* — no side effects. `POST /users` run twice creates *two* separate users, so it's not idempotent.

```js
// Raw http — reading the method to branch logic
const server = http.createServer((req, res) => {
  if (req.method === 'GET' && req.url === '/users') {
    // fetch and return users
  } else if (req.method === 'POST' && req.url === '/users') {
    // read request body, create a new user
  }
});
```
**Quick rule of thumb:** if the action *changes* something on the server (create, update, delete), it shouldn't be a GET — browsers, proxies, and crawlers can pre-fetch or cache GETs, which is dangerous if a GET secretly deletes a record.

---

## PART 5 — Docker Fundamentals I (Week 5)

### Core Concepts
- **Image** = blueprint/recipe (read-only template).
- **Container** = a running instance of an image.
- **VM vs Container**: a VM virtualizes an entire OS (heavy); a container shares the host's kernel and only isolates the process (lightweight, fast to start).

### Dockerfile Anatomy
```dockerfile
FROM node:20-alpine        # base image
WORKDIR /app                # sets working dir inside container
COPY package*.json ./       # copy dependency manifests FIRST
RUN npm install              # install deps (cached if manifests unchanged)
COPY . .                     # copy rest of source code
EXPOSE 3000                  # documents which port the app uses
CMD ["node", "index.js"]     # command that runs when container starts
```

**Why `COPY package*.json` before `COPY . .`?**
Docker caches each instruction as a "layer." If only your source code changes (not dependencies), Docker reuses the cached `npm install` layer instead of reinstalling everything — much faster rebuilds.

### Key Commands
```bash
docker build -t my-app .        # build image from Dockerfile in current dir
docker run -p 3000:3000 my-app  # run container, map host:container port
docker ps                        # list running containers
docker logs <container>          # view container output
docker stop <container>          # stop a running container
```

### `.dockerignore`
Same idea as `.gitignore` — exclude files that shouldn't be copied into the image:
```
node_modules
.git
.env
```
`node_modules` is excluded because `npm install` runs *inside* the container — copying your local one can cause OS/architecture mismatches.

---

## PART 6 — Quick Self-Check Questions

1. What's the difference between `let`, `const`, and `var`?
2. Why does `await` need to be inside an `async function`?
3. What does `path.join()` solve that hardcoding `/` doesn't?
4. Name two operational errors vs. one programmer error.
5. Why is `process.on('uncaughtException')` a "safety net, not a strategy"?
6. What problem do Streams solve that `fs.readFile` doesn't?
6a. What's the difference between a `401` and a `403`? Between `404` and `500`?
6b. Why is GET considered idempotent but POST is not?
7. What's the difference between an image and a container?
8. Why order `COPY package*.json` before `COPY . .` in a Dockerfile?
9. What does `-p 3000:3000` mean in `docker run`?
10. What should go in `.dockerignore` and why?

---

## PART 7 — Milestone Reminder (Week 6 Output)
Your Prelim capstone ("Hello Container") should include:
- ✅ A working CLI/raw-HTTP tool (no frameworks)
- ✅ A working `Dockerfile`
- ✅ A `.dockerignore`
- ✅ A `README.md` with exact `docker build`/`docker run` commands
- ✅ Evidence of async/await, custom error handling, and env-var config

You should be able to explain, out loud: **what an image is, what a container is, and why you containerized your tool.**

---
*Good luck sa prelims! 🍀*
