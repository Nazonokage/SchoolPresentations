# MIDTERMS — APIs, MongoDB & Docker Compose
### Detailed Lesson Plans: Weeks 7–12

**Term goal:** By the end of Midterm, students can build a real, securable REST API backed by MongoDB, and orchestrate it — API + database — as a multi-container app with Docker Compose, no manual setup steps.

**Where this picks up:** Prelim ended with students able to write raw Node (no framework), containerize a single service, and explain images vs. containers. They've felt the pain of hand-rolling routing (Wk4) and hand-running one container (Wk5–6). Midterm exists to remove both pains: Express replaces manual routing, Compose replaces manual multi-container wiring.

**Term output (Week 12):** A fully authenticated REST API (task manager / blog backend) — API container + MongoDB container — that spins up completely via `docker-compose up`, with zero manual setup steps.

---

## Week 7 — Express Deep Dive: Routing, Middleware, Error Handling
*(existing deck — outline below for continuity/reference only)*

### Learning Objectives
By the end of this session, students will be able to:
1. Explain what Express abstracts away versus the raw `http` server from Week 4.
2. Build routes using Express Router, including route params and query strings.
3. Write and mount custom middleware, and explain middleware execution order (`next()`).
4. Centralize error handling with an Express error-handling middleware (4-arg signature).
5. Structure an Express project (routes / controllers / middleware folders) instead of one giant file.

### Lecture Outline

| Time | Segment | Content |
|---|---|---|
| 0:00–0:15 | Recap & bridge | Pull up the Wk4 raw-`http` server side-by-side with its Express equivalent from Wk4's "this is what Express does" preview. Ask: "What did we get for free?" |
| 0:15–0:45 | Routing | `app.get/post/put/delete`, route params (`:id`), query strings, `express.Router()` for modular route files. |
| 0:45–1:10 | Middleware | The request-response cycle, `next()`, built-in (`express.json()`), third-party (`morgan`), and custom middleware (e.g., a request logger). Order matters — demonstrate breaking it on purpose. |
| 1:10–1:20 | Break | — |
| 1:20–1:50 | Project structure | Splitting a monolithic `server.js` into `routes/`, `controllers/`, `middleware/`. Why this matters once MongoDB and auth get added in coming weeks. |
| 1:50–2:15 | Centralized error handling | The 4-arg error middleware, `next(err)` pattern, custom `ApiError` class (ties back to Wk3's custom `Error` subclasses). |
| 2:15–end | Lab kickoff | — |

### Hands-On Lab: Rebuild the Log Server in Express

**Scenario:** Students port the Week 4 raw-HTTP log server to Express, restructured into a proper project.

**Requirements:**
1. Recreate `/summary` and `/raw` routes using Express Router, mounted under `/api/logs`.
2. Move route handlers into a `controllers/logsController.js` — routes file only wires paths to controller functions.
3. Add a custom logging middleware that records method, URL, and timestamp for every request.
4. Add a centralized error-handling middleware; all thrown/`next(err)`-ed errors return consistent JSON: `{ error: { message, status } }`.
5. Return proper status codes: `404` for unknown routes, `400` for a missing/invalid file param.

**Deliverable:** Restructured repo (`routes/`, `controllers/`, `middleware/`) with a README noting what changed from the raw-`http` version.

**Assessment criteria:**
- Correct Router usage and project structure (5 pts)
- Custom middleware works and is properly ordered (5 pts)
- Centralized error handling returns consistent JSON (5 pts)
- Correct status codes across routes (5 pts)

### Homework / Bridge to Week 8
Ask students to list every place their app currently "fakes" persistent data (in-memory arrays, reading from a flat file). Bring that list to Week 8 — it becomes the mapping exercise from "fake storage" to real MongoDB collections.

---

## Week 8 — MongoDB & Mongoose: Schemas, CRUD, Relationships
*(existing deck — outline below for continuity/reference only)*

### Learning Objectives
By the end of this session, students will be able to:
1. Explain documents/collections vs. rows/tables, and when a document database fits better than relational.
2. Define a Mongoose schema and model with validation rules.
3. Perform full CRUD (`create`, `find`, `findById`, `findByIdAndUpdate`, `findByIdAndDelete`) from Express routes.
4. Model one-to-many relationships with references (`ObjectId` + `ref`) and use `.populate()`.
5. Connect an Express app to MongoDB using a connection module, with graceful handling of a failed connection.

### Lecture Outline

| Time | Segment | Content |
|---|---|---|
| 0:00–0:15 | Homework debrief | Walk through the "fake storage" lists — map each one to a future collection. |
| 0:15–0:40 | Document vs. relational | JSON-shaped documents, collections, embedding vs. referencing at a conceptual level. |
| 0:40–1:05 | Connecting Mongoose | `mongoose.connect()`, connection events (`open`, `error`), a dedicated `db.js` connection module, `process.env.MONGO_URI` (ties back to Wk3 env vars). |
| 1:05–1:15 | Break | — |
| 1:15–1:45 | Schemas & models | `required`, `min/max`, `enum`, `default`, custom validators. Live-build a `Task` schema. |
| 1:45–2:10 | CRUD in Express | Wire schema to routes/controllers: `POST /tasks`, `GET /tasks`, `GET /tasks/:id`, `PUT /tasks/:id`, `DELETE /tasks/:id`. |
| 2:10–2:25 | Relationships | Add a `User` reference on `Task` (`ref: 'User'`), demonstrate `.populate('owner')`. |
| 2:25–end | Lab kickoff | — |

### Hands-On Lab: Task Manager API (v1)

**Scenario:** Students build the core of the term's milestone project — a task manager REST API with real persistence.

**Requirements:**
1. Two Mongoose models: `User` (name, email) and `Task` (title, description, completed, `owner: ObjectId ref User`).
2. Full CRUD routes for `Task`, all backed by MongoDB (no in-memory arrays remaining).
3. `GET /tasks/:id` uses `.populate('owner')` to return owner details inline.
4. Schema-level validation (e.g., `title` required, `completed` defaults to `false`) — verify it rejects a bad payload with a `400` and readable message.
5. Connection module handles a DB-down scenario gracefully (log a clear error, don't crash silently).

**Deliverable:** Updated Express repo with `models/`, MongoDB connected via a local install or MongoDB Atlas free tier, and a Postman/Thunder Client collection (or `.http` file) demonstrating all CRUD operations.

**Assessment criteria:**
- Correct schema design with validation (5 pts)
- Full working CRUD against real MongoDB (5 pts)
- Relationship + `.populate()` working correctly (5 pts)
- Graceful handling of connection errors (5 pts)

### Homework / Bridge to Week 9
Ask students to try fetching `/tasks` once they have 50+ seeded documents and notice there's no way to page through or filter results — everything comes back in one giant array. Bring that observation to Week 9.

---

## Week 9 — REST API Design: Status Codes, Pagination, Filtering, Versioning

### Learning Objectives
By the end of this session, students will be able to:
1. Apply the correct HTTP status code for each outcome (200/201/204/400/401/403/404/409/500) rather than defaulting to 200/500 for everything.
2. Implement pagination on a list endpoint using query params (`page`, `limit`) or cursor-based pagination.
3. Implement filtering and sorting via query strings (`?completed=true&sort=-createdAt`).
4. Explain API versioning strategies (URL-based `/api/v1/...` vs. header-based) and implement URL-based versioning.
5. Design consistent response envelopes (`{ data, meta }` for lists; `{ data }` for single resources; `{ error }` for failures).

### Lecture Outline

| Time | Segment | Content |
|---|---|---|
| 0:00–0:15 | Homework debrief | Revisit the "one giant array" problem from Wk8. Frame today as "designing an API someone else can actually use." |
| 0:15–0:45 | Status codes, done right | Walk the full table students should know: 200 vs 201 vs 204, 400 vs 422, 401 vs 403, 404 vs 409, 500. Live examples for each from the Task API. |
| 0:45–1:10 | Response envelopes | Why consistent shapes matter for frontend consumers (foreshadowing Wk14's `fetch`/`axios` work). Refactor existing routes to a shared envelope. |
| 1:10–1:20 | Break | — |
| 1:20–1:45 | Pagination | `?page=2&limit=10` implemented with `.skip()`/`.limit()` in Mongoose; return `meta: { total, page, pages }`. Briefly contrast with cursor-based pagination and when it's preferred (large, frequently-changing datasets). |
| 1:45–2:10 | Filtering & sorting | Building a dynamic Mongoose query object from allowed query params; `sort=-createdAt` parsing. Guard against arbitrary/unsafe fields being filterable. |
| 2:10–2:25 | Versioning | `/api/v1/tasks` via a versioned router mount; discuss why breaking changes need a new version instead of mutating `v1` in place. |
| 2:25–end | Lab kickoff | — |

### Hands-On Lab: Task Manager API (v2 — Query Power)

**Scenario:** Students harden the Task Manager API's list endpoint into something production-usable.

**Requirements:**
1. Mount all existing routes under `/api/v1/`.
2. `GET /api/v1/tasks` supports `page`, `limit` (default sensible values), and returns `{ data: [...], meta: { total, page, pages } }`.
3. Support filtering by `completed` and `owner`, and sorting by `createdAt` or `title` (ascending/descending via `-` prefix).
4. Audit every existing route and correct status codes: `201` on create, `204` on delete, `404` when an `:id` isn't found, `400` on validation failure.
5. Add a `409 Conflict` case somewhere meaningful (e.g., duplicate task title per owner, if you add a uniqueness constraint).

**Deliverable:** Updated repo with a README section documenting every endpoint, its query params, and example request/response pairs.

**Assessment criteria:**
- Pagination works correctly with accurate `meta` (5 pts)
- Filtering and sorting work and are safely scoped (5 pts)
- Status codes audited and correct across all routes (5 pts)
- Versioned route structure in place (5 pts)

### Homework / Bridge to Week 10
Ask students: "Right now, anyone can `DELETE` anyone else's tasks. What's stopping them?" (Nothing.) Have them write down, in plain English, what a login system would need to prevent this. Bring it to Week 10.

---

## Week 10 — Authentication & Authorization: JWT, bcrypt, Protected Routes, Roles

### Learning Objectives
By the end of this session, students will be able to:
1. Explain the difference between authentication (who you are) and authorization (what you're allowed to do).
2. Hash and compare passwords securely using `bcrypt` — never store plaintext passwords.
3. Issue and verify JSON Web Tokens (JWT) for stateless authentication.
4. Write Express middleware that protects routes by verifying a JWT and attaching the authenticated user to `req`.
5. Implement basic role-based access control (e.g., `user` vs. `admin`) and apply it to specific routes.

### Lecture Outline

| Time | Segment | Content |
|---|---|---|
| 0:00–0:15 | Homework debrief | Review the "what's stopping them" answers. Frame today as building exactly that missing layer. |
| 0:15–0:35 | AuthN vs. AuthZ | Clear conceptual split with everyday analogies (ID card vs. permission slip). |
| 0:35–1:00 | Password hashing | Why plaintext storage is unacceptable; `bcrypt.hash`/`bcrypt.compare`; salt rounds trade-off (security vs. speed). Update the `User` model with a `password` field and pre-save hashing hook. |
| 1:00–1:10 | Break | — |
| 1:10–1:40 | JWT | What's inside a JWT (header/payload/signature), signing with a secret (env var — ties back to Wk3), `jwt.sign`/`jwt.verify`, expiry (`expiresIn`). Build `POST /auth/register` and `POST /auth/login`. |
| 1:40–2:05 | Protecting routes | An `authMiddleware` that reads the `Authorization: Bearer <token>` header, verifies it, attaches `req.user`, and calls `next()` — or returns `401`. Apply it to task routes so a task can only be edited/deleted by its owner. |
| 2:05–2:25 | Roles | Add a `role` field to `User` (`user`/`admin`). A `requireRole('admin')` middleware for an admin-only route (e.g., `DELETE /api/v1/users/:id`). |
| 2:25–end | Lab kickoff | — |

### Hands-On Lab: Task Manager API (v3 — Auth-Locked)

**Scenario:** Students lock down the Task Manager API so tasks belong to authenticated owners and only the right people can touch them.

**Requirements:**
1. `POST /auth/register` (hashes password, creates user) and `POST /auth/login` (verifies password, returns a JWT) implemented and tested.
2. `authMiddleware` protecting all `/api/v1/tasks` routes — no valid token, no access (`401`).
3. Ownership check: a user can only `PUT`/`DELETE` their own tasks (`403` if they try someone else's).
4. At least one `admin`-only route (e.g., list all users, or force-delete any task) protected by `requireRole('admin')`.
5. JWT secret and expiry pulled from environment variables, never hardcoded.

**Deliverable:** Updated repo with an updated Postman/Thunder Client collection showing register → login → authenticated request → ownership-denied request (403) → admin route.

**Assessment criteria:**
- Passwords hashed correctly, never stored/returned in plaintext (5 pts)
- Login/register flow works end-to-end and returns a valid JWT (5 pts)
- Protected routes correctly reject missing/invalid tokens (5 pts)
- Ownership and role-based checks work as specified (5 pts)

### Homework / Bridge to Week 11
Ask students to try running their API on a classmate's machine — same friction as the Wk4→Wk5 bridge, but now with an extra dependency: MongoDB has to be running too, with matching connection strings and env vars. Bring the friction list to Week 11.

---

## Week 11 — Docker Compose: Orchestrating API + MongoDB

### Learning Objectives
By the end of this session, students will be able to:
1. Explain why a single Dockerfile isn't enough once an app depends on another service (MongoDB), and what Compose adds on top of plain Docker.
2. Write a `docker-compose.yml` defining two services (`api`, `mongo`) with a shared custom network.
3. Use named volumes to persist MongoDB data across container restarts.
4. Explain and use Docker's internal service-discovery DNS (`mongodb://mongo:27017/...` instead of `localhost`).
5. Manage secrets/config for multi-service apps via `.env` files referenced in `docker-compose.yml`.
6. Use core Compose commands: `docker-compose up`, `up -d`, `down`, `down -v`, `logs -f`, `ps`.

### Lecture Outline

| Time | Segment | Content |
|---|---|---|
| 0:00–0:15 | Homework debrief | Revisit the "extra dependency" friction from Wk10. Frame Compose as: "what if we described the *whole system*, not just one container?" |
| 0:15–0:40 | Why Compose | Single Dockerfile = one image. Real apps = multiple services that need to talk to each other and start in the right way. Compose as a declarative multi-container spec. |
| 0:40–1:10 | Anatomy of `docker-compose.yml` | `services:`, `build:` vs `image:`, `ports:`, `environment:`/`env_file:`, `depends_on:`. Live-write a two-service file for the Task Manager API + Mongo. |
| 1:10–1:20 | Break | — |
| 1:20–1:45 | Networks & service DNS | Compose's default network; containers reach each other by service name, not `localhost`. Live-demo `mongodb://mongo:27017/taskdb` actually resolving inside the `api` container. |
| 1:45–2:05 | Volumes | Named volumes (`mongo_data:/data/db`) vs. bind mounts; why Mongo's data must survive `docker-compose down`. Demonstrate: stop/remove containers, bring them back up, data is still there — then show `down -v` wiping it. |
| 2:05–2:20 | `.env` with Compose | A single `.env` at the project root, referenced by `env_file:` in each service, avoiding duplicated secrets across service definitions. |
| 2:20–end | Lab kickoff | — |

### Hands-On Lab: Compose-ify the Task Manager API

**Scenario:** Students take the Wk10 auth-locked Task Manager API and orchestrate it with MongoDB via Docker Compose — one command, zero manual setup.

**Requirements:**
1. A `Dockerfile` for the API (building on Prelim Wk5 patterns — proper layer caching, `.dockerignore`).
2. A `docker-compose.yml` defining `api` and `mongo` services on a shared custom network, with `depends_on`.
3. A named volume for MongoDB data (`mongo_data:/data/db`), verified to persist across `docker-compose down` (without `-v`) and back `up`.
4. The API connects to Mongo via the service name (`mongodb://mongo:27017/taskdb`), **not** `localhost` — verified working inside the container, not just on the host.
5. A single root `.env` file (with an `.env.example` committed instead of the real `.env`) supplying `MONGO_URI`, `JWT_SECRET`, `PORT`.
6. Entire stack starts with `docker-compose up` — no manual `npm install`, no manually starting Mongo, no local `.env` setup beyond copying `.env.example`.

**Deliverable:** Repo with `Dockerfile`, `docker-compose.yml`, `.env.example`, `.dockerignore`, and a README documenting the exact one-command startup and a note on how to reset data (`docker-compose down -v`).

**Assessment criteria:**
- `docker-compose up` brings up both services successfully with no manual steps (5 pts)
- Service-to-service DNS used correctly (no hardcoded `localhost`) (5 pts)
- Named volume correctly persists Mongo data across restarts (5 pts)
- `.env` handled correctly (secrets not committed, `.env.example` present) (5 pts)

### Homework / Bridge to Week 12
Ask students to send their repo to a classmate with the instruction: "clone this and run one command." Note every question the classmate has to ask before it works — that friction list becomes the final polish checklist going into the Week 12 milestone.

---

## Week 12 — Midterm Milestone: Authenticated, Composed REST API

This week is primarily a work/assessment session rather than new lecture content — use it for troubleshooting, peer testing, and submission.

### Milestone Requirements
Students submit a single repository containing:
1. A fully authenticated REST API (task manager, blog backend, or an approved variant) with complete CRUD, built across Weeks 7–10.
2. Pagination, filtering, sorting, and proper status codes/response envelopes (Week 9).
3. JWT-based auth with hashed passwords, protected routes, ownership checks, and at least one role-gated route (Week 10).
4. A `Dockerfile` for the API and a `docker-compose.yml` orchestrating `api` + `mongo` with a named volume and custom network (Week 11).
5. A `README.md` with exact one-command startup instructions (`docker-compose up`) such that **any classmate or the instructor can run the full stack with zero local setup beyond Docker itself.**

### Suggested In-Class Flow
| Time | Activity |
|---|---|
| 0:00–0:20 | Open troubleshooting clinic — pairs debug any remaining Compose/auth issues from the Wk11 homework. |
| 0:20–1:30 | Peer testing: each student pulls a classmate's repo and runs it using only `docker-compose up` and the README. They exercise the full flow — register, login, protected CRUD, an intentionally-denied request — and report friction. |
| 1:30–2:00 | Fixes based on peer feedback. |
| 2:00–end | Final submission + brief individual check-in with instructor: each student explains, in their own words, why Mongo needed its own service/container, and what `depends_on` does and does not guarantee (it doesn't wait for Mongo to be *ready*, just *started* — a good moment to mention retry/backoff connection logic if any students discovered this the hard way). |

### Assessment Rubric (Midterm Capstone)
- API functions correctly with full CRUD against MongoDB (10 pts)
- Auth (register/login/JWT/protected routes/ownership) works correctly (10 pts)
- Pagination/filtering/sorting/status codes implemented per Week 9 spec (5 pts)
- `docker-compose up` brings up the full stack with zero manual intervention (10 pts)
- Peer was able to run it using only the README (5 pts)
- Student can verbally explain the role of `depends_on`, named volumes, and service DNS (5 pts)

**Total: 45 pts**

### Bridge to Finals
Close the session by connecting forward: "You've built the back half of a real app and containerized it properly. Finals is where a real frontend shows up — React talking to this exact API — and where Docker grows up one more time: building the frontend, serving it efficiently, and running client + api + mongo together like a real deployed product."
