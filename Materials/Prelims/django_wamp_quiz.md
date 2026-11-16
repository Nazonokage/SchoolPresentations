# Django + WAMP User Accounts — Quiz (20 items)

*Based on the "Register → Login → Browse → Edit Yourself" tutorial.*

---

## Part I — Multiple Choice (1–5)

**1.** In `settings.py`, what `ENGINE` value does this project's `DATABASES` config use?
A. `django.db.backends.sqlite3`
B. `django.db.backends.mysql`
C. `django.db.backends.postgresql`
D. `django.db.backends.oracle`

**2.** Which built-in Django model does this app reuse instead of creating a custom one?
A. `Profile`
B. `Account`
C. `User`
D. `Member`

**3.** Since Django 5.0, which HTTP method does `LogoutView` require?
A. GET
B. POST
C. PUT
D. DELETE

**4.** Where must the `django_wamp_db` database itself be created before running `migrate`?
A. Django creates it automatically on first `migrate`
B. In phpMyAdmin
C. Inside `settings.py`
D. Via `manage.py shell`

**5.** Which setting tells Django where to send an unauthenticated user, overriding the `/accounts/login/` default?
A. `LOGIN_REDIRECT_URL`
B. `LOGIN_URL`
C. `ROOT_URLCONF`
D. `AUTH_USER_MODEL`

---

## Part II — Identification (6–10)

**6.** Name the pure-Python package used as a fallback MySQL driver when `mysqlclient` fails to build.

**7.** Name the file that does **not** exist after `startapp` and must be created from scratch to route the `accounts` app's URLs.

**8.** Name the error you get if the templates folder is named `template` instead of `templates` (or `DIRS` isn't set).

**9.** Name the view-level boolean variable that checks whether the logged-in user is viewing/editing their *own* profile.

**10.** Name the Django framework responsible for the "Account created — you're logged in." style banners shown at the top of every page.

---

## Part III — Guess the Output (11–15)

**11.**
```python
LOGIN_URL = 'login'
```
An unauthenticated user visits `/users/`. Where do they end up?

**12.**
```python
@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})
```
What happens if a logged-out visitor requests this view directly?

**13.**
```python
if not is_self:
    messages.error(request, 'You can only edit your own profile.')
    return redirect('user_detail', pk=target_user.pk)
```
User A is logged in and submits a POST trying to edit User B's profile. What's the result?

**14.** Given `path('users/', views.user_list, name='user_list')`, what URL does this render to?
```html
<a href="{% url 'user_list' %}">All users</a>
```

**15.**
```python
form = UserChangeForm(instance=target_user)
form.fields.pop('password', None)
```
What shows up (or doesn't) in the rendered form because of that second line?

---

## Part IV — Write the Code (16–20, 1–2 lines each)

**16.** Write the one `settings.py` line that redirects unauthenticated users to the URL named `'login'`.

**17.** Write the two-line `pymysql` shim that belongs in `core/__init__.py`.

**18.** Write the terminal command to install Django together with the `mysqlclient` MySQL driver.

**19.** Write the one template tag that must sit inside `<form method="post">` to prevent CSRF attacks.

**20.** Write the `path()` line that routes `/logout/` to Django's `LogoutView`, redirecting to `'login'` afterward, named `'logout'`.

---
---

# Answer Key

**Part I — Multiple Choice**
1. B — `django.db.backends.mysql`
2. C — `User`
3. B — POST
4. B — phpMyAdmin (Django only builds tables, never the database itself)
5. B — `LOGIN_URL`

**Part II — Identification**
6. `pymysql`
7. `accounts/urls.py`
8. `TemplateDoesNotExist`
9. `is_self`
10. The messages framework (`django.contrib.messages`)

**Part III — Guess the Output**
11. Redirected to `/login/` (the URL named `'login'`) — they're not authenticated yet.
12. `@login_required` intercepts it and redirects them to `LOGIN_URL` before the view body ever runs.
13. An error message ("You can only edit your own profile.") is queued and they're redirected back to User B's own detail page — nothing is saved.
14. `/users/`
15. The `password` field is removed from the form entirely, so no password/hash field is rendered or editable — only the remaining fields (username, email, names, etc.) show.

**Part IV — Write the Code**
16. `LOGIN_URL = 'login'`
17.
```python
import pymysql
pymysql.install_as_MySQLdb()
```
18. `pip install django mysqlclient`
19. `{% csrf_token %}`
20. `path('logout/', LogoutView.as_view(next_page='login'), name='logout')`
