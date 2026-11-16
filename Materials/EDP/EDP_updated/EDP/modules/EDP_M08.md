# EDP Module 08: Reactive Programming and RxJS Streams

[Module index](README.md) | [Setup and commands](../examples/README.md)

**Period:** Midterm · **Meeting:** 60–90 minutes · **Assessment:** Coding activity

## A. Lesson Preview & Review

A search box produces many values over time. RxJS lets us describe how that sequence should be filtered, delayed and replaced.

**In a nutshell:** Distinguish Observable, observer, subscription and Subject. We will run a small example, explain its behavior and change one part ourselves.

**Learning targets**

1. Distinguish Observable, observer, subscription and Subject.
2. Build and explain a short RxJS operator pipeline.
3. Recover from an inner failure and unsubscribe cleanly.

**Before class:** M03 (DOM events), M05 (stale results, debounce, `AbortController`) and M07 (patterns). `npm ci` must have installed the pinned RxJS.

**60-minute route:** 5 minutes preview, 15 explanation/demo, 30 coding, 10 review. For 90 minutes, add 15 guided exploration and 15 debugging/feedback.

**Scope:** Core: the console pipeline (`m08.mjs`). If time remains: the browser search page. Reference reading only: `TestScheduler` marble tests and `share`/`shareReplay`.

## Visual Guide & HTML Presentation Notes

**Technology visual anchors:** <img src="../visuals/logos/rxjs.svg" width="40" height="40" alt="rxjs logo">

![Reactive search pipeline: Input values → Debounce → Switch latest → Render result](../visuals/m08-guide.svg)

**What the sample image explains:** The browser example uses simulated results. Unsubscription tears down the stream.

**Suggested slides:**

1. Opening: show this diagram and ask students to predict the flow before revealing the explanation.
2. Concept: reveal one labeled stage at a time; connect it to the matching code rather than putting the whole lesson on screen.
3. Code/output: use a readable code panel beside a real output capture from the supplied example. Label input, expected output and any failure state.
4. Practice: keep the quiz or coding task readable and separate from its answer/explanation.

**Sample image to capture:** Use the checked browser screenshot linked below, then capture your own edited result.

**Projector text:** use scalable text, minimum 16px everywhere; aim for 24–32px body text on classroom screens. Scale code and diagram labels too. Give a diagram its own slide when labels would become small. See the [visual guide and scalable presentation prompt](../visuals/README.md).

![Checked sample output for Module 8](../instructor/m08-checked.png)

## B. Main Lesson

### A sequence instead of a single result

An Observable describes how values can be delivered over time. An observer receives next values, errors or completion. A subscription represents the active connection and its teardown. A Subject can receive values through next and distribute them to its subscribers. Our Subject stands in for input events so the example runs without a browser.

A cold source often starts work for each subscription; a hot source can produce independently of a particular subscriber. Do not assume all Observables share or replay their values. `fromEvent` can connect a browser target to a stream, `of` emits given values, and `timer` emits after a delay. `map` transforms values; `filter` keeps values matching a predicate. An Observable is not inherently faster or simpler than a short direct handler.

### Read the pipeline from input to result

`debounceTime(10)` waits for a quiet period. `distinctUntilChanged()` suppresses consecutive equal terms. `switchMap` subscribes to a new inner stream and unsubscribes the previous one. Here each inner stream is a timer representing a search. Because this source supports teardown, unsubscribing stops its pending timer.

For a promise-backed network request, unsubscription does not necessarily cancel the underlying operation. Use an abort-aware source if cancellation matters. Compare other flattening choices: concatMap serializes inner work, mergeMap permits concurrent work (configure bounds when appropriate), and exhaustMap ignores new starts while current inner work remains active. The right choice follows the business rule: discarding an old search may be correct, discarding a payment command may not be.

### Put recovery at the intended boundary

The map callback deliberately throws for the term error. `catchError` inside switchMap replaces that failed inner search with a friendly result. The outer input stream can then keep receiving future terms. Catching only outside can instead replace or end the entire search pipeline depending on what the replacement does. Error placement is part of program behavior, not cosmetic syntax.

`finalize` runs when the subscription terminates through completion, error or unsubscription. It is useful for cleanup but is not a signal that the search succeeded. Always retain and dispose subscriptions when their owning screen/service ends. Sharing with share/shareReplay has lifetime and caching consequences; only add it when multiple consumers need the same work.

### Testing time without guessing

The sample includes small waits to make its console trace easy to see, not as a guarantee for every machine under load. For precise operator tests, RxJS TestScheduler models virtual time; marble diagrams describe emissions, time and termination. Compare expected sequences, including errors and cancellation. The core activity is one pipeline and one independent change, not learning every operator at once.

The pack pins RxJS 7.8.2, and RxJS 7 is still the production line at the time of this revision; newer major versions are prerelease work. Since RxJS 7.2 you can import operators from `'rxjs'` itself, as `m08.mjs` now does; the older `'rxjs/operators'` path still works but is deprecated, and the browser bundle keeps `rxjs.operators`. Check any tutorial against the pinned install before copying its imports.

## C. Analogy, Guided Program & Practice

### Everyday connection

A water filter is a sequence of stages: let the flow settle, remove duplicates, then direct the newest request into a channel. Each operator changes what gets through or when.

### Run the complete example

Run commands from the `EDP/examples` folder. Install the pinned dependencies once with `npm ci`; most `.mjs` examples otherwise use only Node built-ins. See the setup guide for the verified runtime.

```powershell
node m08.mjs
npm run serve
```

The console program shows a fixed input sequence. Then open http://127.0.0.1:4173/m08.html to type into a real search box. The browser loads the pinned local RxJS bundle; no CDN is required. Search results are simulated, not fetched from a real campus database. Stop the server with Ctrl+C.

### File: `m08.mjs`

[Open runnable file](../examples/m08.mjs)

```javascript
import { Subject, of, timer, debounceTime, distinctUntilChanged, switchMap, map, catchError, finalize } from 'rxjs';
const terms = new Subject();
const subscription = terms.pipe(
  debounceTime(10),
  distinctUntilChanged(),
  switchMap(term => timer(30).pipe(
    map(() => {
      if (term === 'error') throw new Error('Search unavailable');
      return 'Results: ' + term.toUpperCase();
    }),
    catchError(error => of('Handled: ' + error.message))
  )),
  finalize(() => console.log('Search subscription closed'))
).subscribe(value => console.log(value));
terms.next('c'); terms.next('ca'); terms.next('canteen');
await new Promise(resolve => setTimeout(resolve, 80));
terms.next('error');
await new Promise(resolve => setTimeout(resolve, 80));
subscription.unsubscribe();
terms.complete();
```

### File: `m08.html`

[Open runnable file](../examples/m08.html)

```html
<!doctype html>
<html lang="en"><meta charset="utf-8"><title>Reactive campus search</title>
<body>
<h1>Reactive campus search</h1>
<label for="search">Campus search (try library or error)</label>
<input id="search" autocomplete="off">
<p id="result" aria-live="polite">Type a search term.</p>
<button id="stop" type="button">Stop search</button>
<script src="/vendor/rxjs.umd.min.js"></script>
<script>
const { fromEvent, timer, of } = rxjs;
const { map, debounceTime, distinctUntilChanged, switchMap, catchError, finalize } = rxjs.operators;
const input = document.getElementById('search');
const result = document.getElementById('result');
const stop = document.getElementById('stop');
const subscription = fromEvent(input, 'input').pipe(
  map(() => input.value.trim().toLowerCase()),
  debounceTime(150),
  distinctUntilChanged(),
  switchMap(term => timer(100).pipe(
    map(() => {
      if (term === 'error') throw new Error('Search unavailable');
      return term ? 'Results: ' + term.toUpperCase() : 'Type a search term.';
    }),
    catchError(error => of('Handled: ' + error.message))
  )),
  finalize(() => { result.textContent = 'Search stopped.'; })
).subscribe(text => { result.textContent = text; });
stop.addEventListener('click', () => {
  subscription.unsubscribe();
  input.disabled = true;
  stop.disabled = true;
}, { once: true });
window.addEventListener('pagehide', () => subscription.unsubscribe(), { once: true });
</script>
</body></html>
```

### Expected behavior and explanation checkpoint

Results: CANTEEN → Handled: Search unavailable → Search subscription closed. The c and ca prefixes are suppressed.

Before editing, identify the producer/input, callback or consumer, state/output, and cleanup boundary in the code. Trace one value through the program. Explain which line changes the outcome rather than only reading the console aloud.

### Your independent change

Normalize terms with trim/lowercase before distinctUntilChanged, then show that equivalent consecutive terms do not produce repeated searches. Keep the error recovery and unsubscribe.

**Checkpoint:** Predict → run → explain → modify. *Hindi sapat na gumana dahil kinopya; dapat kaya mong sabihin kung bakit at baguhin ang isang behavior.*

### Troubleshooting and common mistake

Forgetting subscribe means many Observable descriptions never execute. Nested manual subscriptions make cancellation harder to follow; use an appropriate flattening operator instead.

If a command fails before any lesson output, check the working folder, filename, Node version and installed packages first. Distinguish setup errors from a deliberately rejected input or handled runtime failure.

### Sa madaling salita

Isipin ang input bilang sunod-sunod na values. Ang operators ang naglilinaw kung alin ang gagamitin, kailan, at hanggang kailan.

[Quick reference and glossary](QUICK_REFERENCE.md)

## D. Assessment, Wrap-Up & References

### One coding activity

**Task:** Normalize terms with trim/lowercase before distinctUntilChanged, then show that equivalent consecutive terms do not produce repeated searches. Keep the error recovery and unsubscribe.

**Submit one folder or archive containing:**

1. Your complete modified program and any files needed to run it.
2. A short README with the exact command and expected result.
3. Evidence of one successful case and one rejected/failing case (the `error` term and the unsubscribe), plus a brief explanation of your independent change.

| Criterion | Points | Evidence |
| --- | ---: | --- |
| Required behavior | 4 | Core works (2); terms normalized before `distinctUntilChanged`; equivalent terms do not repeat the search (2) |
| Error/edge behavior | 2 | `error` term is recovered without ending the stream (1); unsubscribe or `finalize` output shown (1) |
| Understanding | 2 | Explain event/data flow (1); explain your own change (1) |
| Reproducibility/readability | 2 | Commands/files are complete (1); names and small structure are understandable (1) |
| Total | 10 | One activity, no separate quiz |

### Wrap-up

Distinguish Observable, observer, subscription and Subject. Recover from an inner failure and unsubscribe cleanly.

**Exit reflection (ungraded):** Where does error recovery sit in the pipeline, and what would change if it moved outside `switchMap`?

**Next connection:** M09 moves events across a real network connection with SSE (and a WebSocket comparison).

### References and further reading

- [Official/reference documentation: rxjs.dev](https://rxjs.dev/guide/overview)
- [Official/reference documentation: github.com](https://github.com/ReactiveX/rxjs/tree/7.8.2/src/internal/operators)
- [Official/reference documentation: rxjs.dev](https://rxjs.dev/guide/testing/marble-testing)

The prose and classroom code are original teaching examples informed by the references. Read [validation notes](../instructor/VALIDATION.md) before distributing a new toolchain version.
