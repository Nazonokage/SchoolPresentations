# IT102 Platform Technologies – Pre-Final Periodical Exam: Answer Key (Updated)

**52 Items (60 Points) | 90 Minutes | 2 pages** — All answers verified against *platform_tech_reviewer.docx* (Parts 1–6).

## I. Multiple Choice (1 pt each)

| # | Answer | Reviewer section |
|---|--------|------------------|
| 1 | C – Drupal | 2.2 |
| 2 | B – getDoc() | 1.10 |
| 3 | B – Joomla | 2.2 |
| 4 | A – CPaaS | 2.3 |
| 5 | B – Realtime Database | 1.11 |
| 6 | C – smtplib | 2.4 |
| 7 | C – Standard Java has no built-in JSON parser | 3.4 |
| 8 | B – ArrayList | 3.1 |
| 9 | A – A sandboxed iframe | 4.4 |
| 10 | C – Blogspot | 4.1 |
| 11 | B – Storage Engine | 5.2 |
| 12 | D – Render | 5.5 |
| 13 | C – PaaS | 5.3 |
| 14 | B – An unstyled div defaults to 0px tall | 6.5 |
| 15 | A – It needs no API key and is open-source | 6.1 |

## II. Identification (1 pt each)

| # | Answer |
|---|--------|
| 16 | Two-Factor Authentication (2FA) |
| 17 | App Password |
| 18 | MIMEMultipart |
| 19 | Destructuring |
| 20 | await |
| 21 | Template Literals |
| 22 | Event Loop |
| 23 | Cloud Firestore |
| 24 | Cloud Storage |
| 25 | doc() |
| 26 | exists() |
| 27 | phpMyAdmin |
| 28 | StringBuilder |
| 29 | Transaction Management |
| 30 | Wix ADI (Artificial Design Intelligence) |
| 31 | HTML Code |
| 32 | Dyno |
| 33 | Sharding (Partitioning) |
| 34 | Caching |
| 35 | Nominatim |

## III. Enumeration (1 pt each)

**5-step Firestore workflow (in order):** 36. Add Firebase to your project · 37. Add SDK dependency · 38. Authenticate (optional) · 39. Access database reference · 40. Fetch the data

**Firebase services (any order):** 41. Realtime Database / Cloud Firestore · 42. Authentication · 43. Cloud Storage · 44. Cloud Messaging

**CMS platforms (any order):** 45. WordPress · 46. Joomla · 47. Drupal

**Leaflet.js building blocks (any order):** 48. Tiles · 49. Layers · 50. Markers & Popups

## IV. Coding Problems – Fill in the Blank (5 pts each, 1 pt per blank)

**51. Gmail SMTP (Python)**

```python
server = smtplib.SMTP("smtp.gmail.com", 587)   # (a)
server.starttls()                               # (b)
server.login("bot@gmail.com", "xyz123")         # (c)
server.sendmail("bot@gmail.com", "admin@mysite.com", msg.as_string())  # (d)
server.quit()                                   # (e)
```

| Blank | Answer |
|-------|--------|
| (a) | 587 |
| (b) | starttls |
| (c) | login |
| (d) | sendmail |
| (e) | quit |

**52. Java Chatbot with HashMap (Java)**

```java
HashMap<String, String> responses = new HashMap<>();
responses.put("hello", "Hi there!");                 // (a)
while (true) {
  String input = scanner.nextLine().trim();
  if (input.equalsIgnoreCase("bye")) break;          // (b)
  String key = input.toLowerCase();                  // (c)
  if (responses.containsKey(key))                    // (d)
    reply = responses.get(key);                      // (e)
  else reply = "I do not understand.";
}
```

| Blank | Answer |
|-------|--------|
| (a) | put |
| (b) | equalsIgnoreCase |
| (c) | toLowerCase |
| (d) | containsKey |
| (e) | get |

## Coverage Check (60 pts)

| Reviewer part | Points | Where |
|---|---|---|
| 1 – JavaScript & Firebase | 19 | MCQ 2, 5; ID 19–26; Enum 36–44 |
| 2 – CMS, Twilio, SMTP, XAMPP | 16 | MCQ 1, 3, 4, 6; ID 16–18, 27; Enum 45–47; Coding 51 |
| 3 – Java | 8 | MCQ 7, 8; ID 28; Coding 52 |
| 4 – Wix & Blogspot | 4 | MCQ 9, 10; ID 30, 31 |
| 5 – Platforms, DB, Heroku | 7 | MCQ 11–13; ID 29, 32–34 |
| 6 – Leaflet.js | 6 | MCQ 14, 15; ID 35; Enum 48–50 |
| **Total** | **60** | |

*Dropped from the 90-pt version to fit 2 pages / 60 pts:* Leaflet and Heroku coding problems, Twilio/XAMPP/DB-pillars enumerations, and duplicate-topic MCQ/ID items.
