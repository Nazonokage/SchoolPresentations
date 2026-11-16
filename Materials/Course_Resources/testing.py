from django import forms
from django.conf import settings


if not settings.configured:
    settings.configure(USE_I18N=False, SECRET_KEY="standalone-test")


class Task:
    def __init__(self, title, priority=1):
        self.title, self.priority = title, priority
    def __str__(self): return f"{self.title} (P{self.priority})"
    def __repr__(self): return f"Task({self.title!r}, {self.priority})"
    def __eq__(self, other): return isinstance(other, Task) and self.title == other.title
t1, t2 = Task("Ship", 2), Task("Ship", 5)
print(t1); print(repr(t2)); print(t1 == t2)
print(t1 , t2)


print("+++++++++++++++++++++++++++++++")

class Item:
    def __repr__(self): return "Item(X)"
i = Item()
print(i); print(str(i)); print(repr(i))

print("+++++++++++++++++++++++++++++++")


class SessionRequest:
    def __init__(self):
        self.session = {}


request = SessionRequest()
visits = request.session.get("visits", 0)
request.session["visits"] = visits + 1
print(request.session.get("visits")); print("visits" in request.session)

print("+++++++++++++++++++++++++++++++")


class TaskForm(forms.Form):
    title = forms.CharField()
    is_done = forms.BooleanField(required=False)


form = TaskForm(data={"title": "", "is_done": True})
print(form.is_valid()); print("title" in form.errors)
