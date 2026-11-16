# PRELIMS — Node.js Foundations + Docker Intro
### Detailed Lesson Plans: Weeks 2–6

**Term goal:** By the end of Prelim, students are comfortable writing and reasoning about Node.js on its own — no frameworks — and understand *why* containers exist and how to build one.

**Where this picks up:** Week 1 (already delivered) covered Node.js internals conceptually — the V8 engine, the event loop, npm, and core modules. Everything below assumes that foundation and moves from "knowing what these things are" to "using them to build something."

**Term output (Week 6):** A working CLI or raw-HTTP tool — no framework — packaged in its own Docker container, proving students understand both what Express abstracts away *and* what Docker abstracts away.

---

## Week 2 — Core Node.js Modules & Asynchronous I/O in Practice

### Learning Objectives
By the end of this session, students will be able to:
1. Use the `fs` module (both callback and Promise-based APIs) to read, write, and manipulate files.
2. Use the `path` module to build cross-platform-safe file paths.
3. Explain the difference between callbacks, Promises, and `async/await`, and convert code between the three styles.
4. Read and write a `package.json` file confidently, including dependencies, scripts, and semantic versioning ranges (`^`, `~`).
5. Build and run a small command-line tool that reads input, transforms it, and writes output — using only core Node modules (no frameworks).

### Lecture Outline (≈2.5–3 hours, adjust to your block length)

| Time | Segment | Content |
|---|---|---|
| 0:00–0:15 | Recap & bridge | Quick recall of Wk1: event loop, npm. Frame today as "now we actually *do* something with Node." |
| 0:15–0:45 | The `fs` module | `readFile`/`writeFile` (callback style) → `fs.promises` → `fs/promises` with `async/await`. Live-code the same file read 3 ways to make the evolution concrete. |
| 0:45–1:05 | The `path` module | `path.join`, `path.resolve`, `path.extname`, `path.basename` — why hardcoded `/` or `\` breaks cross-platform. |
| 1:05–1:15 | Break | — |
| 1:15–1:50 | Async patterns deep dive | Callback hell → Promises (`.then`/`.catch`) → `async/await` with `try/catch`. Show a real "callback pyramid" and refactor it live. |
| 1:50–2:10 | `package.json` & npm scripts | Dependencies vs devDependencies, semver ranges, `npm run` custom scripts, `.gitignore` for `node_modules`. |
| 2:10–2:30 | Live demo of the lab | Instructor builds a minimal version of the lab tool (a line counter) so students see the shape of the exercise before attempting it alone. |
| 2:30–end | Lab kickoff | Students start the hands-on activity below; instructor circulates. |

### Hands-On Lab: Build a "Log Parser" CLI Tool

**Scenario:** Students write a small Node CLI tool that reads a plain-text log file and reports basic stats — no Express, no frameworks, core modules only.

**Requirements:**
1. Accept a file path as a command-line argument (`process.argv`).
2. Read the file using `fs.promises.readFile`.
3. Parse the content and compute:
   - Total number of lines
   - Number of lines containing the word `ERROR`
   - Number of lines containing the word `WARNING`
4. Write a summary to a new file, e.g. `summary.txt`, using `fs.promises.writeFile`, with the output path built via `path.join`.
5. Wrap all file operations in `try/catch` and print a friendly error message if the input file doesn't exist.
6. **Stretch goal (for fast finishers):** Use `fs.createReadStream` with `readline` to process the file line-by-line instead of loading it all into memory — a preview of the streams concept coming in Week 4.

**Deliverable:** A GitHub repo (or zipped folder) containing:
- `index.js`
- `package.json` (with a `start` script: `"start": "node index.js"`)
- A sample `sample.log` input file
- A short `README.md` explaining how to run it

**Assessment criteria:**
- Correct use of async/await over callbacks (5 pts)
- Correct, cross-platform path handling (5 pts)
- Error handling for missing/invalid files (5 pts)
- Working `package.json` with a functional `npm start` (5 pts)

### Homework / Bridge to Week 3
Ask students to intentionally break their own tool by triggering an uncaught error (e.g., pass a non-existent file) and observe what happens in the terminal. Bring the exact error output to Week 3 — it becomes the live example for the error-handling and `process` deep dive.

---

## Week 3 — Event Loop Deep Dive, `process`, and Error Handling

### Learning Objectives
By the end of this session, students will be able to:
1. Explain the phases of the Node.js event loop (timers, pending callbacks, poll, check, close callbacks) and where microtasks (Promises) fit in.
2. Use `process.argv`, `process.env`, and `process.exit()` correctly in a CLI context.
3. Load environment variables from a `.env`-style file and explain why secrets shouldn't be hardcoded.
4. Distinguish operational errors (bad input, missing file) from programmer errors (bugs), and handle each appropriately.
5. Write custom `Error` subclasses and use `try/catch` around both sync and async code.
6. Explain what `uncaughtException` and `unhandledRejection` are, and why relying on them as a primary error-handling strategy is dangerous.

### Lecture Outline

| Time | Segment | Content |
|---|---|---|
| 0:00–0:15 | Homework debrief | Walk through 2–3 student-submitted error outputs from the Wk2 homework. Ask: "What did Node do when it didn't know how to handle this?" |
| 0:15–0:50 | Event loop, revisited | Whiteboard the phases (timers → pending callbacks → poll → check → close). Show `setTimeout` vs `setImmediate` vs `process.nextTick` ordering live in the REPL. |
| 0:50–1:10 | The `process` object | `process.argv`, `process.env`, `process.cwd()`, `process.exit(code)` and exit codes as a concept (0 = success, non-zero = failure — ties into CI/CD and Docker later). |
| 1:10–1:20 | Break | — |
| 1:20–1:40 | Environment variables | Why config/secrets don't belong in source code. Introduce `.env` files and the `dotenv` package conceptually (full use comes with Express in Wk7). |
| 1:40–2:15 | Error handling patterns | Operational vs programmer errors. Custom `Error` classes (`class ValidationError extends Error`). `try/catch` with `async/await`. Global handlers: `process.on('uncaughtException')` / `process.on('unhandledRejection')` — and why they're a safety net, not a strategy. |
| 2:15–end | Lab kickoff | — |

### Hands-On Lab: Harden the Log Parser

**Scenario:** Students take their Week 2 log parser and make it production-grade in terms of error handling and configurability.

**Requirements:**
1. Move any hardcoded settings (e.g., which keywords count as "errors") into a `.env` file, read via `process.env`.
2. Create at least one custom error class (e.g., `InvalidLogFormatError`) and throw it when the input file doesn't look like a log file.
3. Add a top-level `process.on('unhandledRejection', ...)` handler that logs a clean message and exits with a non-zero code — instead of letting Node print a raw stack trace.
4. Support a `--verbose` flag (checked via `process.argv`) that prints extra debug info only when passed.
5. Document in the `README.md`: what exit code the tool returns on success vs. failure, and why that matters.

**Deliverable:** Updated repo from Week 2 with the above changes, plus a short "Error Handling Notes" section in the README.

**Assessment criteria:**
- Correct, meaningful use of a custom Error class (5 pts)
- Environment variables used instead of hardcoded config (5 pts)
- Sensible exit codes on success/failure (5 pts)
- `--verbose` flag works as specified (5 pts)

### Homework / Bridge to Week 4
Ask students to time how long their tool takes to process a very large log file (instructor provides a 500MB+ sample). Most will notice a memory spike or slowdown — this becomes the motivating problem for streams in Week 4.

---

## Week 4 — The `http` Module, EventEmitter, and Streams

### Learning Objectives
By the end of this session, students will be able to:
1. Build a working web server using only the built-in `http` module — no Express.
2. Explain what Express actually does under the hood by contrasting it with raw `http` code.
3. Use `EventEmitter` to build a custom event-driven object.
4. Explain the four stream types (Readable, Writable, Duplex, Transform) and why streams solve the memory problem from the Wk3 homework.
5. Pipe data between streams (`.pipe()`) to process large files without loading them fully into memory.

### Lecture Outline

| Time | Segment | Content |
|---|---|---|
| 0:00–0:15 | Homework debrief | Discuss the large-file slowdown students hit. Frame today's streams section as the fix. |
| 0:15–0:50 | Raw `http` server | Live-code a server with `http.createServer`, handling `req`/`res`, reading `req.method` and `req.url`, manually setting headers and status codes, manual routing with `if/else` on `req.url`. |
| 0:50–1:10 | "This is what Express does" | Side-by-side: the same 3 routes in raw `http` vs. a 10-line Express equivalent (conceptual preview — Express itself arrives in Wk7). |
| 1:10–1:20 | Break | — |
| 1:20–1:40 | EventEmitter | Build a small custom emitter (e.g., an `orderProcessor` that emits `'received'`, `'shipped'`) — ties directly into how `http.Server` itself is an EventEmitter. |
| 1:40–2:15 | Streams | Readable/Writable/Transform explained with a diagram. Live-code `fs.createReadStream(...).pipe(fs.createWriteStream(...))`, then a `Transform` stream that uppercases text on the fly. Revisit the Wk3 large-file problem and fix it with streams. |
| 2:15–end | Lab kickoff | — |

### Hands-On Lab: Streaming Log Server

**Scenario:** Students combine everything so far into a small raw-HTTP server that streams a log file to the client instead of loading it into memory.

**Requirements:**
1. Build an `http` server (no Express) with at least two routes:
   - `GET /summary` → returns the JSON stats computed in Weeks 2–3 (lines, errors, warnings)
   - `GET /raw` → streams the raw log file contents directly to the response using `fs.createReadStream(...).pipe(res)`
2. Use a custom `EventEmitter` to log a `'request'` event (with method + URL) every time a request comes in, separate from the response logic itself.
3. Test `/raw` against the large log file from the Wk3 homework and confirm memory usage stays flat (use `process.memoryUsage()` to print before/after).
4. Handle a `404` for any unknown route with an appropriate status code and JSON error body.

**Deliverable:** A new `server.js` (can live in the same repo as Weeks 2–3) plus a short note in the README comparing memory usage: loading the whole file vs. streaming it.

**Assessment criteria:**
- Working raw `http` server with correct routing (5 pts)
- Correct use of streams for `/raw` (5 pts)
- Custom EventEmitter used meaningfully (5 pts)
- 404 handling and clean JSON error responses (5 pts)

### Homework / Bridge to Week 5
Ask students to try running their server on a classmate's machine. Most will hit friction: "works on my machine" — wrong Node version, missing env var, port already in use. This becomes the motivating problem for Docker in Week 5.

---

## Week 5 — Docker Fundamentals I: Your First Container

### Learning Objectives
By the end of this session, students will be able to:
1. Explain the difference between an image and a container, and between a container and a virtual machine.
2. Write a basic `Dockerfile` for a Node.js application.
3. Build an image with `docker build` and run it with `docker run`, including port mapping (`-p`).
4. Use a `.dockerignore` file and explain why `node_modules` shouldn't be copied into the image.
5. Explain image layers and caching, and order Dockerfile instructions to take advantage of layer caching.

### Lecture Outline

| Time | Segment | Content |
|---|---|---|
| 0:00–0:15 | Homework debrief | Revisit the "works on my machine" friction from Wk4. Frame Docker as: "what if we shipped the machine, not just the code?" |
| 0:15–0:35 | Images vs. containers vs. VMs | Analogy-driven: an image is a recipe/blueprint, a container is a running instance of it. Contrast with VMs (full OS) vs. containers (shared kernel, isolated process) — a diagram works well here. |
| 0:35–1:05 | Anatomy of a Dockerfile | `FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `CMD`. Live-write a Dockerfile for the Wk4 server line by line, explaining each instruction as it's added. |
| 1:05–1:15 | Break | — |
| 1:15–1:40 | Build & run | `docker build -t <name> .`, `docker run -p 3000:3000 <name>`, `docker ps`, `docker logs`, `docker stop`. Show the image actually working identically on the instructor's machine and a student's machine. |
| 1:40–2:05 | Layers, caching, `.dockerignore` | Why `COPY package*.json` + `RUN npm install` *before* `COPY . .` speeds up rebuilds. Why `node_modules` and `.git` belong in `.dockerignore`. |
| 2:05–2:20 | Preview of Week 6 | Explain the Prelim milestone: containerize their own Wk4 server end-to-end. |
| 2:20–end | Lab kickoff | — |

### Hands-On Lab: Containerize the Wk4 Streaming Server

**Scenario:** Students take the raw-HTTP streaming server from Week 4 and package it as a Docker image.

**Requirements:**
1. Write a `Dockerfile` using an official Node base image (e.g., `node:20-alpine`).
2. Order instructions to maximize layer-caching (dependencies copied/installed before the rest of the source).
3. Add a `.dockerignore` excluding `node_modules`, `.git`, and any local `.env` file.
4. Successfully `docker build` the image and `docker run` it with the correct port mapping, hitting both `/summary` and `/raw` from the browser or `curl`.
5. Document the exact `docker build` and `docker run` commands in the README so a classmate can run it with zero local setup beyond having Docker installed.

**Deliverable:** `Dockerfile`, `.dockerignore`, and an updated `README.md` with run instructions, added to the same repo.

**Assessment criteria:**
- Dockerfile builds successfully without errors (5 pts)
- Correct instruction ordering for caching (5 pts)
- `.dockerignore` present and correct (5 pts)
- Container runs and both routes work as expected (5 pts)

### Homework / Bridge to Week 6
Ask students to send their Dockerfile + repo link to a classmate and have that classmate run it with only `docker build` + `docker run` — no other setup. Bring any friction points to Week 6 as troubleshooting material before the milestone submission.

---

## Week 6 — Prelim Milestone: "Hello Container"

This week is primarily a work/assessment session rather than new lecture content — use it for troubleshooting, peer testing, and submission.

### Milestone Requirements
Students submit a single repository containing:
1. A working CLI or raw-HTTP tool (built across Weeks 2–4) — no Express, no frameworks.
2. A `Dockerfile` that successfully builds the tool into an image.
3. A `.dockerignore` file excluding unnecessary files.
4. A `README.md` with exact `docker build` / `docker run` commands, such that **any classmate or the instructor can run the tool with zero local setup beyond Docker itself.**
5. Evidence of error handling and environment-variable-based configuration (from Week 3).

### Suggested In-Class Flow
| Time | Activity |
|---|---|
| 0:00–0:20 | Open troubleshooting clinic — pairs debug any remaining Docker build issues from the Wk5 homework. |
| 0:20–1:30 | Peer testing: each student pulls a classmate's repo and runs it using only the README instructions. They report back on any friction ("had to change the port," "missing `.env.example`," etc.). |
| 1:30–2:00 | Fixes based on peer feedback. |
| 2:00–end | Final submission + brief individual check-in with instructor: each student explains, in their own words, what an image is, what a container is, and why they containerized their tool. |

### Assessment Rubric (Prelim Capstone)
- Tool functions correctly on its own (10 pts)
- Dockerfile builds and runs without instructor intervention (10 pts)
- Peer was able to run it using only the README (10 pts)
- Student can verbally explain image vs. container vs. VM (5 pts)
- Evidence of Week 2–3 concepts (async/await, error handling, env vars) in the final code (10 pts)

**Total: 45 pts**

### Bridge to Midterm
Close the session by connecting forward: "Everything you just did manually — writing routes by hand, wiring up one container — Express and Docker Compose exist to make less painful at scale. Midterm is where we stop reinventing wheels and start using the tools built for this."
