# 📘 Reviewer for Module 5: JSON, Express & Docker  
*Foundations for building, serving, and containerizing a Node.js web app*

---

## 1. JavaScript Fundamentals (Prerequisites)

Before diving into Express and Docker, make sure you are comfortable with these core JS concepts. They appear everywhere in the M5 codebase.

### Variables & Types
- `let` – mutable variable  
- `const` – immutable binding (value can’t be reassigned)  
- Primitives: `string`, `number`, `boolean`, `null`, `undefined`

### Functions
```js
// Declaration
function add(a, b) { return a + b; }

// Expression
const subtract = function(a, b) { return a - b; };

// Arrow function (shorter, no `this` binding)
const multiply = (a, b) => a * b;
```

### Array Methods (🔥 important)
| Method    | Description                                                                 |
|-----------|-----------------------------------------------------------------------------|
| `forEach` | Loops through array – no return value.                                     |
| `map`     | Returns a **new array** by transforming each element.                      |
| `filter`  | Returns a **new array** with only elements that pass a test.              |
| `reduce`  | Folds the array into a single value (e.g., sum, max, etc.).               |
| `find`    | Returns the first element that passes a test.                              |

**Example**  
```js
const students = [
  { name: "Alice", gwa: 1.5 },
  { name: "Bob",   gwa: 1.75 }
];

// map: extract names
const names = students.map(s => s.name); // ["Alice", "Bob"]

// filter: honor students (gwa ≤ 1.5)
const honor = students.filter(s => s.gwa <= 1.5); // [Alice]

// reduce: best GWA (lowest number)
const best = students.reduce((prev, curr) => curr.gwa < prev.gwa ? curr : prev);
// best = { name: "Alice", gwa: 1.5 }
```

### Objects & Nested Access
```js
const user = {
  id: 1,
  name: "Maria",
  contact: {
    email: "maria@school.edu",
    phone: "09171234567"
  },
  tags: ["student", "active"]
};

// Dot notation
console.log(user.name);                 // "Maria"
console.log(user.contact.email);        // "maria@school.edu"

// Bracket notation (when key is variable)
const key = "contact";
console.log(user[key].phone);           // "09171234567"

// Array inside object
console.log(user.tags[1]);              // "active"
```

### Destructuring & Spread (modern ES6)
```js
// Object destructuring
const { name, contact } = user;
console.log(name);          // "Maria"
console.log(contact.email); // "maria@school.edu"

// Array destructuring
const colors = ["red", "green", "blue"];
const [first, second] = colors; // first="red", second="green"

// Spread – copy/merge objects
const updatedUser = { ...user, age: 21 }; // adds age, keeps rest
```

### Template Literals (backticks)
```js
const greeting = `Hello, ${name}!`;   // "Hello, Maria!"
```

### Modules (CommonJS in Node)
```js
// data/students.js
const students = [ /* ... */ ];
module.exports = students;

// another file
const students = require('./data/students');
```

---

## 2. Multidimensional Arrays & Nested Structures

### Array of Arrays (2D grid)
```js
const grades = [
  ["Alice", 88, 92, 79],
  ["Bob",   74, 68, 85],
  ["Charlie", 95, 91, 97]
];
console.log(grades[0][2]); // 79 (third column of first row)
```

### Array of Objects (more readable)
```js
const students = [
  { id: 1, name: "Alice", course: "BSCS", year: 2 },
  { id: 2, name: "Bob",   course: "BSIT", year: 3 }
];
console.log(students[1].name); // "Bob"
```

### Mixed / Nested
```js
const catalog = [
  {
    id: "p01",
    name: "Keyboard",
    specs: { brand: "Keychron", wireless: true },
    tags: ["electronics", "peripherals"]
  }
];
console.log(catalog[0].specs.brand);   // "Keychron"
console.log(catalog[0].tags[1]);       // "peripherals"
```

---

## 3. JSON – JavaScript Object Notation

**JSON is a string** that looks like a JS object. Used to send data over networks.

| Operation              | Code                                  | Result                      |
|------------------------|---------------------------------------|-----------------------------|
| JS object → JSON string | `JSON.stringify(obj)`                | `'{"name":"Alice","age":20}'` |
| JSON string → JS object | `JSON.parse(jsonString)`             | returns a real JS object    |
| Pretty print           | `JSON.stringify(obj, null, 2)`       | indented with 2 spaces      |

**Example**
```js
const obj = { name: "Alice", age: 20 };
const json = JSON.stringify(obj);   // '{"name":"Alice","age":20}'
const parsed = JSON.parse(json);    // { name: "Alice", age: 20 }
console.log(parsed.name);           // "Alice"
```

> 💡 In Express, `res.json(data)` does `JSON.stringify` + sets `Content-Type` automatically.

---

## 4. Express – Web Framework for Node

### Setup
```bash
npm init -y
npm install express
```

### Basic Server (`server.js`)
```js
const express = require('express');
const app = express();
const PORT = 3000;

// Route
app.get('/', (req, res) => {
  res.send('Hello World');
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
```

### Key Route Methods
| Method | Purpose                | Express code                      |
|--------|------------------------|-----------------------------------|
| GET    | retrieve data          | `app.get('/path', handler)`      |
| POST   | create data            | `app.post('/path', handler)`     |
| PUT    | replace / update       | `app.put('/path', handler)`      |
| DELETE | delete data            | `app.delete('/path', handler)`   |

### Request & Response Objects
- `req.params` – URL parameters (e.g., `/users/:id`)
- `req.query` – query string (e.g., `?role=admin`)
- `req.body` – parsed request body (needs `express.json()` middleware)
- `res.send()` – send HTML, text, or JSON
- `res.json()` – send JSON (stringifies automatically)
- `res.status(code)` – set HTTP status (e.g., 404)

### Serving Static Files
```js
app.use(express.static('public'));
```
Now files in `public/` (e.g., `style.css`) are served at `http://localhost:3000/style.css`.

### Reading a Template & Injecting Data
```js
const fs = require('fs');
const path = require('path');

app.get('/students', (req, res) => {
  let html = fs.readFileSync(path.join(__dirname, 'views', 'students.html'), 'utf8');
  const cards = students.map(s => `<div class="card">...</div>`).join('');
  html = html.replace('{{count}}', students.length).replace('{{cards}}', cards);
  res.send(html);
});
```

> 📁 **Project Structure** (M5 example)
```
m5-express/
├── data/students.js        ← array of student objects
├── views/students.html     ← HTML template with {{placeholders}}
├── server.js               ← main Express app
├── package.json
├── Dockerfile
└── .dockerignore
```

---

## 5. Docker – Containerization

### What Docker Does
Packages your app + its environment (Node, dependencies, files) into an **image**. The image runs as an isolated **container**.

### Dockerfile (minimal for Node app)
```dockerfile
FROM node:20-alpine          # light base image
WORKDIR /app                 # working directory inside container
COPY package*.json ./        # copy package files first (layer caching)
RUN npm install --omit=dev   # install dependencies
COPY . .                     # copy all source code
EXPOSE 3000                  # document the port
CMD ["node", "server.js"]    # start command
```

### .dockerignore (exclude unnecessary files)
```
node_modules
.git
.env
```

### Commands
| Command                                           | Description                                          |
|---------------------------------------------------|------------------------------------------------------|
| `docker build -t m5-express .`                    | Build image tagged `m5-express` from Dockerfile     |
| `docker run -p 3000:3000 m5-express`              | Run container, map host:3000 → container:3000       |
| `docker run -d -p 3000:3000 --name m5-app m5-express` | Run in background (detached)                   |
| `docker ps`                                       | List running containers                              |
| `docker logs m5-app`                              | View logs                                            |
| `docker stop m5-app`                              | Stop container                                       |
| `docker rm m5-app`                                | Remove container                                     |
| `docker rmi m5-express`                           | Remove image                                         |

### Port Mapping
`-p HOST_PORT:CONTAINER_PORT`  
Your browser hits `localhost:3000` → Docker forwards to the container’s port 3000 where Node is listening.

---

## 6. The M5 Project Flow (Step by Step)

1. **Data** – create `data/students.js` with an array of student objects, export it.
2. **Situation 1** – write `situation1.js` that `require()`s the data, logs it with `JSON.stringify`, filters active students, uses `reduce` to find best GWA. Run with `node situation1.js`.
3. **Situation 2** – build Express app (`server.js`):
   - Serve static files from `public/`.
   - Route `/students`: read HTML template, generate cards via `map()`, replace `{{count}}` and `{{cards}}`, send the resulting HTML.
   - Route `/api/students`: send raw JSON with `res.json(students)`.
   - Run locally with `node server.js`.
4. **Dockerize** – add `Dockerfile` and `.dockerignore`. Build image, run container, test that `http://localhost:3000/students` works inside the container.

---

## 7. Quick Reference – HTTP Status Codes & Verbs

| Verb     | Typical Use            | Example URL        |
|----------|------------------------|---------------------|
| GET      | Retrieve data          | `/students`         |
| POST     | Create new record      | `/students`         |
| PUT      | Replace entire record  | `/students/1`       |
| PATCH    | Partially update       | `/students/1`       |
| DELETE   | Remove record          | `/students/1`       |

| Status Code | Meaning                |
|-------------|------------------------|
| 200 OK      | Success                |
| 201 Created | Created new resource   |
| 400 Bad Request | Client error      |
| 404 Not Found | Resource missing     |
| 500 Internal Server Error | Server error |

---

## 8. Key Takeaways

- **JSON** is a string – use `JSON.stringify` to send, `JSON.parse` to read.
- **Array methods** like `map`, `filter`, `reduce` are essential for data transformation.
- **Express** turns Node into a web server; routes map URLs to handler functions.
- **Docker** encapsulates the app and its runtime, making it portable and reproducible.

---

## ✅ Self-Check Questions

1. Write code to extract all names from an array of objects.
2. Convert a JS object to a JSON string with 4-space indentation.
3. Write an Express route that responds with a JSON array of users.
4. Explain why we copy `package*.json` before `COPY .` in a Dockerfile.
5. What command maps host port 8080 to container port 3000?

---

*Good luck – you’ve got this!* 🚀