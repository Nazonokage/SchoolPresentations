# EDP Module 11: Testing and Debugging Event-Driven Programs

[Module index](README.md) | [Setup and commands](../examples/README.md)

**Period:** Midterm · **Meeting:** 60–90 minutes · **Assessment:** 10-item quiz

## A. Lesson Preview & Review

The program worked during the demo. Can you prove it still works after a listener is removed or an operation fails?

**In a nutshell:** Write assertions for listener order and cleanup. We will run a small example, explain its behavior and change one part ourselves.

**Learning targets**

1. Write assertions for listener order and cleanup.
2. Await asynchronous tests correctly.
3. Diagnose a failure using a small reproducible trace.

**Before class:** M04 (`EventEmitter`, `once`, `off`, the special `error` event) and M05 (awaiting async work). Know how to run `node --test`.

**60-minute route:** 5 minutes preview, 25 explanation/demo, 15 guided code, 10 quiz, 5 feedback. For 90 minutes, add 15 minutes practice and 15 discussion/debugging.

**Scope:** Core: the three supplied tests and one mutation check. Reference reading only: fake timers, browser automation, Testcontainers.

## Visual Guide & HTML Presentation Notes

**Technology visual anchors:** <img src="../visuals/logos/nodejs.svg" width="40" height="40" alt="nodejs logo">

![Behavior test cycle: Arrange instance → Perform action → Assert result → Clean up](../visuals/m11-guide.svg)

**What the sample image explains:** A useful test checks rejected actions and cleanup as well as success.

**Suggested slides:**

1. Opening: show this diagram and ask students to predict the flow before revealing the explanation.
2. Concept: reveal one labeled stage at a time; connect it to the matching code rather than putting the whole lesson on screen.
3. Code/output: use a readable code panel beside a real output capture from the supplied example. Label input, expected output and any failure state.
4. Practice: keep the quiz or coding task readable and separate from its answer/explanation.

**Sample image to capture:** Run this module’s supplied program and capture the terminal with the meaningful result visible. Include a caption naming the command and the observed behavior; avoid invented output screenshots.

**Projector text:** use scalable text, minimum 16px everywhere; aim for 24–32px body text on classroom screens. Scale code and diagram labels too. Give a diagram its own slide when labels would become small. See the [visual guide and scalable presentation prompt](../visuals/README.md).

## B. Main Lesson

### Test a contract, not a screenshot of success

A useful test states an observable promise: a once listener runs once, invalid input is rejected, or cleanup prevents later reactions. Arrange a fresh instance, perform an action, and assert a result. Independent instances prevent one test's listeners from leaking into another. A test that only runs code without checking anything may pass while behavior is wrong.

The supplied suite uses built-in node:test and strict assertions. The first test captures listener order in an array, removes a callback and emits again. Comparing the entire trace proves both order and absence of later calls. The listener count checks teardown. Test one important contract per focused case; avoid assertions about internal variable names that do not matter to users.

### Async tests must finish at the right time

An async test must return or await its asynchronous work. Otherwise the test can finish before the failure occurs. Register events.once before emitting, then await the resulting promise. Prefer an event or injected scheduler over an arbitrary long sleep. A test that depends on “this should take exactly 10 ms” is fragile on busy machines.

Fake timers or virtual schedulers can model time deterministically, but they must match the environment and API. Restoring mocked clocks after each test is essential. Promise microtasks and timer queues are not identical, so advancing a fake timer may not settle every async continuation automatically. Use the test tool's documented behavior.

### Negative cases are part of correctness

The third test asserts that an unhandled EventEmitter error throws. Because the failure is expected and captured by assert.throws, the suite can pass. For an async rejection, use an asynchronous rejection assertion instead; assert.throws only observes synchronous throws. Add cases for duplicate registration, malformed payloads, missing IDs and cleanup after failure.

Mutation checking can be simple: temporarily remove off from the implementation and confirm the relevant test fails, then restore it. If the test still passes, it may not exercise the intended contract. Do not leave intentionally broken production code in the completed starter.

### Diagnose before adding machinery

Use browser breakpoints to inspect target/currentTarget and call stacks. In Node, inspect logs or a debugger and reduce the example until the error is reproducible. Add event IDs and a short timeline rather than printing entire private objects. A duplicate message may originate from duplicate registration, retry delivery or two producers; those require different fixes.

Unit tests isolate logic. Integration tests verify contracts across actual components. End-to-end tests exercise a complete user path. A Docker/Testcontainers broker test can be useful later, but the core course does not require students to install several services just to test a listener. Browser automation and RxJS virtual-time tests are appropriate extensions after the basic assertions are understood.

## C. Analogy, Guided Program & Practice

### Everyday connection

A checklist before a bus trip covers brakes and emergency exits, not only whether the engine starts. Failure-path tests check the exits of our program.

### Run the complete example

Run commands from the `EDP/examples` folder. Install the pinned dependencies once with `npm ci`; most `.mjs` examples otherwise use only Node built-ins. See the setup guide for the verified runtime.

```powershell
node --test m11.test.mjs
```

A successful run reports three passing tests. Output timing values can differ.

### File: `m11.test.mjs`

[Open runnable file](../examples/m11.test.mjs)

```javascript
import test from 'node:test';
import assert from 'node:assert/strict';
import { EventEmitter, once } from 'node:events';
test('listeners run in order and removed listeners stay removed', () => {
  const bus = new EventEmitter(); const trace = [];
  const first = value => trace.push('first:' + value);
  bus.on('ready', first);
  bus.once('ready', value => trace.push('once:' + value));
  bus.emit('ready', 'A1'); bus.off('ready', first); bus.emit('ready', 'A2');
  assert.deepEqual(trace, ['first:A1', 'once:A1']);
  assert.equal(bus.listenerCount('ready'), 0);
});
test('waiting is registered before dispatch', async () => {
  const bus = new EventEmitter();
  const result = once(bus, 'ready'); bus.emit('ready', { id: 'A1' });
  assert.deepEqual(await result, [{ id: 'A1' }]);
});
test('failure can be asserted without crashing the suite', () => {
  const bus = new EventEmitter();
  assert.throws(() => bus.emit('error', new Error('printer')), /printer/);
});
```

### Expected behavior and explanation checkpoint

All three m11 tests pass. Removing bus.off in the first test creates an extra first:A2 entry and causes the trace assertion to fail.

Before editing, identify the producer/input, callback or consumer, state/output, and cleanup boundary in the code. Trace one value through the program. Explain which line changes the outcome rather than only reading the console aloud.

### Your independent change

During guided practice, add an assertion that a known payload reaches two listeners unchanged. Restore all deliberate faults before running the full suite.

**Checkpoint:** Predict → run → explain → modify. *Hindi sapat na gumana dahil kinopya; dapat kaya mong sabihin kung bakit at baguhin ang isang behavior.*

### Troubleshooting and common mistake

An async callback launched without returning its promise can fail after the test finishes. Tests that share a global emitter can contaminate one another.

If a command fails before any lesson output, check the working folder, filename, Node version and installed packages first. Distinguish setup errors from a deliberately rejected input or handled runtime failure.

### Sa madaling salita

Hindi sapat ang walang error sa screen. Mag-assert ng inaasahang result at patunayang tumitigil ang listener pagkatapos ng cleanup.

[Quick reference and glossary](QUICK_REFERENCE.md)

## D. Assessment, Wrap-Up & References

### 10-item quiz

One point per item. Answer after the explanation and guided practice. Give short answers; no extra graded coding submission today. The instructor keeps the answer key separately.

1. What is an assertion?
2. What distinguishes an integration test from an isolated unit test?
3. Why use fresh emitters in independent tests?
4. A once listener sees two sequential emits. How many times should it run?
5. The supplied first test removes first before A2. What trace remains?
6. If an asserted expected error is thrown correctly, must the test fail?
7. An async test starts a promise but neither returns nor awaits it. What is the risk?
8. Why is a long arbitrary sleep a weak synchronization strategy?
9. Choose a test for cleanup correctness.
10. How can you check whether a test really detects a missing cleanup call?
### Wrap-up

Write assertions for listener order and cleanup. Diagnose a failure using a small reproducible trace.

**Exit reflection (ungraded):** What would you temporarily break to prove a test detects a missing `off`, and how did you restore it?

**Next connection:** M12 leaves the single process: queues, Pub/Sub and retained logs. Keep your tests; later modules reuse them.

### References and further reading

- [Official/reference documentation: nodejs.org](https://nodejs.org/api/test.html)
- [Official/reference documentation: nodejs.org](https://nodejs.org/api/assert.html)
- [Official/reference documentation: developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Debugging_JavaScript)

The prose and classroom code are original teaching examples informed by the references. Read [validation notes](../instructor/VALIDATION.md) before distributing a new toolchain version.
