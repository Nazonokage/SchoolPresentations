# Answer Key — IT103 Pre-Final Periodical Exam

**Total: 60 points** (MC 20 · ID 20 · Enumeration 20)

## I. Multiple Choice (1–20)

| # | Ans | Module | Note |
|---|---|---|---|
| 1 | **B** | M10 | SOA = coarse-grained, shared, often an ESB; microservices = small, decentralized, own their data. |
| 2 | **C** | M10 | ViewModel + two-way data binding (Vue, Angular). |
| 3 | **A** | M10 | services/ = external API integrations; middleware/ is auth, logging, validation. |
| 4 | **D** | M10 | Webhooks = server-to-server push on an event; WebSockets = persistent two-way client connection. |
| 5 | **B** | M11 | PascalCase.jsx, UPPER_SNAKE_CASE, snake_case. |
| 6 | **C** | M11 | Long params = 5+ parameters; use an object/config argument. |
| 7 | **D** | M11 |  |
| 8 | **A** | M12 | Replication = copies for reads; sharding = split by key. |
| 9 | **B** | M12 | Statelessness: session data lives in a shared store. |
| 10 | **C** | M12 | Tracing is most relevant in microservices and integration-heavy systems. |
| 11 | **D** | M13 | (2000 × 2 × 0.5) / 4 = 500. |
| 12 | **A** | M13 | Debt is managed continuously, not by freezing all feature work. |
| 13 | **B** | M13 | Modern SQL databases can also scale horizontally, so D is wrong. |
| 14 | **D** | M14 | Apache is thread-based; Nginx is event-driven. |
| 15 | **A** | M14 | Flutter uses Dart and its own UI toolkit. |
| 16 | **C** | M14 |  |
| 17 | **A** | M15 | Pool size ≠ as big as possible; leave headroom (~18–20 per instance). |
| 18 | **B** | M15 | Expand-contract pattern. |
| 19 | **C** | M15 | Identical TTLs cause the stampede. |
| 20 | **D** | M15 | Graceful shutdown. |

Tally: A=5, B=5, C=5, D=5

## II. Identification (21–40)

| # | Answer | Module | Note |
|---|---|---|---|
| 21 | **Monolithic architecture** | M10 |  |
| 22 | **Loose coupling** | M10 |  |
| 23 | **MVP (Model-View-Presenter)** | M10 | Passive View, Presenter holds the UI logic. |
| 24 | **God function** | M11 | Violates one-thing-per-function. |
| 25 | **Magic numbers (use a named constant)** | M11 |  |
| 26 | **Dead code** | M11 | Delete it; version control remembers. |
| 27 | **Asynchronous processing (message queue + workers)** | M12 |  |
| 28 | **Least Connections** | M12 |  |
| 29 | **Continuous Integration (CI)** | M12 |  |
| 30 | **ADR (Architecture Decision Record)** | M13 |  |
| 31 | **YAGNI (You Aren’t Gonna Need It)** | M13 |  |
| 32 | **.NET stack (ASP.NET Core)** | M14 |  |
| 33 | **MEAN stack** | M14 |  |
| 34 | **Python AI stack (FastAPI / Flask)** | M14 |  |
| 35 | **Ruby on Rails** | M14 | Convention over configuration. |
| 36 | **Missing index (full table scan)** | M15 | Fix: CREATE INDEX; confirm with EXPLAIN ANALYZE. |
| 37 | **Idempotency (idempotency key)** | M15 |  |
| 38 | **Missing pagination** | M15 | Fix: cursor/offset pagination with an enforced max page size. |
| 39 | **Inconsistent error responses** | M15 | Fix: one error contract via central handler/middleware. |
| 40 | **Single Point of Failure (SPOF)** | M15 | Fix: redundant load balancers / multi-AZ. |

## III. Enumeration (41–60)

Any order within a set; 1 point per correct, non-repeated answer. Accept reasonable equivalents (e.g., “in-memory cache” for Application cache).

**Enumerate the five SOLID principles (full names).** (M10)

- 41. Single Responsibility
- 42. Open/Closed
- 43. Liskov Substitution
- 44. Interface Segregation
- 45. Dependency Inversion

**Enumerate the four caching layers in the notes.** (M12)

- 46. Browser cache
- 47. CDN
- 48. Application cache (in-memory)
- 49. DB query cache

**Enumerate the four quadrants of the Impact vs Effort matrix.** (M13)

- 50. Quick Wins
- 51. Major Projects
- 52. Fill-ins
- 53. Avoid

**Enumerate the four log levels.** (M15)

- 54. ERROR
- 55. WARN
- 56. INFO
- 57. DEBUG

**JAMstack stands for:** (M14)

- 58. JavaScript
- 59. APIs
- 60. Markup

