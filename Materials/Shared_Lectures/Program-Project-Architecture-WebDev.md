# Program & Project Architecture Concepts for Web Development
### Reference Notes — Integrative Programming

---

## 1. What is "Architecture" in Software Development?

**Software architecture** is the high-level structure of a system — how it's broken into parts (components/modules), how those parts talk to each other, and the rules/principles that guide their design. It's the "blueprint" of a program, made *before* heavy coding starts, because architecture decisions are expensive to change later.

Two related but distinct terms often used in this subject:

| Term | Meaning |
|---|---|
| **Program Architecture** | The internal structure of *one* application — how its code is organized (e.g., MVC pattern inside a single web app). |
| **Project/System Architecture** | The bigger picture — how multiple programs/services, servers, databases, and third-party systems interact as a whole (e.g., a web app + mobile app + API + database + payment gateway all working together). |

**Why architecture matters:**
- **Maintainability** – easier to fix bugs and add features
- **Scalability** – system can grow (more users, more data) without collapsing
- **Reusability** – components can be reused across projects
- **Team collaboration** – different devs can work on different layers without stepping on each other
- **Testability** – isolated components are easier to test
- **Integration** – (core theme of this subject) different systems/technologies can be connected cleanly

---

## 2. Core Design Principles Behind All Architectures

Before the specific patterns, know these guiding principles — they explain *why* the patterns look the way they do.

- **Separation of Concerns (SoC)** – each part of the system should handle one specific responsibility (e.g., don't mix database code with UI code).
- **DRY (Don't Repeat Yourself)** – avoid duplicating logic; centralize it.
- **KISS (Keep It Simple, Stupid)** – avoid unnecessary complexity.
- **Loose Coupling** – components should depend on each other as little as possible, so changing one doesn't break another.
- **High Cohesion** – code that belongs together (related logic) should be grouped together.
- **SOLID Principles** (common in OOP-based backend design):
  - **S** – Single Responsibility Principle
  - **O** – Open/Closed Principle
  - **L** – Liskov Substitution Principle
  - **I** – Interface Segregation Principle
  - **D** – Dependency Inversion Principle

---

## 3. Foundational Web Architecture: Client-Server Model

Nearly every web architecture pattern sits on top of this base model.

```
 ┌────────────┐        HTTP Request        ┌────────────┐
 │   CLIENT   │  ─────────────────────────► │   SERVER   │
 │ (Browser / │                             │ (Web/App   │
 │  Mobile)   │  ◄───────────────────────── │  Server)   │
 └────────────┘        HTTP Response        └────────────┘
                                                    │
                                                    ▼
                                             ┌────────────┐
                                             │  DATABASE  │
                                             └────────────┘
```

- **Client** – requests and displays data (browser, mobile app)
- **Server** – processes requests, applies business logic
- **Database** – stores and retrieves persistent data

This is a **2-tier** setup in its simplest form. Real-world web apps almost always expand this into **3-tier or N-tier** architecture (below).

---

## 4. Tiered (Layered) Architectures

### 4.1 Three-Tier Architecture
The most common architecture taught for web systems. Each tier is a **physically or logically separate layer**.

| Tier | Responsibility | Web Examples |
|---|---|---|
| **1. Presentation Tier** | UI, what the user sees/interacts with | HTML/CSS/JS, React, Blazor |
| **2. Application/Logic Tier** | Business rules, processing, validation | Node.js/Express, ASP.NET, Django, Laravel |
| **3. Data Tier** | Storage and retrieval of data | MySQL, PostgreSQL, MongoDB |

**Advantages:** clear separation, each layer can scale/be developed independently, easier to maintain.
**Disadvantage:** more overhead/complexity than a simple 2-tier setup.

### 4.2 N-Tier (Multi-Tier) Architecture
An extension of 3-tier where more specialized layers are added, e.g.:
```
Presentation → API/Gateway → Business Logic → Data Access Layer → Database
```
Used in enterprise systems where extra layers (caching, security, integration) are needed.

---

## 5. Architectural (Design) Patterns for Program Structure

These describe how code *within* an application is organized — very relevant for "program architecture."

### 5.1 MVC (Model-View-Controller)
The most widely used pattern in web frameworks (Laravel, Django, Ruby on Rails, ASP.NET MVC, Spring MVC).

```
        User Interaction
              │
              ▼
       ┌─────────────┐
       │ CONTROLLER  │  receives input, decides what happens
       └─────────────┘
          │        │
          ▼        ▼
     ┌────────┐  ┌───────┐
     │ MODEL  │  │ VIEW  │
     │ (data/ │  │ (UI/  │
     │ logic) │  │output)│
     └────────┘  └───────┘
```

- **Model** – data and business logic (e.g., database interaction)
- **View** – what the user sees (UI templates)
- **Controller** – handles user input, coordinates Model and View

**Use case:** traditional server-rendered web apps.

### 5.2 MVVM (Model-View-ViewModel)
Common in modern frontend frameworks (Vue, Angular, sometimes React with state managers).

- **Model** – data/business logic
- **View** – UI (declarative, e.g., HTML template)
- **ViewModel** – binds Model to View, handles UI state/logic; View updates automatically when ViewModel changes (data-binding)

**Key difference from MVC:** the View and ViewModel are tightly bound via **two-way data binding**, reducing manual DOM manipulation.

### 5.3 MVP (Model-View-Presenter)
Similar to MVC, but the **Presenter** handles all UI logic and the View is kept "passive" (dumb) — it just displays what the Presenter tells it to.

- **Model** – data
- **View** – passive UI, forwards user actions to Presenter
- **Presenter** – contains logic, updates the View directly

**Use case:** apps where you want the UI to be easily testable/mockable (common in some enterprise & Android-influenced designs).

---

## 6. System-Level (Project) Architectures

These describe how an entire application/project is structured at a system level — beyond just one program's internal code.

### 6.1 Monolithic Architecture
The entire application (UI, business logic, data access) is built and deployed as **one single unit**.

```
┌─────────────────────────────┐
│        ONE APPLICATION      │
│  UI + Business Logic + DB   │
│         Access Layer        │
└─────────────────────────────┘
```
**Pros:** simple to develop, test, and deploy initially; easy for small teams.
**Cons:** hard to scale specific parts; one bug can bring down the whole app; harder to adopt new tech gradually.

### 6.2 Microservices Architecture
The application is split into **small, independent services**, each responsible for one business capability, communicating via APIs (often REST or messaging queues).

```
 ┌───────────┐   ┌───────────┐   ┌───────────┐
 │   User    │   │  Order    │   │  Payment  │
 │  Service  │   │  Service  │   │  Service  │
 └─────┬─────┘   └─────┬─────┘   └─────┬─────┘
       │               │               │
       └────────┬──────┴──────┬────────┘
                 ▼             ▼
           ┌────────────────────────┐
           │     API Gateway        │
           └────────────────────────┘
                       │
                       ▼
                    Client
```
**Pros:** each service can be developed, deployed, and scaled independently; different services can even use different tech stacks; failure isolation.
**Cons:** complex to manage (networking, deployment); requires strong DevOps practices; data consistency across services is harder.

### 6.3 Service-Oriented Architecture (SOA)
A predecessor/relative of microservices. Services are larger ("coarse-grained") and typically communicate through an **Enterprise Service Bus (ESB)**. Focused on reusability of services across an organization, not just one app.

**Difference from Microservices:**
| SOA | Microservices |
|---|---|
| Larger, shared services | Small, independent services |
| Often uses ESB (centralized) | Usually decentralized (API calls, messaging) |
| Shares a common data store sometimes | Each service usually owns its own database |

### 6.4 Serverless Architecture
Code runs in stateless functions managed by a cloud provider (AWS Lambda, Azure Functions, Google Cloud Functions). Developers don't manage servers — the platform automatically provisions resources.

**Pros:** no server management, automatic scaling, pay-per-execution.
**Cons:** cold-start latency, vendor lock-in, harder to debug/test locally.

### 6.5 Event-Driven Architecture (EDA)
Components communicate by producing and reacting to **events** rather than direct calls, often through a message broker (Kafka, RabbitMQ).

```
Producer → [Event] → Message Broker → Consumer(s)
```
**Use case:** systems needing high decoupling and real-time processing (e.g., notifications, order processing pipelines).

---

## 7. API-Centric Architecture (Integration Focus)

Since this subject is *Integrative Programming*, APIs are the "glue" that connects different systems.

### 7.1 RESTful Architecture
Uses standard HTTP methods to perform operations on **resources**.

| HTTP Method | Action | Example |
|---|---|---|
| GET | Read | `GET /api/students` |
| POST | Create | `POST /api/students` |
| PUT/PATCH | Update | `PUT /api/students/5` |
| DELETE | Delete | `DELETE /api/students/5` |

**REST principles:** stateless, resource-based URLs, uses standard status codes (200, 404, 500, etc.), typically returns JSON.

### 7.2 Other Integration Styles (good to know)
- **SOAP** – XML-based, strict protocol, common in older enterprise/banking systems.
- **GraphQL** – client specifies exactly what data it needs in a single query (alternative to REST).
- **WebSockets** – persistent two-way connection for real-time apps (chat, live dashboards).
- **Webhooks** – server-to-server "push" notifications when an event happens (e.g., payment confirmation).

---

## 8. Typical Web Project Folder Structure (Program-Level Architecture in Practice)

Example of an MVC-based Node.js/Express project:

```
project-root/
│
├── controllers/       # Handles requests, calls models, returns responses
├── models/             # Database schemas & business logic
├── views/               # Templates (if server-rendered)
├── routes/              # Defines API endpoints/URLs
├── middleware/       # Auth, logging, validation
├── config/               # DB connection, environment configs
├── public/               # Static assets (CSS, JS, images)
├── services/            # External API integrations, reusable logic
├── utils/                 # Helper functions
├── tests/                 # Unit/integration tests
├── app.js / server.js    # Entry point
└── package.json
```

This structure directly reflects **separation of concerns** in action.

---

## 9. Comparison Summary Table

| Architecture | Best For | Complexity | Scalability |
|---|---|---|---|
| Monolithic | Small apps, MVPs, small teams | Low | Limited |
| 3-Tier/N-Tier | Standard business web apps | Medium | Good |
| MVC | Server-rendered web frameworks | Low–Medium | Good |
| MVVM | Modern SPA frontends | Medium | Good |
| Microservices | Large, complex, evolving systems | High | Excellent |
| SOA | Enterprise systems needing shared services | High | Good |
| Serverless | Event-driven, variable-load workloads | Medium | Excellent (auto) |
| Event-Driven | Real-time, decoupled systems | High | Excellent |

---

## 10. How to Choose an Architecture (Quick Guide)

Ask these questions:
1. **How big is the team/project?** → Small team = monolithic/MVC; large team = microservices.
2. **Do we expect rapid scaling?** → Yes = microservices/serverless.
3. **How complex is the domain?** → Complex, many business units = microservices/SOA.
4. **What's the deployment/DevOps maturity?** → Low maturity = avoid microservices (too much overhead).
5. **Do we need real-time features?** → Consider event-driven architecture / WebSockets.
6. **Is this integrating multiple external systems?** (core to Integrative Programming) → Focus on well-designed **API layer** (REST/GraphQL) regardless of the underlying architecture.

---

## 11. Key Takeaways for the Subject

- **Program architecture** = internal code organization (MVC, MVVM, MVP, layering).
- **Project/system architecture** = how whole systems/services interact (monolith, microservices, SOA, client-server).
- **Integrative Programming** cares most about the **connections** between systems — APIs, data formats (JSON/XML), protocols (REST/SOAP), and how loosely-coupled components can be integrated reliably.
- Good architecture isn't about picking the "fanciest" pattern — it's about matching the pattern to the project's size, team, and integration needs.

---

*Note: I don't have live document/database access — this is compiled from general software engineering knowledge, so it's worth cross-checking specifics (e.g., exact framework terminology your professor uses) against your course materials.*
