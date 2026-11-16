# 🔑 ANSWER KEY — Integrative Programming Prelim Exam

---

## Part I — Multiple Choice (35 items, 1 pt each)

**A. HTTP Basics**
1. A — HyperText Transfer Protocol
2. B — GET
3. B — POST
4. C — 403
5. C — 4xx

**B. Django Setup**
6. B — `pip3 install Django`
7. B — `django-admin startproject <name>`
8. B — Your own local computer
9. C — `urls.py`
10. B — A command executor
11. C — Keeps `manage.py` at project root, no double-nesting

**C. MVT & Project vs. App**
12. B — MVT
13. B — Controller
14. C — Template
15. B — An apartment complex is to one unit
16. B — `startapp`
17. B — `INSTALLED_APPS` in `settings.py`

**D. Dynamic URLs**
18. B — Converter type
19. C — The URL path converter
20. B — They must have identical names
21. C — `f`
22. B — "Harry"
23. B — Twitter/X (`twitter.com/<username>`)

**E. WAMP + MySQL Account App**
24. B — `django.db.backends.mysql`
25. B — In phpMyAdmin
26. C — User
27. B — POST
28. A — `pymysql`
29. B — Still works if the URL path ever changes
30. B — `TemplateDoesNotExist`
31. B — In the server-side view (`is_self` check)

**F. Git, GitHub, Vercel**
32. B — A distributed version control system
33. B — Google Drive relates to your local files
34. B — Frontend deployment & hosting
35. B — Clone → branch → commit → push → PR → review → merge

---

## Part II — Identification (10 items, 1 pt each)

**Straight Identification (1–7)**
1. `pymysql`
2. `django.contrib.messages` (the messages framework)
3. `4xx`
4. GitHub
5. `@login_required`
6. `is_self`
7. Preview Deployments

**Guess the Output (8–10)**
8. `Hello, Harry!`
9. `GREAT!!!`
10. `ognajd`

---

## Part III — HTTP Status Code Enumeration (6 items, 1 pt each)

Any 6 valid codes (other than `200`) with a correct meaning should be accepted. Sample acceptable answers:

- `201 - Created`
- `301 - Moved Permanently`
- `302 - Found (Temporary Redirect)`
- `400 - Bad Request`
- `403 - Forbidden`
- `404 - Not Found`
- `405 - Method Not Allowed`
- `500 - Internal Server Error`
- `502 - Bad Gateway`
- `503 - Service Unavailable`

> Grading note: accept minor wording variants (e.g. "Not Found" / "Page Not Found", "Server Error" / "Internal Server Error").

---

## Part IV — Python Coding Problems (3 items, 3 pts each)

**1. "The Bouncer's Clipboard"**
```python
def find_room(route):
    for entry in clipboard:
        if entry["route"] == route:
            return entry["room"]
    return None
```
*Rubric: 1 pt loop through list, 1 pt correct key comparison, 1 pt returns `None` on no match.*

**2. "The Politeness Filter"**
```python
def greet_properly(name):
    return f"Hello, {name.capitalize()}!"
```
*Rubric: 1 pt uses `.capitalize()`, 1 pt correct f-string substitution, 1 pt exact output format `"Hello, ___!"`.*

**3. "Who's Allowed to Touch This"**
```python
def can_edit(visitor_id, owner_id):
    return visitor_id == owner_id
```
*Rubric: 1 pt correct comparison operator, 1 pt returns boolean (not string), 1 pt matches both sample cases.*

---

**Total: 60 pts** (35 MC + 10 Identification + 6 Enumeration + 9 Coding)
