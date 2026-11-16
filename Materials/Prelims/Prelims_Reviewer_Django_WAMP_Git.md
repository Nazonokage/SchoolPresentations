# 📚 PRELIMS REVIEWER — Django, WAMP/MySQL, HTTP, and Git/GitHub/Vercel

> Covers: HTTP basics → Django setup → MVC vs MVT → Dynamic URLs → Full Register/Login/Edit app with MySQL (WAMP) → Version Control & Deployment.

---

## 1. HTTP — The Protocol Behind Every Request

**HTTP** = HyperText Transfer Protocol — the agreed set of rules for how messages travel between a **client** (browser) and a **server** (Django app).

```
CLIENT SENDS →           ← SERVER RESPONDS
GET /page HTTP/1.1       HTTP/1.1 200 OK
Host: example.com        Content-Type: text/html
```

### Request Methods
| Method | Meaning | Example |
|---|---|---|
| `GET` | Retrieve a page. No server state changes. | Typing a URL, clicking a link |
| `POST` | Submit data that **changes** something. Data lives in the request body, not the URL. | Submitting a form (register, add task) |

### Status Codes (memorize these 5)
| Code | Category | Meaning |
|---|---|---|
| `200` | 2xx Success | OK — everything worked |
| `301` | 3xx Redirection | Moved Permanently |
| `403` | 4xx Client Error | Forbidden (e.g., missing CSRF token) |
| `404` | 4xx Client Error | Not Found |
| `500` | 5xx Server Error | Server-side bug |

**Quick logic:** 2xx = "got it", 3xx = "look over there", 4xx = "you messed up", 5xx = "I messed up".

---

## 2. Django Setup — From Install to Running Server

```bash
# 1. Isolate dependencies per project
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 2. Install Django
pip install django
django-admin --version

# 3. Scaffold the project (the trailing "." avoids double nesting)
django-admin startproject core .

# 4. Create an app inside the project
python manage.py startapp accounts

# 5. Run the dev server
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` → `127.0.0.1` = your own machine (loopback), `8000` = the port.

### What each generated file does
| File | Role | Analogy |
|---|---|---|
| `manage.py` | Runs every command (`runserver`, `migrate`, `startapp`) | TV remote |
| `settings.py` | Config: apps, database, security, templates | Office manual / control panel |
| `urls.py` | Table of routes → views | Receptionist's directory |
| `__init__.py` | Marks folder as a Python package | — |
| `wsgi.py` / `asgi.py` | Entry point for production servers (sync/async) | — |

### Project vs. App
| | **Project** | **App** |
|---|---|---|
| Scope | Whole website/system | One feature/module |
| Command | `django-admin startproject` | `python manage.py startapp` |
| Contains | settings, root urls, wsgi/asgi | models, views, templates, admin, migrations |
| Reusable? | No | Yes — plug into other projects |
| Analogy | Apartment complex | One apartment unit |

> 💡 A **Project** can hold **many Apps**. An app is registered by adding its name to `INSTALLED_APPS` in `settings.py`.

---

## 3. MVC vs Django's MVT

Django does **not** use MVC — it uses **MVT (Model–View–Template)**. The naming is the #1 trap in quizzes.

```
Traditional MVC:            Django MVT:
Controller (logic)     -->  View (views.py) = does the logic job
View (what's shown)    -->  Template (.html) = what's shown
                             urls.py = the "Controller"/router
```

| Role | MVC | MVT (Django) |
|---|---|---|
| Data & DB logic | Model | **Model** (`models.py`) |
| Decides logic / handles request | Controller | **View** (`views.py`) |
| What the user sees | View | **Template** (`.html`) |
| Routes requests | (varies) | `urls.py` |

⚠️ **Django's "View" = MVC's Controller. Django's "Template" = MVC's "View."**

### Restaurant analogy
| Restaurant | Django |
|---|---|
| Kitchen inventory/recipes | **Model** — stores/manages data |
| Waiter | **View** — takes the request, talks to the model, decides response |
| Printed menu / plated dish | **Template** — what the customer actually sees |
| Host who seats & routes | `urls.py` — sends the request to the right view |

### Full request-response flow
```
🌐 Browser Request
   ↓
urls.py       → "Which view?"
   ↓
views.py      → "What data?" (logic)
   ↓
models.py     → "Fetch from DB"
   ↓
template.html → "Render HTML"
   ↓
📨 HTTP Response back to Browser
```

---

## 4. Dynamic URLs & Path Converters

**Problem:** hardcoding one route per value doesn't scale.
```python
# the tedious way — never do this
path("hello/brian/", views.brian)
path("hello/david/", views.david)
path("hello/harry/", views.harry)   # ...never ends
```

**Fix:** a **path converter** — a placeholder in angle brackets `<type:name>`.

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hello/<str:name>", views.greet, name="greet"),
]
```
```python
# views.py
from django.http import HttpResponse

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
```

**Key rules:**
- `str` = the **converter type** ("match any string here"). Others include `int`, `slug`, `uuid`.
- `name` = the **variable name** — it **must match exactly** the view function's parameter name.
- Whatever the URL captures is passed straight into the view as an argument.

### Python refresher used here
```python
name = "harry"
f"Hello, {name}!"          # → 'Hello, harry!'   (f-string substitution)
f"Hello, {name.capitalize()}!"   # → 'Hello, Harry!'
word[::-1]                 # reverses a string (slicing, step -1)
```
> The `f` prefix turns on `{ }` substitution. Any valid Python (`.capitalize()`, `.upper()`, slicing) can run inside it before the response is sent — there's no special "Django way," it's just Python.

**Real-world example:** `profile/<str:username>` — the same mechanism behind `twitter.com/<username>`.

---

## 5. Full Project: Register → Login → Browse → Edit Yourself (Django + WAMP/MySQL)

### 5.1 Planning
- Reuses Django's **built-in `User` model** — no custom model needed unless you need extra fields (avatar, bio → then make a `Profile` model).
- File layout (flat `templates/` + `static/` at project root):
```
django_wamp_app/
  manage.py
  core/            (project: settings.py, urls.py, __init__.py)
  accounts/        (app: views.py, urls.py, models.py)
  templates/       (base.html, register.html, login.html, user_list.html, user_detail.html)
  static/accounts/ (style.css, logo.png)
  venv/
```

### 5.2 `DIRS` vs `APP_DIRS` (template lookup)
| | `APP_DIRS` (default) | `DIRS` (project-level) |
|---|---|---|
| Location | `accounts/templates/accounts/*.html` | `templates/*.html` at root |
| Naming | Must nest under app name | Flat, no nesting |
| Best for | Large projects, many apps | Small/medium, one app |

> Django checks `DIRS` first, then falls back to each app's own folder — keep `APP_DIRS: True` too or `/admin/` breaks.

### 5.3 Terminal setup
```bash
mkdir django_wamp_app && cd django_wamp_app
python -m venv venv
venv\Scripts\activate

pip install django mysqlclient
# if mysqlclient fails to build on Windows:
pip install pymysql

django-admin startproject core .
python manage.py startapp accounts
```

### 5.4 Create the database — **in phpMyAdmin, not Django**
1. Open WAMP's phpMyAdmin (`localhost/phpmyadmin<version>/`).
2. Databases tab → type exact name `django_wamp_db` → **Create**.

> ⚠️ **Django never creates the database itself.** `migrate` only builds *tables* inside a database that already exists. Skipping this step throws `OperationalError: Unknown database`.

### 5.5 `core/__init__.py` — pymysql shim (only if using `pymysql` instead of `mysqlclient`)
```python
import pymysql
pymysql.install_as_MySQLdb()
```
> Runs *before* `settings.py` is parsed, so `pymysql` is already registered as `MySQLdb` by the time Django reads `DATABASES`.

### 5.6 `settings.py`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_wamp_db',
        'USER': 'root',
        'PASSWORD': '',        # WAMP default: root, no password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

LOGIN_URL = 'login'                 # overrides default /accounts/login/
LOGIN_REDIRECT_URL = 'user_list'
```

### 5.7 `accounts/views.py`
```python
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views, login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created — you're logged in.")
            return redirect('user_list')
        else:
            messages.error(request, 'Registration failed. See errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class MyLoginView(auth_views.LoginView):
    template_name = 'login.html'


@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


@login_required
def user_detail(request, pk):
    target_user = get_object_or_404(User, pk=pk)
    is_self = target_user.pk == request.user.pk

    if request.method == 'POST':
        if not is_self:
            messages.error(request, 'You can only edit your own profile.')
            return redirect('user_detail', pk=target_user.pk)
        form = UserChangeForm(request.POST, instance=target_user)
        form.fields.pop('password', None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated.')
            return redirect('user_detail', pk=target_user.pk)
    else:
        form = UserChangeForm(instance=target_user)
        form.fields.pop('password', None)

    return render(request, 'user_detail.html',
        {'target_user': target_user, 'is_self': is_self, 'form': form})
```
> 🔒 **The real security check:** `target_user.pk == request.user.pk`, done **server-side**. Hiding an edit button in HTML is never enough — a forged POST could still hit the view directly.

### 5.8 URL routing (two layers)
```python
# accounts/urls.py  — brand-new file, does NOT exist after startapp
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
]
```
```python
# core/urls.py — already exists; you only ADD the last two lines
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='users/', permanent=False)),
    path('', include('accounts.urls')),
]
```

### 5.9 Templates (key patterns to remember)
```html
{# templates/base.html #}
{% load static %}
<link rel="stylesheet" href="{% static 'accounts/style.css' %}">
{% if messages %}
    {% for message in messages %}
        <p class="msg-{{ message.tags }}">{{ message }}</p>
    {% endfor %}
{% endif %}
{% block content %}{% endblock %}
```
```html
{# any form template #}
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```
```html
{# POST-only logout — GET is blocked since Django 5.0 #}
<form method="post" action="{% url 'logout' %}" style="display:inline;">
    {% csrf_token %}
    <button type="submit" class="link-button">Logout</button>
</form>
```
```html
{# conditionally show edit form vs read-only view #}
{% if is_self %}
    <form method="post">{% csrf_token %}{{ form.as_p }}<button>Save changes</button></form>
{% else %}
    <p>Email: {{ target_user.email }}</p>
    <p><em>You can only edit your own profile.</em></p>
{% endif %}
```

### 5.10 Final steps
```bash
python manage.py migrate
python manage.py runserver
```

---

## 6. Bugs You Will Get Asked About (Cause → Fix)

| Error | Cause | Fix |
|---|---|---|
| `OperationalError 1049 — Unknown database` | Database wasn't created in phpMyAdmin first | Create `django_wamp_db` in phpMyAdmin **before** `migrate` |
| `TemplateDoesNotExist: login.html` | Folder named `template` (no "s") or `DIRS` missing | Rename to `templates`; set `'DIRS': [BASE_DIR / 'templates']` |
| `ModuleNotFoundError: pymysql` | `import pymysql` added but package never installed | `pip install pymysql` |
| `404 Not Found: /accounts/login/` | Django's default `LOGIN_URL` doesn't match your route | Set `LOGIN_URL = 'login'` (by **name**, not raw path) |
| `405 Method Not Allowed: /logout/` | Django 5+ blocks GET on `LogoutView` | Use `<form method="post">` styled as a link, not `<a href>` |

### Lessons worth remembering
- The **database** must exist before `migrate` — Django only builds tables, never the database itself.
- `templates` must be spelled exactly that way.
- An `import` line does nothing until you actually `pip install` the package in the active `venv`.
- Since Django 5, **logout requires POST**.
- The real "edit only yourself" permission check lives in the **view**, server-side — never trust a hidden button.

---

## 7. Version Control & Deployment — Git, GitHub, Vercel

### What is Git?
**Distributed version control system** — tracks changes to code over time.
Key concepts: **repository, commit, branch, merge**.
> Analogy: "Track Changes" for an entire project / a save-game system / a time machine for your codebase.

**Similar tools:** Mercurial (Hg), SVN (older, centralized), Perforce (game dev). Git won — it's the industry standard.

**Core commands:**
```bash
git init
git add .
git commit -m "message"
git branch <name>
git checkout <branch>   # or: git switch <branch>
git merge <branch>
git pull
git push
```

**Workflow:** `working directory → staging area → local repo → remote repo`

### What is GitHub?
**Cloud hosting platform** for Git repositories — collaboration layer on top of Git.
- Git = the tool (local). GitHub = the platform/service (remote + social).
- Features: remote repos, pull requests, issues, Actions (CI/CD), Pages.
> Analogy: Google Drive for your Git repos, or a social network for code. Git is the engine, GitHub is the garage.

**Similar tools:** GitLab (popular for self-hosting/CI-CD), Bitbucket (integrates with Jira/Trello).

**Git vs GitHub:**
| Git | GitHub |
|---|---|
| Local version control | Online collaboration + hosting |

**Typical team workflow:** clone → branch → commit → push → open PR → review → merge

### What is Vercel?
**Cloud platform for frontend deployment & hosting** — built for Next.js/React, zero-config deploys, instant previews.
> Analogy: a vending machine for websites (push code in, get a live URL out), or valet parking for your app.

**Similar tools:** Netlify (static/JAMstack), AWS Amplify (more infra control), Railway/Render (backend+DB too), GitHub Pages (static only).

**Why Vercel:** Git integration (auto-deploy on push), preview deployments per branch/PR, global CDN, free tier.

### The full pipeline (the "aha" moment)
```
Code locally (Git) → Push to GitHub → Vercel auto-deploys → Live site
```

### Recap
- **Git** = version control (the time machine)
- **GitHub** = collaboration & hosting (the shared garage)
- **Vercel** = deployment & hosting (the valet)
- Together = full dev-to-production pipeline

---

## 8. Quick Syntax Cheat Sheet (all modules, side by side)

```python
# ── Path converters ──────────────────────────
path("hello/<str:name>", views.greet, name="greet")
path("users/<int:pk>/", views.user_detail, name="user_detail")

# ── f-strings ─────────────────────────────────
f"Hello, {name.capitalize()}!"
f"{word.upper()}!!!"
word[::-1]                       # reverse a string

# ── Common settings.py lines ──────────────────
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'user_list'
DATABASES = {'default': {'ENGINE': 'django.db.backends.mysql', ...}}

# ── pymysql shim (core/__init__.py) ───────────
import pymysql
pymysql.install_as_MySQLdb()

# ── Auth decorators/views ─────────────────────
@login_required
def my_view(request): ...

from django.contrib.auth.views import LogoutView
path('logout/', LogoutView.as_view(next_page='login'), name='logout')
```
```html
<!-- CSRF token — required inside every POST form -->
{% csrf_token %}

<!-- Static files -->
{% load static %}
<img src="{% static 'accounts/logo.png' %}">

<!-- URL reversal -->
<a href="{% url 'user_list' %}">All users</a>
```
```bash
# ── Terminal command cheat sheet ──────────────
python -m venv venv
pip install django mysqlclient
django-admin startproject core .
python manage.py startapp accounts
python manage.py migrate
python manage.py runserver
git init && git add . && git commit -m "init"
git push origin main
```

---

## 9. Rapid-Fire Self-Check (answer, then compare with the quiz file)

1. What ENGINE does MySQL use in `DATABASES`? → `django.db.backends.mysql`
2. What model does the account app reuse? → built-in `User`
3. What HTTP method does `LogoutView` require since Django 5.0? → `POST`
4. Where must `django_wamp_db` be created? → phpMyAdmin (not by Django)
5. What overrides the default `/accounts/login/` redirect? → `LOGIN_URL`
6. Pure-Python fallback MySQL driver? → `pymysql`
7. File that must be created manually for app routing? → `accounts/urls.py`
8. Error from a `template` (singular) folder? → `TemplateDoesNotExist`
9. Boolean that checks "is this your own profile"? → `is_self`
10. Framework behind the success/error banners? → `django.contrib.messages`

---

*Good luck sa prelims! Review the code blocks by actually typing them out — muscle memory helps more than re-reading.*
