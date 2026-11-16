# Testing, Automated Testing, and Security Quality Assurance

> **Course:** Information Assurance and Security  
> **Module:** 15 — Testing, Automated Testing, and Security Quality Assurance  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Welcome back, students! Today, we are covering a critical phase of the Software Development Life Cycle (SDLC): **Testing, Automated Testing, and Security Quality Assurance**.

To set the stage, let's recall the CIA Triad (Confidentiality, Integrity, Availability). While testing ensures all three, it is most crucial for maintaining the **Integrity** of data and systems.

**Quick Review:**
Have you ever performed testing without a formal plan? If so, that is called **ad-hoc testing**—an ineffective, informal, and unstructured method that is highly discouraged in the industry.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Understand the importance of having proper test documentation.
2.  Create test cases.
3.  Understand what automated testing is.

![Software Testing Concept](https://images.unsplash.com/photo-1516259762381-22954d7d3ad2?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### Core Concepts of Software Testing
We are already familiar with the testing phase of the software development cycle. This is where almost-finished software is tested for errors and returned to IT developers to fix them. 

> **Pro Tip:** Avoid the term "testers." In modern development, these professionals are called **Quality Assurance (QA) Engineers**.

**Test Case**
A **Test Case** is a set of actions executed to verify a particular feature or function of your software application. It contains test steps, test data, preconditions, and postconditions developed for specific test scenarios. A test case includes specific variables or conditions, using which a testing engineer can compare **Expected Results** and **Actual Results** to determine whether the software is functioning per the customer's requirements.

**Test Scenario**
A **Test Scenario** is a wider range or general test description. It gives testers a general idea of what they are testing. In other words, the test scenario acts as a container that holds multiple test cases.

*Example:*
*   **Test Scenario:** Test User Login Functionality.
    *   *Test Case 1:* Check results on entering a valid User ID and Password.
    *   *Test Case 2:* Check results on entering an invalid User ID and Password.
    *   *Test Case 3:* Check the response when the User ID is empty and the Login button is pressed.

### Standard Test Case Format
A well-structured test case should be easily understood by the tester and filled out with a pass or fail response. Below is the standard format:

| Test Case ID | Test Case Description | Test Steps | Test Data / Input | Expected Results | Actual Results | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TS1C01** | Check user login with **valid** data | 1. Go to login page<br>2. Enter username<br>3. Enter password<br>4. Click submit | username: `user1`<br>password: `password1` | User login and has access to the next page. | User login and has access to the next page. | **Pass** |
| **TS1C02** | Check user login with **invalid** data | 1. Go to login page<br>2. Enter username<br>3. Enter password<br>4. Click submit | username: `user1`<br>password: `error1` | User should not be logged in; an invalid password error should prompt. | User failed to access and an invalid password error prompted. | **Pass** |
| **TS1C03** | Check user login with **Admin** credentials | 1. Go to login page<br>2. Enter username<br>3. Enter password<br>4. Click submit | username: `admin`<br>password: `admin` | User should not be logged in; an invalid username or password error should prompt. | Admin login and has access to the admin page. | **Fail** |
| **TS1C04** | Check user login with **empty** data | 1. Go to login page<br>2. Enter username<br>3. Enter password<br>4. Click submit | username: `(blank)*`<br>password: `(blank)*` | User should not be logged in; a username and password should not be empty prompt. | Nothing happens, no prompt or anything. | **Fail** |

*\*(blank) means empty spaces.*

### Rules in Test Case Creation
To ensure quality and effectiveness, follow these three rules when creating test cases:
1.  **Test cases should not be created or performed by the developer**, as it can cause bias.
2.  **Test cases should be clear and easily understood.**
3.  **Test cases should cover all bases** that can exploit the system.

### Test Cases Involving Security
Testing for security vulnerabilities is critical. Let's look at how XSS and SQL Injection appear in a test case format:

| Test Case ID | Test Case Description | Test Steps | Test Data / Input | Expected Results | Actual Results | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TS1C05** | Check user login with **XSS input** | 1. Go to login page<br>2. Enter username<br>3. Enter password<br>4. Click submit | username: `/><script>alert('XSS!');</script>`<br>password: `/><script>alert('XSS!');</script>` | User login should be an error; username and password not found. | User login should be an error; username and password not found. | **Pass** |
| **TS1C06** | Check user login with **SQL Injection** | 1. Go to login page<br>2. Enter username<br>3. Enter password<br>4. Click submit | username: `or 1=1--`<br>password: `or 1=1--` | User login should be an error; username and password not found. | User managed to login. | **Fail** |

> **Critical Warning:** In the example above, **TS1C06 failed** and managed to breach the security through SQL Injection. This is a critical security breach and must be fixed with the highest priority.

### Post Test and Post Fix
After the codes are fixed, the test cases are returned to the QA engineers, and once again should be tested. Sometimes, for the sake of not missing any errors, the entire **Test Scenario** is tested again, as the edited code might have inadvertently brought errors to the other test cases.

### Automated Testing
As mentioned, there are situations where testing takes thousands of tests and months to finish. This is why software development companies now use **automated testing**.

Automated testing requires you to place the test cases and the links or even coordinates of your mouse button for the automated testing to test the developed system. 

> **Note for Capstone Projects:** Most capstone projects do not require extensive automated testing. Manual testing is highly recommended to fully understand the Quality Assurance part of software development.

**Common Automated Testing Tools:**

| Product | Application(s) Under Test | Setup Difficulty | Low-code & Script Mode | Supported Language(s) | Parallel Testing | Object Spy | Ratings & # of Reviews |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Katalon** | Web, Mobile, API & Desktop (Windows) | Low | Both | Java & Groovy | Built-in | Built-in | 4.4/5 (740 reviews) |
| **Selenium** | Web | High | Scripting Only | Java, Python, C#, Ruby, etc. | Coding Required | Coding Required | 4.5/5 (443 reviews) |
| **Appium** | Mobile | High | Scripting Only | Any language Selenium supports | Coding Required | Coding Required | 4.4/5 (90 reviews) |
| **JMeter** | Web & API | High | Scripting Only | Java | Coding Required | Coding Required | 4.3/5 (98 reviews) |
| **SoapUI** | API | Medium | Scripting Only | Groovy & Javascript | Coding Required | Coding Required | 4.5/5 (113 reviews) |

> *Most of the time, automated testing requires coding to ensure that there will be no errors in inputs and controls. This is why even in the field of IT, Quality Assurance still requires the ability to code, since it requires logical capabilities in setting up automated testing.*

---

## C. Analogies and Use Cases

### The "Building Inspection" Analogy
Think of developing software as building a house.
*   **Test Scenario:** "Inspect the plumbing system." (The general area).
*   **Test Case:** "Turn on the kitchen faucet and check for leaks." (The specific action).
*   **Rule 1 (No Bias):** You don't ask the plumber who installed the pipes to inspect their own work. You hire a third-party inspector (QA Engineer).
*   **Security Test Case:** "Pour toxic waste into the water supply to see if the filter catches it." (Simulating an SQL Injection or XSS attack).
*   **Automated Testing:** Installing smart sensors that continuously monitor water pressure and flow rates, rather than having a human manually check every faucet every hour.

### Real-World Use Case: The Banking App Login
A bank develops a new mobile app. The QA team writes a test case for the login screen.
*   *Test Case 1:* Enter a valid username and password -> Expected: Successful login.
*   *Test Case 2:* Enter a valid username but wrong password -> Expected: "Invalid credentials" error.
*   *Test Case 3:* Enter an SQL injection payload (`' OR 1=1 --`) -> Expected: "Invalid credentials" error.
If Test Case 3 returns a "Successful login" (Pass/Fail = Fail), the developers know they have a critical SQL injection vulnerability that must be patched immediately before the app is released to the public.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **Test Cases** are specific, step-by-step actions to verify a feature.
*   **Test Scenarios** are broader descriptions containing multiple test cases.
*   **Expected Results** define what should happen; **Actual Results** define what did happen.
*   QA Engineers use **Pass/Fail** to communicate bugs to developers.
*   **Security Testing** (XSS, SQL Injection) is critical and must be prioritized.
*   **Automated Testing** is used for large-scale projects and requires coding skills, but **Manual Testing** is preferred for smaller projects like capstones to build foundational QA skills.
*   **Post-Test and Post-Fix** ensures that fixing one bug doesn't break another part of the system.

### Frequently Asked Questions
**1. Are there other levels of authorization beyond what we discussed?**
**A:** (Note: This FAQ was originally a typo in the source material, likely copy-pasted from an authorization module. In the context of *Testing*, a relevant question would be: *Are there other types of testing?*) Yes, besides functional testing (like login) and security testing (XSS/SQLi), there is performance testing (load/stress), usability testing, and regression testing. The depth depends on the project scope.

**2. What is the difference between a Test Case and a Test Scenario?**
**A:** A Test Scenario is a high-level, general description of what to test (e.g., "Test Login"). A Test Case is a detailed, step-by-step set of instructions with specific data inputs to execute that scenario (e.g., "Enter user1 and pass1, click submit, expect dashboard").

**3. Why shouldn't the developer test their own code?**
**A:** Developers have inherent cognitive bias. They wrote the code intending it to work in a specific way, and they may unconsciously test it in a way that avoids breaking it. An independent QA Engineer approaches the system with a fresh perspective and a "hacker mindset" to find edge cases and vulnerabilities the developer missed.

**4. When should we use Automated Testing over Manual Testing?**
**A:** Automated testing should be used when a project is large-scale, requires thousands of repetitive tests, and runs on a frequent basis (like CI/CD pipelines). For smaller projects, like a student capstone, manual testing is recommended because it allows the developers to intimately understand the QA process and the system's behavior.

---

## E. Guided Drills / Code Projects

### Solo Project Update: Creating Test Cases for Your Capstone
**Project Overview:** 
For Module 15, you will expand your ongoing project by creating a formal set of **Test Cases** for your system's main features. 

> *Note: This was originally designed as a group activity. We are adapting it as a **solo activity**. You will act as the sole Quality Assurance Engineer for this assignment.*

**Project Guidelines:**
*   **Format:** Individual work.
*   **Objective:** Create test cases for your capstone system. Focus on the main features. **Do not fill in the "Pass/Fail" or "Actual Results" columns yet**, as the system is not yet in the development stage.
*   **Submission:** Add this to your ongoing project documentation.

**Step-by-Step Deliverable:**
1.  Choose 3-5 core features of your system (e.g., Login, Registration, Data Entry).
2.  Create a Markdown table for each feature using the standard test case format.
3.  Include at least one Security Test Case (e.g., testing for SQL Injection or XSS in an input field).

**Draft your test cases below:**

```json
// Example JSON representation of a Test Case structure
{
  "test_scenario": "User Login Functionality",
  "test_cases": [
    {
      "id": "TC-01",
      "description": "Check login with valid credentials",
      "steps": ["Navigate to login page", "Enter username", "Enter password", "Click submit"],
      "test_data": {"username": "user1", "password": "pass123"},
      "expected_result": "Redirect to user dashboard",
      "actual_result": "",
      "pass_fail": ""
    },
    {
      "id": "TC-02",
      "description": "Check login with SQL Injection payload",
      "steps": ["Navigate to login page", "Enter username", "Enter password", "Click submit"],
      "test_data": {"username": "' OR 1=1 --", "password": "anything"},
      "expected_result": "Show 'Invalid Credentials' error",
      "actual_result": "",
      "pass_fail": ""
    }
  ]
}
```

*(Continue drafting your test cases in a similar table format in your project document)*

---

## F. Skill-Building Check

### Check for Understanding (10 mins Quiz)

**1. Short Essay: Explain the relationship of security fit in testing?**
*Guidance:* Security is a critical component of the testing phase because software vulnerabilities (like SQL Injection and XSS) often hide in plain sight during standard functional testing. Security fit in testing means intentionally including malicious inputs and edge cases in test cases (like TS1C05 and TS1C06) to verify that the system's defenses are robust. Testing solely for functionality without testing for security leaves the application vulnerable to exploitation after deployment. 

**2. Multiple Choice: Which of the following is a set of specific actions executed to verify a particular feature or function of your software application?**
A. Test Scenario
B. Test Case
C. Ad-hoc Testing
D. Automated Testing
**Correct Answer: B** (A Test Case is the specific action, whereas a Test Scenario is the broader description).

**3. Multiple Choice: According to the rules in test case making, who should NOT create or perform test cases?**
A. The QA Engineer
B. The Developer
C. The Project Manager
D. The End User
**Correct Answer: B** (Developers should not test their own code due to bias).

**4. True or False: Automated testing is highly recommended for small-scale student capstone projects to ensure the highest quality.**
**Correct Answer: False** (Manual testing is recommended for capstones to fully understand the QA process. Automated testing is usually reserved for large-scale enterprise applications with thousands of tests).

**5. Short Answer: Why is the "Post Test and Post Fix" phase necessary?**
**Correct Answer:** When a developer fixes a bug, there is a risk that the changes made could introduce a new bug elsewhere in the system (a regression). The Post Test and Post Fix phase involves re-running the entire Test Scenario to ensure that the fix did not break any previously working functionality.