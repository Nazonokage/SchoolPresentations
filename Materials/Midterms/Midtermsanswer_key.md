# IT103 Integrative Programming — Periodical Exam
## Answer Key

**Final Structure (Total 70 pts)**

| Section              | Numbers | Count | Pts each | Subtotal |
|----------------------|---------|-------|----------|----------|
| Multiple Choice      | 1–20    | 20    | 1        | 20       |
| Identification       | 21–25   | 5     | 1        | 5        |
| Enumeration (M10)    | 26–45   | 20    | 1        | 20       |
| Guess the Output     | 46–50   | 5     | 1        | 5        |
| Coding Problems      | 51–54   | 4     | 5        | 20       |
| **Total**            |         | **54**|          | **70**   |

---

### I. Multiple Choice (1–20)

| # | Ans |
|---|-----|
| 1 | A 
| 2 | B 
| 3 | C 
| 4 | C 
| 5 | C 
| 6 | B 
| 7 | A 
| 8 | C 
| 9 | A 
| 10 | B 

| # | Ans |
|---|-----|
| 11 | C |
| 12 | B |
| 13 | A |
| 14 | B |
| 15 | C |
| 16 | A |
| 17 | B |
| 18 | A |
| 19 | A |
| 20 | C |
---

### II. Identification (21–25)

| # | Answer |
|---|--------|
| 21 | Monolithic architecture |
| 22 | Separation of Concerns (SoC) |
| 23 | ViewModel |
| 24 | Service-Oriented Architecture (SOA) |
| 25 | GraphQL |

---

### III. Enumeration (26–45)

**Benefits (any valid order)**  
26–28: Maintainability / Scalability / Reusability / Testability / Integration / Team collaboration (any three)

**3-Tier**  
29. Presentation  
30. Application / Logic  
31. Data  

**MVC**  
32. Model  
33. View  
34. Controller  

**REST**  
35. GET  
36. POST  
37. PUT / PATCH  
38. DELETE  

**Design principles**  
39. Separation of Concerns (SoC)  
40. DRY  
41. KISS  
42. Loose coupling  
43. High cohesion  

**System architectures**  
44. Monolithic  
45. Microservices  

---

### IV. Guess the Output (46–50)

**46.**
```
Ship (P2)
Task('Ship', 5)
True
```

**47.**
```
Item(X)
Item(X)
Item(X)
```

**48.**
```
1
True
```

**49.**
```
<li>A-1</li>
<li>B-2</li>
```

**50.**
```
False
True
```

---

### V. Coding Problems (51–54) — 5 pts each

**51.**
```python
class Task:
    def __init__(self, title, priority=1):
        self.title = title
        self.priority = priority

    def __str__(self):
        return f"{self.title} (Priority: {self.priority})"

    def __eq__(self, other):
        return self.title == other.title

    def __lt__(self, other):
        return self.priority < other.priority
```

**52.**
```python
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import TaskForm

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            return redirect(reverse("tasks:task_list"))
    else:
        form = TaskForm()
    return render(request, "tasks/add_task.html", {"form": form})
```

**53.**
```python
def homepage(request):
    visits = request.session.get("visits", 0)
    visits += 1
    request.session["visits"] = visits
    return render(request, "home.html", {"visits": visits})
```

**54.**
```django
{% extends "blog/layout.html" %}

{% block content %}
  {% for post in posts %}
    <a href="{% url 'blog:post_detail' post.id %}">{{ post.title }}</a>
  {% endfor %}
{% endblock %}
```
