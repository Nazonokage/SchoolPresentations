# IT108_SIA Midterm Periodical Exam – Answer Key
51 points · 47 items

---

## I. Multiple Choice

| # | Answer | Brief note (only when needed) |
|---|--------|-------------------------------|
| 1 | B | Definition of System Integration |
| 2 | C | N(N−1)/2 = 10×9/2 = 45 |
| 3 | C | Horizontal Integration / ESB |
| 4 | B | Classic Point-to-Point analogy |
| 5 | C | UN/EDIFACT |
| 6 | C | Abstraction |
| 7 | B | SOAP = protocol; REST = style |
| 8 | B | Database-per-service |
| 9 | B | Middleware definition |
| 10 | B | Pub/Sub is one-to-many |
| 11 | C | Decoupling & fault tolerance |
| 12 | B | Base of the Testing Pyramid |
| 13 | B | CI definition |
| 14 | C | Canary |
| 15 | B | ISO 9241-11 triad |
| 16 | B | Slip = right goal, wrong action |
| 17 | C | SUS = 0–100 |
| 18 | B | API definition |
| 19 | C | Database Normalization is not a REST constraint |
| 20 | C | Loose Coupling |
| 21 | C | GET |
| 22 | B | Hypermedia Links |
| 23 | D | ETL |
| 24 | B | Two identical environments + traffic switch (Blue-Green) |
| 25 | B | Ease of Learning = completing tasks quickly without extensive instruction |

---

## II. Identification

| # | Answer |
|---|--------|
| 26 | Point-to-Point Integration (or Point-to-Point / Star) |
| 27 | Common Data Format Integration |
| 28 | Publish/Subscribe (or Pub/Sub / Topic) |
| 29 | ETL (Extract, Transform, Load) |
| 30 | Ask a classmate / peer to write “OK” on their hand, then show / present your answers (answer sheet) to the instructor (3 pts – gimmick) |
| 31 | Microservices (Architecture) |
| 32 | Slip |
| 33 | System Usability Scale (SUS) |
| 34 | Statelessness |
| 35 | API (or the intermediary / waiter = API) |

---

## III. Enumeration

| # | Answer |
|---|--------|
| 36 | Point-to-Point Integration |
| 37 | Vertical Integration (or Star / Spaghetti) |
| 38 | Horizontal Integration (or ESB) |
| 39 | Common Data Format Integration |
| 40 | Any one of: Loose Coupling / Reusability / Interoperability / Abstraction |
| 41 | A second distinct principle from the same list |
| 42 | N(N−1)/2 |
| 43 | POST |
| 44 | DELETE |
| 45 | Blue-Green Deployment |

*Accept minor wording variations that clearly identify the same concept.*

---

## IV. Coding Problems

### 46. Complete the Node.js server

**Blanks in order:**

1. `http`
2. `createServer`
3. `200`
4. `stringify`
5. `listen`

Completed structure:

```js
const http = require('http');
const server = http.createServer(
  (req, res) => {
    res.setHeader('Content-Type', 'application/json');
    res.statusCode = 200;
    res.end(JSON.stringify(
      { status: 'ok' }));
  });

server.listen(3000, () => {
  console.log('Server running');
});
```

### 47. POST `/api/echo` echoes body under `received`; else 404

**Blanks in order:**

1. `POST`
2. `end`
3. `parse`
4. `received`
5. `404`

Completed structure:

```js
const http = require('http');
const server = http.createServer(
  (req, res) => {
    res.setHeader('Content-Type', 'application/json');
    if (req.method === 'POST' &&
        req.url === '/api/echo') {
      let body = '';
      req.on('data', c => body += c);
      req.on('end', () => {
        const p = JSON.parse(body);
        res.statusCode = 200;
        res.end(JSON.stringify(
          { received: p }));
      });
    } else {
      res.statusCode = 404;
      res.end(JSON.stringify(
        { error: 'Not Found' }));
    }
  });

server.listen(3000);
```

---

## Gimmick note (item 30 – 3 pts)

Expected answer: Ask a classmate to write “OK” on their hand, then show your answers to the instructor.

Students who write that description **or** actually perform the action receive full credit.

---

## Update note

This answer key is aligned with the **final PDF version** of the IT108 SIA Midterm. In particular, Coding Problems 46–47 were updated to match the blanks and code shown in the final PDF.
