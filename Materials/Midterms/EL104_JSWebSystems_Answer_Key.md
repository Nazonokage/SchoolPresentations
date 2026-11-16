# EL104 — JS Web Systems Midterms
## Answer Key

**Total: 60 pts**

---

## Part I — Multiple Choice (20 pts)

| # | Answer |
|---|--------|
| 1 | **B) "undefined"** |
| 2 | **C) const** |
| 3 | **C) forEach** |
| 4 | **C) an indented JSON string** |
| 5 | **B) req.params** |
| 6 | **B) express.json()** |
| 7 | **C) PUT** |
| 8 | **B) 201** |
| 9 | **B) documents the intended port** |
| 10 | **A) docker ps** |
| 11 | **B) exclude files from the build context** |
| 12 | **B) Docker layer caching** |
| 13 | **B) find** |
| 14 | **B) copy user's props and add/override age** |
| 15 | **B) (a,b) => a + b** |
| 16 | **B) stringifies data & sets Content-Type** |
| 17 | **B) node:20-alpine** |
| 18 | **B) -p 8080:3000** |
| 19 | **B) expose values for require() elsewhere** |
| 20 | **C) reduce** |

---

## Part II — Identification (10 pts)

1. **docker run -d** (or `docker run --detach` / `-d` flag)
2. **res.json()** (or `res.json`)
3. **map**
4. **Backtick** `` ` `` (template literal)
5. **WORKDIR**
6. **docker build -t <name> .** (or `docker build -t`)
7. **Destructuring** (or destructuring assignment)
8. **fs** (or `fs` module / `require('fs')`)
9. **req.query**
10. **404**

---

## Part III — Situational Identification (10 pts)

1. **JSON.stringify** (or `JSON.stringify()`)
2. **forEach**
3. **express.json()** (middleware)
4. **req.params** (or `req.params.id`)
5. **-d** (or `--detach` / detached mode)
6. **Layer caching** (or Docker layer caching / build cache)
7. **.dockerignore**
8. **Because `y` was declared with `const`** (immutable binding / cannot reassign)
9. **req.query** (or `req.query.role`)
10. **express.static()** (or `express.static('public')`)

---

## Part IV — Guess the Output (5 pts)

1. **`[2, 4, 6, 8]`**
2. **`{"a":1,"b":2}`**
3. **B**
4. **Rae is 18**
5. **2**

---

## Part V — Coding Problems (15 pts)

### 1. Filter + Map (one-liner)

```js
const result = students.filter(s => s.gwa <= 1.75).map(s => s.name);
// → ["Ana", "Cy"]
```

### 2. Express GET /api/students

```js
app.get('/api/students', (req, res) => {
  res.status(200).json(students);
});
```

*(Also acceptable: `res.json(students)` — 200 is the default status)*

### 3. Minimal Dockerfile

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install --omit=dev
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

*(Acceptable variants: `npm ci --only=production` or `npm install --production`)*

---

***End of Answer Key***
