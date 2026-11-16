# Comprehensive Reviewer: Program & Project Architecture + Django + Python

---

## PART 1: COURSE OVERVIEW & CONTEXT

### Integrative Programming — The Big Picture

This course combines three major areas:
1. **Python programming** — logic, data structures, OOP
2. **Web development with Django** — building dynamic web applications
3. **System architecture** — how programs and systems are structured

---

## PART 2: PYTHON DUNDER (MAGIC) METHODS

### What Are Dunder Methods?

**Dunder** = **D**ouble **Under**score (methods with `__` at start and end). These are special methods in Python that define how objects behave with built-in operations.

### Most Important Dunder Methods

| Method | Purpose | Example Use |
|--------|---------|-------------|
| `__init__(self, ...)` | Constructor — initializes object | `obj = MyClass()` |
| `__str__(self)` | String representation for users | `print(obj)` |
| `__repr__(self)` | String representation for developers | `repr(obj)` |
| `__len__(self)` | Length of object | `len(obj)` |
| `__getitem__(self, key)` | Indexing/slicing | `obj[key]` |
| `__setitem__(self, key, value)` | Assignment by index | `obj[key] = value` |
| `__call__(self, ...)` | Object callable like a function | `obj()` |
| `__eq__(self, other)` | Equality comparison | `obj == other` |
| `__lt__(self, other)` | Less than | `obj < other` |
| `__add__(self, other)` | Addition | `obj + other` |
| `__enter__` / `__exit__` | Context manager | `with obj:` |

### Example: Creating a Custom Class

```python
class Task:
    def __init__(self, title, priority=1):
        self.title = title
        self.priority = priority
        self.completed = False
    
    def __str__(self):
        return f"{self.title} (Priority: {self.priority})"
    
    def __repr__(self):
        return f"Task('{self.title}', {self.priority})"
    
    def __eq__(self, other):
        if not isinstance(other, Task):
            return False
        return self.title == other.title
    
    def __lt__(self, other):
        return self.priority < other.priority

# Usage
t1 = Task("Learn Django", 2)
t2 = Task("Build a project", 1)
print(t1)              # Uses __str__
print(repr(t1))        # Uses __repr__
print(t1 == t2)        # Uses __eq__
print(t1 < t2)         # Uses __lt__ (False because 2 < 1 is False)
```

### Django Models & Dunder Methods

Django models commonly override `__str__` for readable admin display:

```python
class Task(models.Model):
    title = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title  # Shows in admin, shell, and debugging
```

---

## PART 3: PROGRAM & PROJECT ARCHITECTURE (M10)

### 3.1 What Is Architecture?

**Software Architecture** = the high-level structure of a system:
- How it's broken into parts (components/modules)
- How those parts communicate
- The principles guiding their design

**Two Key Distinctions:**

| Term | What It Means |
|------|---------------|
| **Program Architecture** | Internal structure of ONE application (e.g., MVC inside a Django app) |
| **Project/System Architecture** | How MULTIPLE systems interact (web app + API + database + payment gateway) |

**Why It Matters:**
- ✅ **Maintainability** — easier to fix bugs, add features
- ✅ **Scalability** — system grows without collapsing
- ✅ **Reusability** — components reused across projects
- ✅ **Team Collaboration** — different devs work on different layers
- ✅ **Testability** — isolated components easier to test
- ✅ **Integration** — connecting different systems cleanly

---

### 3.2 Core Design Principles

| Principle | Meaning | Example |
|-----------|---------|---------|
| **Separation of Concerns (SoC)** | Each part handles ONE responsibility | Don't mix database code with UI code |
| **DRY** (Don't Repeat Yourself) | Avoid duplicating logic | Centralize common functions |
| **KISS** (Keep It Simple, Stupid) | Avoid unnecessary complexity | Choose simple solutions first |
| **Loose Coupling** | Components depend as little as possible | Changing one doesn't break another |
| **High Cohesion** | Related logic grouped together | All user-related code in one module |
| **SOLID Principles** | Five OOP design principles | Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion |

---

### 3.3 Foundational Architecture: Client-Server Model

```
┌────────────┐        HTTP Request        ┌────────────┐
│   CLIENT   │  ─────────────────────────► │   SERVER   │
│ (Browser/  │                             │ (Web/App   │
│  Mobile)   │  ◄───────────────────────── │  Server)   │
└────────────┘        HTTP Response        └────────────┘
                                                    │
                                                    ▼
                                             ┌────────────┐
                                             │  DATABASE  │
                                             └────────────┘
```

- **Client** — requests and displays data
- **Server** — processes requests, applies logic
- **Database** — stores persistent data

This is **2-tier**. Real web apps usually expand to **3-tier** or **N-tier**.

---

### 3.4 Tiered (Layered) Architectures

#### Three-Tier Architecture (Most Common)

| Tier | Responsibility | Examples |
|------|---------------|----------|
| **1. Presentation** | UI — what user sees/interacts with | HTML/CSS/JS, React |
| **2. Application/Logic** | Business rules, processing, validation | Django, Node.js/Express |
| **3. Data** | Storage and retrieval | MySQL, PostgreSQL, MongoDB |

#### N-Tier (Multi-Tier) Architecture
Extension of 3-tier with more specialized layers:

```
Presentation → API/Gateway → Business Logic → Data Access → Database
```

---

### 3.5 Program Architecture Patterns

#### MVC (Model-View-Controller)
*Most common in web frameworks (Django, Rails, Spring MVC)*

```
        User Interaction
              │
              ▼
       ┌─────────────┐
       │ CONTROLLER  │ ← receives input, decides action
       └─────────────┘
          │        │
          ▼        ▼
     ┌────────┐  ┌───────┐
     │ MODEL  │  │ VIEW  │
     │ (data/ │  │ (UI/  │
     │ logic) │  │output)│
     └────────┘  └───────┘
```

| Component | Responsibility |
|-----------|----------------|
| **Model** | Data + business logic (e.g., database interaction) |
| **View** | What user sees (UI templates) |
| **Controller** | Handles user input, coordinates Model and View |

#### MVVM (Model-View-ViewModel)
Common in modern frontend (Vue, Angular, React with state managers)
- **ViewModel** binds Model to View with two-way data binding
- View updates automatically when ViewModel changes

#### MVP (Model-View-Presenter)
- **Presenter** handles ALL UI logic
- View is "passive" (dumb) — just displays what Presenter tells it
- Easier to test/mock the UI

---

### 3.6 System-Level (Project) Architectures

#### Monolithic Architecture
Entire application built and deployed as ONE unit.

```
┌─────────────────────────────┐
│        ONE APPLICATION      │
│  UI + Logic + DB Access     │
└─────────────────────────────┘
```

| Pros | Cons |
|------|------|
| Simple to develop, test, deploy | Hard to scale specific parts |
| Easy for small teams | One bug can bring down whole app |
| | Harder to adopt new tech gradually |

#### Microservices Architecture
Split into small, independent services, each responsible for one business capability.

```
 ┌───────────┐   ┌───────────┐   ┌───────────┐
 │   User    │   │  Order    │   │  Payment  │
 │  Service  │   │  Service  │   │  Service  │
 └─────┬─────┘   └─────┬─────┘   └─────┬─────┘
       │               │               │
       └────────┬──────┴──────┬────────┘
                 ▼             ▼
           ┌────────────────────────┐
           │     API Gateway        │
           └────────────────────────┘
                       │
                       ▼
                    Client
```

| Pros | Cons |
|------|------|
| Independently deployable | Complex to manage |
| Different tech stacks possible | Needs strong DevOps |
| Failure isolation | Data consistency harder |

#### SOA (Service-Oriented Architecture)
Predecessor to microservices. Larger, shared services communicate through **Enterprise Service Bus (ESB)**.

**Difference SOA vs Microservices:**
| SOA | Microservices |
|-----|---------------|
| Larger, shared services | Small, independent services |
| Often uses ESB (centralized) | Usually decentralized |
| Shares data store sometimes | Each owns its own database |

#### Serverless Architecture
Code runs in stateless functions (AWS Lambda, Azure Functions, Google Cloud Functions). No server management.

| Pros | Cons |
|------|------|
| No server management | Cold-start latency |
| Automatic scaling | Vendor lock-in |
| Pay-per-execution | Harder to debug locally |

#### Event-Driven Architecture (EDA)
Components communicate by producing/reacting to **events** via message broker (Kafka, RabbitMQ).

```
Producer → [Event] → Message Broker → Consumer(s)
```

**Use case:** real-time systems, notifications, order processing pipelines.

---

### 3.7 API-Centric Architecture (Integration Focus)

**RESTful Architecture** — uses standard HTTP methods:

| Method | Action | Example |
|--------|--------|---------|
| GET | Read | `GET /api/students` |
| POST | Create | `POST /api/students` |
| PUT/PATCH | Update | `PUT /api/students/5` |
| DELETE | Delete | `DELETE /api/students/5` |

**REST Principles:**
- Stateless
- Resource-based URLs
- Standard status codes (200, 404, 500, etc.)
- Typically returns JSON

**Other Integration Styles:**
- **SOAP** — XML-based, strict protocol (older enterprise/banking)
- **GraphQL** — client specifies exact data needed
- **WebSockets** — persistent two-way connection (chat, live dashboards)
- **Webhooks** — server-to-server "push" notifications

---

### 3.8 Typical Web Project Folder Structure (MVC-based)

```
project-root/
├── controllers/       # Handles requests, calls models
├── models/            # Database schemas & business logic
├── views/             # Templates (if server-rendered)
├── routes/            # Defines API endpoints/URLs
├── middleware/        # Auth, logging, validation
├── config/            # DB connection, environment configs
├── public/            # Static assets (CSS, JS, images)
├── services/          # External API integrations
├── utils/             # Helper functions
├── tests/             # Unit/integration tests
├── app.js             # Entry point
└── package.json
```

This reflects **Separation of Concerns** in action.

---

### 3.9 Architecture Comparison Summary

| Architecture | Best For | Complexity | Scalability |
|--------------|----------|------------|-------------|
| Monolithic | Small apps, MVPs | Low | Limited |
| 3-Tier/N-Tier | Standard business web apps | Medium | Good |
| MVC | Server-rendered web frameworks | Low–Medium | Good |
| MVVM | Modern SPA frontends | Medium | Good |
| Microservices | Large, complex systems | High | Excellent |
| SOA | Enterprise systems | High | Good |
| Serverless | Event-driven, variable workloads | Medium | Excellent (auto) |
| Event-Driven | Real-time, decoupled systems | High | Excellent |

---

### 3.10 How to Choose an Architecture

**Key Questions:**
1. **Team/Project size?** — Small = monolithic/MVC; Large = microservices
2. **Expected scaling?** — Yes = microservices/serverless
3. **Domain complexity?** — Complex = microservices/SOA
4. **DevOps maturity?** — Low = avoid microservices (too much overhead)
5. **Real-time needs?** — Consider event-driven / WebSockets
6. **Integration with external systems?** — Focus on well-designed API layer

---

## PART 4: DJANGO BASICS (From CS50 Transcript)

### 4.1 What is Django?

**Django** = Python web framework that allows writing Python code to **dynamically generate HTML and CSS**.

Instead of static HTML pages (same every time), Django creates **dynamic web applications**.

---

### 4.2 HTTP Fundamentals

**Protocol**: HyperText Transfer Protocol (HTTP) — how messages are sent over the internet.

**Request-Response Cycle:**
```
Client (Browser) → GET / → Server → Response (HTML)
```

**HTTP Request Example:**
```
GET / HTTP/1.1
Host: example.com
```

**HTTP Response Example:**
```
HTTP/1.1 200 OK
Content-Type: text/html

<html>...</html>
```

**Common Status Codes:**
| Code | Meaning |
|------|---------|
| 200 | OK (success) |
| 301 | Moved Permanently (redirect) |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

### 4.3 Setting Up a Django Project

**Install Django:**
```bash
pip3 install Django
```

**Create a Project:**
```bash
django-admin startproject projectname
```

**Project Structure:**
```
projectname/
├── manage.py          # Command-line utility
├── projectname/
│   ├── __init__.py
│   ├── settings.py    # Configuration
│   ├── urls.py        # URL routing (table of contents)
│   └── wsgi.py
```

**Run the Server:**
```bash
python manage.py runserver
```

### 4.4 Django Apps vs Project

- **Project** = entire website (e.g., Google)
- **App** = specific functionality within project (e.g., Google Search, Google Maps)
- One project can have **multiple apps**

**Create an App:**
```bash
python manage.py startapp appname
```

**App Structure:**
```
appname/
├── __init__.py
├── admin.py
├── apps.py
├── models.py         # Database models
├── tests.py
├── views.py          # Request handlers
└── migrations/
```

**Install App in settings.py:**
```python
INSTALLED_APPS = [
    # ...default apps...
    'appname',  # <-- add your app
]
```

---

### 4.5 Views (views.py)

**View** = Python function that handles a request and returns a response.

```python
# views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")
```

**Using render()** — render a template:
```python
from django.shortcuts import render

def index(request):
    return render(request, "appname/index.html", {"key": "value"})
```

The third argument is **context** — a dictionary of variables passed to the template.

---

### 4.6 URL Routing (urls.py)

**Purpose:** Map URLs to view functions.

**Project-level urls.py:**
```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appname/', include('appname.urls')),
]
```

**App-level urls.py** (create it yourself):
```python
from django.urls import path
from . import views

app_name = "appname"  # Namespace (prevents collisions)

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("<str:name>/", views.greet, name="greet"),  # Parameterized URL
]
```

**URL Parameters with Path Converters:**
- `<str:name>` — captures a string
- `<int:post_id>` — captures an integer
- `<slug:slug>` — captures a slug

---

### 4.7 Templates

**Location:** `appname/templates/appname/template.html`

**Template Inheritance** — DRY for HTML:

**layout.html (parent):**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <nav>...</nav>
    {% block body %}{% endblock %}
    <footer>...</footer>
</body>
</html>
```

**child.html:**
```html
{% extends "appname/layout.html" %}

{% block title %}Tasks{% endblock %}

{% block body %}
    <h1>My Tasks</h1>
    {% for task in tasks %}
        <li>{{ task }}</li>
    {% endfor %}
{% endblock %}
```

### 4.8 Template Syntax

| Syntax | Purpose |
|--------|---------|
| `{{ variable }}` | Print a variable value |
| `{% if condition %}` | Conditional logic |
| `{% for item in list %}` | Loop over a list |
| `{% block name %}` | Define a block for inheritance |
| `{% extends "parent.html" %}` | Inherit from parent template |
| `{% url 'appname:name' %}` | Generate URL from name |

### 4.9 Static Files

**Location:** `appname/static/appname/`

**Loading static files in templates:**
```html
{% load static %}
<link rel="stylesheet" href="{% static 'appname/style.css' %}">
```

---

### 4.10 Forms & CSRF Protection

**CSRF** = Cross-Site Request Forgery — a security vulnerability where attackers forge requests.

**Django's CSRF Protection:**
- Enabled by default via `CsrfViewMiddleware`
- Requires `{% csrf_token %}` in every POST form

**Creating a Form with Django Forms:**

```python
# forms.py
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task", max_length=200)
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)
```

**Using the form in views:**
```python
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # Save task...
            return redirect("tasks:index")
    else:
        form = NewTaskForm()
    return render(request, "tasks/add.html", {"form": form})
```

**Template:**
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Add</button>
</form>
```

**The Form Processing Flow:**
```
GET → display blank form
POST → validate data
  → Valid → save() + redirect
  → Invalid → re-render with errors
```

---

### 4.11 Sessions

**What are Sessions?**
- Way for server to remember a specific user between requests
- Stored as a dictionary: `request.session`

**Storing data in session:**
```python
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    tasks = request.session["tasks"]
    return render(request, "tasks/index.html", {"tasks": tasks})
```

**Adding to session:**
```python
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]  # Add to session
            return redirect("tasks:index")
```

**IMPORTANT:** Sessions require a database table. Run migrations:
```bash
python manage.py migrate
```

**Always check if key exists first:**
```python
visits = request.session.get("visits", 0)  # Safe! Returns 0 if not set
request.session["visits"] = visits + 1
```

---

### 4.12 Namespaces & URL Naming

**Prevent URL Name Collisions:**
```python
# tasks/urls.py
app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
]
```

**Referencing URLs:**
- In templates: `{% url 'tasks:index' %}`
- In views: `from django.urls import reverse` → `reverse("tasks:index")`

**Why?** If you change the URL path, all references update automatically.

---

### 4.13 Reverse URL Resolution

```python
from django.urls import reverse
from django.http import HttpResponseRedirect

def add(request):
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("tasks:index"))
```

---

## PART 5: KEY DJANGO COMMANDS SUMMARY

| Command | Purpose |
|---------|---------|
| `django-admin startproject name` | Create a new project |
| `python manage.py startapp name` | Create a new app |
| `python manage.py runserver` | Run development server |
| `python manage.py makemigrations` | Create migration files |
| `python manage.py migrate` | Apply migrations to database |
| `python manage.py dbshell` | Open database shell |
| `python manage.py shell` | Open Django shell (with models) |

---

## PART 6: DJANGO FLOW SUMMARY

### Request-Response Flow in Django

```
1. Client sends HTTP request
2. Django matches URL in urls.py
3. Django calls the associated view function
4. View processes request (checks method, validates data)
5. View interacts with Model/Form/Session if needed
6. View returns HttpResponse (or render() of template)
7. Template is rendered with context data
8. HTTP response is sent back to client
```

### Form Processing Pattern (Common in Every Django Form View)

```
GET Request:
  → Display blank/unbound form
  → User fills it out

POST Request:
  → Create bound form with request.POST
  → if form.is_valid():
      → form.save() (for ModelForm) or process cleaned_data
      → redirect to success page
    else:
      → Re-render form with errors
```

---

## PART 7: STUDY TIPS & KEY TAKEAWAYS

### Most Important Concepts to Remember

1. **Architecture Principles:**
   - Separation of Concerns (SoC)
   - DRY (Don't Repeat Yourself)
   - Loose Coupling / High Cohesion
   - MVC pattern

2. **Django Core Concepts:**
   - Project vs App
   - Views (functions that handle requests)
   - Templates (HTML + Django templating)
   - URL routing (urls.py)
   - Sessions (per-user data)

3. **Form Handling:**
   - Always use POST for data-changing operations
   - Always include `{% csrf_token %}`
   - Always validate with `form.is_valid()`

4. **Best Practices:**
   - Use `{% url %}` and `reverse()` — never hardcode URLs
   - Use `app_name` for namespacing
   - Use template inheritance to avoid duplication
   - Always check session keys with `.get(key, default)`

### Common Pitfalls to Avoid

- ❌ Forgetting `{% csrf_token %}` in POST forms
- ❌ Hardcoding URLs instead of using `{% url %}`
- ❌ Forgetting to run `migrate` after creating models or using sessions
- ❌ Not checking if a session key exists before reading it
- ❌ Mixing Python logic and HTML without template inheritance

---

## PART 8: QUICK REFERENCE CARDS

### URL Parameter Types
```python
path("<str:name>/", views.greet, name="greet")     # String
path("<int:post_id>/", views.detail, name="detail") # Integer
path("<slug:slug>/", views.article, name="article") # Slug
```

### Template Variable Syntax
```html
{{ variable }}          <!-- Print value -->
{% if condition %}      <!-- Condition -->
{% for item in list %}  <!-- Loop -->
{% block name %}        <!-- Block for inheritance -->
{% extends "parent" %}  <!-- Inherit from parent -->
{% url 'app:name' %}    <!-- URL from name -->
{% load static %}       <!-- Load static files -->
```

### Session Operations
```python
request.session["key"] = value      # Set value
value = request.session["key"]      # Get value (raises KeyError if missing)
value = request.session.get("key")  # Get value (returns None if missing)
del request.session["key"]          # Delete key
"key" in request.session            # Check if key exists
```

### Form Validation Flow
```python
form = FormClass(request.POST)  # Bind data
if form.is_valid():             # Validate
    data = form.cleaned_data    # Get clean data
    form.save()                 # Save (ModelForm)
    return redirect(...)        # Redirect on success
else:                           # Invalid
    return render(request, "template.html", {"form": form})  # Show errors
```

---

**Good luck on your exam! 🎉**