# EDP Module 21 · Mini-capstone announcement and solo project readiness

[Module index](README.md) | [Setup and commands](../examples/README.md)

**Period:** Finals · **Meeting:** 60–90 minutes · **Assessment:** Coding activity

## Announcement

Build and defend one individual project. Continue the personal feature you began in M18. Choose one idea below or propose a comparable campus problem. Use the M20 essays to explain your decisions. Confirm the submission date with your instructor.

| Solo project idea | How to apply the principle | Defense demonstration |
|---|---|---|
| 1. Canteen order board | State machines (M07). Accept a collect command only in the ready state. Emit a collected event after the transition succeeds. | Attempt collection early, then after preparation. Show one collected event across both attempts. |
| 2. Campus search | Stale-response protection (M05, M08). Tag each search with a request number and let only the newest request update the screen. | Make the earlier search deliberately slower. Show its late result arriving while the newer result stays visible. |
| 3. Live announcements | Server-sent events (M09). Stream announcements to a browser board, validate each message and close the subscription when the user disconnects. | Open two boards, disconnect one, then send another announcement. Only the connected board should update. |
| 4. Inventory history | Pure replay (M15). Represent stock received and reserved as events. Rebuild the quantity by folding the history from zero. | Replay the same history twice. Show the same final quantity and no second notification or stock movement. |
| 5. Library return bell | Observer pattern (M04). Publish one book-returned event to separate shelf and receipt listeners. Keep the receipt listener reference so it can be removed. | Return one book, disable receipts, then return another. The shelf count should increase twice and the receipt count once. |
| 6. Quiz buzzer | Timers and cleanup (M01, M05, M11). Open a short answer window for each round. Cancel the pending timeout when a contestant buzzes or the host resets. | Reset an unfinished round and immediately start another. Show that the old timer cannot close the new round. |
| 7. Campus cleanup signup board | DOM event delegation (M03). Register one click listener on the board and use the clicked row’s ID to withdraw a signup. | Add a row after the listener is registered, then click its nested button label. Only that signup should disappear. |
| 8. Print job dispatcher | Work queues and bounded retries (M12–13). Assign each print job to one simulated printer. Retry temporary failures and park jobs that reach the limit. | Submit three jobs, make one repeatedly fail, then show two completions and one parked job with its attempt count. |
| 9. Club points ledger | Idempotent consumption (M13–14). Give each award a unique event ID and skip a delivery whose ID was already applied. | Deliver one award twice, then a different award of the same value. Show two credits and explain why the amount cannot serve as the ID. |
| 10. Field trip booking simulator | Saga compensation (M16). Reserve a seat, simulate payment and release the reservation if payment fails. Record each step under one booking ID. | Force a payment failure. Follow the trace from reservation to release and verify the available-seat count is restored. |
| 11. Signed webhook receiver | Inbox at the edge (M14 optional extension). Verify an HMAC signature over the raw body, reject a stale timestamp and skip a repeated event ID. | Send one valid event twice, one tampered body and one old request. Show one accepted event and three rejections or duplicates, with the reason for each. |

**Bring to the defense:** runnable source, setup instructions, a diagram, one successful case, one deliberate failure and evidence of your own change. Walk the panel through one design choice and one limitation. Use the existing readiness exercise below to rehearse. Its runnable starter keeps its original M20 filename/selector.

## A. Lesson Preview & Review

Someone else should be able to run your project and understand what you built without guessing missing steps.

**In a nutshell:** Package and rehearse a reproducible solo project. We will run a small example, explain its behavior and change one part ourselves.

**Learning targets**

1. Package and rehearse a reproducible solo project.
2. Demonstrate successful behavior, rejected input and cleanup.
3. Explain personal work, tests and limitations clearly.

**Before class:** M18 (your project), M19 (repair rehearsal) and M20 (defense essays). Bring your project folder and one failing case ready to demonstrate.

**60-minute route:** 5 minutes preview, 15 explanation/demo, 30 coding, 10 review. For 90 minutes, add 15 guided exploration and 15 debugging/feedback.

**Scope:** Core: package one project that someone else can run, and rehearse a five-minute walkthrough. No new infrastructure is introduced.

## Visual Guide & HTML Presentation Notes

![Submission readiness: Clean setup → Main flow → Failure demo → Explain and package](../visuals/m20-guide.svg)

**What the sample image explains:** Include reproducible commands, references and known limitations; keep credentials out of the archive.

**Suggested slides:**

1. Opening: show this diagram and ask students to predict the flow before revealing the explanation.
2. Concept: reveal one labeled stage at a time; connect it to the matching code rather than putting the whole lesson on screen.
3. Code/output: use a readable code panel beside a real output capture from the supplied example. Label input, expected output and any failure state.
4. Practice: keep the quiz or coding task readable and separate from its answer/explanation.

**Sample image to capture:** Run this module’s supplied program and capture the terminal with the meaningful result visible. Include a caption naming the command and the observed behavior; avoid invented output screenshots.

**Projector text:** use scalable text, minimum 16px everywhere; aim for 24–32px body text on classroom screens. Scale code and diagram labels too. Give a diagram its own slide when labels would become small. See the [visual guide and scalable presentation prompt](../visuals/README.md).

## B. Main Lesson

### Verify the submitted artifact

Open the actual submission folder, not a separate working copy with uncommitted fixes. Follow its README from the beginning. Confirm entry points, package lockfile, commands and any required sample data. Document supported runtime versions and expected output. Do not include node_modules, private credentials, access tokens or real student data in the submission archive.

**Fresh-install check (do this before you submit):** copy the submission to an empty folder, run `npm ci`, then follow only your README. If any step needs something not written there, fix the README, not your memory.

The m20 readiness script uses the starter board to check two orders, one transition, three history entries and listener cleanup. These checks illustrate a delivery gate; they are not a universal automatic grader for every student project. Adapt checks to your own acceptance criteria. The separate project tests cover rejected input and duplicate transitions.

### Rehearse a short, evidence-based walkthrough

Suggested five-minute sequence: state the user's problem; run the main path; show one deliberate invalid action; point to the responsible event handler and state rule; run a relevant test; explain one limitation. If the project includes a network service, show what the interface does when that service is unavailable. Do not claim a simulation demonstrates a production deployment.

Prepare one independent change that you can explain and implement, such as a new valid transition or validation rule. The instructor may ask a comparable modification during the actual practical. Understanding the data flow matters more than remembering every line verbatim.

### Evidence and documentation

Include a short architecture/event-flow diagram, a list of event names and payloads, setup instructions, tests, known limitations and references. State whether data survives restart. If using SQL or MongoDB, include a schema/seed or sample document process and a non-secret configuration template. If using only a local model, say so plainly.

Distinguish borrowed starter code, external libraries and your own additions. Explain the changes you wrote and how you checked them. A readable attribution section supports an honest discussion; it does not replace understanding the submitted implementation.

### Submission and final practical boundaries

This module's coding assessment is the preparation package and demonstration rehearsal. It is not a second name for the final practical exam. The actual exam instructions and institutional grading rules are issued separately. Do not reuse this preparation score as an exam score without an explicit instructor policy.

Use the final minutes to fix only defects that threaten the required path. Keep optional feature ideas in a future-work list. Back up the submission, run the documented checks once more and record the result. A small working system with clear limitations is an appropriate outcome for this course.

## C. Analogy, Guided Program & Practice

### Everyday connection

Handing over a recipe means providing ingredients, quantities and steps—not just a photograph of the meal. A runnable project needs the same reproducibility.

### Run the complete example

Run commands from the `EDP/examples` folder. Install the pinned dependencies once with `npm ci`; most `.mjs` examples otherwise use only Node built-ins. See the setup guide for the verified runtime.

```powershell
node m20.mjs
node --test project.test.mjs
```

Keep project.mjs beside the entry file. This starter is an in-memory model; it does not persist records across restarts.

### File: `project.mjs`

[Open runnable file](../examples/project.mjs)

```javascript
import { EventEmitter } from 'node:events';
export function createBoard() {
  const bus = new EventEmitter(); const orders = new Map(); const log = [];
  const record = event => log.push({ ...event });
  bus.on('order.changed', record);
  function add(id, title) {
    if (typeof id !== 'string' || !id.trim() || typeof title !== 'string' || !title.trim()) throw new Error('ID and title required');
    if (orders.has(id)) throw new Error('Duplicate ID');
    const order = { id, title: title.trim(), status: 'waiting' };
    orders.set(id, order); bus.emit('order.changed', { ...order });
  }
  function ready(id) {
    const order = orders.get(id);
    if (!order || order.status !== 'waiting') throw new Error('Invalid transition');
    const updated = { ...order, status: 'ready' };
    orders.set(id, updated); bus.emit('order.changed', { ...updated });
  }
  return {
    add, ready,
    list: () => [...orders.values()].map(order => ({ ...order })),
    history: () => log.map(event => ({ ...event })),
    close: () => bus.off('order.changed', record),
    listenerCount: () => bus.listenerCount('order.changed')
  };
}
```

### File: `m20.mjs`

[Open runnable file](../examples/m20.mjs)

```javascript
import { createBoard } from './project.mjs';
const board = createBoard();
for (const [id, title] of [['A1', 'Juice'], ['A2', 'Bread']]) board.add(id, title);
board.ready('A1');
const checks = [
  ['two orders', board.list().length === 2],
  ['first ready', board.list()[0].status === 'ready'],
  ['three domain events', board.history().length === 3]
];
board.close(); checks.push(['listeners cleaned', board.listenerCount() === 0]);
for (const [label, passed] of checks) console.log(passed ? 'PASS' : 'FAIL', label);
if (checks.some(([, passed]) => !passed)) process.exitCode = 1;
```

### File: `project.test.mjs`

[Open runnable file](../examples/project.test.mjs)

```javascript
import test from 'node:test';
import assert from 'node:assert/strict';
import { createBoard } from './project.mjs';
test('valid transition produces a history, invalid transition does not', () => {
  const board = createBoard(); board.add('A1', 'Bread'); board.ready('A1');
  assert.equal(board.list()[0].status, 'ready');
  assert.throws(() => board.ready('A1'), /Invalid transition/);
  assert.equal(board.history().length, 2); board.close();
  assert.equal(board.listenerCount(), 0);
});
test('rejects blanks and duplicates; callers cannot change internal state', () => {
  const board = createBoard();
  assert.throws(() => board.add('A1', '  '), /required/);
  board.add('A1', 'Bread');
  assert.throws(() => board.add('A1', 'Milk'), /Duplicate/);
  board.list()[0].status = 'hacked';
  assert.equal(board.list()[0].status, 'waiting'); board.close();
});
```

### Expected behavior and explanation checkpoint

PASS two orders; PASS first ready; PASS three domain events; PASS listeners cleaned. The separate test suite must also pass.

Before editing, identify the producer/input, callback or consumer, state/output, and cleanup boundary in the code. Trace one value through the program. Explain which line changes the outcome rather than only reading the console aloud.

### Your independent change

Package your own project with README, event map, tests, personal feature and failure demonstration. Use the starter only as a reference, not as your unchanged final submission.

**Checkpoint:** Predict → run → explain → modify. *Hindi sapat na gumana dahil kinopya; dapat kaya mong sabihin kung bakit at baguhin ang isang behavior.*

### Troubleshooting and common mistake

A project that runs only because of an undocumented global package is not reproducible. A successful setup on your machine does not prove a fresh installation works. Never archive secrets with the project.

If a command fails before any lesson output, check the working folder, filename, Node version and installed packages first. Distinguish setup errors from a deliberately rejected input or handled runtime failure.

### Sa madaling salita

Dapat kayang patakbuhin ng ibang tao ang project gamit ang instructions mo. Sabihin nang malinaw ang nagawa at ang limitasyon.

[Quick reference and glossary](QUICK_REFERENCE.md)

## D. Assessment, Wrap-Up & References

### One coding activity

**Task:** Package your own project with README, event map, tests, personal feature and failure demonstration. Use the starter only as a reference, not as your unchanged final submission.

**Submit one folder or archive containing:**

1. Your complete modified program and any files needed to run it.
2. A short README with the exact command and expected result.
3. Evidence of one successful case and one rejected/failing case (your deliberate failure demonstration), plus a brief explanation of your own feature and one stated limitation.

| Criterion | Points | Evidence |
| --- | ---: | --- |
| Required behavior | 4 | Main path works (2); your own personal feature works (2) |
| Error/edge behavior | 2 | Deliberate failure is detected and shown (1); state is preserved or the limit is stated clearly (1) |
| Understanding | 2 | Explain the event/data flow (1); defend one design choice and one limitation (1) |
| Reproducibility/readability | 2 | Fresh-install check passes using the README alone (1); borrowed versus own code is attributed, with no secrets in the archive (1) |
| Total | 10 | One preparation activity, not the final practical exam |

### Wrap-up

Package and rehearse a reproducible solo project. Explain personal work, tests and limitations clearly.

**Exit reflection (ungraded):** Could a stranger run your project from the README alone? Which limitation will you state first?

**Next connection:** Use the instructor’s separately issued final-practical instructions. This preparation activity does not replace the actual exam.

### References and further reading

- [Official/reference documentation: docs.npmjs.com](https://docs.npmjs.com/cli/v11/commands/npm-ci)
- [Official/reference documentation: nodejs.org](https://nodejs.org/api/test.html)

The prose and classroom code are original teaching examples informed by the references. Read [validation notes](../instructor/VALIDATION.md) before distributing a new toolchain version.

