# EDP Module 01: Foundations of Event-Driven Programming and Day-One Refresher

[Module index](README.md) | [Setup and commands](../examples/README.md)

**Period:** Prelim · **Meeting:** 60–90 minutes · **Assessment:** 10-item quiz

## A. Lesson Preview & Review

Imagine the canteen taking another order while your food is being prepared. The cashier does not freeze until your meal is ready. Today we connect familiar programming syntax to that kind of response.

**In a nutshell:** Trace variables, a condition, a loop and a function in one short program. We will run a small example, explain its behavior and change one part ourselves.

**Learning targets**

1. Trace variables, a condition, a loop and a function in one short program.
2. Identify a producer, listener and payload.
3. Predict delayed callback output and cancel a pending timer.

**Before class:** A basic idea of variables, conditions and loops from any language, and a working Node.js install (check with `node -v`). All JavaScript syntax needed today is refreshed in class. Keep a clean copy of the example files before editing.

**60-minute route:** 5 minutes preview, 25 explanation/demo, 15 guided code, 10 quiz, 5 feedback. For 90 minutes, add 15 minutes practice and 15 discussion/debugging.

**Scope:** Core: trace one short program, call listeners as functions, schedule and cancel a timer. Optional take-home: the TypeScript companion (`m01-types.ts`). Observer versus Pub/Sub is reference reading today.

## Visual Guide & HTML Presentation Notes

**Technology visual anchors:** <img src="../visuals/logos/javascript.svg" width="40" height="40" alt="javascript logo"> <img src="../visuals/logos/typescript.svg" width="40" height="40" alt="typescript logo"> <img src="../visuals/logos/nodejs.svg" width="40" height="40" alt="nodejs logo">

![Callback and delayed order: Register callback → Continue main code → Timer eligible → Run callback](../visuals/m01-guide.svg)

**What the sample image explains:** A timer schedules work; it does not pause subsequent statements.

**Suggested slides:**

1. Opening: show this diagram and ask students to predict the flow before revealing the explanation.
2. Concept: reveal one labeled stage at a time; connect it to the matching code rather than putting the whole lesson on screen.
3. Code/output: use a readable code panel beside a real output capture from the supplied example. Label input, expected output and any failure state.
4. Practice: keep the quiz or coding task readable and separate from its answer/explanation.

**Sample image to capture:** Run this module’s supplied program and capture the terminal with the meaningful result visible. Include a caption naming the command and the observed behavior; avoid invented output screenshots.

**Projector text:** use scalable text, minimum 16px everywhere; aim for 24–32px body text on classroom screens. Scale code and diagram labels too. Give a diagram its own slide when labels would become small. See the [visual guide and scalable presentation prompt](../visuals/README.md).

## B. Main Lesson

### Values, decisions, repetition and functions

`const` binds a name that cannot be reassigned; it does not make every object stored there deeply immutable. Use `let` when a binding changes, such as a running total. In our program, `prices` is an array, `total` is a number, and the `for...of` loop visits each price. `total += price` means “add this price to the current total.” After two iterations, 25 + 35 gives 60.

An `if/else` selects a branch using a Boolean condition. `canAfford(100, 60)` returns true because the budget is at least the cost. A function receives parameters and may return a result; returning is different from printing. `console.log` displays something, while `return` makes a value available to the caller. A `while` loop repeats while a condition holds; unlike our bounded array loop, it needs a condition that eventually becomes false.

An object groups related properties: `{ id: 'A1', total: 60 }`. A function can itself be a value. Putting `invoice` in an array stores its function reference; writing `invoice(order)` calls it. That difference is the bridge to callbacks. *Ipinapasa natin ang gagawin; hindi pa natin ginagawa.*

### From direct calls to reactions

Procedural code says “do step A, then B.” Event-driven code also performs setup, but registers reactions that execute when a relevant occurrence is reported. The producer reports an occurrence; the listener handles it; the payload carries useful data. An order-created event may trigger both an invoice and a kitchen notice. Neither reaction is automatically asynchronous: our loop calls both listeners synchronously.

Observer commonly involves a subject holding listener references. Pub/Sub introduces a topic or channel between publishers and subscribers. These patterns reduce some direct dependencies, but they do not remove the need for agreed payloads and error policies. A command requests an action (`prepareOrder`); an event reports a fact (`order.created`); a query requests information (`getOrder`). A button click is a UI event with an API-defined name, not necessarily a past-tense domain name.

### Schedule a callback, not a frozen program

`setTimeout(callback, delay)` schedules a one-time callback. The delay is milliseconds: 1000 means one second. The code after the call continues immediately. A timer can execute later than requested when other work or host scheduling intervenes. Even zero delay does not interrupt the currently running JavaScript. Save the returned handle to cancel pending work with `clearTimeout(handle)`. Cancellation cannot undo a callback that already executed.

The example uses 50 milliseconds to keep classroom tests quick; change it to 1000 to observe the pause. The “Taking the next order” message appears before “Ready na ang order!” Do not implement delay using a busy loop: that keeps the thread occupied. Module 2 explains the scheduling model; today's goal is to see and describe the behavior.

### Workspace and fit

Run `.mjs` files with Node; use the browser for HTML/DOM examples. **Optional take-home:** the supplied `m01-types.ts` adds an interface and a typed function. If you try it, run the pack’s type-check command first; running the file is not a type check, and external data still needs runtime validation (Module 6 covers this properly).

Events are useful when multiple independent reactions follow a change. For one simple calculation, a direct function call is often easier. More events can mean harder tracing and listener cleanup. Today’s emitter is deliberately a small loop; Node's established event API arrives in Module 4.

## C. Analogy, Guided Program & Practice

### Everyday connection

A canteen bell announces that an order is ready. One person collects the food, another updates the board. The bell does not determine what each person must do, but they must understand what it means.

### Run the complete example

Run commands from the `EDP/examples` folder. Install the pinned dependencies once with `npm ci`; most `.mjs` examples otherwise use only Node built-ins. See the setup guide for the verified runtime.

```powershell
node m01.mjs
```

This needs no third-party library. **Optional take-home** once the basic program is understood: `npm run typecheck` and then `node m01-types.ts` (its output is A1: PHP 60).

### File: `m01.mjs`

[Open runnable file](../examples/m01.mjs)

```javascript
const prices = [25, 35];
let total = 0;
for (const price of prices) total += price;
function canAfford(budget, amount) { return budget >= amount; }
console.log('Total:', total);
if (canAfford(100, total)) console.log('Order accepted');
else console.log('Kulang ang baon');
function invoice(order) { console.log('Invoice:', order.id); }
function kitchen(order) { console.log('Kitchen:', order.id); }
const listeners = [invoice, kitchen];
const order = { id: 'A1', total };
for (const listener of listeners) listener(order);
setTimeout(() => console.log('Ready na ang order!'), 50);
const cancelled = setTimeout(() => console.log('SHOULD NOT RUN'), 100);
clearTimeout(cancelled);
console.log('Taking the next order');
```

### Optional take-home file: `m01-types.ts`

[Open runnable file](../examples/m01-types.ts)

```typescript
interface Order { id: string; total: number }
function receipt(order: Order): string {
  return `${order.id}: PHP ${order.total}`;
}
console.log(receipt({ id: 'A1', total: 60 }));
// Change total to "60" to see a type error, then restore the number.
```

### Expected behavior and explanation checkpoint

Total: 60 → Order accepted → Invoice: A1 → Kitchen: A1 → Taking the next order → Ready na ang order! The cancelled message never appears.

Before editing, identify the producer/input, callback or consumer, state/output, and cleanup boundary in the code. Trace one value through the program. Explain which line changes the outcome rather than only reading the console aloud.

### Your independent change

Change the budget to 40, add a third price, and predict the branch and total before running. The sample still broadcasts its demonstration event after the affordability branch; explain how you would move publication inside the accepted branch for real ordering.

**Checkpoint:** Predict → run → explain → modify. *Hindi sapat na gumana dahil kinopya; dapat kaya mong sabihin kung bakit at baguhin ang isang behavior.*

### Troubleshooting and common mistake

If the callback runs during registration, you likely wrote `setTimeout(fn(), 1000)` instead of passing `fn` or `() => fn()`. If a string price produces unexpected addition, inspect its type before calculating.

If a command fails before any lesson output, check the working folder, filename, Node version and installed packages first. Distinguish setup errors from a deliberately rejected input or handled runtime failure.

### Sa madaling salita

Ang callback ay function na ipinapasa para tawagin kapag kailangan. Sa setTimeout, naka-schedule ito; tuloy pa rin ang kasunod na code.

[Quick reference and glossary](QUICK_REFERENCE.md)

## D. Assessment, Wrap-Up & References

### 10-item quiz

One point per item. Answer after the explanation and guided practice. Give short answers; no extra graded coding submission today. The instructor keeps the answer key separately.

1. What does a listener do?
2. How does a command differ from an event?
3. How many milliseconds are in one second?
4. What total results from adding prices 25 and 35 starting at zero?
5. What does canAfford(40, 60) return?
6. Predict: log A; setTimeout(() => log B, 0); log C.
7. Why is setTimeout(show(), 1000) usually wrong for delaying show?
8. A long while loop makes a timer late. Is the timer necessarily broken?
9. One order should notify kitchen and invoice independently. Suggest a suitable pattern.
10. How do you cancel a pending timeout?
### Wrap-up

Trace variables, a condition, a loop and a function in one short program. Predict delayed callback output and cancel a pending timer.

**Exit reflection (ungraded):** Which line shows that a callback was scheduled but has not run yet? What would change if you wrote `setTimeout(show(), 50)`?

**Next connection:** M02 explains *why* the callback ran later: the call stack, task queue and microtasks. Keep your `m01.mjs`; M02 reuses the timer idea.

### References and further reading

- [Official/reference documentation: developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [Official/reference documentation: developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout)
- [Official/reference documentation: www.typescriptlang.org](https://www.typescriptlang.org/tsconfig/strict.html)

The prose and classroom code are original teaching examples informed by the references. Read [validation notes](../instructor/VALIDATION.md) before distributing a new toolchain version.
