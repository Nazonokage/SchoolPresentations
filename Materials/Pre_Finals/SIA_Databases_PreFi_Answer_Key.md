# SIA Periodical Exam: Answer Key (Corrected, v2)
**Databases: E-Commerce Architecture, MySQL, SQLite, WAMPP and NoSQL (Modules 18–22) · 50 points**

> **Changes from v1:** (1) Part I #8 explanation fixed. (2) Part II #15 now accepts `DELETE FROM` with no WHERE. (3) Part III #2 accepts any row order. (4) Part IV #1 notes the price tie. (5) Part IV now shows sample output for every query.

| Part | Items | Points |
|---|---|---|
| I. Multiple choice | 15 | 15 |
| II. Identification / Enumeration | 15 | 15 |
| III. Guess the Output | 10 | 10 |
| IV. SQL coding | 5 | 5 |
| V. NoSQL coding | 1 problem | 5 |
| **Total** | **46 items** | **50** |

---

## Part I. Multiple Choice (1 pt each)

| # | Ans | Why |
|---|---|---|
| 1 | **C** | Keeping credentials in the web-server tier means each tier exposes only what the next one needs. That is the **security** benefit. |
| 2 | **A** | Files must be saved in `C:\wamp64\www\` to be served at `http://localhost`. A green icon means the servers are running, so the folder is the cause. |
| 3 | **D** | Modify = `UPDATE … WHERE`; Delete = `DELETE FROM … WHERE`. The others change structure, empty or drop whole tables, or are not valid mappings. |
| 4 | **B** | De-duplicating and cleansing merged data gives **universally reliable business data**. Sharding, truncating and hybrid hosting do not fix duplicates. |
| 5 | **A** | SQLite suits local, zero-admin kiosks. MySQL (client-server) suits head office's many concurrent analysts and JOINs. |
| 6 | **C** | SQLite locks the file on writes, so concurrent writers wait or fail. It does not shard, convert to JSON or start servers. |
| 7 | **D** | `DISTINCT` after SELECT removes repeats and `ORDER BY category DESC` sorts Z→A. The other statements are invalid syntax. |
| 8 | **B** | Only rows with v > 10 are updated: 20 → 25 and 30 → 35. The row with v = 10 stays 10. SUM = 10 + 25 + 35 = **70**. (60 = no update; 75 = all rows +5; 65 = only one row updated.) |
| 9 | **A** | `TRUNCATE` removes the rows but keeps the table structure, so a later `INSERT` works. |
| 10 | **D** | Relationships between entities (friends of friends) are what a **graph** database models. Examples: Neo4j, Amazon Neptune. |
| 11 | **C** | Shredding: 1 + 3 + 2 = **6 rows across 3 tables** (USERS, USER_SKILLS, USER_EXPERIENCE). Reading it back needs JOINs. |
| 12 | **B** | A bigger single machine is **vertical** scaling; adding servers is **horizontal** scaling (the NoSQL approach). |
| 13 | **D** | **Hybrid** bridges on-premises and cloud (best of both, gradual migration) but is more complex to manage. |
| 14 | **A** | AND binds tighter than OR: `Phones OR (Computers AND price > 500)`. Phone matches; Laptop matches (650 > 500); Mouse does not. Result: **2 rows**. |
| 15 | **C** | A true condition (days > 0 holds for every row) updates **every** row. A WHERE clause only protects when it filters. |

**Quick key:** 1C 2A 3D 4B 5A 6C 7D 8B 9A 10D 11C 12B 13D 14A 15C

---

## Part II. Identification / Enumeration (1 pt each)

| # | Answer |
|---|---|
| 1 | **Backend tier** (Tier 1) |
| 2 | **CRUD** (Create, Read, Update, Delete) |
| 3 | **WHERE** |
| 4 | `C:\wamp64\www\` |
| 5 | `ALTER TABLE Customers ADD Email VARCHAR(255);` (accept: **ALTER TABLE**) |
| 6 | **DROP TABLE** |
| 7 | **Primary key** |
| 8 | **COUNT** (`COUNT(column)`) |
| 9 | **ORDER BY … DESC** (accept: ORDER BY with DESC) |
| 10 | **SQLite** |
| 11 | **Object-relational impedance mismatch** (also called the "shredding" problem) |
| 12 | **insertOne()** |
| 13 | **Document, Key-Value, Wide-Column, Graph** (any order; e.g. MongoDB, Redis, Cassandra, Neo4j) |
| 14 | **Universally reliable business data; holistic operations oversight; simplified security; easier compliance** (any order) |
| 15 | **TRUNCATE TABLE** (best answer). **Also accept** `DELETE FROM <table>;` with no WHERE, since it also empties the table and keeps its structure. |

*Items 13 and 14: 1 point only if all four are correct (no partial credit).*
*Optional rewording for #15 if you want one answer only: "…Which command empties the table in one step without removing its structure?" Even then, accepting DELETE FROM is fair.*

---

## Part III. Guess the Output (1 pt each)

Original data after the setup scripts:

| id | name | category | price | stock |
|---|---|---|---|---|
| 1 | Laptop | Computers | 650.00 | 5 |
| 2 | Mouse | Accessories | 15.50 | 40 |
| 3 | Keyboard | Accessories | 30.00 | 25 |
| 4 | Smartphone | Phones | 400.00 | 10 |
| 5 | Charger | Accessories | 15.50 | 0 |

| # | Answer | Explanation |
|---|---|---|
| 1 | The table above (all 5 rows, all 5 columns) | `SELECT *` returns every row and column. Award the point only if all rows and values are correct. |
| 2 | `Computers`, `Accessories`, `Phones` (3 rows, one each). **Accept any order.** | `DISTINCT` removes the repeated Accessories. SQL does not guarantee order without ORDER BY. Award the point if there are exactly 3 unique values. |
| 3 | `Mouse`, `Keyboard`, `Charger` (in that order) | Prices 15.50, 30.00, 15.50 are all within 15–30 (BETWEEN is inclusive). Names sorted Z→A. Laptop and Smartphone are excluded. |
| 4 | **61.00** | 15.50 + 30.00 + 15.50 |
| 5 | **110** | Original stock total is 5 + 40 + 25 + 10 + 0 = 80. Three Accessories get +10 each (+30), so 110. |
| 6 | **4** | Only the Charger has stock 0, so it is deleted. 5 − 1 = 4. |
| 7 | **3** | All three customer documents are counted. |
| 8 | `{ name: "Tavish" }` and `{ name: "Marisol" }` | Gold members only; projection shows `name`, hides `_id`. |
| 9 | `{ name: "Ilsa", membership: "Silver", address: { city: "Davao" }, orders: 1 }` | Dot notation matches the nested city; `_id: 0` hides the id. |
| 10 | **0** | No customer lives in Manila. It returns 0, not an error. |

---

## Part IV. SQL Coding (1 pt each), with sample output

Each query is run **separately, starting from the original data**.

### 1. All Accessories, highest price to lowest
```sql
SELECT * FROM products WHERE category = 'Accessories' ORDER BY price DESC;
```
| id | name | category | price | stock |
|---|---|---|---|---|
| 3 | Keyboard | Accessories | 30.00 | 25 |
| 2 | Mouse | Accessories | 15.50 | 40 |
| 5 | Charger | Accessories | 15.50 | 0 |

*Mouse and Charger tie at 15.50, so either order is correct. Needs WHERE for the category and `ORDER BY price DESC`.*

### 2. Insert the Webcam
```sql
INSERT INTO products VALUES (6, 'Webcam', 'Accessories', 45.00, 12);
```
Output: `1 row affected`. Checking with `SELECT * FROM products;` now shows 6 rows:

| id | name | category | price | stock |
|---|---|---|---|---|
| 1 | Laptop | Computers | 650.00 | 5 |
| 2 | Mouse | Accessories | 15.50 | 40 |
| 3 | Keyboard | Accessories | 30.00 | 25 |
| 4 | Smartphone | Phones | 400.00 | 10 |
| 5 | Charger | Accessories | 15.50 | 0 |
| 6 | Webcam | Accessories | 45.00 | 12 |

*Also accept the column-list form: `INSERT INTO products (id, name, category, price, stock) VALUES (...)`. Text values must be quoted.*

### 3. Restock the Charger to 20
```sql
UPDATE products SET stock = 20 WHERE name = 'Charger';
```
Output: `1 row affected`. Checking with `SELECT * FROM products WHERE name = 'Charger';`:

| id | name | category | price | stock |
|---|---|---|---|---|
| 5 | Charger | Accessories | 15.50 | 20 |

*Other rows are unchanged. **No WHERE = 0 points** (it would set every product's stock to 20).*

### 4. Remove the Mouse
```sql
DELETE FROM products WHERE name = 'Mouse';
```
Output: `1 row affected`. Checking with `SELECT * FROM products;` now shows 4 rows:

| id | name | category | price | stock |
|---|---|---|---|---|
| 1 | Laptop | Computers | 650.00 | 5 |
| 3 | Keyboard | Accessories | 30.00 | 25 |
| 4 | Smartphone | Phones | 400.00 | 10 |
| 5 | Charger | Accessories | 15.50 | 0 |

*Only the Mouse is gone. **No WHERE = 0 points.** `DROP TABLE` is wrong.*

### 5. Tagalog algorithm: highest price
Steps: Simulan (start) → get the highest price → Ipakita (display) → Tapusin (end).
```sql
SELECT MAX(price) FROM products;
```
| MAX(price) |
|---|
| 650.00 |

*Accept an alias such as `SELECT MAX(price) AS highest_price FROM products;`.*

Accept equivalent correct queries (e.g. `WHERE id = 3` in items 3–4, or `price = 15.50 AND name = 'Mouse'`). Minor spacing or capitalization differences are not penalized.

---

## Part V. NoSQL Coding (5 pts, one problem)

**Model answer**

```javascript
db.customers.insertOne({
  "name": "Rhea",
  "membership": "Silver",
  "address": { "city": "Iloilo" },
  "orders": 2
});

db.customers.find({ "membership": "Gold", "address.city": "Cebu" }, { "_id": 0, "name": 1 });
```

**Result of (b):** `{ name: "Tavish" }` and `{ name: "Marisol" }` (Rhea is Silver and in Iloilo, so she is not returned).

**Rubric**

| Criterion | Pts |
|---|---|
| Uses `insertOne` (or accepts `insertMany` with one document) on `db.customers` | 1 |
| Nested `address` object with city "Iloilo" | 1 |
| Correct `membership` ("Silver") and `orders` (2) fields | 1 |
| Filter for Gold members in Cebu using dot notation `"address.city"` | 1 |
| Projection shows only `name` and hides `_id` (`{ _id: 0, name: 1 }`) | 1 |

Syntax slips such as a missing semicolon or unquoted field names are not penalized, since MongoDB accepts both.

---

## Score sheet

| Part | Max | Score |
|---|---|---|
| I | 15 | |
| II | 15 | |
| III | 10 | |
| IV | 5 | |
| V | 5 | |
| **Total** | **50** | |
