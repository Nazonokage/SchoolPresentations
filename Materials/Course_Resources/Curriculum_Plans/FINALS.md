# FINALS — React, Full-Stack Integration & Production Docker
### Detailed Lesson Plans: Weeks 13–18

**Term goal:** By the end of Finals, students can build a React frontend that talks to their own authenticated API, wire up a complete full-stack auth flow, and ship the entire application — client, API, database, optional reverse proxy — as a production-grade, multi-stage, containerized system.

**Where this picks up:** Midterm ended with a fully authenticated REST API, containerized with Compose (API + Mongo, two services). Finals adds the third piece — a real UI — and closes the loop: build it, connect it, protect it, then package it the way a real deployment would look.

**Term output (Week 18):** A complete full-stack app — React + Express/Node API + MongoDB — fully containerized, orchestrated with a single `docker-compose.yml`, with a short write-up on what changes to actually deploy it (Render/Railway/a VPS).

---

## Week 13 — React Fundamentals: JSX, Components, Props/State, Hooks

### Learning Objectives
By the end of this session, students will be able to:
1. Explain what JSX compiles to and why React uses a component model instead of manually manipulating the DOM (contrast with the raw `http`/DOM-adjacent thinking from Prelim).
2. Build functional components and compose them via props.
3. Manage local component state with `useState`.
4. Use `useEffect` correctly, including the dependency array and cleanup functions.
5. Understand the React render cycle well enough to explain an unnecessary re-render.

### Lecture Outline

| Time | Segment | Content |
|---|---|---|
| 0:00–0:15 | Recap & bridge | "You've built the engine (API). Today we start on the dashboard (UI)." Quick show of the Midterm API's Postman responses — "this is the data React will render." |
| 0:15–0:45 | JSX & components | JSX-to-`React.createElement` mental model; functional components; composing a small component tree (`App` → `TaskList` → `TaskItem`). |
| 0:45–1:10 | Props | Passing data down, prop drilling as a concept (not yet a problem to solve — just name it for later). |
| 1:10–1:20 | Break | — |
| 1:20–1:50 | `useState` | Local state, updater functions, why state shouldn't be mutated directly. Build a toggle-completed checkbox on a static task list. |
| 1:50–2:15 | `useEffect` | Dependency array behavior (`[]` vs `[dep]` vs none), cleanup functions, a first (mocked, no real fetch yet) "on mount" example. |
| 2:15–end | Lab kickoff | — |

### Hands-On Lab: Static Task Dashboard

**Scenario:** Students build the UI shell for the term's milestone — a task dashboard — using hardcoded/mock data (no API calls yet; that's Week 14).

**Requirements:**
1. Scaffold a React app (Vite recommended) named appropriately for the milestone project.
2. Component tree: `App` → `TaskList` → `TaskItem`, with a hardcoded array of mock tasks passed down as props.
3. Each `TaskItem` has a "completed" checkbox wired to local `useState`, toggling a strikethrough style — purely client-side for now.
4. A `useEffect` that logs to the console on mount and cleans up on unmount (demonstrated by conditionally rendering `TaskList`).
5. Basic component-level styling (CSS modules, plain CSS, or a utility framework — instructor's call).

**Deliverable:** A new frontend repo/folder (`client/`) with a working `npm run dev` and a README describing the component tree.

**Assessment criteria:**
- Correct component composition and prop passing (5 pts)
- `useState` correctly toggles UI without mutating state directly (5 pts)
- `useEffect` used correctly, including cleanup (5 pts)
- Clean, working `npm run dev` with no console errors (5 pts)

### Homework / Bridge to Week 14
Ask students to try replacing the mock array with "what if this came from a server instead" — sketch (on paper or in a comment) where a fetch call would go and what loading/error UI would need to exist. Bring the sketch to Week 14.

---

## Week 14 — Data Fetching: fetch/axios, Loading & Error States, TanStack Query Intro

### Learning Objectives
By the end of this session, students will be able to:
1. Fetch data from their own Express API using both native `fetch` and `axios`, and explain the practical differences.
2. Model loading, success, and error states explicitly in the UI instead of assuming the happy path.
3. Attach a JWT to outgoing requests (`Authorization: Bearer <token>`) from the frontend.
4. Explain what problem TanStack Query solves relative to manual `useEffect`+`useState` fetching (caching, refetching, avoiding race conditions).
5. Wire up basic TanStack Query (`useQuery`) for a real GET endpoint.

### Lecture Outline

| Time | Segment | Content |
|---|---|---|
| 0:00–0:15 | Homework debrief | Review sketches from Wk13. Frame today as making that sketch real. |
| 0:15–0:40 | CORS reality check | Students will hit a CORS error the first time they call their API from `localhost:5173`. Explain what CORS is and add the `cors` middleware to the Express API (bridges back to Midterm Wk7 middleware). |
| 0:40–1:05 | `fetch` vs. `axios` | Same GET request both ways; interceptors as an axios advantage worth knowing about (used again for attaching JWTs automatically). |
| 1:05–1:15 | Break | — |
| 1:15–1:40 | Loading/error states | Manual pattern: `useState` for `data`, `loading`, `error`; render three distinct UI states. Why "just show the data" breaks the moment the network is slow or down. |
| 1:40–1:55 | Attaching JWT | Reading a token (from state/localStorage for now — proper flow comes Wk16), attaching it via header, hitting a protected route from Midterm Wk10. |
| 1:55–2:20 | TanStack Query | `useQuery` replacing the manual fetch/loading/error dance; automatic caching and refetch-on-focus; brief mention of `useMutation` (used properly in Wk15). |
| 2:20–end | Lab kickoff | — |

### Hands-On Lab: Wire the Dashboard to the Real API

**Scenario:** Students replace the Week 13 mock data with real calls to their Midterm API.

**Requirements:**
1. `cors` middleware added to the Express API, scoped appropriately (not a wide-open `*` in comments — discuss why).
2. `TaskList` fetches real tasks from `GET /api/v1/tasks` using either `axios` or TanStack Query (student's choice, but must justify the choice in the README).
3. Explicit loading, error, and empty (`0 tasks`) states are all visibly different in the UI — demonstrate each by throttling the network and by pointing at a wrong port.
4. A hardcoded/temporary JWT (pasted in from a Postman login) is attached to the request and successfully hits the protected route.
5. Pagination controls (Next/Prev) wired to the Midterm Wk9 `page`/`limit` query params, showing `meta.page` of `meta.pages`.

**Deliverable:** Updated `client/` repo connected to the running API (started separately or via the Wk11 Compose setup), with a short README section on the fetch strategy chosen and why.

**Assessment criteria:**
- CORS correctly configured and explained (5 pts)
- Real data fetched and rendered correctly (5 pts)
- Loading/error/empty states all implemented and visibly distinct (5 pts)
- Pagination controls work against real `meta` data (5 pts)

### Homework / Bridge to Week 15
Ask students to try creating a new task from the UI. There's currently no form for it — just a "what would this need?" thought exercise. Bring notes to Week 15.

---

## Week 15 — Forms, Controlled Inputs, React Router

### Learning Objectives
By the end of this session, students will be able to:
1. Build controlled form inputs bound to component state, and explain controlled vs. uncontrolled inputs.
2. Handle form submission, basic client-side validation, and submission-in-flight UI (disabled button, spinner).
3. Use `useMutation` (TanStack Query) to create/update/delete data and invalidate/refetch the relevant query afterward.
4. Set up React Router for multi-page navigation (`/`, `/tasks/:id`, `/login`, `/register`).
5. Use `useParams` and `useNavigate` to read route params and programmatically redirect after actions (e.g., after creating a task).

### Lecture Outline

| Time | Segment | Content |
|---|---|---|
| 0:00–0:15 | Homework debrief | Review "what would a create-task form need" notes. |
| 0:15–0:45 | Controlled inputs | `value`/`onChange` pattern for text inputs, checkboxes, selects; why React "owns" the input value. |
| 0:45–1:10 | Form submission | `onSubmit`, `e.preventDefault()`, basic validation (required fields, simple format checks) before hitting the API. |
| 1:10–1:20 | Break | — |
| 1:20–1:45 | `useMutation` | POST a new task via `useMutation`, invalidate the tasks query on success so the list refreshes automatically — no manual refetch plumbing. |
| 1:45–2:10 | React Router setup | `createBrowserRouter`/`<Routes>`, layout routes, `<Link>` vs. full page reloads, `useParams` for a task detail page. |
| 2:10–2:25 | `useNavigate` | Redirect to `/tasks/:id` after successful creation; redirect to `/login` as a stub for what's coming in Week 16. |
| 2:25–end | Lab kickoff | — |

### Hands-On Lab: Multi-Page Task Manager

**Scenario:** Students turn the single-page dashboard into a real multi-page app with working create/edit/delete flows.

**Requirements:**
1. React Router configured with at least: `/` (task list), `/tasks/:id` (task detail), `/login`, `/register` (stub pages, functional in Week 16).
2. A controlled "Create Task" form with client-side validation (title required, sensible length limits) submitting via `useMutation` to `POST /api/v1/tasks`.
3. On success, the task list auto-refreshes (query invalidation) and the user is navigated to the new task's detail page.
4. Edit and delete functionality on the detail page, both using `useMutation` with proper query invalidation.
5. A loading/disabled state on the submit button while the mutation is in flight, and a visible error message if it fails (e.g., simulate by stopping the API).

**Deliverable:** Updated `client/` repo with working navigation between all routes and full create/edit/delete flows against the real API.

**Assessment criteria:**
- Controlled form with working validation (5 pts)
- `useMutation` correctly creates/edits/deletes with query invalidation (5 pts)
- React Router navigation works correctly across all routes (5 pts)
- In-flight/error states handled visibly on mutations (5 pts)

### Homework / Bridge to Week 16
Ask students to try visiting `/tasks/:id` for a task that belongs to someone else, using the hardcoded token from Week 14. It'll either fail oddly or "just work" with no real login — both are the wrong experience. Bring observations to Week 16.

---

## Week 16 — Full-Stack Auth Flow: Login/Register UI, Protected Frontend Routes

### Learning Objectives
By the end of this session, students will be able to:
1. Build working login and register forms that call the Midterm auth endpoints and store the returned JWT.
2. Explain the trade-offs of storing a JWT in `localStorage` vs. an httpOnly cookie, and implement one deliberately (not by default/accident).
3. Create a global auth context (`useContext` + `useState`/`useReducer`) so any component can know if a user is logged in.
4. Build a `ProtectedRoute` wrapper that redirects unauthenticated users to `/login`.
5. Attach the stored JWT automatically to all outgoing API requests (axios interceptor or a fetch wrapper) instead of doing it manually per-call.

### Lecture Outline

| Time | Segment | Content |
|---|---|---|
| 0:00–0:15 | Homework debrief | Revisit the Wk15 "wrong experience" observations. Frame today as replacing hardcoded tokens with a real flow. |
| 0:15–0:40 | Where does the token live? | `localStorage` (simple, XSS-exposed) vs. httpOnly cookies (safer, more setup — CORS `credentials`, cookie-parser on the API). Instructor picks one path for the class to standardize on and explains why. |
| 0:40–1:05 | Login/Register forms | Controlled forms (Wk15 patterns) hitting `POST /auth/login` / `/auth/register`; storing the token on success; redirecting to `/`. |
| 1:05–1:15 | Break | — |
| 1:15–1:45 | Auth context | `AuthContext` with `user`, `token`, `login()`, `logout()`; wrap the app in `<AuthProvider>`; any component can now read auth state via `useContext`. |
| 1:45–2:05 | Protected routes | A `<ProtectedRoute>` component wrapping React Router routes, redirecting to `/login` if no valid session; show/hide nav links based on auth state. |
| 2:05–2:25 | Auto-attaching the token | An axios instance with a request interceptor that adds `Authorization: Bearer <token>` automatically; a response interceptor that logs the user out on a `401`. |
| 2:25–end | Lab kickoff | — |

### Hands-On Lab: Real Auth, End to End

**Scenario:** Students replace every piece of hardcoded/manual auth from Weeks 14–15 with a real, working login system.

**Requirements:**
1. Working `/login` and `/register` pages, both hitting the real Midterm auth endpoints, with visible error messages on bad credentials or a duplicate email.
2. `AuthContext` providing `user`, `token`, `login()`, `logout()` app-wide; a visible "logged in as X / Logout" state in the nav.
3. `/tasks/:id`, task creation, and edit/delete are all wrapped in `<ProtectedRoute>` — an unauthenticated visitor is redirected to `/login`, not shown a broken page.
4. All API calls use a shared axios instance that auto-attaches the JWT — no more manually copy-pasted tokens anywhere in the codebase.
5. A `401` response from the API (e.g., expired token) triggers an automatic logout and redirect to `/login`, rather than a silent failure.

**Deliverable:** Updated `client/` repo with the complete auth flow working end-to-end against the real API, demoed live: register → auto/manual login → create a task → logout → confirm protected routes redirect.

**Assessment criteria:**
- Login/register work correctly against the real API, with visible errors on failure (5 pts)
- `AuthContext` correctly shares auth state across the app (5 pts)
- Protected routes correctly block/redirect unauthenticated access (5 pts)
- Token auto-attached via interceptor; 401 triggers logout (5 pts)

### Homework / Bridge to Week 17
Ask students to try running `client` and `api` together on a classmate's machine, same as the Wk10→Wk11 bridge — except now there's a third moving piece (the React dev server) and a question nobody's answered yet: "how does this get built and served once it's not `npm run dev` anymore?" Bring that question to Week 17.

---

## Week 17 — Docker for Production: Multi-Stage Builds, Nginx, Full Compose Stack

### Learning Objectives
By the end of this session, students will be able to:
1. Explain why `npm run dev` is unsuitable for production and what "build then serve" means for a React app (static files, not a dev server).
2. Write a multi-stage Dockerfile: a `build` stage (Node, `npm run build`) and a `serve` stage (Nginx, copying only the built static files).
3. Configure Nginx to serve a single-page app correctly, including client-side routing fallback (all paths → `index.html`).
4. Extend `docker-compose.yml` to a 3–4 service stack: `client`, `api`, `mongo`, optionally an `nginx` reverse proxy in front of both.
5. Differentiate environment configuration for development vs. production (API base URLs, CORS origins, `NODE_ENV`) without hardcoding values.
6. Apply basic image-size optimization: `alpine` base images, multi-stage builds discarding `node_modules`/dev dependencies, minimal final image inspection (`docker image ls`, `docker history`).

### Lecture Outline

| Time | Segment | Content |
|---|---|---|
| 0:00–0:15 | Homework debrief | Revisit the "how does this get served in prod" question from Wk16. Frame today as the answer. |
| 0:15–0:45 | Dev server vs. production build | `npm run build` produces static HTML/CSS/JS — no Node needed to *serve* it, just to *build* it. This is the conceptual hinge for multi-stage builds. |
| 0:45–1:15 | Multi-stage Dockerfile | Live-write: Stage 1 `FROM node:20-alpine AS build` → `npm ci` → `npm run build`; Stage 2 `FROM nginx:alpine` → `COPY --from=build /app/dist /usr/share/nginx/html`. Explain why the final image has no Node, no `node_modules`, no source — just static files and Nginx. |
| 1:15–1:25 | Break | — |
| 1:25–1:50 | Nginx SPA config | A minimal `nginx.conf` with `try_files $uri /index.html;` so client-side routes (from Wk15's React Router) don't 404 on refresh. Copy this custom config into the image. |
| 1:50–2:15 | Full Compose stack | Extend the Midterm `docker-compose.yml` with a `client` service (built from the multi-stage Dockerfile) and, optionally, an `nginx` reverse-proxy service routing `/api/*` to `api` and everything else to `client`. Discuss when a reverse proxy is worth the extra complexity vs. exposing both services on separate ports. |
| 2:15–2:30 | Env config & image size | `VITE_API_URL` (or similar) baked in at build time vs. runtime — discuss the trade-off explicitly, since it trips people up. Quick `docker image ls` comparison: dev-style single-stage image vs. the new multi-stage image. |
| 2:30–end | Lab kickoff | — |

### Hands-On Lab: Production-Ready Full Stack

**Scenario:** Students take the complete Week 16 full-stack app (client + api + mongo) and package it as a production-style, multi-container system.

**Requirements:**
1. A multi-stage `Dockerfile` for the React `client`: build stage compiles the app, serve stage runs Nginx with a custom `nginx.conf` supporting SPA client-side routing.
2. `docker-compose.yml` extended to include `client` alongside `api` and `mongo` — at minimum 3 services, with an optional 4th (`nginx` reverse proxy) for extra credit.
3. A documented decision on how the client knows the API's URL in each environment (build-time env var vs. runtime config vs. reverse-proxy same-origin routing) — with a one-paragraph justification in the README.
4. Confirm client-side routing works correctly *after* the production build — refreshing on `/tasks/:id` must not 404.
5. A before/after image-size comparison (`docker image ls`) between a naive single-stage client image and the multi-stage version, explained in the README.

**Deliverable:** Full repo (or merged `client`/`api` repos) with `docker-compose.yml` bringing up all services via one command, and a README section titled "Production Notes" covering the env-config decision and the image-size comparison.

**Assessment criteria:**
- Multi-stage Dockerfile correctly builds and serves the React app via Nginx (5 pts)
- SPA routing correctly configured (no 404 on refresh of a nested route) (5 pts)
- Full stack (client + api + mongo) starts via one `docker-compose up` (5 pts)
- Env-config decision documented and correctly implemented (5 pts)

### Homework / Bridge to Week 18
Ask students to research, in five minutes or less, what would actually need to change to put this on Render, Railway, or a VPS instead of their laptop — domain names, managed MongoDB vs. the `mongo` container, HTTPS, environment secrets in a real host's dashboard instead of a local `.env`. Bring rough notes to Week 18; they'll turn directly into the capstone's deployment write-up.

---

## Week 18 — Finals Capstone: Complete Containerized Full-Stack App

This week is primarily a work/assessment session rather than new lecture content — use it for final integration, troubleshooting, peer testing, and submission.

### Milestone Requirements
Students submit a single repository containing:
1. A complete full-stack app: React frontend (Weeks 13–16) + Express/Node API (Midterm Weeks 7–10) + MongoDB, with full CRUD and authenticated, role-aware access.
2. A working full-stack auth flow: register/login/logout, protected frontend routes, protected/ownership-checked API routes.
3. A multi-stage `Dockerfile` for the client (build + Nginx serve) and a working `Dockerfile` for the API (from Midterm).
4. A single `docker-compose.yml` orchestrating the complete stack (`client`, `api`, `mongo`, and optionally `nginx`) — **one command, zero manual setup, beyond copying `.env.example`.**
5. A short deployment write-up (`DEPLOYMENT.md`) covering: what changes for a real host (Render/Railway/VPS) — domain/HTTPS, managed vs. containerized MongoDB, where secrets live in production, and any CI/CD next steps a student would take if continuing this project.

### Suggested In-Class Flow
| Time | Activity |
|---|---|
| 0:00–0:20 | Open troubleshooting clinic — pairs debug any remaining multi-stage build or full-stack Compose issues from the Wk17 homework. |
| 0:20–1:30 | Peer testing: each student pulls a classmate's repo and runs the entire stack using only `docker-compose up` and the README. They exercise the full user journey — register, login, create/edit/delete a task, logout, refresh a nested route — and report any friction. |
| 1:30–2:00 | Fixes based on peer feedback; polish `DEPLOYMENT.md`. |
| 2:00–end | Final submission + brief individual check-in with instructor: each student walks through their `docker-compose.yml` service by service and explains what would need to change to actually deploy it (tying back to the Wk17 homework notes). |

### Assessment Rubric (Finals Capstone)
- Full-stack app functions correctly end-to-end (register → auth → full CRUD → logout) (10 pts)
- Frontend and backend correctly integrated (routing, data fetching, mutations, protected routes) (10 pts)
- Multi-stage client build + Nginx SPA serving works correctly (10 pts)
- Complete stack starts via a single `docker-compose up` with zero manual intervention (10 pts)
- Peer was able to run the entire stack using only the README (5 pts)
- `DEPLOYMENT.md` demonstrates real understanding of dev-vs-prod differences (5 pts)
- Student can walk through the full Compose file and explain each service's role (5 pts)

**Total: 55 pts**

### Closing the Loop
This is the moment to make the throughline explicit one last time: Week 5 was one container around a plain HTTP server because that's all there was to containerize. Week 11 was two containers because Express and MongoDB finally had a real relationship worth orchestrating. Week 17–18 is three-plus containers, multi-stage builds, and production config — because now there's an actual product: a frontend, a backend, and a database, shipped the way real teams ship it. "Containerize it" should, by now, be a reflex rather than a special topic — which was the whole point.
