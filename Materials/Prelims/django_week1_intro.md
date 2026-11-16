---
marp: true
theme: default
paginate: true
class: lead
---

# 🐍 Django Bootcamp — Week 1
## The Framework Jump & Setup
### Intro to MVT

---

## 📋 Today's Agenda

1. Why do we even need a framework?
2. MVC vs MVT — the mental model shift
3. Analogies & real-world use cases
4. Hands-on: `venv`, install, `startproject`
5. Tour of the default folder structure
6. Recap + homework

---

# Part 1
## From Raw Scripts → Framework Thinking

---

## 🧠 The Problem with "Just Scripts"

When you write raw Python scripts for a web app, you handle everything yourself:

- Parsing HTTP requests manually
- Writing your own routing logic
- Manually opening DB connections, writing raw SQL
- Mixing HTML strings inside Python logic
- No consistent folder structure — every project looks different

**Result:** it works... until it needs to scale, or someone else joins the project.

---

## 🏗️ Analogy: Building a House

| Without a Framework | With a Framework (Django) |
|---|---|
| You gather your own bricks, wiring, plumbing | Pre-built foundation, wiring conduits, plumbing lines already planned |
| Every house you build looks different | Every Django project follows the same blueprint |
| One mistake (bad wiring) can collapse the house | Framework enforces safe, tested patterns |
| Fast for a tiny shed, painful for a mansion | Slower to start, but scales to a skyscraper |

> A framework doesn't limit your creativity — it gives you a **blueprint** so you stop reinventing plumbing.

---

## ⚙️ What a Framework Actually Enforces

- **Structure** → every app has the same shape (easy for new devs to onboard)
- **Separation of concerns** → data, logic, and presentation don't mix
- **Convention over configuration** → sensible defaults, less decision fatigue
- **Security & best practices baked in** → CSRF protection, ORM (prevents SQL injection), escaping in templates

---

# Part 2
## MVC vs MVT

---

## 🧩 Traditional MVC (Model-View-Controller)

```
         User Request
              │
              ▼
        ┌───────────┐
        │ Controller│  ← handles input, decides logic
        └─────┬─────┘
              │
     ┌────────┴────────┐
     ▼                 ▼
 ┌───────┐         ┌────────┐
 │ Model │         │  View  │  ← renders output (HTML)
 └───────┘         └────────┘
```

- **Model** → data & business logic
- **View** → what the user sees (UI/HTML)
- **Controller** → the "middleman" that receives requests and decides what to do

---

## 🧩 Django's MVT (Model-View-Template)

```
         User Request
              │
              ▼
        ┌───────────┐
        │   urls.py │  ← routes the request
        └─────┬─────┘
              │
              ▼
        ┌───────────┐
        │   View    │  ← Django's "View" = Controller's job!
        └─────┬─────┘
              │
     ┌────────┴────────┐
     ▼                 ▼
 ┌───────┐         ┌──────────┐
 │ Model │         │ Template │  ← the actual HTML (MVC's "View")
 └───────┘         └──────────┘
```

⚠️ **The naming trap:** Django's "View" is NOT the same as MVC's "View."
Django's View = MVC's Controller (logic).
Django's Template = MVC's View (what's displayed).

---

## 🔄 Side-by-Side Comparison

| Role | MVC | MVT (Django) |
|---|---|---|
| Data & DB logic | Model | Model |
| Decides logic / handles request | Controller | **View** (`views.py`) |
| What the user actually sees | View | **Template** (`.html` files) |
| Routes requests | (varies) | `urls.py` |

> Django handles the "Controller" part for you internally (URL dispatcher), so you mostly just write **Views** and **Templates**.

---

## 🍽️ Analogy: The Restaurant

| Restaurant Role | Django Equivalent | Job |
|---|---|---|
| **Kitchen inventory / recipes** | Model | Stores and manages the raw data (ingredients) |
| **Waiter** | View | Takes the order (request), talks to the kitchen (model), decides what goes back out |
| **Printed Menu / Plated Dish** | Template | What the customer actually sees and receives |
| **Host who seats you & routes your order** | `urls.py` | Directs incoming requests to the right "waiter" (view) |

> You don't ask the printed menu to cook your food — that's the waiter's (View's) job talking to the kitchen (Model), then handing it off to be presented (Template).

---

## 💼 Real-World Use Cases of MVT

- **E-commerce site** (Amazon-style): Model = products/orders table, View = "add to cart" logic, Template = product page HTML
- **Blog platform**: Model = Post/Comment tables, View = fetch latest posts, Template = blog listing page
- **Admin dashboards**: Model = user records, View = filtering/search logic, Template = dashboard UI
- **APIs (with Django REST Framework)**: Same MVT skeleton, but Template is replaced by JSON output

---

# Part 3
## Hands-On Setup 🛠️

---

## Step 1 — Create a Virtual Environment

A `venv` isolates your project's dependencies so different projects don't fight over package versions.

```bash
# Create the virtual environment
python -m venv venv

# Activate it (Mac/Linux)
source venv/bin/activate

# Activate it (Windows)
venv\Scripts\activate
```

> 💡 Analogy: `venv` is like giving each project its **own toolbox**, so a screwdriver used in Project A doesn't accidentally get changed for Project B.

---

## Step 2 — Install Django

```bash
pip install django

# Verify installation
django-admin --version
```

Freeze your dependencies so teammates (or future you) can recreate the exact setup:

```bash
pip freeze > requirements.txt
```

---

## Step 3 — Start Your Project

```bash
django-admin startproject mysite
cd mysite
```

This scaffolds your entire project blueprint automatically — no manual folder creation needed.

```bash
# Run the dev server to confirm it works
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` → 🚀 Django's welcome rocket page.

---

## 📁 The Default Folder Structure

```
mysite/
│
├── manage.py            ← CLI utility to run commands (server, migrations, etc.)
│
└── mysite/               ← the actual project package
    ├── __init__.py       ← marks this as a Python package
    ├── settings.py       ← project configuration (DB, apps, security, etc.)
    ├── urls.py           ← root URL routing table
    ├── asgi.py           ← entry point for async servers
    └── wsgi.py           ← entry point for traditional (sync) servers
```

> 🧭 Analogy: `manage.py` is your **remote control** — you press buttons on it (`runserver`, `migrate`, `startapp`) to operate the whole project.

---

## 🔍 Peek Inside `settings.py`

```python
# mysite/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

This is Django's **control panel** — every app, database, and security setting lives here.

---

## 🔍 Peek Inside `urls.py`

```python
# mysite/urls.py

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # more routes will go here as we build views
]
```

> Analogy: `urls.py` is the **receptionist** — it looks at the incoming request address and directs it to the correct "office" (view).

---

## ✅ Recap — Week 1

- Frameworks trade a bit of freedom for **structure, safety, and speed**
- Django uses **MVT**: Model (data) → View (logic) → Template (display)
- `venv` keeps dependencies isolated per project
- `django-admin startproject` scaffolds the whole blueprint instantly
- `settings.py` = control panel, `urls.py` = receptionist, `manage.py` = remote control

---

## 📝 Homework / Next Steps

1. Set up your own `venv` and Django project locally
2. Explore `settings.py` — identify 3 settings you don't recognize and look them up
3. Try adding a second `path()` entry in `urls.py` (it's okay if it errors — we'll build the View next session!)
4. Come prepared next week: **Models, Views & Your First App** (`startapp`)

---

# Thank You! 🙌
### Questions before we move to hands-on labs?
