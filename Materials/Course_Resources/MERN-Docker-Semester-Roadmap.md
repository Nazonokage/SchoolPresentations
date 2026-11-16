# MERN + Docker Semester Roadmap
### 18-Week Curriculum — Prelim / Midterm / Finals

**Starting point:** Week 1 is complete (Node.js internals: V8, event loop, npm, core modules — per your existing deck).
**End goal:** Students deploy a fully containerized MERN application (React + Express + Node + MongoDB, orchestrated with Docker Compose).

Docker is **not** bolted on as a final "extra topic." It's introduced in three deliberate passes, each time only as complex as what the students actually have to containerize:

| Pass | When | Why then |
|---|---|---|
| **1. Single container** | Week 5 (end of Prelim) | They already have a small Node/HTTP app — enough to justify "why put this in a box?" without Express/Mongo complexity muddying the concept. |
| **2. Multi-container (Compose)** | Week 11 (end of Midterm) | They now have Express *and* MongoDB — two services that genuinely need to talk to each other, which is the whole reason Compose exists. |
| **3. Production/multi-stage** | Week 17 (end of Finals) | They have a React frontend to build and serve — the point where multi-stage builds, Nginx, and environment-based config actually matter. |

---

## 🟢 PRELIM — Node.js Foundations + Docker Intro (Weeks 1–6)
*Goal: comfortable writing and reasoning about Node on its own, then learning what a container is and why it exists.*

- **Wk 1 (✅ done):** Node.js internals — V8, event loop, npm, core modules, installation, `package.json`
- **Wk 2:** Core modules in depth — `fs`, `path`, streams; async patterns (callbacks → promises → async/await); npm scripts & semver *(see detailed plan below)*
- **Wk 3:** Event loop deep dive, `process`, environment variables, error-handling patterns (`try/catch`, `uncaughtException`, custom error classes)
- **Wk 4:** `http` module from scratch, EventEmitter patterns — build a raw HTTP server with no framework
- **Wk 5:** **Docker Fundamentals I** — images vs. containers, the Dockerfile, `docker build` / `docker run`, `.dockerignore`, layers & caching. Lab: containerize the Wk4 HTTP server.
- **Wk 6 (Prelim output):** Milestone — *"Hello Container"*: a working CLI or raw-HTTP tool, packaged with its own Dockerfile, that anyone can run with a single `docker run` command — no local Node install required.

## 🟡 MIDTERM — APIs, MongoDB & Docker Compose (Weeks 7–12)
*Goal: build real, securable REST APIs, persist data, and orchestrate multi-service apps.*

- **Wk 7:** Express deep dive — routing, middleware, error handling *(your existing deck)*
- **Wk 8:** MongoDB + Mongoose — schemas, CRUD, relationships/population *(your existing deck)*
- **Wk 9:** REST API design — status codes, pagination, filtering, versioning
- **Wk 10:** Authentication & authorization — JWT, `bcrypt`, protected routes, role-based access
- **Wk 11:** **Docker Compose** — multi-container setups, `docker-compose.yml`, named volumes (persisting Mongo data), custom networks, service-to-service DNS (`mongodb://mongo:27017` instead of `localhost`), `.env` files for secrets/config
- **Wk 12 (Midterm output):** Milestone — a fully authenticated REST API (task manager / blog backend) that spins up completely via `docker-compose up` — API container + MongoDB container, no manual setup steps.

## 🔴 FINALS — React, Full-Stack Integration & Production Docker (Weeks 13–18)
*Goal: connect everything into one deployed, containerized full-stack application.*

- **Wk 13:** React fundamentals — JSX, components, props/state, `useState`/`useEffect`
- **Wk 14:** Data fetching from their own API — `fetch`/`axios`, loading/error states, intro to TanStack Query
- **Wk 15:** Forms, controlled inputs, React Router for multi-page navigation
- **Wk 16:** Full-stack auth flow — login/register UI wired to the JWT API, protected frontend routes
- **Wk 17:** **Docker for Production** — multi-stage builds (build React → serve via Nginx), a 3–4 service `docker-compose.yml` (client, api, mongo, optional nginx reverse proxy), environment config for prod vs. dev, image size/optimization basics
- **Wk 18 (Finals/Capstone):** A complete full-stack app — React + Express/Node API + MongoDB — fully containerized, orchestrated with one `docker-compose.yml`, with a short deployment write-up (what changes for a real host like Render/Railway/a VPS).

**Throughline:** each term's output becomes the next term's foundation *and* each term's Docker pass builds on the last — single container → multi-container → production-grade. By Week 18, "containerize it" is a reflex, not a special topic.

---

📄 **Detailed week-by-week lesson plans for the Prelim term (Weeks 2–6) live in a separate file: `PRELIMS.md`** — learning objectives, lecture outlines, and hands-on labs for each week, including the two Docker Fundamentals sessions and the Week 6 capstone milestone.
