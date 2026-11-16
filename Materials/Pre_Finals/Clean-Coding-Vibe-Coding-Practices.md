# Clean Coding & Clean "Vibe Coding" Practices
### Reference Notes — Integrative Programming

---

## 1. What is "Clean Code"?

**Clean code** is code that is easy to **read, understand, change, and maintain** — by you in 6 months, and by anyone else on your team. It's not about being clever; it's about being *clear*.

> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." — Martin Fowler

**Why it matters (especially in integrative/team projects):**
- Multiple people/systems touch the same codebase
- Bugs are cheaper to fix when code is readable
- Onboarding new devs is faster
- Integration with other systems is safer when code behavior is predictable

---

## 2. What is "Vibe Coding"?

**Vibe coding** refers to writing code quickly, intuitively, and often with heavy AI assistance (Copilot, Claude, ChatGPT, Cursor, etc.) — prioritizing speed and "flow" over deep upfront planning. It's great for prototyping and momentum, but **without discipline it produces messy, hard-to-maintain code**.

**"Clean vibe coding"** = keeping that fast, AI-assisted, momentum-driven workflow, but layering in just enough discipline so the output doesn't turn into spaghetti. Think of it as *"move fast, but don't leave a mess."*

### Clean Vibe Coding Ground Rules
1. **Always read what the AI generates** before accepting it — don't paste blindly.
2. **Prompt with structure/context in mind** (mention naming conventions, architecture, existing patterns) so generated code fits the codebase.
3. **Refactor immediately after generating** — rename vague variables, remove dead code, break up long functions.
4. **Keep a consistent style** even across AI-generated and hand-written code (same linter/formatter rules apply to both).
5. **Don't let AI decide architecture silently** — you decide the structure; AI fills in implementation.
6. **Test AI-generated code** — "vibes" are not a substitute for verification, especially for logic-heavy or security-sensitive code.
7. **Commit in small chunks** — easier to review/rollback if a "vibe" turns out wrong.

---

## 3. Core Clean Code Principles

### 3.1 Meaningful Naming
- Names should reveal **intent** — no guessing needed.
- Avoid abbreviations that aren't obvious (`usr`, `tmp1`, `dataX`).
- Use pronounceable, searchable names.

```js
// ❌ Bad
let d; // elapsed time in days

// ✅ Good
let elapsedTimeInDays;
```

```js
// ❌ Bad
function calc(a, b) { return a * b * 0.12; }

// ✅ Good
function calculateTax(price, quantity) {
  const TAX_RATE = 0.12;
  return price * quantity * TAX_RATE;
}
```

**Naming conventions cheat sheet:**
| Type | Convention | Example |
|---|---|---|
| Variables/functions (JS) | camelCase | `getUserData()` |
| Classes/Components | PascalCase | `UserProfile` |
| Constants | UPPER_SNAKE_CASE | `MAX_RETRIES` |
| Files (React components) | PascalCase.jsx | `UserCard.jsx` |
| Files (general/utils) | kebab-case or camelCase | `date-utils.js` |
| Database tables/columns | snake_case | `user_id`, `created_at` |
| Booleans | prefix is/has/can | `isActive`, `hasPermission` |

### 3.2 Functions Should Do One Thing
- If a function needs "and" to describe it ("saves the user **and** sends an email"), split it.
- Keep functions short (ideally under ~20 lines as a rule of thumb).

```js
// ❌ Bad — does too much
function processOrder(order) {
  validateOrder(order);
  calculateTotal(order);
  saveToDatabase(order);
  sendConfirmationEmail(order);
}

// ✅ Good — orchestrator calls single-purpose functions
function processOrder(order) {
  if (!isValidOrder(order)) throw new Error("Invalid order");
  const total = calculateOrderTotal(order);
  const savedOrder = saveOrder({ ...order, total });
  sendOrderConfirmation(savedOrder);
  return savedOrder;
}
```

### 3.3 DRY — Don't Repeat Yourself
If you copy-paste code more than twice, extract it into a function/component/module.

```js
// ❌ Repeated logic
const adultDiscount = price * 0.9;
const seniorDiscount = price * 0.8;

// ✅ Reusable
function applyDiscount(price, rate) {
  return price * (1 - rate);
}
```

### 3.4 Avoid Magic Numbers/Strings
Use named constants so the *meaning* is clear.

```js
// ❌ Bad
if (user.role === 2) { ... }

// ✅ Good
const ROLES = { ADMIN: 1, EDITOR: 2, VIEWER: 3 };
if (user.role === ROLES.EDITOR) { ... }
```

### 3.5 Comments — Explain "Why," Not "What"
Good code explains *what* it does through naming. Comments should explain **why** a decision was made (business logic, edge cases, workarounds).

```js
// ❌ Redundant comment
// increment i by 1
i++;

// ✅ Useful comment
// Retry 3 times because the payment gateway is occasionally flaky
for (let attempt = 0; attempt < 3; attempt++) { ... }
```

### 3.6 Consistent Formatting
- Use a linter/formatter (ESLint + Prettier for JS, Black for Python, etc.) so style is automatic, not debated.
- Consistent indentation, spacing, and bracket style across the whole team.

### 3.7 Error Handling Done Right
- Don't swallow errors silently.
- Fail loudly in development, gracefully in production.

```js
// ❌ Bad — silent failure
try {
  await saveUser(user);
} catch (e) {}

// ✅ Good
try {
  await saveUser(user);
} catch (error) {
  logger.error("Failed to save user:", error);
  throw new Error("Unable to save user. Please try again.");
}
```

### 3.8 Avoid Deep Nesting — Use Guard Clauses
```js
// ❌ Deep nesting
function getDiscount(user) {
  if (user) {
    if (user.isActive) {
      if (user.isPremium) {
        return 0.2;
      }
    }
  }
  return 0;
}

// ✅ Guard clauses (early returns)
function getDiscount(user) {
  if (!user || !user.isActive) return 0;
  if (!user.isPremium) return 0;
  return 0.2;
}
```

### 3.9 Keep Components/Modules Small & Focused
Related to Separation of Concerns (see architecture doc) — a file/component should have **one clear responsibility**.

```
❌ UserPage.jsx (500+ lines: fetching, form logic, styling, validation all mixed)

✅
UserPage.jsx        → layout/composition only
useUserData.js       → data fetching hook
UserForm.jsx         → form UI
userValidation.js    → validation logic
```

---

## 4. Clean Code Checklist (Quick Self-Review)

Before committing/pushing code, ask:

- [ ] Can someone else understand this function's purpose just from its name?
- [ ] Does each function/component do just ONE thing?
- [ ] Are there any magic numbers/strings that should be constants?
- [ ] Is there duplicated logic I should extract?
- [ ] Are errors handled (not silently swallowed)?
- [ ] Did I remove console.logs, commented-out code, and debug leftovers?
- [ ] Is the formatting consistent (ran the linter/formatter)?
- [ ] If AI-generated: did I review and understand every line, not just accept it?
- [ ] Are variable/function names descriptive without needing a comment to explain them?
- [ ] Would I be comfortable if a teammate reviewed this right now?

---

## 5. Common Clean Code "Smells" to Avoid

| Code Smell | Description | Fix |
|---|---|---|
| **God Function/Class** | One function/class does everything | Split into smaller, focused units |
| **Shotgun Surgery** | One change requires edits in many unrelated files | Improve cohesion, centralize logic |
| **Copy-Paste Code** | Same logic duplicated everywhere | Extract to reusable function/module |
| **Dead Code** | Unused variables, functions, commented-out blocks | Delete it — version control remembers it |
| **Long Parameter Lists** | Functions with 5+ parameters | Use an object/config parameter instead |
| **Deep Nesting** | Multiple nested if/for blocks | Use guard clauses, early returns |
| **Inconsistent Naming** | Mixing camelCase, snake_case randomly | Pick one convention, enforce with linter |

---

## 6. Clean Vibe Coding Workflow (Practical Flow)

```
1. Plan briefly       → know the goal/structure before prompting
2. Prompt with context → mention style, patterns, existing code
3. Generate            → let AI draft the code
4. Read & understand    → don't accept blindly
5. Refactor             → clean names, remove redundancy
6. Test                 → run it, check edge cases
7. Lint/Format           → auto-fix style issues
8. Commit small          → clear, descriptive commit messages
```

**Good commit message habits:**
```
❌ "fixed stuff"
✅ "fix: handle null user in checkout validation"

❌ "update"
✅ "refactor: extract discount logic into utils/pricing.js"
```

---

## 7. Key Takeaways

- Clean code = **readable, predictable, and easy to change** — not "clever" code.
- **Vibe coding** (AI-assisted, fast-flow coding) is fine and productive — as long as you **review, refactor, and test** what's generated instead of blindly accepting it.
- Small, single-purpose functions/files + meaningful names + no duplication = 80% of clean code in practice.
- Discipline (linting, consistent naming, small commits) is what keeps *fast* code from becoming *messy* code.

---

*Note: I don't have live document/database access — this is compiled from general software engineering knowledge, so cross-check specific conventions against what your professor/course requires.*
