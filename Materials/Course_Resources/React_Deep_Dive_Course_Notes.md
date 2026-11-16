# EL104: Web Systems & Technologies — Comprehensive Course Notes (Modules 8 to 18)

Welcome to the official, in-depth study reference for **EL104: Web Systems & Technologies**. This document bridges frontend client engineering (React JS) to backend API microservices (Express Node.js, MongoDB) and production container orchestration (Docker & Docker Compose).

---

## 📌 Curriculum Sitemap
- [Module 8: React Side Effects & Component Lifecycle](#module-8-react-side-effects--component-lifecycle)
- [Module 9: HTTP Data Fetching, Axios & Express CORS Security](#module-9-http-data-fetching-axios--express-cors-security)
- [Module 10: Enterprise Caching & Server State (TanStack Query)](#module-10-enterprise-caching--server-state-tanstack-query)
- [Module 11: Advanced State Machines with `useReducer`](#module-11-advanced-state-machines-with-usereducer)
- [Module 12: Global State & Context API](#module-12-global-state--context-api)
- [Module 13: Custom Hooks, Refs & Performance Memoization](#module-13-custom-hooks-refs--performance-memoization)
- [Module 14: Client-Side Routing with React Router v6](#module-14-client-side-routing-with-react-router-v6)
- [Module 15: Full-Stack Auth & Protected Routes](#module-15-full-stack-auth--protected-routes)
- [Module 16: Connecting React Frontend to Express Backend](#module-16-connecting-react-frontend-to-express-backend)
- [Module 17: Production Docker for React & Multi-Stage Builds](#module-17-production-docker-for-react--multi-stage-builds)
- [Module 18: Full-Stack Orchestration with Docker Compose](#module-18-full-stack-orchestration-with-docker-compose)

---

## Module 8: React Side Effects & Component Lifecycle

### 1. Detailed Lecture & Concept Breakdown
A **Side Effect** in React is any operation that reaches outside the pure function render pipeline to synchronize with an external system. Examples include making HTTP API calls, subscribing to browser events, setting timer intervals, or directly mutating the DOM.

#### The `useEffect` Hook Mental Model
React components must remain pure during the render phase. `useEffect` defers the execution of side effect code until **after** React has called component functions, calculated DOM diffs, and painted the updated HTML to the user's screen.

#### Dependency Array Rules
1. `useEffect(fn)`: **No array.** The effect function executes after *every single render cycle*. (Use with extreme caution).
2. `useEffect(fn, [])`: **Empty array.** The effect function executes *exactly once*, immediately after the initial component mount. Ideal for initial data fetching.
3. `useEffect(fn, [userId, status])`: **Dependency array.** The effect executes on mount, and re-executes whenever `userId` or `status` changes reference between renders.

#### Cleanup Functions & `AbortController`
When a component unmounts or before a dependency update re-runs an effect, React calls the cleanup function returned inside `useEffect`. To prevent memory leaks or updating state on unmounted components during asynchronous fetches, we pass an `AbortController` signal to `fetch()` and call `controller.abort()` in the cleanup function.

### 2. Real-World Analogy: Automatic Light Switch
Think of `useEffect` like an automated room lighting system. Rendering JSX is like building the room. `useEffect` is the sensor that turns on the lights *after* you enter the room (mount). The cleanup function is the automatic switch that turns off the lights *when you leave* (unmount) so electricity isn't wasted on an empty room.

### 3. Runnable Code Sample
```jsx
import { useState, useEffect } from 'react';

export function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // 1. Create AbortController instance
    const controller = new AbortController();

    async function fetchUser() {
      try {
        setLoading(true);
        const res = await fetch(`http://localhost:5000/api/users/${userId}`, {
          signal: controller.signal // Attach signal to fetch
        });
        const data = await res.json();
        setUser(data);
      } catch (err) {
        if (err.name !== 'AbortError') {
          console.error('Fetch error:', err.message);
        }
      } finally {
        setLoading(false);
      }
    }

    fetchUser();

    // 2. Return cleanup function
    return () => {
      controller.abort(); // Cancels pending HTTP call if component unmounts
    };
  }, [userId]);

  if (loading) return <div>Loading user profile...</div>;
  return <div>Welcome, {user?.name}</div>;
}
```

---

## Module 9: HTTP Data Fetching, Axios & Express CORS Security

### 1. Detailed Lecture & Concept Breakdown
In Web Systems, frontends communicate with backends over the HTTP protocol using REST architectural constraints. 

#### 3-UI State Pattern
Every asynchronous data fetch must explicitly handle 3 distinct UI states:
1. **Loading State**: Display spinners or skeleton screens while network requests are in flight.
2. **Error State**: Render clear error notifications if network or server errors (4xx/5xx) occur.
3. **Data/Success State**: Render the successfully retrieved data payload.

#### Native `fetch()` vs `axios`
- **Native `fetch()`**: Built into browsers. Requires explicit two-step parsing (`await res.json()`). Crucially, `fetch()` **does NOT throw** an error on HTTP 404 or 500 status responses—you must manually verify `if (!res.ok)`.
- **`axios`**: Popular third-party HTTP client. Automatically parses response JSON into `res.data` and **automatically rejects promises** (jumping to `catch`) whenever HTTP status codes fall outside 2xx.

#### Express CORS (Cross-Origin Resource Sharing)
Security engines in web browsers enforce the **Same-Origin Policy**. If your React client runs on `http://localhost:5173` and calls Express on `http://localhost:5000`, the browser blocks the response unless Express configures the `cors` middleware:
```javascript
const cors = require('cors');
app.use(cors({ origin: 'http://localhost:5173' }));
```

### 2. Real-World Analogy: Translating Mail Envelope & Security Guard
- Using `axios` is like receiving a pre-opened package: it unwraps the cardboard box (`res.data`) and throws an alarm if the package arrives damaged (4xx/5xx).
- `cors` is like a security guard at a building gate checking the visitor's badge origin before allowing them inside.

---

## Module 10: Enterprise Caching & Server State (TanStack Query)

### 1. Detailed Lecture & Concept Breakdown
Remote API data is **Server State**—it is remotely owned, shared asynchronously, and requires caching, revalidation, and deduplication.

#### TanStack Query (React Query) Hooks
- **`useQuery`**: Reads data. Takes a unique `queryKey` array (e.g. `['tasks']`) and a `queryFn`. Automatically handles caching, background revalidation on window focus, retries, and returns `{ data, isLoading, isError }`.
- **`useMutation`**: Writes data (POST, PUT, DELETE). Returns `{ mutate, isPending }`.
- **Query Invalidation (`invalidateQueries`)**: Instructs TanStack Query to mark cached queries as stale, triggering automatic background refetches after mutations.

### 2. Real-World Analogy: Library Card Catalog & Auto-Sync
`useQuery` acts like a personal assistant. When you ask for a book (`['tasks']`), the assistant checks their desk cache first. If available, they hand it to you instantly, while calling the main library in the background to check if a newer edition was released.

---

## Module 11: Advanced State Machines with `useReducer`

### 1. Detailed Lecture & Concept Breakdown
When component state involves multiple interdependent variables (e.g. shopping carts, multi-step forms, complex filter combinations), multiple `useState` setters cause fragmented code.

#### `useReducer` Structure
- **Reducer Function**: A pure function `(state, action) => newState`.
- **Actions**: Objects describing *what happened* (e.g. `{ type: 'ADD_ITEM', payload: product }`).
- **`dispatch(action)`**: The trigger function that sends action objects to the reducer.

### 2. Real-World Analogy: Fast-Food Order Ticket Counter
Instead of walking into a kitchen and modifying ingredients yourself (`useState`), you hand a ticket order (`dispatch({ type: 'ORDER_BURGER' })`) to the cashier. The chef (`reducer`) follows a strict recipe and hands back the new order tray (`newState`).

---

## Module 12: Global State & Context API

### 1. Detailed Lecture & Concept Breakdown
**Prop-Drilling** occurs when data must be passed down through 5+ layers of intermediate components that don't need the data themselves.

#### React Context API
- **`createContext()`**: Instantiates a Context object.
- **`<Context.Provider value={...}>`**: Wraps a component subtree, broadcasting state data down to all child components.
- **`useContext(Context)`**: Consumes the broadcasted data directly inside any descendant component.

### 2. Real-World Analogy: Satellite Radio Broadcast
Prop-drilling is like passing a physical paper note down a line of 10 people. The Context API is like a radio tower broadcasting a signal: any component with a receiver (`useContext`) can tune in directly without interrupting the people in between.

---

## Module 13: Custom Hooks, Refs & Performance Memoization

### 1. Detailed Lecture & Concept Breakdown
- **Custom Hooks**: Functions starting with `use` that encapsulate reusable stateful logic (e.g. `useLocalStorage`, `useAuth`). They share *logic*, not state memory instances.
- **`useRef`**: Returns `{ current: initialValue }`. Mutating `.current` does **NOT** trigger a re-render. Essential for direct DOM access (e.g. `inputRef.current.focus()`) and background timers.
- **`useMemo`**: Caches the **computed result** of an expensive calculation.
- **`useCallback`**: Caches a **function reference** to prevent unnecessary re-renders of child components wrapped in `React.memo`.

---

## Module 14: Client-Side Routing with React Router v6

### 1. Detailed Lecture & Concept Breakdown
Single-Page Applications (SPAs) intercept browser URL changes client-side without executing full HTTP page reloads.

#### React Router v6 Data Routers
- **`createBrowserRouter`**: Configures path routes and layout hierarchies.
- **`<Outlet />`**: Component placeholder in parent layout routes where child routes render.
- **`useParams()`**: Extracts dynamic URL path tokens (e.g. `/tasks/:id`).
- **`useNavigate()`**: Executes programmatic redirects (e.g. `navigate('/dashboard', { replace: true })`).

---

## Module 15: Full-Stack Auth & Protected Routes

### 1. Detailed Lecture & Concept Breakdown
- **JWT (JSON Web Token)**: Cryptographically signed token string issued by Express upon authentication.
- **`localStorage` vs `httpOnly` Cookies**:
  - `localStorage`: Easy to access in JS, but vulnerable to XSS script attacks.
  - `httpOnly` Cookie: Cannot be read by client JavaScript, protecting against XSS token theft.
- **`<ProtectedRoute>` Guard**: Layout wrapper checking authentication status; renders `<Outlet />` if logged in, or redirects to `/login` via `<Navigate />` if unauthenticated.

---

## Module 16: Connecting React Frontend to Express Backend

### 1. Detailed Lecture & Concept Breakdown
- **Vite Environment Variables**: Defined in `.env` starting with `VITE_` (e.g. `VITE_API_URL`) and accessed via `import.meta.env.VITE_API_URL`.
- **Axios Interceptors**:
  - **Request Interceptor**: Injects `Authorization: Bearer <token>` into outgoing request headers automatically.
  - **Response Interceptor**: Detects HTTP 401 Unauthorized errors from Express, purges expired local storage tokens, and redirects users to `/login`.

---

## Module 17: Production Docker for React & Multi-Stage Builds

### 1. Detailed Lecture & Concept Breakdown
- **Dev Server vs Production Build**: `npm run dev` runs Vite HMR. `npm run build` compiles raw JSX into optimized static HTML/CSS/JS files inside `/dist`.
- **Multi-Stage Dockerfile**:
  - **Stage 1 (Build)**: `FROM node:20-alpine AS build` &rarr; compiles app via `npm run build`.
  - **Stage 2 (Serve)**: `FROM nginx:alpine` &rarr; copies `/dist` static files into Nginx. Node runtime is discarded, reducing image size from 900MB to 25MB!
- **Nginx `try_files` SPA Fallback**: `try_files $uri /index.html;` ensures client-side routes (e.g. `/tasks/10`) do not return Nginx 404 errors on page refresh.

---

## Module 18: Full-Stack Orchestration with Docker Compose

### 1. Detailed Lecture & Concept Breakdown
- **3-Tier System Architecture**: Managing `client` (React Nginx), `api` (Express Node), and `mongo` (Database) in a unified `docker-compose.yml`.
- **Container Networking**: Services communicate over isolated internal Docker bridge networks using service names as DNS hostnames (e.g. `mongodb://mongo:27017/db`).
- **Named Volumes**: Mapping `/data/db` ensures database records persist even if container instances restart.
