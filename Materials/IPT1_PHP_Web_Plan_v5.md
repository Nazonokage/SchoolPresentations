# Integrative Programming & Technologies 1 (IPT 1)

**Stack:** HTML + CSS + JavaScript + PHP + MySQL (XAMPP). No frameworks, no libraries, no Python.
**Focus:** build a database-backed website from a first HTML page to a hand-built MVC application, learning programming fundamentals along the way.
**Plan status:** version 5, November 2026. **Everything runs offline.** Paced for students who are new to programming.

---

## How the course is organized

| Module numbers | What happens | Points |
|---|---|---:|
| **Odd** (M1, M3, …, M25) | A short lesson, then a **5-item quiz or a related written activity** (essay, paper trace, code review) | 10 each |
| **Even** (M2, M4, …, M24) | A **simple computer-lab project** that applies the lesson before it | 10 each |

Each even module applies the odd module before it: *learn, then build.* That gives **13 written scores and 12 projects, 250 points in all.**

**Timing (60 to 90 minutes).**
- Odd module: about 40 to 50 minutes of lesson with a guided demo (ungraded), then 20 to 25 minutes for the graded quiz or activity.
- Even module: 10 minutes of recap, about 60 minutes in the lab, 10 minutes of wrap-up and checking.

---

## Course description

Students build a working website in layers: **HTML** gives it structure, **CSS** gives it a look, **JavaScript** makes pages interactive in the browser, **PHP** makes them dynamic on the server, and **MySQL** stores the data. They then restructure the site into **Model-View-Controller (MVC)** and build a small MVC application.

The "integrative" part is how these technologies work together: a browser form (HTML) checked by JavaScript, validated again by PHP, saved in MySQL, and shown back in a styled page.

**Prerequisite:** none beyond basic computer use. Programming is taught from scratch, first in JavaScript (M5 and M6) and then again in PHP (M7 to M12), using the same ideas so each reinforces the other.

### One running project: the Campus Services Hub

Every project adds one piece to the same website. Use invented offices, people and records only.

---

## Learning outcomes (measurable)

| # | Outcome | Modules |
|---|---|---|
| 1 | Explain how the web works and the role of HTML, CSS, JavaScript, PHP and MySQL | 1 |
| 2 | Use a local server, an editor and Git to build and run a project | 2 |
| 3 | Write structured, styled and responsive web pages | 3, 4 |
| 4 | Use variables, conditions, loops, functions and events in JavaScript | 5, 6 |
| 5 | Write PHP pages that use arrays, functions and includes | 7 to 10 |
| 6 | Build forms with client-side and server-side validation and safe output | 11, 12 |
| 7 | Design a database, write SQL, and use PDO with prepared statements | 13, 14 |
| 8 | Build complete CRUD pages | 15, 16 |
| 9 | Implement login, roles and the main web protections | 17, 18 |
| 10 | Write object-oriented PHP and refactor an application into MVC with a router | 19 to 24 |
| 11 | Present, explain and defend a complete web system | 16, 24, 25 |

---

## Technology stack (all offline)

| Tool | Purpose | Notes (checked November 2026) |
|---|---|---|
| XAMPP | Apache, MySQL (MariaDB), PHP, phpMyAdmin | Newest installers: 8.2.12, 8.1.25, 8.0.30. The 8.2.12 build bundles PHP 8.2.12, Apache 2.4.58 and MariaDB 10.4.32 |
| PHP | Server-side language | **Teach PHP 8.2 features only.** PHP 8.2 security support ends 31 Dec 2026 |
| MySQL | Database | XAMPP's "MySQL" is **MariaDB**. Course SQL is identical |
| HTML, CSS, JavaScript | Front end | Plain, in the browser. **No Bootstrap, no jQuery, no CDN** |
| VS Code | Editor | Installer and extensions copied from USB |
| Git | Version control | Light use: commit at the end of each project |
| Browser dev tools | Inspecting HTML, CSS, JS, HTTP | Built in |

**No Composer, no package installs, no internet.** The autoloader is written by hand (M19 and M20).

### XAMPP setup and hardening (taught in M2 and M14)

- Keep Apache and MySQL reachable from **`localhost` only**. Stop them after class.
- Set a password for the database `root` user and create a **dedicated course user** with rights on the course database only. The application never connects as `root`.
- Create databases with `utf8mb4` explicitly.
- Show PHP errors while developing, and explain why a real site hides them.
- One third-party write-up (October 2026) reports critical PHP vulnerabilities fixed upstream on 21 October 2026 with no matching XAMPP build. **Verify against php.net before relying on it.** A localhost-only lab limits exposure.
- **Verify on your own lab image before teaching:** that `pdo_mysql` and `mbstring` are enabled, where the document root is, and whether `.htaccess` and `mod_rewrite` work (used only as an option in M24).

### Offline lab kit (copy to every lab PC and a USB drive)

- XAMPP installer, Git, VS Code and its extensions (as files)
- A **starter folder per project** with the hard parts written and `TODO` markers where students work
- Sample data and a short `CHECK.md` per project saying what a correct result looks like
- A one-page **debugging guide**: how to read a PHP error, a browser console error and an SQL error
- A lab image smoke test: `php -v`, `git --version`, `localhost` opens, `localhost/phpmyadmin` opens

### Suggested folder structure

```text
IPT1/
├── modules/                      one folder per module
├── projects/
│   ├── m02-hello-hub/ … m24-mvc-app/    starter + CHECK.md per even module
├── resources/                    sample data, cheat sheets, debugging guide
└── README.md
```

Projects live under XAMPP's `htdocs`.

---

## The 25 modules

### Part 1: The web and the front end (M1 to M6)

| # | Type | Module | Evidence (10 points) |
|---|---|---|---|
| 1 | Odd | **Introduction: how the web works.** Clients and servers, HTTP requests and responses, URLs, status codes; what HTML, CSS, JavaScript, PHP and MySQL each do; how integrating them makes a website | **5-item quiz** |
| 2 | Even | **Project: Hello, Campus Hub.** Install and start XAMPP, create `index.html` and `index.php` in VS Code, view both in the browser, find the request in dev tools, make a Git commit | Screenshot of both pages and the dev-tools request; commit log; one failure case (Apache stopped) |
| 3 | Odd | **HTML and CSS essentials.** Document structure, headings, links, images, lists, tables, form elements; CSS selectors, the box model, colors, fonts, flexbox, media queries | **5-item quiz** (identify the tag or property, fix a broken snippet) |
| 4 | Even | **Project: The static hub.** Three linked pages (home, offices table, contact form markup) with one shared CSS file and a layout that adapts to a narrow window | Three valid pages; a resized screenshot |
| 5 | Odd | **JavaScript basics.** Variables, data types, operators, conditions, loops, functions, arrays, the DOM, events; `console.log` and reading errors | **5-item quiz** (read code and predict the output) |
| 6 | Even | **Project: An interactive page.** A search box that filters the offices table as you type, a show/hide button, and a form check that reports empty fields before submitting | Features work; the empty-list case shows a message |

### Part 2: PHP fundamentals (M7 to M12)

| # | Type | Module | Evidence (10 points) |
|---|---|---|---|
| 7 | Odd | **PHP basics.** Tags, variables, types, operators, `echo`, mixing PHP with HTML, `if` and `switch`, loops; the same ideas as JavaScript, on the server | **5-item quiz** (read PHP and predict the page) |
| 8 | Even | **Project: Announcements page.** A PHP page loops over an array of announcements, highlights urgent ones, shows today's date and prints a friendly message when the list is empty | Page works; an empty array and a missing field handled |
| 9 | Odd | **Functions, arrays and reusable pages.** Functions and return values, indexed and associative arrays, string functions, `include` and `require`, header and footer | **5-item quiz** (predict the output of a function and an array loop) |
| 10 | Even | **Project: Shared layout.** A header, footer and navigation in `include` files and a small `functions.php` (including a safe-output helper); three pages built from arrays | Three pages share the layout; the current page is highlighted. **Midterm covers M1 to M12** |
| 11 | Odd | **Forms, validation and safe output.** GET vs POST, `$_POST`, validating on the client (JavaScript) and again on the server (PHP), sticky forms, `htmlspecialchars` | **Short essay (100 to 150 words):** how an attacker abuses an unescaped form and how escaping stops it |
| 12 | Even | **Project: Feedback form.** A form checked by JavaScript and again by PHP, sticky after an error, saving entries to a text or CSV file outside the web folder and listing them with escaped output | A `<script>` typed in the form appears as text; with JavaScript turned off the server still rejects bad input |

### Part 3: Databases and CRUD (M13 to M16)

| # | Type | Module | Evidence (10 points) |
|---|---|---|---|
| 13 | Odd | **Databases and SQL.** Tables, rows, data types, primary keys, relationships; `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `WHERE`, `ORDER BY`; phpMyAdmin | **5-item quiz:** write five short SQL statements (2 points each) |
| 14 | Even | **Project: The hub database.** Create the `hub` database (`utf8mb4`) and an `announcements` table from an SQL file, create the dedicated user, and run the supplied queries in phpMyAdmin | Table and rows exist; a deliberate error (a duplicate key) is read and explained |
| 15 | Odd | **PHP, PDO and CRUD.** Connect with PDO, **prepared statements**, fetch rows; create, read, update, delete; redirect after POST and flash messages | **Paper-trace activity:** trace one "edit and save" request from the browser through PHP and SQL and back (6 steps, 10 points) |
| 16 | Even | **Project 1: CRUD website.** From a starter with `TODO` markers: list, search, add, edit and delete announcements with PDO, validation, a flash message and your own CSS. *Stretch:* a live search box where JavaScript calls a PHP script that returns JSON | Working site; a short manual test table; one invalid-input case; Git history |

### Part 4: Users and security (M17 and M18)

| # | Type | Module | Evidence (10 points) |
|---|---|---|---|
| 17 | Odd | **Sessions, login and security.** Sessions and cookies, `password_hash` and `password_verify`, role checks, CSRF tokens, SQL injection, XSS, keeping settings and secrets out of the web folder | **Code review:** find 5 flaws in a short page (2 points each) |
| 18 | Even | **Project: Staff login.** A `users` table with hashed passwords, login and logout, an admin and a staff role, CSRF tokens on forms; fix a supplied page that has one SQL injection and one XSS flaw | Login and roles work; both flaws fixed, with before and after evidence |

### Part 5: Object-oriented PHP and MVC (M19 to M24)

| # | Type | Module | Evidence (10 points) |
|---|---|---|---|
| 19 | Odd | **Object-oriented PHP.** Classes, objects, properties and methods, visibility, constructors, namespaces, a hand-written autoloader | **5-item quiz** (read a class and predict the result) |
| 20 | Even | **Project: Classes and an autoloader.** Move the PDO code into `Database` and `Announcement` classes with `spl_autoload_register`; the pages use the classes | Pages still work; no SQL left in the page files |
| 21 | Odd | **The MVC idea.** What a Model, a View and a Controller each do and must not do; folder layout | **Short essay (100 to 150 words):** explain MVC with the announcements example and say where each of five given pieces of code belongs |
| 22 | Even | **Project: One feature in MVC.** Rebuild the announcements list and detail pages with a Model, a View and a Controller | No SQL in the controller; no logic beyond loops in the view |
| 23 | Odd | **Front controller and router.** One entry point, reading the URL, routes, controller actions, 404 pages | **5-item quiz:** trace five URLs to the controller and action they reach |
| 24 | Even | **Project 2: Mini MVC application.** A front controller and router (query-string routes first; clean URLs only if `mod_rewrite` is verified), controllers, models and views, a login filter, your own CSS and JavaScript | Working app; a test table; Git history |

### Part 6: Synthesis (M25)

| # | Type | Module | Evidence (10 points) |
|---|---|---|---|
| 25 | Odd | **Course synthesis and defense.** Review how the technologies fit together | **Reflection essay (150 to 200 words) plus a 5-minute defense of your M24 project** |

---

## Supporting beginners

- **Starter code with `TODO` markers.** Each project gives students working scaffolding, so they spend lab time on the new idea, not on blank-page panic. Later projects remove more scaffolding.
- **Predict, then run.** Every lesson asks students to predict the output before running code; quizzes use the same habit.
- **Same ideas twice.** Variables, conditions, loops and functions appear in JavaScript first (M5 and M6) and in PHP next (M7 to M10), side by side.
- **Trace tables** for loops and functions, written by hand before using the computer.
- **A debugging guide** and a rule: read the first error message, fix one thing, run again.
- **Small steps:** commit and check after every working change.
- **Pair work for practice only.** Graded evidence is individual and each student explains their own code.

---

## Scoring

| Item | Count | Points each | Total |
|---|---:|---:|---:|
| Odd modules: quiz, essay, trace or code review | 13 | 10 | 130 |
| Even modules: lab projects | 12 | 10 | 120 |
| **Module total** | 25 | | **250** |

**Suggested grade composition (adjust to school policy):** module points 80%, midterm exam 20% (separate slot, covers M1 to M12). If your school requires another exam, tell students at the start.

### Rubrics (all 10 points)

**5-item quiz.** 2 points each; 1 point for a partly correct answer.

**Essay or reflection.**

| Criterion | Points |
|---|---:|
| Correct main idea with the right terms | 4 |
| A specific example from the course project | 3 |
| Clear, organized writing within the length limit | 3 |

**Paper trace or code review.** Correct steps or flaws found, scaled to 10 points, with credit for a short reason.

**Lab project (even modules).**

| Evidence | Points |
|---|---:|
| Works and meets the goal in `CHECK.md` | 4 |
| A meaningful edge or failure case handled | 2 |
| Explains how it works in 3 to 5 sentences | 2 |
| Reproducible: readable code, committed to Git | 2 |

M25 defense: reflection essay 5, oral defense 5.

---

## Offline and fairness plan

Every lab runs on lab PCs or a personal laptop prepared in advance. If a student has no working machine on the day:

- **Odd modules:** nothing changes; the quiz or activity is on paper.
- **Even modules:** the student completes a **paper-trace version** of the project (a table of each step, the expected output and one failure case), worth the same 10 points. A student who later runs it may replace the score.

---

## Teaching tips

- Show the browser dev tools in M1 and use them in every module: Elements for HTML and CSS, Console for JavaScript, Network for requests.
- Teach **escaping output and prepared statements from the first form and the first query**, not as a late add-on.
- Build the same feature three times (plain, with classes, in MVC) so students see why each step exists.
- Keep PHP to 8.2 features so the code runs on XAMPP as shipped.
- Every project includes one failure case.
- Use invented data only.

---

## Version check

| Item | Checked | Note |
|---|---|---|
| XAMPP | Nov 2026 | Newest installers 8.2.12, 8.1.25, 8.0.30; MariaDB 10.4.32 |
| PHP | Nov 2026 | 8.1 is end of life; 8.2 ends security support 31 Dec 2026; 8.4 and 8.5 are current |

Re-check before each term.

---

## What changed from version 4, and decisions for you

- **Removed:** Python, Bootstrap, and the data-format (XML, JSON, CSV), socket and messaging modules. Their slots now teach HTML, CSS, JavaScript and more PHP.
- **Added:** HTML and CSS (M3, M4), JavaScript (M5, M6), a separate PHP fundamentals run (M7 to M12) and a beginner-support section.
- **Kept:** the odd/even pattern, 10 points per module, the offline rule, XAMPP with its hardening checklist, and the MVC finish.
- **Decide:**
  1. **Syllabus match.** If your official syllabus requires XML or JSON exchange, sockets or messaging, tell me where to fit them (the quickest place is a short JSON topic in M15 and M16).
  2. **Bootstrap.** Removed for "pure" CSS. Add it back only if your department expects it.
  3. **Grade composition** (80/20 is a suggestion).
  4. **Extra time** for M16 and M24, the biggest projects.
  5. **Clean URLs** (`mod_rewrite`, unverified on your XAMPP) or query-string routes only.
  6. **Midterm** after M12.
