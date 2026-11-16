# EDP Module 19: Finals Review, Summative Preparation, and Mock Practical

[Module index](README.md) | [Setup and commands](../examples/README.md)

**Period:** Finals · **Meeting:** 60–90 minutes · **Assessment:** 10-item quiz

## A. Lesson Preview & Review

Finals preparation is the time to repair familiar mistakes and explain your own choices—not install a new architecture.

**In a nutshell:** Diagnose callback, cleanup and input-validation errors. We will run a small example, explain its behavior and change one part ourselves.

**Learning targets**

1. Diagnose callback, cleanup and input-validation errors.
2. Explain one event path and its failure behavior.
3. Prioritize final project repairs using evidence.

**Before class:** M18 (the starter board and tests) and your own project checkpoint. Bring the feedback from earlier quizzes and coding activities.

**60-minute route:** 5 minutes preview, 25 explanation/demo, 15 guided code, 10 quiz, 5 feedback. For 90 minutes, add 15 minutes practice and 15 discussion/debugging.

**Scope:** Core: one fault at a time, predict, repair, regression check. No new framework, broker or deployment service is introduced.

## Visual Guide & HTML Presentation Notes

![Repair rehearsal: Observe symptom → Trace handler → Repair cause → Regression check](../visuals/m19-guide.svg)

**What the sample image explains:** Introduce one fault at a time and explain the mechanism before adding more complexity.

**Suggested slides:**

1. Opening: show this diagram and ask students to predict the flow before revealing the explanation.
2. Concept: reveal one labeled stage at a time; connect it to the matching code rather than putting the whole lesson on screen.
3. Code/output: use a readable code panel beside a real output capture from the supplied example. Label input, expected output and any failure state.
4. Practice: keep the quiz or coding task readable and separate from its answer/explanation.

**Sample image to capture:** Run this module’s supplied program and capture the terminal with the meaningful result visible. Include a caption naming the command and the observed behavior; avoid invented output screenshots.

**Projector text:** use scalable text, minimum 16px everywhere; aim for 24–32px body text on classroom screens. Scale code and diagram labels too. Give a diagram its own slide when labels would become small. See the [visual guide and scalable presentation prompt](../visuals/README.md).

## B. Main Lesson

### Revisit the complete event path

Start with a user action or producer, follow the payload to validation, observe the accepted state change, then identify every reaction. Mark which steps run synchronously and which resume later. State what happens on failure and who owns cleanup. If you cannot point to the responsible handler, simplify the example before adding another abstraction.

Review setTimeout versus blocking, promise versus repeated event stream, browser listener versus Node emitter, and type checking versus runtime validation. These distinctions explain many practical mistakes. Browser propagation and Node special error events have different rules; name the environment when giving an answer.

### A controlled repair rehearsal

The supplied m19 file is the corrected version. On a separate copy, the teacher can introduce one fault at a time: change on('ready', handle) to on('ready', handle()), replace the off callback with a new arrow function, or remove trim from the input check. Predict the symptom before running. Restore the fix and explain why it works.

Do not pile several hidden faults into the first practice. One clear defect lets the student connect evidence and cause. After each repair, run a regression check to make sure the existing behavior still works. A symptom such as two reactions may come from duplicate listeners or duplicate messages; inspect the path instead of assuming one cause.

### Architecture recap in ordinary language

A queue shares work; Pub/Sub fans out reactions; a log can support replay. Idempotency protects repeated processing. An outbox links a business commit to pending publication. Event sourcing reconstructs state from accepted facts. CQRS separates write/read responsibilities. A saga coordinates local steps and compensations. None is automatically required by a small event-driven program.

Choose one architecture trade-off from your project and explain why a simpler alternative was or was not sufficient. For example, in-memory storage may be acceptable for a clearly labeled demonstration but cannot meet a requirement to survive restart. Honesty about that limit is more useful than naming a database that is not actually connected.

### Prepare for the actual assessment

Today's 10-item quiz checks taught concepts. Guided repair is practice, not a second graded coding task. The summative before the periodical and the actual final practical have their own timetable slots. Use quiz feedback to choose repairs: first failures that block the main path, then data correctness, then usability and optional polish.

Rehearse explaining a function, changing one rule and demonstrating one failure case. Record the starter code and references you used so you can distinguish your own decisions from the starter. No new framework, broker or deployment service is introduced in this finals module.

## C. Analogy, Guided Program & Practice

### Everyday connection

Before a performance, musicians rehearse difficult passages and check instruments; they do not replace the entire arrangement backstage.

### Run the complete example

Run commands from the `EDP/examples` folder. Install the pinned dependencies once with `npm ci`; most `.mjs` examples otherwise use only Node built-ins. See the setup guide for the verified runtime.

```powershell
node m19.mjs
```

Wait for completion and compare behavior with the expected trace before editing.

### File: `m19.mjs`

[Open runnable file](../examples/m19.mjs)

```javascript
// Repair rehearsal: this executable version shows the corrected behavior.
import { EventEmitter } from 'node:events';
const bus = new EventEmitter(); let calls = 0;
function handle() { calls++; }
bus.on('ready', handle); // Register the function, not handle().
bus.emit('ready');
bus.off('ready', handle); // Same function identity.
bus.emit('ready');
console.log('Calls:', calls);
const input = '   ';
console.log('Input accepted:', input.trim().length > 0);
console.log('Listener count:', bus.listenerCount('ready'));
```

### Expected behavior and explanation checkpoint

Calls: 1; Input accepted: false; Listener count: 0. Each output corresponds to one common repaired mistake.

Before editing, identify the producer/input, callback or consumer, state/output, and cleanup boundary in the code. Trace one value through the program. Explain which line changes the outcome rather than only reading the console aloud.

### Your independent change

On a disposable copy, introduce one of the three listed faults, record its symptom, repair it, and describe the reason aloud. This is ungraded rehearsal.

**Checkpoint:** Predict → run → explain → modify. *Hindi sapat na gumana dahil kinopya; dapat kaya mong sabihin kung bakit at baguhin ang isang behavior.*

### Troubleshooting and common mistake

Memorizing output without explaining the handler does not transfer to a new problem. A last-minute dependency upgrade can change behavior; retain the tested baseline for the practical.

If a command fails before any lesson output, check the working folder, filename, Node version and installed packages first. Distinguish setup errors from a deliberately rejected input or handled runtime failure.

### Sa madaling salita

Balikan ang alam na: predict, run, hanapin ang sanhi, ayusin, at i-test ulit. Hindi ito oras para magdagdag ng bagong framework.

[Quick reference and glossary](QUICK_REFERENCE.md)

## D. Assessment, Wrap-Up & References

### 10-item quiz

One point per item. Answer after the explanation and guided practice. Give short answers; no extra graded coding submission today. The instructor keeps the answer key separately.

1. What does a promise represent compared with a repeated event stream?
2. Does a TypeScript interface validate fetched JSON at runtime?
3. What problem does an outbox address?
4. Predict log A; setTimeout(log B callback, 0); log C.
5. Register handle, emit once, remove handle, emit again. How many calls?
6. A waiting order becomes ready; another ready is attempted in the starter. What happens?
7. Why does on("ready", handle()) cause a registration problem?
8. Why does removing a new anonymous wrapper leave the original handler registered?
9. What evidence should support a claim that cleanup works?
10. Your app loses data on restart. How should the submission describe it?
### Wrap-up

Diagnose callback, cleanup and input-validation errors. Prioritize final project repairs using evidence.

**Exit reflection (ungraded):** Which fault did you introduce, what symptom did you predict, and which output proved the repair?

**Next connection:** M20 practices defending decisions in writing; M21 is the final packaging and demonstration rehearsal.

### References and further reading

- [Official/reference documentation: nodejs.org](https://nodejs.org/api/events.html)
- [Official/reference documentation: developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/removeEventListener)

The prose and classroom code are original teaching examples informed by the references. Read [validation notes](../instructor/VALIDATION.md) before distributing a new toolchain version.
