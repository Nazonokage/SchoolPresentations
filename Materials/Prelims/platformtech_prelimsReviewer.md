# 📚 Platform Technologies — Prelims Reviewer
### ITE 401 | Covers Modules 1–8 + Git/GitHub/Vercel

> **How to use this:** Read each section, test yourself on the bolded terms, and use the 🧠 memory tricks to lock things in.

---

## MODULE 1 — Introduction to Platform Technologies

### What is a Platform?
> **Formula to memorize:** `Hardware + Software + Networks = Platform`

A **platform** is any base of technologies on which other technologies or processes are built. Think of it as the *pundasyon (foundation)* of a building — you can't build apps without it.

Most services end users interact with are built *on top* of a platform (e.g., your apps run on Android/iOS, which runs on hardware).

---

### Generations of Computing (memorize the timeline!)

| # | Era | Years | Key Tech |
|---|-----|-------|----------|
| 1 | Vacuum Tubes | 1945–55 | Punch cards, machine language |
| 2 | Transistors & Batch Systems | 1955–65 | IBM 1401, IBM 7094, FORTRAN |
| 3 | ICs & Multiprogramming | 1965–80 | IBM System/360, MULTICS, timesharing |
| 4 | Personal Computers | 1980–present | IBM PC, DOS, Macintosh, Windows, Linux |
| 5 | Mobile Computers | 1990–present | PDAs, Symbian, Blackberry, iOS, Android |

🧠 **Memory trick:** *"Very Tired Individuals Program Mobiles"* → Vacuum, Transistors, ICs, Personal, Mobile

**Batch Processing (Gen 2) workflow:**
Programmers bring cards → 1401 reads onto tape → Operator carries to 7094 → 7094 computes → Operator carries output tape to 1401 → 1401 prints output

**Multiprogramming (Gen 3):** Multiple jobs (Job 1, 2, 3) run simultaneously in separate memory partitions, improving CPU utilization.

---

### What is an Operating System?

An **OS** is a collection of software that:
- Manages computer hardware resources
- Provides common services for computer programs
- Acts as an **intermediary** between the user and the hardware

Three ways to think about the OS:
1. **Resource Manager** — manages CPU, memory, disk, I/O
2. **Extended Machine** — turns ugly hardware details into beautiful abstractions for apps
3. **Intermediary** — simplifies and manages complexity

> The OS is the **first program loaded**. All other programs need it to function.

**OS multiplexes resources in two ways:**
- **In time** — different programs take turns using the CPU
- **In space** — memory is split into partitions for different programs

---

### OS Concepts (key terms to know)

- **Processes** — a running program with its own address space
- **Address spaces** — memory allocated to a process
- **Files** — stored data on disk
- **Input/Output** — interaction with hardware devices
- **Protection** — preventing programs from interfering with each other
- **Shell** — the user interface to the OS (command line or GUI)

**Memory Hierarchy (top to bottom = fastest to slowest):**
CPU Registers → Cache (L1, L2, L3) → Main Memory RAM → Secondary Storage (HDD, SSD, ROM/BIOS)

**Types of OS:**
Mainframe · Server · Multiprocessor · Personal Computer · Handheld · Embedded · Sensor node · Real-time · Smart card

**Hardware Architecture Types:**
Commodity computing platforms · Video game consoles · RISC · Midrange computers · Mainframes · Supercomputers

---

### Evolution of IT Infrastructure

| Era | Years | Key Trait |
|-----|-------|-----------|
| Mainframe & Minicomputer | 1959–present | IBM mainframes (1958), DEC minicomputers (1965) |
| Personal Computer | 1981–present | IBM PC (1981), growth of personal software |
| Client/Server | 1983–present | Desktop clients networked to servers; 2-tier or N-tier |
| Enterprise Computing | 1992–present | Integrating disparate networks with Internet standards |
| Cloud & Mobile | 2000–present | Computing power and software delivered over the Internet |

---

### 7 IT Infrastructure Components (memorize with COEDN CI)

1. **C**omputer hardware platforms — Dell, IBM, HP, Lenovo; chips: Intel, AMD, ARM
2. **O**perating system platforms — Server: 65% Unix/Linux, 35% Windows; Client: 90% Windows
3. **E**nterprise software applications — SAP, Oracle (enterprise); BEA (middleware)
4. **D**ata management and storage — IBM DB2, Oracle, SQL Server, MySQL; EMC Corp for physical storage
5. **N**etworking/telecommunications — AT&T, Verizon; Cisco, Alcatel-Lucent (hardware)
6. **I**nternet platforms — IBM, Dell, Oracle, HP (hardware); Amazon, Google (cloud); Microsoft .NET, Oracle Java, Adobe (dev tools)
7. **C**onsulting & system integration services — Accenture, IBM Global Services, Infosys, Wipro

🧠 **Memory trick:** *"Can Oscar Ever Do Nice Internet Consulting?"*

---

## MODULE 3 — Databases & Software Development

### What is a Database?

A **database** is an organized collection of structured information, controlled by a **DBMS** (Database Management System).

🧠 **Analogy:** Database = digital filing cabinet. DBMS = the secretary who finds, stores, and guards your files.

**SQL (Structured Query Language)** — developed at IBM in the 1970s, now an ANSI standard. Used to:
- **Query** — search/retrieve data
- **Manipulate** — add, update, delete records
- **Define** — create/modify table structures

---

### 11 Types of Databases

| Type | Description |
|------|-------------|
| **Relational (RDBMS)** | Tables, rows, columns, keys — like connected Excel sheets |
| **Object-oriented** | Data as objects (Java-style) |
| **Distributed** | Files spread across multiple physical sites/servers |
| **Data Warehouse** | Central repository for fast queries and business analytics |
| **NoSQL** | Unstructured/semi-structured data (posts, logs) |
| **Graph** | Nodes & edges — like a Facebook friend network |
| **Open Source** | Free, open code (PostgreSQL, MySQL) |
| **Cloud Database** | DBaaS — AWS/Google handle the hardware |
| **Multimodel** | Combines relational + document models |
| **Document/JSON** | Stores flexible JSON documents |
| **Self-driving** | AI/ML automates updates, backup, security |

---

### Front-End Development (Client-Side)

The **Front-End Developer** builds what users see, touch, and experience.

🧠 **Analogy:** Website = Restaurant. Front-end = decoration, menu card, lighting, waiter uniforms.

**3 Core Languages:**

| Language | Role | Analogy |
|----------|------|---------|
| **HTML** | Structure / Skeleton | The bones of the page |
| **CSS** | Styling | The clothes / appearance |
| **JavaScript** | Logic / Behavior | The brain / movement |

---

### React.js (UI Library)

Built by Facebook. Makes UIs with **reusable component blocks**.

**Setup steps:**
```
npx create-react-app my-app
cd my-app
npm start
```

Key concepts:
- **Components** — reusable UI pieces (like Lego bricks)
- **State** — memory object that stores data that can change
- **Hooks** — e.g., `useState` for managing dynamic states

---

### Back-End Development (Server-Side)

Handles logic, APIs, database architectures, and background processing.

🧠 **Analogy:** Back-end = Kitchen. You don't see it, but if it breaks, nobody eats.

**Cloud Components:**

| Component | Description |
|-----------|-------------|
| **Virtual Machines (VMs)** | Emulated software computers in the cloud |
| **Containers (Docker)** | Isolated packages of app + all its dependencies |
| **Serverless** | Upload code, run on demand — no OS config needed |

**Node.js:** A JavaScript runtime that lets JS run *outside* the browser (on servers). 
🧠 **Analogy:** JS is a fish that could only live in the aquarium (browser). Node.js gave it legs to walk on land (the server).

---

### What is a Database? (Purpose)
Three main purposes:
- **Storing** — securely saves data digitally
- **Maintaining** — allows updating without losing other data
- **Accessing** — lets you retrieve specific records via queries

---

## MODULE 4 — Utility Platforms & Business Models

### What is a Utility Platform?

A **utility platform** is a software or technology infrastructure that provides various services and functionalities to users. It serves as a **centralized hub** for accessing and managing resources.

🧠 **Analogy:** Like electricity or running water — you don't build the power plant; you just flip a switch.

**Key trait:** Attracts users by providing useful and often free services.

---

### 6 Domains of Utility Platforms

| Domain | Description | Examples |
|--------|-------------|---------|
| **Cloud Computing** | On-demand computing power, storage, networking | AWS, Azure, GCP |
| **Energy Management** | Monitor, control, optimize energy use | Smart grids, sensors, real-time analytics |
| **IoT (Internet of Things)** | Connect, manage, control IoT devices | Device provisioning, remote monitoring |
| **Smart Cities** | Centralized system for urban services | Transportation, utilities, civic services |
| **Data & Analytics** | Process, analyze, visualize data | ML algorithms, data integration, reporting |
| **Communication & Collaboration** | Messaging, video, docs, task management | Slack, Microsoft Teams, Google Workspace |
| **Financial** | Payment processing, banking, investment, crypto | PayPal, exchanges, banking apps |

---

### 9 Types of Software Platforms

Utility Platform · Content Distribution Platform · Data Harvesting Platform · Interaction Network · Technology Platform · Marketplace · On-demand Service Platform · Computing Platform · Content Crowdsourcing Platform

---

### 11-Step Business Model for Software/Hardware

| Step | Name | What It Means |
|------|------|---------------|
| 1 | **Identify Target Market** | Understand needs and preferences of potential customers |
| 2 | **Market Research** | Gather insights into customer needs, competition, trends |
| 3 | **Product Development** | Design and build aligned with market needs |
| 4 | **Pricing Strategy** | Balance costs, competition, and perceived value |
| 5 | **Distribution Channels** | Direct sales, retail, online platforms |
| 6 | **Sales & Marketing** | Promotional strategies, digital advertising |
| 7 | **Customer Support** | Documentation, FAQs, phone, email, chat |
| 8 | **Revenue Generation** | Sales, subscriptions, usage-based pricing |
| 9 | **Continuous Improvement** | Updates, bug fixes, new features |
| 10 | **Partnerships & Expansion** | Collaborations to enter new markets |
| 11 | **Financial Management** | Track sales growth, CAC (Customer Acquisition Cost), LTV (Lifetime Value) |

🧠 **Memory trick:** *"I Make Products, Distributing Sales. Customers Receive Continuous Partnership Finances."*

---

### True/False Quick Review (from class)

- ✅ Identifying target market = understanding customer wants/needs (Step 1)
- ❌ "Data and analysis is a utility platform in Smart Cities" — FALSE. Smart Cities = urban management; Data & Analytics is a *separate* domain.
- ✅ Gathering customer feedback helps products improve (Step 9)
- ✅ Payment processing, banking, and crypto = financial utility platforms
- ❌ "Financial platforms help optimize energy consumption" — FALSE. That's *Energy Management*.
- ❌ "Distribution Channels involves marketing collateral and events" — FALSE. That's Sales & Marketing (Step 6).

---

## MODULE 5 — IDEs & Kotlin

### What is an IDE?

An **Integrated Development Environment** is a comprehensive software suite that consolidates tools to write, edit, compile, test, and debug code in one interface.

**6 Key Features of an IDE:**

| Feature | What It Does |
|---------|-------------|
| **Code Editor** | Syntax highlighting, auto-completion, formatting |
| **Compiler/Interpreter** | Translates source to executable; live error-checking |
| **Collaboration Tools** | Real-time editing, code reviews, in-workspace chat |
| **Version Control** | Direct Git connectivity for branches, merging |
| **Project Management** | File trees, timelines, issue logs |
| **Deployment Options** | Direct connections to hosting/deployment servers |

---

### Popular IDEs in the Industry

| IDE | Best For |
|-----|---------|
| **VS Code** (Visual Studio Code) | Lightweight, cross-platform, IntelliSense, huge extension ecosystem |
| **IntelliJ IDEA** | Java and Kotlin — deep static analysis (JetBrains flagship) |
| **Xcode** | Apple ecosystem — macOS, iOS, watchOS, tvOS |
| **Android Studio** | Android development, built on IntelliJ, advanced emulator |
| **AWS Cloud9** | Browser-based IDE, serverless work, built-in terminal |
| **Eclipse** | Java, C++, PHP via plugins (open-source classic) |
| **PhpStorm / Zend Studio** | PHP, Laravel, Symfony, WordPress |
| **WebStorm** | JavaScript, TypeScript, React, Vue, Angular (JetBrains) |
| **Arduino IDE** | Arduino microcontroller programming |
| **RubyMine** | Ruby and Rails |

---

### Popular Online Compilers/IDEs

| Platform | Key Feature |
|----------|-------------|
| **GeeksforGeeks (GFG)** | Educational portal with smart browser-based IDE |
| **Ideone** | Paste code in dozens of languages, run instantly |
| **Repl.it (Replit)** | Full-stack apps, hosting, coding challenges, collaboration |
| **OnlineGDB** | Fast integrated compiler + debugger for C, C++, Python, Java |
| **JDOODLE** | Minimal — test, save, and share snippets; zero setup |

---

### Introduction to Kotlin

**Kotlin** is a modern, concise, and safer programming language — the official language for Android development.

**6 Key Features:**

| Feature | What It Means |
|---------|--------------|
| **Concise Syntax** | Less boilerplate compared to Java |
| **Null Safety** | Nullable vs. non-nullable types — catches NullPointerExceptions at compile time |
| **Extension Functions** | Add behavior to existing classes without modifying or inheriting them |
| **Smart Casts** | Compiler handles type casting automatically after a type check |
| **Coroutines** | Built-in lightweight threads for smooth asynchronous programming |
| **Data Classes** | Concise data holders — auto-generates equals(), hashCode(), toString() |
| **Java Interoperability** | Zero-overhead co-existence with Java code |

**Reading Kotlin Syntax:**
- `fun main(...)` — functions live at the top level; no wrapping class required
- `val world` — immutable/read-only reference (use `var` for mutable)
- `$world` — string interpolation: embeds variable values inside text
- Semicolons are **optional** at the end of a line

**AIDE (Android IDE):** Lets you build native Android `.apk` files directly on your phone/tablet via Google Play.

---

### Fetching JSON Data in the Browser

A basic web data-fetching project uses 3 files:
- `index.html` — page structure and display container
- `style.css` — layout and card presentation
- `script.js` — the fetch request, response handling, error states

---

## MODULE 6 — Firebase & Cloud Backends

### What is Firebase?

**Firebase** is a comprehensive, cloud-based **Backend-as-a-Service (BaaS)** platform provided by **Google**. It gives developers tools and infrastructure to build, scale, and maintain web and mobile apps.

**Why it matters:** Firebase eliminates manual server management — developers focus on user experiences instead of infrastructure.

**Client-Server Workflow:**
```
Your App → REST API Layer → Firebase Database
```
Your frontend app *never* talks to the database directly. It goes through a REST API — same flow whether using Realtime Database or Firestore.

**Supported Platforms:** Android (Kotlin/Java) · iOS (Swift) · JavaScript · Node.js · Unity

---

### 10 Core Firebase Services (must memorize!)

| Service | What It Does |
|---------|-------------|
| **Realtime Database** | Cloud-hosted NoSQL DB, stores data as a JSON tree, syncs across clients in milliseconds — great for chat and multiplayer |
| **Cloud Firestore** | Google's flagship document-based NoSQL DB — collections, complex queries, offline support, multi-region replication |
| **Authentication** | Ready-to-use login flows — email/password, phone, social logins (OAuth) |
| **Cloud Storage** | Object storage for binary assets — photos, videos, audio |
| **Hosting** | Fast, secure static hosting with global CDN, free SSL, custom domain |
| **Cloud Functions** | Serverless — runs backend code in response to events; no standalone server needed |
| **Analytics** | Free app-measurement — tracks usage and engagement |
| **Performance Monitoring** | Visibility into app speed across devices — pinpoints slow renders and latency |
| **Remote Config** | Change app behavior/look without an app store update — A/B testing and feature flags |
| **Cloud Messaging (FCM)** | Cross-platform push notifications and data messages at zero cost |

🧠 **Memory trick for services:** *"Real Cloud Auth Storage Hosts Cloud Analytics, Performing Remote Messaging"*

---

### Creating a Firebase Database (Step-by-Step)

1. Visit `console.firebase.google.com` → "Get started"
2. Sign in with Gmail → "Go to Console"
3. Click "Add project" → name and configure it
4. In dashboard → navigate to "Database" (left sidebar)
5. Click "Create database"
6. Choose model: **Realtime Database** (JSON tree) or **Firestore** (document-based)
7. Set location and security rules
8. Connect your app using the Firebase SDK config

**Security Modes:**

| Mode | Access | Best For |
|------|--------|---------|
| **Test Mode** | Open by default; anyone with URL can read/write/delete; expires in **30 days** | Learning, prototypes, classroom labs |
| **Locked Mode** | Private by default; access only via custom rules; no expiry | Production apps with real users |

⚠️ **Warning:** Always update security rules before deploying any real app!

---

## MODULES 7–8 — Firebase API Part 2 & NoSQL

### JSON (JavaScript Object Notation)

**JSON** = JavaScript Object Notation
- Stores data as **key-value pairs**
- The native format of JavaScript and the **default export format of Firebase**
- Supported by every modern browser and JavaScript runtime

**JSON Value Types:** string, number, boolean, array, nested object

**Example:**
```json
{
  "Address": "Cabatuan",
  "Name": "Someone",
  "Occupation": "Tanod"
}
```

---

### cURL (Client URL)

**cURL** is a command-line tool for transferring data using URLs. Supports HTTP, HTTPS, FTP, and more.

**Used for:**
- Data retrieval
- Form submission
- API testing
- Automation in development pipelines

**HTTP Methods cURL supports:** GET · POST · PUT · DELETE

**Fetching Firebase data with cURL:** Append `.json` to your Firebase database URL in the command prompt → Firebase returns your full data as a live JSON response.

---

### NoSQL Databases

**NoSQL** = "Not Only SQL" — a family of databases designed as an alternative to traditional relational databases.

**Designed for:**
- Large volumes of unstructured or semi-structured data
- Greater flexibility and scalability
- Real-time apps, big data pipelines, content management, distributed cloud environments

**Key characteristic:** No fixed schema — structure can differ between records.

---

### 4 Types of NoSQL Databases (MUST KNOW)

| Type | Description | Use Cases | Examples |
|------|-------------|-----------|---------|
| **Document Databases** | Stores flexible documents (JSON, BSON, XML); structure can differ between records | Content management, e-commerce, mobile apps | MongoDB · CouchDB · Couchbase · MarkLogic |
| **Graph Databases** | Uses nodes and edges to map complex relationships | Social networks, recommendation engines | Neo4j · AllegroGraph · IBM Graph |
| **Key-Value Stores** | Each unique key paired with a single value; extremely fast and scalable | Caching, session management, shopping carts | Redis · DynamoDB · Aerospike · Riak |
| **Wide-Column Stores** | Tables where column names and formatting differ row-by-row; each column stored separately on disk | Fraud detection, analytics | Cassandra · HBase · Amazon SimpleDB |

🧠 **Memory trick:** *"Don't Get Key Wide"* → Document, Graph, Key-Value, Wide-Column

---

### NoSQL Advantages vs. Disadvantages

**✅ Advantages:**
- Simplifies development for real-time web apps using REST APIs
- Flexible data models — no schema migrations needed for new fields
- High scalability for large datasets in analytics and AI applications

**❌ Disadvantages:**
- No universal query language — each system uses its own syntax (unlike SQL)
- Lack of rigid schema removes built-in data integrity safeguards
- Schema consistency must be enforced by the developer, not the DB

---

### Quick Answer Key (from class exercises)

- **JSON** = JavaScript Object Notation (key-value pairs)
- **Graph Database** = uses nodes + edges for relationships
- **cURL** = CLI tool for HTTP requests to APIs
- **Wide-Column Stores** = variable columns per row, disk-level column storage
- **NoSQL** = Not Only SQL; the non-relational database family
- **Test Mode** = allows open access for 30 days (classroom use)
- Firebase cURL: append **`.json`** to your database URL
- **Redis, DynamoDB, Aerospike** = Key-Value Stores (NOT Graph)
- **No universal query syntax** = biggest disadvantage of NoSQL vs. SQL

---

## BONUS MODULE — Git, GitHub & Vercel

### Git — Version Control

**Git** is a **distributed version control system** that tracks every change to your code, who made it, and when.

🧠 **Analogy:** Git = save-game system with checkpoints you can return to anytime. Or "Track Changes" in Word, but for entire projects.

**3 Core Concepts:**

| Concept | Meaning |
|---------|---------|
| **Repository** | The project folder that Git watches |
| **Commit** | A saved snapshot of changes (checkpoint) |
| **Branch & Merge** | Work in parallel, then combine |

**The Git Commit Lifecycle:**
```
Working Directory → Staging Area → Local Repository → Remote Repository
```
The staging area lets you pick exactly what goes into each commit.

**Core Git Commands:**

| Command | What It Does |
|---------|-------------|
| `git init` | Begin tracking a new project |
| `git add` | Stage files for a snapshot |
| `git commit` | Save a checkpoint with a message |
| `git branch / switch` | Create/switch branches to work in isolation |
| `git merge` | Combine branches together |
| `git push / pull` | Share with the remote / get updates |

**Git Alternatives:** Mercurial (distributed, now rare) · SVN (centralized, older) · Perforce (game dev, large binaries)

---

### GitHub — Where Code Lives Together

**GitHub** = cloud platform for hosting Git repos, collaborating, and reviewing code.

🧠 **Analogy:** GitHub = Google Drive for code, plus a social network with profiles, stars, and contributions.

| | Git | GitHub |
|--|-----|--------|
| What | Local version control tool | Online platform |
| Runs | On your machine | In the cloud |
| Does | Tracks changes | Hosts repos, enables collaboration |

**GitHub Key Features:**
- **Pull Requests** — propose changes, get reviews before merging
- **Issues & Project Boards** — track bugs, tasks, and roadmap
- **Actions** — automate testing and CI/CD pipelines
- **GitHub Pages** — host static sites directly from a repo

**GitHub Alternatives:** GitLab (self-hosted, built-in CI/CD) · Bitbucket (integrates with Jira/Trello)

---

### Vercel — Push Code, Get a Live URL

**Vercel** is a cloud platform for **frontend deployment**. Built for Next.js, React, and modern frameworks.

**Key Features:**
- **Git Integration** — auto-deploys on every push to GitHub
- **Preview Deployments** — every branch gets its own live URL for testing
- **Global CDN** — fast builds, instant delivery worldwide
- **Free Tier** — perfect for personal projects and prototypes

**Vercel Alternatives:** Netlify (great for static sites) · AWS Amplify (more control, steeper curve) · Railway/Render (backend + databases too)

---

### The Full Pipeline (End-to-End)

```
Write Code locally (Git) → Push to GitHub → Vercel auto-deploys → Live Site
```

| Tool | Role |
|------|------|
| **Git** | The time machine — version control |
| **GitHub** | The shared garage — collaboration |
| **Vercel** | The valet — deployment & hosting |

**Common use cases:** Personal portfolios · Team projects with CI/CD · Open source collaboration

---

## 🔑 Master Cheat Sheet

### Key Definitions to Memorize

| Term | One-Line Definition |
|------|---------------------|
| Platform | Hardware + Software + Networks |
| OS | Software that manages hardware and provides services to programs |
| DBMS | Software that manages a database (the "secretary") |
| SQL | Language to query, manipulate, and define data in relational DBs |
| NoSQL | "Not Only SQL" — non-relational, flexible, scalable database family |
| JSON | Key-value pair data format used by JavaScript and Firebase |
| IDE | All-in-one tool to write, compile, test, and debug code |
| Firebase | Google's Backend-as-a-Service (BaaS) cloud platform |
| Utility Platform | Centralized tech infrastructure providing ready-to-use services |
| Git | Distributed version control system |
| GitHub | Cloud platform for hosting Git repos and team collaboration |
| Vercel | Frontend deployment platform with auto-deploy from GitHub |
| cURL | Command-line tool for making HTTP requests to APIs |
| BaaS | Backend-as-a-Service — cloud backend without managing servers |
| CDN | Content Delivery Network — serves content fast from nearby servers |
| React | Facebook's JavaScript UI library using reusable components |
| Node.js | JavaScript runtime that runs JS outside the browser (on servers) |
| Kotlin | Modern, concise, null-safe language — official Android language |

---

### People & Companies to Know

| Company/Product | Known For |
|----------------|-----------|
| IBM | Mainframes, DB2, first commercial mainframe (1958) |
| Intel, AMD, ARM | Top chip producers |
| Dell, HP, Lenovo | Top hardware firms |
| Microsoft | Windows OS, SQL Server, .NET |
| Oracle | Java, enterprise DB |
| SAP | Enterprise software applications |
| Google | Firebase, GCP, Android |
| Cisco, Alcatel-Lucent | Network hardware |
| AT&T, Verizon | Telecommunications |
| Accenture, IBM Global Services | IT consulting & system integration |
| MongoDB | Document database (NoSQL) |
| Redis | Key-value store (NoSQL) |
| Neo4j | Graph database (NoSQL) |
| Cassandra, HBase | Wide-column store (NoSQL) |

---

*Good luck on your prelims! 🍀 You got this.*
