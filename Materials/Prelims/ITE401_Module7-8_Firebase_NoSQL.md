# 🔥 ITE 401 — Platform Technologies
## Module 7–8: Firebase API Part 2 & Not Only Sequel (NoSQL)

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/firebase/firebase-plain-wordmark.svg" alt="Firebase" width="110" style="margin: 8px 0;"/>

> *"Strive for progress, not perfection."*

---

| Field | Details |
|---|---|
| **Course Code** | ITE 401 — Platform Technologies |
| **Module** | #7–8 |
| **Topic** | Firebase API Part 2 & NoSQL Databases |
| **Delivery** | Lecture + Hands-On Lab |

---

## 🎯 Learning Targets

By the end of this module, you will be able to:

1. Use a **Gmail account** to create a Firebase project and set up a Realtime Database.
2. **Retrieve data** from a Firebase Realtime Database using the OS Command Line Interface (CLI) via **cURL**.

**Materials:** Student Activity Sheets, Firebase Console, Windows Command Prompt

**References:**
- https://en.wikipedia.org/wiki/JSON
- https://console.firebase.google.com/
- https://en.wikipedia.org/wiki/CURL
- https://www.techtarget.com/searchdatamanagement/definition/NoSQL-Not-Only-SQL
- https://www.youtube.com/watch?v=L_U6qDI1uKo

---

---

## A. Lesson Preview & Review

### Introduction

In the previous module, we explored the **Firebase API** — a powerful toolset that enables developers to build real-time web applications quickly. Now we go one step further: learning how to **store and retrieve data** using the Firebase **Realtime Database** (a cloud-hosted NoSQL database) and how to interact with that data from the command line.

Before we dive into new content, let's do a quick review:

> **❓ Review Question:** What are the services that Firebase offers?

---

### 📌 Key Terms to Know Before You Begin

| Term | Quick Definition |
|---|---|
| **Firebase** | A Google Backend-as-a-Service (BaaS) platform providing databases, authentication, hosting, and more. |
| **Realtime Database** | Firebase's cloud NoSQL database that stores and syncs data in real time. |
| **JSON** | JavaScript Object Notation — a lightweight data format for storing and exchanging data. |
| **NoSQL** | "Not Only SQL" — databases that don't rely on traditional relational table structures. |
| **cURL** | A command-line tool for transferring data using URLs and HTTP methods. |
| **CLI** | Command Line Interface — a text-based interface to interact with your OS or applications. |

---

---

## B. Main Lesson

---

### 🔑 What is JSON?

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript / JSON" width="70"/>

**JSON (JavaScript Object Notation)** is a data format designed to be both human-readable and machine-parseable. Key facts:

- It is a **lightweight**, easy-to-read **data interchange format**.
- Data is represented as **key-value pairs** — each key is a string, and each value can be a string, number, array, object, boolean, or null.
- It is **widely used** for transmitting data between a server and a web application.
- It is the **native data format** supported by JavaScript, making it ideal for web development.
- In Firebase, **JSON is the default format** for storing, viewing, and exporting Realtime Database data.

#### Example: A JSON Object

```json
{
  "name": "Maria Santos",
  "age": 20,
  "id": "2024-001-IT",
  "location": "Cebu City",
  "course": "BS Information Technology"
}
```

Each entry follows the pattern `"key": value`. String values are enclosed in double quotes; numbers are not.

---

### 🏗️ Working with Firebase Realtime Database

Follow these steps to create a Firebase project, build a Realtime Database, populate it with data, and export it as JSON.

---

#### Step 1 — Go to the Firebase Console

Sign in to the Firebase Console using your **Google account**:

🔗 [https://console.firebase.google.com/](https://console.firebase.google.com/)

---

#### Step 2 — Add or Select a Project

- If you already have projects, they appear on the **Firebase dashboard**. Select the one you want to work in.
- To start fresh, click the **"+ Add project"** card.
- You can also switch between projects using the **project selector dropdown** at the top-left of the console.

---

#### Step 3 — Create a New Project

1. Click the **`+` (Add project)** card on the Firebase dashboard.
2. **Enter a project name** (e.g., `student-db-project`).
3. Click **Continue**.
4. When prompted, **enable Google Analytics** for this project.
5. In the dropdown, select the **Default Account for Firebase** under Google Analytics.
6. Click **Create Project** and wait for initialization to complete.
7. Click **Continue** when the project is ready.

---

#### Step 4 — Create a Realtime Database

1. In the **left sidebar**, click **Build** to expand the menu.
2. Select **Realtime Database** from the dropdown.
3. Click the **"Create Database"** button on the main panel.

**Configure your database in two sub-steps:**

**Sub-step A — Database Options:**
- Under *Realtime Database location*, select **`United States (us-central1)`**.
- Click **Next**.

**Sub-step B — Security Rules:**
- Select **"Start in test mode"** to allow open access during development.
- Click **Enable**.

> ⚠️ **Important Warning:** Test mode security rules allow **anyone** to read and write to your database for 30 days. This is fine for learning, but you **must** update your security rules before deploying any real application.

Default test mode rules look like this:

```json
{
  "rules": {
    ".read": "now < 1693440000000",
    ".write": "now < 1693440000000"
  }
}
```

---

#### Step 5 — Add Data to Your Database

1. Inside the Realtime Database view, find your **database URL** (e.g., `https://your-project-default-rtdb.firebaseio.com/`).
2. Click the **`+` icon** to the right of the URL to add a new key-value entry.
3. Enter a **key** (field name) and a **value**, then click **Add**.
4. Repeat for each field you want to store.

**Sample data to enter:**

| Key | Value |
|---|---|
| `name` | `"Maria Santos"` |
| `age` | `20` |
| `id` | `"2024-001-IT"` |
| `location` | `"Cebu City"` |
| `course` | `"BS Information Technology"` |

After entering all fields, your database tree will look like this:

```
https://your-project-default-rtdb.firebaseio.com/
  ├── age: 20
  ├── course: "BS Information Technology"
  ├── id: "2024-001-IT"
  ├── location: "Cebu City"
  └── name: "Maria Santos"
```

---

#### Step 6 — Export Data as JSON

1. Click the **three-dot menu (⋮)** on the far-right of your database URL row.
2. Select **"Export JSON"** from the options.
3. A `.json` file containing all your database data will be downloaded to your computer.

---

### 💻 What is cURL?

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" alt="Bash / CLI" width="70"/>

**cURL** (Client URL) is:

- A **command-line tool and library** used for transferring data with URLs.
- Capable of making various HTTP requests: `GET`, `POST`, `PUT`, `DELETE`, and more.
- Widely used in **scripting, programming, and API testing** for tasks like data retrieval, form submission, and service interaction.
- Pre-installed on modern versions of Windows 10/11, macOS, and most Linux distributions.

---

### 🖥️ Displaying Firebase Data in the CLI Using cURL

These steps walk you through retrieving your Realtime Database data and displaying it directly in **Windows Command Prompt**.

#### Prerequisites
Download and install cURL (if not already on your system):  
🔗 [https://curl.se/download.html](https://curl.se/download.html)

---

#### Steps

**1. Open Command Prompt**

Press `Win + R`, type `cmd`, and press Enter. You'll see:

```batch
Microsoft Windows [Version 10.0.22621.1992]
(C) Microsoft Corporation. All rights reserved.

C:\Users\Administrator>
```

**2. Navigate to the Windows System directory**

```batch
C:\Users\Administrator> cd\

C:\> cd windows

C:\Windows> cd system

C:\Windows\System>
```

**3. Verify cURL is installed**

```batch
C:\Windows\System> curl --help
```

This prints the cURL help menu. If you see it, cURL is ready to use.  
You can also run `curl -V` to see the version number.

**4. Test the Firebase URL without `.json`**

```batch
C:\Windows\System> curl "https://your-project-default-rtdb.firebaseio.com/"
```

This returns an empty or redirect response — Firebase requires the `.json` suffix.

**5. Append `.json` to retrieve your data**

```batch
C:\Windows\System> curl "https://your-project-default-rtdb.firebaseio.com/.json"
```

> 📌 **Key Rule:** Always append **`.json`** to the end of your Firebase Realtime Database URL when using cURL. This tells Firebase to return the data in JSON format.

**6. Expected Output**

```json
{"age":20,"course":"BS Information Technology","id":"2024-001-IT","location":"Cebu City","name":"Maria Santos"}
```

Your data from Firebase is now displayed directly in the Command Prompt. 🎉

---

### 🗄️ What is NoSQL (Not Only SQL)?

**NoSQL** is a broad term for databases that provide an alternative to traditional relational (SQL) databases. The name stands for **"Not Only SQL"** — meaning these systems can support query languages other than SQL, or none at all.

NoSQL databases are designed to:
- Handle **large volumes of unstructured or semi-structured data**.
- Offer **greater flexibility** without requiring a fixed table schema.
- Provide **higher scalability** for distributed, cloud-based, and high-traffic applications.
- Excel in situations where traditional SQL databases are too rigid or slow.

---

### 📦 Four Popular Types of NoSQL Databases

---

#### 1. 📄 Document Databases

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original-wordmark.svg" alt="MongoDB" width="90"/>

Also called **document stores**, these databases store semi-structured data and metadata together in flexible **document format** (such as JSON, BSON, or XML).

- Use of document databases has grown alongside JavaScript and the adoption of JSON.
- Documents can hold nested data structures, making them very flexible.
- **Best for:** content management systems, blogging platforms, web analytics, mobile application data handling, and e-commerce.

**Examples:** MongoDB, CouchDB, Couchbase Server, MarkLogic

---

#### 2. 🔗 Graph Databases

Graph databases organize data as **nodes** (entities, similar to rows in a relational DB) and **edges** (connections/relationships between nodes).

- Because the graph system stores relationships directly, it can represent **richer, more complex data relationships** than relational models.
- Unlike relational models with rigid schemas, the graph data model can **evolve over time** as requirements change.
- **Best for:** social media platforms, reservation systems, customer relationship management (CRM), fraud detection networks.

**Examples:** AllegroGraph, IBM Graph, Neo4j

---

#### 3. 🔑 Key-Value Stores

Also known as **key-value databases**, these systems implement a simple data model that pairs a **unique key** with an **associated value**. Due to their simplicity, they are extremely fast and scalable.

- Ideal when you need quick lookups without complex queries.
- **Best for:** session management, caching, shopping cart data for online stores, managing session details for multiplayer gaming.

**Examples:**

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original-wordmark.svg" alt="Redis" width="90"/>

Redis, Aerospike, DynamoDB, Riak

---

#### 4. 📊 Wide-Column Stores

These databases use familiar **tables, columns, and rows** — similar to relational databases — but with a key difference: **column names and formatting can differ from row to row** within a single table. Each column is also stored separately on disk.

- As opposed to traditional row-orientated storage, a wide-column store is **optimal when querying data by columns**.
- **Best for:** recommendation engines, product catalogs, fraud detection, event logging.

**Examples:** Apache Cassandra, HBase, Accumulo, Amazon SimpleDB, Hypertable

---

### ✅ Advantages of NoSQL Databases

| Advantage | Explanation |
|---|---|
| **Simplified App Development** | Streamlines development for interactive, real-time web apps using REST APIs and web services. |
| **Flexible Data Models** | Handles non-normalized data or data with varying properties per entity — no schema changes needed. |
| **High Scalability** | Scales efficiently for large datasets, making it ideal for analytics and AI/ML applications. |
| **Cloud & Mobile Ready** | Well-suited for cloud environments, mobile apps, social media platforms, and big data pipelines. |
| **Use-Case Optimized** | Easier to use than general-purpose SQL databases for specific application types (real-time, distributed, etc.). |

---

### ❌ Disadvantages of NoSQL Databases

| Disadvantage | Explanation |
|---|---|
| **No Universal Query Language** | Each NoSQL system has its own query syntax; there is no universal standard like SQL. |
| **Weaker Data Integrity** | The lack of a rigid schema removes the built-in integrity safeguards of relational systems. |
| **Developer-Managed Schema** | Ensuring schema consistency is the **developer's responsibility**, not the database system's. |
| **Eventual Consistency** | Most NoSQL databases use eventual consistency, making them unsuitable for transactions requiring immediate data accuracy (e.g., banking, ATM withdrawals). |
| **No Industry Standards** | NoSQL is relatively newer — no comprehensive cross-system standards exist as with SQL/relational DBMSes. |

---

---

## C. Lesson Wrap-Up / FAQs

---

### ❓ FAQ 1: What is NoSQL and why is it used?

**NoSQL** databases use a variety of data models for accessing and managing data. They are specifically designed for applications that require:

- **Large data volumes** — handling massive amounts of structured or unstructured data efficiently.
- **Low latency** — delivering data quickly for real-time user experiences.
- **Flexible data models** — achieved by relaxing some of the strict data consistency requirements that SQL databases impose.

NoSQL is widely chosen for applications like social media feeds, recommendation engines, IoT data streams, and mobile backends — anywhere traditional SQL would become a bottleneck.

---

### ❓ FAQ 2: What is the difference between CMD and CLI?

| Term | Description |
|---|---|
| **CLI (Command Line Interface)** | The **general concept** of a text-based interface for interacting with a computer or application. It takes typed commands as input and returns text-based output. CLI requires a *shell* to run (e.g., Bash, Zsh, PowerShell). |
| **CMD (Command Prompt)** | A **specific Windows application** that serves as Microsoft's implementation of a CLI. It functions similarly to Shell on Unix/Linux/macOS systems but is specific to the Windows OS. |

> **In short:** CLI is the *broad concept* — the category. CMD (Command Prompt) is the *specific Windows tool* that falls into that category. On macOS and Linux, the equivalent is the **Terminal (Shell)**.

---

---

## D. Guided Drills / Code Projects

### 🛠️ Project: Build and Query a Firebase Student Profile Database

**Objective:** Create a Firebase Realtime Database with student profile data, then retrieve and display it via cURL from the Command Prompt.

---

#### Part 1 — Set Up Your Firebase Project

1. Go to [https://console.firebase.google.com/](https://console.firebase.google.com/) and sign in.
2. Create a new project (or select an existing one).
3. Navigate to **Build → Realtime Database → Create Database**.
4. Choose **Test Mode** and location **`us-central1`**, then click **Enable**.

---

#### Part 2 — Populate the Database

Add the following key-value fields by clicking the `+` icon next to your database URL:

| Key | Value |
|---|---|
| `id` | `"2024-CS-007"` |
| `name` | `"Juan dela Cruz"` |
| `age` | `21` |
| `location` | `"Manila"` |
| `course` | `"BS Computer Science"` |

Your database should display as:

```json
{
  "age": 21,
  "course": "BS Computer Science",
  "id": "2024-CS-007",
  "location": "Manila",
  "name": "Juan dela Cruz"
}
```

---

#### Part 3 — Retrieve Data via cURL

Open **Command Prompt** and execute the following commands in order:

```batch
cd\
cd windows
cd system
curl "https://YOUR-PROJECT-ID-default-rtdb.firebaseio.com/.json"
```

> 🔁 **Replace** `YOUR-PROJECT-ID` with your actual Firebase project ID, visible in your database URL on the Firebase Console.

---

#### Part 4 — Expected Terminal Output

```json
{"age":21,"course":"BS Computer Science","id":"2024-CS-007","location":"Manila","name":"Juan dela Cruz"}
```

If you see your data printed in the terminal, you have successfully completed the hands-on lab. ✅

---

#### Part 5 — Export JSON from Firebase Console

1. In your Realtime Database view, click the **⋮ (three-dot menu)** beside your database URL.
2. Click **Export JSON**.
3. Save the downloaded `.json` file — you may need to submit this as proof of completion.

---

#### Submission Checklist

- [ ] Firebase project created with a Realtime Database
- [ ] All five fields added: `id`, `name`, `age`, `location`, `course`
- [ ] Data retrieved via `curl` command and confirmed in terminal
- [ ] JSON exported from Firebase Console
- [ ] Instructor notified upon completion

---

---

## E. Skill-Building Check

> **Instructions:** Read each description carefully and identify the correct concept or technology it refers to. Write your answer in the space provided.  
> *(2 points each)*

---

### 🧠 Fill in the Blank

---

**Item 1.**
*"It can be used to develop highly scalable and performant applications."*

**Answer: `Key-Value Stores` (a type of NoSQL Database)**

---

**Item 2.**
*"It applies to systems that must map relationships, such as social media platforms, reservation systems, or customer relationship management tools."*

**Answer: `Graph Databases`**

---

**Item 3.**
*"It is a kind of NoSQL database that uses familiar tables, columns, and rows — similar to relational databases — but column names and formatting can differ from row to row in a single table."*

**Answer: `Wide-Column Stores`**

---

**Item 4.**
*"It is widely used in scripting and programming for tasks like data retrieval, data submission, and testing APIs."*

**Answer: `cURL`**

---

**Item 5.**
*"It is a common data interchange format with diverse uses in electronic data exchange, including transmitting data between web servers and applications."*

**Answer: `JSON (JavaScript Object Notation)`**

---

### 🗝️ Answer Key Summary

| # | Answer |
|---|---|
| 1 | **Key-Value Stores** (NoSQL) |
| 2 | **Graph Databases** |
| 3 | **Wide-Column Stores** |
| 4 | **cURL** |
| 5 | **JSON** |

---

### 🔁 Quick Concept Recap

| Concept | One-Line Summary |
|---|---|
| **JSON** | Lightweight key-value data format native to JavaScript; used everywhere on the web. |
| **Firebase Realtime Database** | Google's cloud-hosted NoSQL database that syncs in real time. |
| **cURL** | A command-line tool for making HTTP requests and retrieving data from URLs. |
| **NoSQL** | A family of non-relational databases built for flexibility, scale, and speed. |
| **Document DB** | Stores data in flexible document format (e.g., JSON). Example: MongoDB. |
| **Graph DB** | Stores entities as nodes and relationships as edges. Example: Neo4j. |
| **Key-Value Store** | Pairs a unique key with a value. Simple, fast, and scalable. Example: Redis. |
| **Wide-Column Store** | Tables where column names can vary per row. Example: Cassandra. |

---

> 📘 **Module Complete!** You now know how to create a Firebase Realtime Database, populate it with structured data, retrieve that data using cURL from the command line, and understand the fundamentals of NoSQL database types and their trade-offs.

---

*Module 7–8 | ITE 401 — Platform Technologies*  
*Document generated for educational reference only.*
