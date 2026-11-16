# Advanced Database — Prelims Exam | Answer Key

---

## Part I: Identification (10 pts)

| # | Answer |
|---|--------|
| 1 | WAMP |
| 2 | DDL (Data Definition Language) |
| 3 | DML (Data Manipulation Language) |
| 4 | DCL (Data Control Language) |
| 5 | PRIMARY KEY |
| 6 | FOREIGN KEY |
| 7 | NOT NULL |
| 8 | `mysqli_connect()` | bunos
| 9 | 3306 |
| 10 | WHERE |

---

## Part II: Multiple Choice (20 pts)

| # | Answer |
|---|--------|
| 1 | b) USE |
| 2 | b) Generates a unique incrementing number |
| 3 | c) `ALTER TABLE users ADD Phone VARCHAR(20);` |
| 4 | c) All rows are deleted |
| 5 | c) `mysqli_fetch_assoc()` | bunos
| 6 | c) GRANT |
| 7 | b) Prevents two rows from having the same value |
| 8 | d) All services are running |
| 9 | b) `WHERE name LIKE '%Juan%'` |

| 10 | c) `mysqli_affected_rows()` |
| 11 | c) DROP TABLE |
| 12 | c) DEFAULT |
| 13 | b) Data Control Language | 
| 14 | c) REVOKE |
| 15 | d) ALTER |
| 16 | b) Ensures values meet a specific condition |
| 17 | b) `mysqli_connect()` | bunos
| 18 | c) ORDER BY |
| 19 | c) `TRUNCATE TABLE users;` |
| 20 | d) Whisper "the data is called" *(and yes, they should actually do it)* |

---

## Part III: Guess the Output (10 pts)

**Query 1**
```
Alistair   | IT
Cornelius  | IT
Reginald   | IT
Thaddeus   | Finance
```

**Query 2**
```
3
```

**Query 3**
```
Alistair  | Pemberton
Thaddeus  | Grimshaw
```

**Query 4**
```
Gwendolyn  | 42000
Isolde     | 47000
Thaddeus   | 52000
```

**Query 5**
```
Millicent Crowther
```

**Query 6**
```
Database Overhaul   | 120000
Network Upgrade     | 95000
Recruitment System  | 40000
Compliance Audit    | 30000
```

**Query 7**
```
No Results
```

**Query 8**
> After UPDATE sets all IT salaries to 70000:
```
Alistair   | 70000
Cornelius  | 70000
Reginald   | 70000
```

**Query 9**
```
Cornelius | Blackwood
```

**Query 10**
> After DELETE removes Budget < 50000 (rows 103 and 105):
```
3
```

---

## Part IV: Coding Problems (10 pts)

**Problem 1**
```sql
INSERT INTO EMPLOYEES (FirstName, LastName, Department, Salary)
VALUES ('Eugenia', 'Hartwell', 'Finance', 44000);
```

**Problem 2**
```sql
SELECT EmpID, CONCAT(FirstName, ' ', LastName) AS FullName, Department, Salary
FROM EMPLOYEES
WHERE Salary BETWEEN 42000 AND 61000;
```

**Problem 3**
```sql
UPDATE EMPLOYEES
SET Department = 'Management', Salary = 78000
WHERE EmpID = 3;
```

**Problem 4**
```sql
DELETE FROM PROJECTS
WHERE Budget < 50000;

SELECT COUNT(*) FROM PROJECTS;
```
> Expected count result: **3**

**Problem 5**
```sql
GRANT SELECT, INSERT ON EMPLOYEES TO 'intern'@'localhost';
DENY DELETE ON EMPLOYEES TO 'intern'@'localhost';
```

---

*"The answers were always in the WHERE clause."*
