Since you're already anchoring this to the two decks (MongoDB+Express, then Node.js), here's how I'd lay out the full 3-term roadmap on top of them — built for a typical PH-style term system (Prelim → Midterm → Finals), each roughly 5–6 weeks.

## 🟢 Prelim — Node.js Foundations (weeks 1–6)
*Goal: comfortable writing and reasoning about Node on its own, before frameworks.*

- **Wk 1–2:** JS refresher for Node context (async/await, closures, modules) → CommonJS vs ESM, npm & package.json *(covered in your Node.js deck)*
- **Wk 3:** Event loop deep dive, `process`, environment variables, error handling patterns (`try/catch`, `uncaughtException`)
- **Wk 4:** Core modules in practice — `fs`, `path`, `os`, streams (build a small CLI tool, e.g., a file-renamer or log parser)
- **Wk 5:** `http` module from scratch, then EventEmitter patterns
- **Wk 6 (Prelim exam/output):** A working CLI or raw-HTTP mini tool — no framework — to prove they understand what Express abstracts away

## 🟡 Midterm — APIs & Bridging to the Frontend (weeks 7–12)
*Goal: build real, securable REST APIs and understand why the frontend needs special handling.*

- **Wk 7:** Express deep dive — routing, middleware, error handling *(covered in your MongoDB+Express deck)*
- **Wk 8:** MongoDB + Mongoose — schemas, CRUD, relationships/population *(also covered)*
- **Wk 9:** REST API design conventions — status codes, pagination, filtering, versioning
- **Wk 10:** Authentication & authorization — JWT, hashed passwords (`bcrypt`), protected routes, role-based access
- **Wk 11:** CORS explained properly, API documentation basics (Swagger/OpenAPI), testing routes with Postman/`supertest`
- **Wk 12 (Midterm exam/output):** A fully authenticated REST API (e.g., a task manager or blog backend) with protected CRUD routes

## 🔴 Finals — React & Full-Stack Integration (weeks 13–18)
*Goal: connect everything into one deployed full-stack application.*

- **Wk 13:** React fundamentals — JSX, components, props/state, `useState`/`useEffect`
- **Wk 14:** Data fetching from their own API — `fetch`/`axios`, loading/error states, intro to React Query/TanStack Query
- **Wk 15:** Forms, controlled inputs, React Router for multi-page navigation
- **Wk 16:** Full-stack auth flow — login/register UI wired to the JWT API, protected frontend routes
- **Wk 17:** Deployment — React build served by Express vs. split deploy (Vercel + Render/Railway), env config for prod
- **Wk 18 (Finals/capstone):** A complete full-stack app — React frontend + Express/Node API + MongoDB — with auth, CRUD, and a live deployment link

**Throughline:** every term's output becomes the next term's foundation — the Prelim CLI tool teaches the runtime, the Midterm API becomes the backend for the Finals capstone. If it's useful, I can turn any one term into its own slide deck like the two you already have — just tell me which one to build first.