# Answer Key  
**DC104 Advanced Database — Midterm Periodical Exam**  
Items: 39 | Points: 55

---

## I. Multiple Choice

| # | Answer | Notes |
|---|--------|-------|
| 1 | **B** | Single-threaded non-blocking event loop |
| 2 | **B** | Create a copy of data for protection against loss |
| 3 | **C** | LEFT JOIN keeps all left-table rows |
| 4 | **C** | `http` module |
| 5 | **B** | `mysqldump` |
| 6 | **C** | Controller mediates Model ↔ View |
| 7 | **C** | `ON` keyword |
| 8 | **C** | Ctrl + C (SIGINT) |
| 9 | **B** | Recovery |
| 10 | **C** | Model (business logic / data) |

| 11 | **B** | Project metadata & dependencies |
| 12 | **C** | `system()` |
| 13 | **C** | All rows from both tables, NULL where no match |
| 14 | **C** | `require('http');` (CommonJS) |
| 15 | **B** | Present data to the user |
| 16 | **B** | False — Node.js is a runtime, not a language |
| 17 | **B** | False — INNER returns only matching rows |
| 18 | **B** | False — backups matter for every application |
| 19 | **B** | False — the View renders HTML |
| 20 | **A** | True — `res.end()` finalizes the response |

---

## II. Identification

| # | Answer |
|---|--------|
| 21 | recovery *(or database recovery / restore)* |
| 22 | LEFT |
| 23 | fs |
| 24 | View |
| 25 | .sql |
| 26 | node |
| 27 | ON |
| 28 | MVC *(or Model-View-Controller)* |
| 29 | mysql |
| 30 | listen |

---

## III. Guess the Output

| # | Answer |
|---|--------|
| 31 | listening |
| 32 | 2 |
| 33 | backup_done |
| 34 | 4 |
| 35 | 125 |

---

## IV. Coding Problems — Sample Solutions

### 36. HTTP Server (5 pts)

```js
const http = require('http');

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Welcome to the Community Library!');
});

server.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

### 37. backupDatabase with mysqldump (5 pts)

```js
const { exec } = require('child_process');

function backupDatabase(host, user, password, database) {
  const ts = new Date().toISOString().replace(/[:.]/g, '-');
  const file = `backup_${ts}.sql`;
  const cmd = `mysqldump --host=${host} --user=${user} --password=${password} ${database} > ${file}`;

  exec(cmd, (err) => {
    if (err) console.error('Backup error:', err.message);
    else console.log('Backup saved to', file);
  });
}
```

### 38. INNER JOIN with mysql2/promise (5 pts)

```js
const mysql = require('mysql2/promise');

async function getOrdersWithCustomers() {
  const conn = await mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'pass',
    database: 'shop'
  });

  const [rows] = await conn.execute(`
    SELECT customers.name, orders.order_date, orders.total
    FROM customers
    INNER JOIN orders ON customers.id = orders.customer_id
  `);

  console.log(rows);
  await conn.end();
}
```

### 39. Express + EJS controller method (5 pts)

```js
exports.getHomePage = (req, res) => {
  const user = { name: 'Student Developer' }; // or fetch from Model
  res.render('index', { user });
};
```

---

**Grading notes**  
- Award partial credit for correct structure even if minor syntax differs.  
- Coding answers must be complete and runnable in principle.  
- Parameter / variable names may vary as long as logic is correct.
