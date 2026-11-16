# EDP Module 05: Async Patterns, Cancellation, and Race Conditions

[Module index](README.md) | [Setup and commands](../examples/README.md)

**Period:** Prelim · **Meeting:** 60–90 minutes · **Assessment:** 10-item quiz

## A. Lesson Preview & Review

A student types a new search, but an older slow result arrives afterward and overwrites it. Successful requests can still produce an incorrect interface.

**In a nutshell:** Explain stale results and protect the latest request. We will run a small example, explain its behavior and change one part ourselves.

**Learning targets**

1. Explain stale results and protect the latest request.
2. Cancel pending work and distinguish cancellation from failure.
3. Compare debounce, throttle and promise-composition choices.

**Before class:** M02 (promises, `async/await`, timers) and M03 (what a user input event is). Be comfortable with `try/catch` around `await`.

**60-minute route:** 5 minutes preview, 25 explanation/demo, 15 guided code, 10 quiz, 5 feedback. For 90 minutes, add 15 minutes practice and 15 discussion/debugging.

**Scope:** Core: latest-request check, `AbortController` and debounce. Reference reading only: throttle, `fetch` error handling and concurrency limiters.

## Visual Guide & HTML Presentation Notes

**Technology visual anchors:** <img src="../visuals/logos/javascript.svg" width="40" height="40" alt="javascript logo">

![Latest request wins: Request 1 starts → Request 2 starts → Result 2 shown → Result 1 ignored](../visuals/m05-guide.svg)

**What the sample image explains:** An old response must not overwrite a newer request; cancellation alone is not the correctness check.

**Suggested slides:**

1. Opening: show this diagram and ask students to predict the flow before revealing the explanation.
2. Concept: reveal one labeled stage at a time; connect it to the matching code rather than putting the whole lesson on screen.
3. Code/output: use a readable code panel beside a real output capture from the supplied example. Label input, expected output and any failure state.
4. Practice: keep the quiz or coding task readable and separate from its answer/explanation.

**Sample image to capture:** Run this module’s supplied program and capture the terminal with the meaningful result visible. Include a caption naming the command and the observed behavior; avoid invented output screenshots.

**Projector text:** use scalable text, minimum 16px everywhere; aim for 24–32px body text on classroom screens. Scale code and diagram labels too. Give a diagram its own slide when labels would become small. See the [visual guide and scalable presentation prompt](../visuals/README.md).

## B. Main Lesson

### Choose a completion model

A callback is a function another piece of code calls. A promise describes a single eventual outcome. An event emitter represents repeated named notifications. An async iterator exposes a sequence consumed over time. Pick the model that matches the information: wrapping a click stream in one promise only captures one occurrence.

Use sequential awaits when the second operation requires the first result. For independent work, start both operations before awaiting their combined result. `Promise.all` rejects when an input rejects, but does not automatically cancel the other work. `allSettled` reports every result. `race` settles from the first settlement; `any` needs one fulfillment and rejects only when all inputs reject. Do not confuse concurrent waiting with running a CPU loop in parallel.

### Latest request wins

The example increments `latestRequest` for each search. Each invocation captures its own request number. Before displaying a result, it compares its number with the current latest value. A stale result is ignored even if the transport could not be cancelled. This identity check protects correctness; cancellation helps avoid unnecessary work.

An AbortController has a signal that cooperative APIs observe. Aborting does not forcibly interrupt arbitrary JavaScript or undo server-side work already committed. Our simulation uses Node's abortable promise timer. We abort the previous controller, create a new one, then await a simulated response. AbortError is an expected cancellation path; unknown errors are rethrown.

### Debounce and throttle

Debounce waits for a quiet period before invoking work; each new input resets the timer. The three rapid terms in the example produce only the final announcement. Throttle limits invocation frequency over time and may retain leading/trailing calls depending on the chosen policy. A search field often benefits from debounce; a continuously updated scroll indicator may need throttle or animation-frame scheduling. Neither automatically prevents stale network responses.

The returned debounced function has a cancel method. Call it during disposal so it cannot update a destroyed interface. Decide whether a final queued action should be flushed or discarded; cancellation here discards it.

### Real HTTP and bounded lifetimes

With fetch, inspect `response.ok` before parsing; HTTP 404 does not itself behave like a network rejection. JSON parsing can fail, and parsed data can have the wrong shape. Validate it before using properties. A timeout needs a policy: cancel the request, show a retry option, and avoid retrying unsafe mutations blindly.

Async iteration can make consumption clearer, but does not guarantee an upstream producer has bounded buffering. Dispose generators/listeners and handle loop exits. For this lesson, request IDs, cancellation and debounce form the practical core; HTTP schema libraries and full concurrency limiters remain extensions.

## C. Analogy, Guided Program & Practice

### Everyday connection

Calling a new number at the counter makes the previous slip obsolete. Cancelling a preparation may save work, but checking the slip number still prevents the wrong order from reaching the customer.

### Run the complete example

Run commands from the `EDP/examples` folder. Install the pinned dependencies once with `npm ci`; most `.mjs` examples otherwise use only Node built-ins. See the setup guide for the verified runtime.

```powershell
node m05.mjs
```

Wait for completion and compare behavior with the expected trace before editing.

### File: `m05.mjs`

[Open runnable file](../examples/m05.mjs)

```javascript
import { setTimeout as delay } from 'node:timers/promises';
let latestRequest = 0;
let active;
async function search(term, milliseconds) {
  const request = ++latestRequest;
  active?.abort();
  const controller = new AbortController();
  active = controller;
  try {
    await delay(milliseconds, undefined, { signal: controller.signal });
    const results = [term.toUpperCase()];
    if (request !== latestRequest) return;
    console.log('Show:', results.join(', '));
  } catch (error) {
    if (error.name === 'AbortError') console.log('Cancelled:', term);
    else throw error;
  }
}
const old = search('old', 60);
const fresh = search('new', 10);
await Promise.all([old, fresh]);
function debounce(fn, milliseconds) {
  let timer;
  const run = (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), milliseconds);
  };
  run.cancel = () => clearTimeout(timer);
  return run;
}
const announce = debounce(term => console.log('Debounced:', term), 10);
announce('c'); announce('ca'); announce('canteen');
await delay(30);
announce.cancel();
```

### Expected behavior and explanation checkpoint

Cancelled: old → Show: NEW → Debounced: canteen. Earlier typed prefixes never reach the debounced callback.

Before editing, identify the producer/input, callback or consumer, state/output, and cleanup boundary in the code. Trace one value through the program. Explain which line changes the outcome rather than only reading the console aloud.

### Your independent change

Remove the abort call but keep the request-number check; the old result must still not display. Then explain why restoring cancellation is useful.

**Checkpoint:** Predict → run → explain → modify. *Hindi sapat na gumana dahil kinopya; dapat kaya mong sabihin kung bakit at baguhin ang isang behavior.*

### Troubleshooting and common mistake

Reusing an already-aborted controller immediately cancels later work. Catching every error and silently returning hides genuine failures. Promise.race alone does not stop the losing request.

If a command fails before any lesson output, check the working folder, filename, Node version and installed packages first. Distinguish setup errors from a deliberately rejected input or handled runtime failure.

### Sa madaling salita

Hindi dahil huling dumating ang response ay iyon na ang pinakabagong request. Tingnan ang request ID bago ipakita ang result.

[Quick reference and glossary](QUICK_REFERENCE.md)

## D. Assessment, Wrap-Up & References

### 10-item quiz

One point per item. Answer after the explanation and guided practice. Give short answers; no extra graded coding submission today. The instructor keeps the answer key separately.

1. What does debounce wait for?
2. Does AbortController undo an already committed server write?
3. Which promise combinator reports each fulfillment or rejection?
4. Requests 1 then 2 start; request 2 finishes first. With latest-request checking, may result 1 replace it?
5. Inputs c, ca and canteen arrive within one debounce window. Which term is used after the quiet interval?
6. Promise.all receives one rejected input. Does that automatically cancel the other operations?
7. A second request reuses an aborted signal and fails immediately. What should change?
8. Why is assuming fetch rejects for every HTTP 404 incorrect?
9. Two independent read requests are needed. Should they necessarily be awaited sequentially?
10. How should an obsolete search be handled?
### Wrap-up

Explain stale results and protect the latest request. Compare debounce, throttle and promise-composition choices.

**Exit reflection (ungraded):** Which check ignores the stale result: the abort or the request number? What happens to a request that already reached the server?

**Next connection:** M06 describes event payloads for the compiler and shows why runtime data still needs validation.

### References and further reading

- [Official/reference documentation: developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)
- [Official/reference documentation: developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [Official/reference documentation: nodejs.org](https://nodejs.org/api/timers.html#timers-promises-api)

The prose and classroom code are original teaching examples informed by the references. Read [validation notes](../instructor/VALIDATION.md) before distributing a new toolchain version.
