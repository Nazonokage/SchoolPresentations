
# Node.js Web Systems – Comprehensive Reviewer

> A complete study guide covering Node.js fundamentals, HTTP servers, MVC architecture, SQL JOINs, and backup/recovery — all in JavaScript (Node.js). No PHP code here; everything is reimplemented in Node.js.

---

## Table of Contents

1. [Node.js Introduction (Modules 10–11)](#1-nodejs-introduction-modules-10-11)
   - What is Node.js?
   - The V8 Engine
   - Event Loop & Non‑blocking I/O
   - Core Modules
   - npm & `package.json`
   - CommonJS Modules
   - Global Objects

2. [Node.js HTTP Server (Module 12)](#2-nodejs-http-server-module-12)
   - The `http` Module
   - Creating a Server
   - Handling Requests & Responses
   - Listening on a Port
   - Complete Example

3. [MVC Architecture (Module 13)](#3-mvc-architecture-module-13)
   - What is MVC?
   - Model – View – Controller
   - Express.js & Routing
   - Mongoose Models
   - EJS Views
   - Folder Structure & Full Example

4. [SQL JOINs in Node.js (Module 6)](#4-sql-joins-in-nodejs-module-6)
   - JOIN Types
   - Using `mysql2` in Node.js
   - Example Queries

5. [Backup & Recovery in Node.js (Modules 7–8)](#5-backup--recovery-in-nodejs-modules-7-8)
   - Why Backup Matters
   - Using `mysqldump` via `child_process`
   - Restoring with `mysql`
   - Example Scripts
   - Best Practices

6. [Key Concepts & Tips](#6-key-concepts--tips)

7. [Sample Quiz Questions](#7-sample-quiz-questions)

---

## 1. Node.js Introduction (Modules 10–11)

### What is Node.js?
- **Open‑source, cross‑platform JavaScript runtime** built on Chrome's V8 engine.
- Allows JavaScript to run **outside the browser** – on servers, desktops, IoT devices.
- Uses an **event‑driven, non‑blocking I/O** model – efficient for I/O‑heavy applications.

### The V8 Engine
- Developed by Google for Chrome.
- Compiles JavaScript directly to **machine code** (just‑in‑time compilation).
- Node.js wraps V8 and adds **server‑side APIs** (file system, networking, etc.).

### Event Loop & Non‑blocking I/O
- **Non‑blocking I/O**: when a request involves waiting (file read, DB query), Node.js delegates the task to the OS and immediately moves on to the next request.
- The **event loop** continuously checks for completed operations and executes their callbacks.
- Order of execution:
  1. Synchronous code (call stack)
  2. `process.nextTick()` (highest priority microtasks)
  3. Promise callbacks (microtasks)
  4. Timers (`setTimeout`, `setInterval`)
  5. I/O callbacks

```javascript
// Example: event loop order
console.log('1 - sync');

setTimeout(() => console.log('4 - timer'), 0);

Promise.resolve().then(() => console.log('3 - promise'));

process.nextTick(() => console.log('2 - nextTick'));

console.log('5 - sync end');
// Output: 1, 5, 2, 3, 4
```

### Core Modules (built‑in)
- `http` – create HTTP servers and clients
- `fs` – file system operations
- `path` – path manipulation
- `os` – operating system information
- `events` – event emitter

> No need to install – just `require()`.

### npm & `package.json`
- **npm** is the default package manager (world's largest software registry).
- `package.json` – manifest file:
  - `name`, `version`, `description`
  - `main` – entry point
  - `scripts` – aliases for commands (`npm start`, `npm run dev`)
  - `dependencies` – production packages
  - `devDependencies` – development tools (testing, linting, etc.)

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "main": "app.js",
  "scripts": {
    "start": "node app.js",
    "dev": "nodemon app.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "nodemon": "^3.0.0"
  }
}
```

### CommonJS Modules
- Use `require()` to import, `module.exports` to export.
- Node.js uses CommonJS by default (ES modules are also supported with `"type": "module"`).

```javascript
// math.js
function add(a, b) { return a + b; }
function multiply(a, b) { return a * b; }
module.exports = { add, multiply };

// app.js
const { add, multiply } = require('./math');
console.log(add(2, 3)); // 5
```

### Global Objects
- `process` – environment, arguments, exit
- `__dirname` – absolute path of current directory
- `__filename` – absolute path of current file
- `console` – logging
- `require`, `module`, `exports`

---

## 2. Node.js HTTP Server (Module 12)

### The `http` Module
- Provides `createServer()` to instantiate an HTTP server.
- Every request triggers a callback with `req` (request) and `res` (response).

### Creating a Server

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  // handle request
});
```

### Handling Requests & Responses
- `req` – contains method, URL, headers, body (stream)
- `res` – use `statusCode`, `setHeader()`, and `end()` to send response.

```javascript
const server = http.createServer((req, res) => {
  res.statusCode = 200;               // OK
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!');
});
```

### Listening on a Port
```javascript
server.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
```

### Complete Example

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello from my first Node.js server!');
});

server.listen(3000, () => {
  console.log('Server running at http://localhost:3000/');
});
```

**Run:** `node server.js`  
**Test:** `curl http://localhost:3000` or open in browser.  
**Stop:** Press `Ctrl + C`.

---

## 3. MVC Architecture (Module 13)

### What is MVC?
- **Model-View-Controller** – a design pattern that separates an application into three interconnected components.
- **Separation of Concerns** – each component has a distinct responsibility.

| Component | Role |
|-----------|------|
| **Model** | Manages data and business logic (database, APIs). |
| **View**   | Renders the user interface (HTML, templates). |
| **Controller** | Mediates between Model and View; handles requests, invokes Model, selects View. |

### Express.js & Routing
- Express is a minimal web framework for Node.js that simplifies routing and middleware.
- Routes are defined using `app.get()`, `app.post()`, etc.

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.render('index', { user: { name: 'Alice' } });
});

app.post('/login', authController.login);
```

### Mongoose Models
- Mongoose is an ODM for MongoDB, providing schema validation and model methods.

```javascript
// models/User.js
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true }
});

module.exports = mongoose.model('User', userSchema);
```

### EJS Views
- Embedded JavaScript templates – embed JS logic inside HTML.

```html
<!-- views/index.ejs -->
<h1>Welcome</h1>
<% if (user) { %>
  <p>Hello, <%= user.name %></p>
<% } else { %>
  <a href="/login">Login</a>
<% } %>
```

### Folder Structure (Typical MVC)

```
my-app/
├── models/
│   └── User.js
├── views/
│   └── index.ejs
├── controllers/
│   ├── authController.js
│   └── homeController.js
├── routes/
│   └── index.js
├── app.js
└── package.json
```

### Full Example: MVC with Express + Mongoose + EJS

**app.js**

```javascript
const express = require('express');
const mongoose = require('mongoose');
const homeController = require('./controllers/homeController');

const app = express();

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/mvc-demo');

// Set view engine
app.set('view engine', 'ejs');

// Body parsers
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Routes
app.get('/', homeController.getHomePage);

app.listen(3000, () => console.log('Server running on port 3000'));
```

**controllers/homeController.js**

```javascript
exports.getHomePage = (req, res) => {
  // In real app, fetch from Model
  const user = { name: 'Student Developer' };
  res.render('index', { user });
};
```

**views/index.ejs**

```html
<!DOCTYPE html>
<html>
<head><title>MVC Demo</title></head>
<body>
  <h1>Welcome to My App</h1>
  <p>Hello, <%= user.name %></p>
</body>
</html>
```

---

## 4. SQL JOINs in Node.js (Module 6)

### JOIN Types
- **INNER JOIN** – returns rows where there is a match in both tables.
- **LEFT JOIN** – all rows from left table, matching rows from right (NULL if no match).
- **RIGHT JOIN** – all rows from right table, matching rows from left.
- **FULL OUTER JOIN** – all rows from both tables (not supported in MySQL; use `UNION` of LEFT and RIGHT).

### Using `mysql2` in Node.js
- Install: `npm install mysql2`
- Create a connection pool or use a promise-based API.

### Example: INNER JOIN

```javascript
const mysql = require('mysql2/promise');

async function getOrdersWithCustomers() {
  const connection = await mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    database: 'shop'
  });

  const [rows] = await connection.execute(`
    SELECT customers.name, orders.order_date, orders.total
    FROM customers
    INNER JOIN orders ON customers.id = orders.customer_id
  `);

  console.log(rows);
  await connection.end();
}

getOrdersWithCustomers();
```

### Example: LEFT JOIN

```javascript
const [rows] = await connection.execute(`
  SELECT customers.name, orders.order_date
  FROM customers
  LEFT JOIN orders ON customers.id = orders.customer_id
`);
```

### Using an ORM (Sequelize)
- Alternatively, you can use Sequelize which provides a more JavaScript-friendly interface.

```javascript
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = new Sequelize('shop', 'root', 'password', { dialect: 'mysql' });

const Customer = sequelize.define('Customer', { name: DataTypes.STRING });
const Order = sequelize.define('Order', {
  order_date: DataTypes.DATE,
  total: DataTypes.FLOAT
});

Customer.hasMany(Order, { foreignKey: 'customer_id' });
Order.belongsTo(Customer);

// Fetch with JOIN
const customersWithOrders = await Customer.findAll({
  include: Order
});
```

---

## 5. Backup & Recovery in Node.js (Modules 7–8)

### Why Backup Matters
- Protects against data loss (hardware failure, human error, corruption, ransomware).
- Ensures business continuity and regulatory compliance.
- Regular backups and tested restores are essential.

### Using `mysqldump` via `child_process`
- Node.js can execute shell commands using `child_process.exec` or `spawn`.
- **Backup**: run `mysqldump` to export the database to a `.sql` file.

```javascript
const { exec } = require('child_process');
const fs = require('fs');

function backupDatabase(host, user, password, database) {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const backupFile = `backup_${timestamp}.sql`;
  const command = `mysqldump --host=${host} --user=${user} --password=${password} ${database} > ${backupFile}`;

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Backup error: ${error.message}`);
      return;
    }
    console.log(`Backup saved to ${backupFile}`);
  });
}

backupDatabase('localhost', 'root', 'secret', 'myapp');
```

### Restoring with `mysql`
- Use the `mysql` command to import the backup file.

```javascript
function restoreDatabase(host, user, password, database, backupFile) {
  const command = `mysql --host=${host} --user=${user} --password=${password} ${database} < ${backupFile}`;

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Restore error: ${error.message}`);
      return;
    }
    console.log(`Database restored from ${backupFile}`);
  });
}
```

### Using `spawn` for Better Control
- `spawn` gives more control over streams and can handle large files without buffering.

```javascript
const { spawn } = require('child_process');
const fs = require('fs');

function backupWithSpawn(host, user, password, database, outputFile) {
  const dump = spawn('mysqldump', [
    `--host=${host}`,
    `--user=${user}`,
    `--password=${password}`,
    database
  ]);

  const writeStream = fs.createWriteStream(outputFile);
  dump.stdout.pipe(writeStream);

  dump.stderr.on('data', (data) => console.error(`stderr: ${data}`));
  dump.on('close', (code) => {
    if (code === 0) console.log('Backup completed');
    else console.error(`Backup process exited with code ${code}`);
  });
}
```

### Best Practices
- **Automate** backups using cron jobs (Linux) or Task Scheduler (Windows).
- **Store backups off‑site** (cloud storage, external drive).
- **Test restores** periodically – an untested backup is not a backup.
- **Keep multiple versions** (e.g., daily, weekly, monthly) and clean up old ones.
- **Use environment variables** for credentials, never hardcode.

---

## 6. Key Concepts & Tips

- **Non‑blocking I/O** enables Node.js to handle high concurrency with a single thread.
- **Event loop** prioritises `nextTick` > Promises > Timers > I/O.
- **Express** simplifies routing and middleware; it’s built on top of the `http` module.
- **MVC** separates concerns, making code maintainable, testable, and scalable.
- **SQL JOINs** are essential for relational data; choose the right type based on what you need.
- **Backup & recovery** is your safety net – always have a plan.

---

## 7. Sample Quiz Questions

### Multiple Choice
1. Which Node.js module is used to create an HTTP server?
   - A) `fs`
   - B) `http`
   - C) `path`
   - D) `os`

2. In the MVC pattern, which component directly interacts with the database?
   - A) Controller
   - B) View
   - C) Model
   - D) Router

3. What is the correct way to stop a running Node.js server in the terminal?
   - A) `server.stop()`
   - B) `Ctrl + C`
   - C) `exit`
   - D) `kill -9`

4. Which SQL JOIN returns all rows from the left table and matching rows from the right?
   - A) INNER JOIN
   - B) LEFT JOIN
   - C) RIGHT JOIN
   - D) FULL OUTER JOIN

5. What is the primary purpose of `package.json`?
   - A) Store database credentials
   - B) Manage project metadata and dependencies
   - C) Define routes
   - D) Configure the server port

### Answers
1. **B** – `http`
2. **C** – Model
3. **B** – `Ctrl + C`
4. **B** – LEFT JOIN
5. **B** – Manage project metadata and dependencies

---

## Final Words

You now have a solid foundation in Node.js web development, covering everything from the runtime basics to building MVC applications, querying relational databases with JOINs, and implementing backup strategies. Practice writing code, experiment with the examples, and always refer back to the official documentation when in doubt.

Happy coding! 🚀