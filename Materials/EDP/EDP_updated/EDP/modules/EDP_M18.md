# EDP Module 18: Integrated Solo Project Design and Architecture Checkpoint

[Module index](README.md) | [Setup and commands](../examples/README.md)

**Period:** Pre-final · **Meeting:** 60–90 minutes · **Assessment:** Coding activity

## A. Lesson Preview & Review

Your final project needs a clear working story, not a collection of every library mentioned this semester.

**In a nutshell:** Define a manageable individual project and acceptance criteria. We will run a small example, explain its behavior and change one part ourselves.

**Learning targets**

1. Define a manageable individual project and acceptance criteria.
2. Integrate events, state rules, validation and cleanup.
3. Produce setup instructions, an event diagram and meaningful tests.

**Before class:** M07, M11 and M13–M17 for patterns, tests and reliability (skim the Quick Reference table if short on time). Bring a rough project idea; the M21 table lists ten you can adapt.

**60-minute route:** 5 minutes preview, 15 explanation/demo, 30 coding, 10 review. For 90 minutes, add 15 guided exploration and 15 debugging/feedback.

**Scope:** Core: the starter board, one personal feature and its tests. Optional tier: API, SSE or persistence behind the server boundary. No new infrastructure is introduced.

## Visual Guide & HTML Presentation Notes

![Solo project vertical slice: Input → Validate command → Change and emit → Test result](../visuals/m18-guide.svg)

**What the sample image explains:** One complete personal feature is the core; label optional network/database boundaries honestly.

**Suggested slides:**

1. Opening: show this diagram and ask students to predict the flow before revealing the explanation.
2. Concept: reveal one labeled stage at a time; connect it to the matching code rather than putting the whole lesson on screen.
3. Code/output: use a readable code panel beside a real output capture from the supplied example. Label input, expected output and any failure state.
4. Practice: keep the quiz or coding task readable and separate from its answer/explanation.

**Sample image to capture:** Run this module’s supplied program and capture the terminal with the meaningful result visible. Include a caption naming the command and the observed behavior; avoid invented output screenshots.

**Projector text:** use scalable text, minimum 16px everywhere; aim for 24–32px body text on classroom screens. Scale code and diagram labels too. Give a diagram its own slide when labels would become small. See the [visual guide and scalable presentation prompt](../visuals/README.md).

## B. Main Lesson

### Choose a small vertical slice

A vertical slice connects input, decision, state change and visible evidence. The supplied board accepts an order, moves it to ready, records an event and rejects an invalid repeated transition. That is a coherent slice even without a remote broker. Your own project must add a meaningful personal feature or domain adaptation; submitting the unchanged teacher starter does not demonstrate independent work.

Possible domains include a clinic queue, library reservation, study timer, campus notification board or inventory tracker. A chat app adds connection handling; a payment/logistics architecture adds much more operational responsibility. Choose scope from the time and machines available, not from how many technologies the course mentioned.

### Write requirements that can be checked

For each core action, write one successful case and one rejected case. Example: “A nonblank item with a new ID creates one order”; “a repeated ID does not overwrite the original order.” Identify actor, command, emitted fact, payload, state and handler. Include one cleanup rule and one failure/recovery behavior.

Draw input → validation → command decision → state change → event → reaction. Label browser, Node, API and database boundaries when present. If storage is in memory, say that restart loses data. MongoDB or SQL is optional for EDP, and must sit behind the server boundary if used. A browser client should never contain database credentials.

### Read the starter's design

createBoard owns an emitter and a Map. add validates strings and uniqueness before inserting; ready checks the current state before replacing the record. It emits a copy after the change. list and history return copies so a caller cannot directly edit the stored objects. close removes the owned history listener. This is deliberately a local domain model, not an authenticated API or durable event store.

The history is a teaching audit trail. It is not a full event-sourcing implementation: it contains snapshots and does not rebuild the Map. Explain that distinction in your project write-up. Likewise, observing local events does not prove network resilience or database atomicity.

### Deliver evidence incrementally

Use small Git commits or saved checkpoints with meaningful notes. Keep installation commands, Node/package versions, sample data and non-secret configuration in a README. Run tests for valid behavior, rejected input, invalid transitions and cleanup. Screenshots can support a demo but cannot replace runnable files.

Suggested core tier: local JS/TS app with an event flow and tests. Extension tier: API, SSE or persistent data. Architecture tier: diagram brokers, outbox or sagas and explain which are actually implemented. You may share a campus domain with ADET, but EDP assessment focuses on event behavior and reliability rather than mobile styling.

## C. Analogy, Guided Program & Practice

### Everyday connection

A food stall that reliably serves one complete meal is a better first delivery than an unfinished mall with twenty restaurant signs.

### Run the complete example

Run commands from the `EDP/examples` folder. Install the pinned dependencies once with `npm ci`; most `.mjs` examples otherwise use only Node built-ins. See the setup guide for the verified runtime.

```powershell
node m18.mjs
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

### File: `m18.mjs`

[Open runnable file](../examples/m18.mjs)

```javascript
import { createBoard } from './project.mjs';
const board = createBoard();
board.add('A1', 'Pandesal'); board.ready('A1');
try { board.ready('A1'); } catch (error) { console.log('Handled:', error.message); }
console.log('Orders:', JSON.stringify(board.list()));
console.log('Events:', board.history().length);
board.close(); console.log('Listeners:', board.listenerCount());
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

Repeated ready is handled as Invalid transition; A1 remains ready; Events prints 2; cleanup leaves 0 listeners.

Before editing, identify the producer/input, callback or consumer, state/output, and cleanup boundary in the code. Trace one value through the program. Explain which line changes the outcome rather than only reading the console aloud.

### Your independent change

Implement one personal feature such as cancellation from waiting or a collected transition from ready. Add a success test and a rejected-transition test, plus an updated diagram.

**Checkpoint:** Predict → run → explain → modify. *Hindi sapat na gumana dahil kinopya; dapat kaya mong sabihin kung bakit at baguhin ang isang behavior.*

### Troubleshooting and common mistake

A proposal with many features but no complete path is not an integrated project. A screenshot-only submission is difficult to reproduce. Declaring an in-memory history “durable” is inaccurate.

If a command fails before any lesson output, check the working folder, filename, Node version and installed packages first. Distinguish setup errors from a deliberately rejected input or handled runtime failure.

### Sa madaling salita

Unahin ang isang buong gumaganang flow. Mas madaling ipaliwanag at i-test ang maliit pero malinaw na project.

[Quick reference and glossary](QUICK_REFERENCE.md)

## D. Assessment, Wrap-Up & References

### One coding activity

**Task:** Implement one personal feature such as cancellation from waiting or a collected transition from ready. Add a success test and a rejected-transition test, plus an updated diagram.

**Submit one folder or archive containing:**

1. Your complete modified program and any files needed to run it.
2. A short README with the exact command and expected result.
3. Evidence of one successful case and one rejected/failing case (the rejected transition test), plus a brief explanation of your independent change.

| Criterion | Points | Evidence |
| --- | ---: | --- |
| Required behavior | 4 | Core works (2); your personal feature works (2) |
| Error/edge behavior | 2 | Rejected transition is tested (1); tests pass and the event diagram is updated (1) |
| Understanding | 2 | Explain event/data flow (1); explain your own change (1) |
| Reproducibility/readability | 2 | Commands/files are complete (1); names and small structure are understandable (1) |
| Total | 10 | One activity, no separate quiz |

### Wrap-up

Define a manageable individual project and acceptance criteria. Produce setup instructions, an event diagram and meaningful tests.

**Exit reflection (ungraded):** Which part of your project is borrowed from the starter and which part is yours? What does your in-memory model lose on restart?

**Next connection:** M19 is a repair rehearsal on the starter and your project; M20 prepares your defense and M21 is the final packaging rehearsal.

### References and further reading

- [Official/reference documentation: nodejs.org](https://nodejs.org/api/events.html)
- [Official/reference documentation: nodejs.org](https://nodejs.org/api/test.html)

The prose and classroom code are original teaching examples informed by the references. Read [validation notes](../instructor/VALIDATION.md) before distributing a new toolchain version.
