# Event-Driven Programming in JavaScript & TypeScript — Compiled Contents

**Current finals sequence:** M19 rehearsal, [M20 defense quiz and essays](modules/EDP_M20.md), then [M21 solo mini-capstone announcement and readiness](modules/EDP_M21.md). Alternating assessments apply through M19. If finals has only two teaching meetings, assign M20 as individual preparation between M19 and M21. Keep summative and periodical exam time separate.

**Authored lesson pack available:** [21 teaching modules](modules/README.md), [runnable examples](examples/README.md), and [validation notes](instructor/VALIDATION.md). This file remains the curriculum specification; the linked files contain the full lessons.

**Revision:** 3 November 2026. **Purpose:** detailed 21-module table of contents and the basis for subsequent full lesson authoring. **Status:** curriculum specification, not completed lessons or tested code.

This revision follows the supplied JS/TS course and both architecture reports. It replaces the earlier refresher-heavy version. Variables, conditionals, loops and functions are refreshed **on Day 1**, while Prelim immediately develops event-driven programming. All major topic families from the supplied material are mapped below.

[Original JS/TS course](research/raw_ai/Event-Driven%20Programming%20in%20JavaScript%20%26%20TypeSc.md) | [Production masterclass](research/raw_ai/INPUT_Production_Masterclass.md) | [Fundamentals-to-architecture report](research/raw_ai/INPUT_Fundamentals_to_Architecture.md) | [Technical review](research/TECHNICAL_REVIEW.md)

## Course overview and depth contract

Use JavaScript/TypeScript in the browser and Node.js. Python/asyncio examples in the reports are comparative references; the required programs remain JS/TS. Supply starter environments and concise catch-up sheets so the Day 1 refresher does not become four separate modules.

Every module will have explanations, source-linked subtopics, complete guided code, output traces, independent changes and troubleshooting. **Practical core** means a small behavior students build. **Guided demonstration** means prepared code students inspect/run. **Architecture/reference** means a diagram, simulation or comparison; it does not imply a production deployment. All topics receive a place, but not equal implementation depth in 60–90 minutes.

| Period | Modules | Count | Focus |
| --- | --- | ---: | --- |
| Prelim | M01–M05 | 5 | Foundations, runtime, DOM, Node events, async patterns |
| Midterm | M06–M11 | 6 | Types, patterns, reactive streams, real-time, streams/workers, testing |
| Pre-final | M12–M18 | 7 | Messaging, delivery, contracts, advanced architecture, observability, integration |
| Final | M19–M21 | 3 | Review and solo practical-project preparation |
| **Total** | **M01–M21** | **21** | **Prepared content inventory** |

The split is flexible. Four Prelim meetings can group selected M04/M05 core material while retaining the separate prepared chapters. Additional Pre-final time expands demonstrations; an eighth numbered Pre-final module would otherwise increase the total to 21. Combined meetings use reduced exercises, not two complete lessons at double speed. Summative exams precede each periodical and remain separate from content modules. Saturdays are excluded. Actual dates remain subject to the institution's timetable and the [calendar analysis](../Modern_2026_Course_Pack/CALENDAR_AND_CAPACITY.md).

## In a nutshell — What we will discuss and create

This is the quick lesson-plan overview. Start with the smallest working program, let students explain and change it, then show the deeper connections. “Create” below means a small guided program or model; production services are demonstrations or extensions, not assumed classroom deployments.

| Module | We will talk about… | We will create… |
| --- | --- | --- |
| **01 — Foundations and refresher** | How events make programs respond; Observer/Pub/Sub; a Day 1 reminder of variables, conditionals, loops and functions; prepared strict TypeScript workspace; first setTimeout/clearTimeout preview | A delayed order-ready message and a tiny baon/order program, then a simple event with two reactions: “Isang pangyayari, dalawang response.” |
| **02 — Event loop and concurrency** | Why synchronous code, timers and promise callbacks run in different orders; how promises and async/await handle waiting | A short output-order experiment and simulated order-preparation program that handles success and failure |
| **03 — DOM events** | How HTML controls connect to JavaScript inside `<script>`; selecting elements, registering a listener, reading input and updating the page | First a button that changes text; then a small order form or counter. Delegated rows and custom events extend the same example |
| **04 — Node events** | How a Node program broadcasts an event to listeners; listener order, once-only responses, errors and cleanup | A canteen broadcaster where an order triggers an invoice message and an inventory/log message |
| **05 — Async patterns** | Awaiting results, combining operations, cancellation, stale search results, debounce and throttle | A campus search demonstration where a slow old result cannot replace the latest query; add timing controls in stages |
| **06 — Typed events** | How TypeScript describes event names and payloads, and why incoming data still needs runtime checks | A small typed order bus that flags a wrong payload and rejects invalid external data |
| **07 — Patterns and state** | Observer, Pub/Sub, mediator, commands/events/queries, and valid state transitions; brief framework/signals comparison | An order-state machine: waiting → preparing → ready → collected, with invalid actions rejected |
| **08 — Reactive streams** | How RxJS represents a sequence of events and transforms it through operators; subscription cleanup | A short reactive version of the familiar search box using a prepared RxJS setup; compare it with plain JavaScript |
| **09 — Real-time communication** | How SSE, WebSockets and other channels deliver updates; connection and message safety | A live-announcement board using a labeled simulation or teacher-provided local service, with connection status |
| **10 — Streams and workers** | What happens when data arrives faster than it can be processed; how workers help suitable CPU-heavy tasks | A small log-processing pipeline/backpressure demonstration; optionally compare blocking calculation with a worker |
| **11 — Testing and debugging** | How to prove listeners, timing, errors and cleanup behave as intended | Tests for an earlier event bus or state machine, including a failing case that students repair |
| **12 — Brokers and messaging** | How work queues, Pub/Sub and retained event logs differ; where RabbitMQ/Kafka and cloud services fit | A local message-routing model and a system diagram; an actual broker is a prepared extension |
| **13 — Reliable delivery** | Duplicates, ordering, acknowledgment, retries and dead-letter handling | A bounded job queue that receives a duplicate order and retries a temporary failure safely |
| **14 — Outbox and contracts** | Why saving data and publishing an event can disagree; outbox/inbox and versioned payloads | A failure-window diagram and small outbox model, plus checks for two payload versions |
| **15 — Event sourcing** | How a history of domain events can rebuild state; projections, replay and snapshots | A small inventory/account replay program that reconstructs state without repeating external side effects |
| **16 — CQRS and sagas** | Separate read/write models and multi-step workflows with compensating actions | A simple reserve → confirm workflow simulation with a deliberate failure and recovery step |
| **17 — Observability and resilience** | How logs, metrics and traces explain failures; validation, access boundaries and bounded recovery | A structured event timeline and a failure investigation; tracing infrastructure remains a demonstration |
| **18 — Solo project integration** | Choosing a manageable problem, designing its event flow and planning meaningful tests | An individual project proposal, event/state diagram and one working end-to-end feature |
| **19 — Finals rehearsal** | The common mistakes and practical skills already taught | An individual mock-practical repair and a checklist of remaining project issues |
| **20 — Defense preparation** | Apply course principles to project scenarios | 20 quiz answers and two essays |
| **21 — Finals readiness** | How to demonstrate, explain, test and package personal work | A ready-to-run solo project submission with README, evidence and honest limitations; the actual exam has its own slot |

### Understanding checkpoints for the lesson plan

Understanding cannot be guaranteed from a topic list. Before increasing complexity, ask students to **predict one result, run the program, point to the responsible handler, and make one independent change**. Use brief Taglish explanations and revisit earlier code. If the checkpoint fails, repeat a smaller example and shorten the advanced demonstration. Completing a broad survey is different from independently implementing every architecture.

## Assessment rhythm and realistic meeting plan

Updated 3 November 2026: alternate **odd modules = one 10-item quiz**, **even modules = one coding activity**. This replaces earlier suggestions of multiple assessed drills per lesson. Guided code-alongs remain in every module; they are learning time, not another graded submission. Module 1's quiz is diagnostic after the refresher, with feedback rather than a prerequisite barrier.

- Quiz blueprint: 3 concept/recognition items, 3 code/output traces, 2 error diagnoses, and 2 application decisions. One point each; prepare an answer key with brief explanations. Use only content already taught; M19 is cumulative revision. Allow about 10–15 minutes, adjusting accessibility accommodations as needed.
- Coding activity: one small individual deliverable, one meaningful modification, and one failure case. Suggested 10-point rubric: required behavior 4, handling errors/edge cases 2, explanation and independent change 2, reproducible setup/readability 2. This is a proposed classroom rubric, not an institutional grading policy.
- Optional challenges and extra drills are ungraded. Do not require a quiz AND a separate graded coding task in the same module. Do not count the same artifact again as the summative or periodical exam.
- At 60 minutes: quiz meeting = 5 recap + 25 explanation/demo + 15 guided practice + 10 quiz + 5 feedback; coding meeting = 5 recap + 15 explanation/demo + 30 coding + 10 review. At 90 minutes, add 15 minutes guided practice and 15 feedback/debugging. Setup-heavy lessons need prepared starters.
- Summative exams before each periodical retain their own scheduled slots. M19/M20 prepare students for the solo final practical; they are not the actual final exam.
- If two chapters share a shortened meeting, use one primary assessment and move or omit the other with a recorded adjustment. Never double the workload merely to preserve numbering. Twenty prepared modules do not guarantee twenty available teaching meetings.

Every full lesson will include a plain-language preview, 2–4 observable outcomes, prerequisites, numbered explanations, exact setup/files, complete runnable checkpoint, expected output, one common failure and repair, short Taglish support, and sources. Students should predict, run, explain, and independently change code. “Gumana” is the starting point; “kaya kong ipaliwanag at baguhin” is the understanding check.

## Detailed module contents


## Module 1: Foundations of Event-Driven Programming and Day-One Refresher

**Assessment plan:** 10-item quiz. Identify producer, listener and effect; trace a condition/loop/function and explain one event with two listeners. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Prelim. **Prerequisites:** Basic prior programming exposure; Day 1 refreshes the syntax.


### 1.1 Opening and programming refresher

Brief introductions and an engaging order-board demo; let/const, values and operators, if/else, for/while, named functions, parameters, returns, and a short scope reminder. Trace one tiny program rather than reteaching a full introductory course. Briefly recognize arrays, objects, and arrow callbacks used in the starter.


### 1.1.1 First delayed callback: setTimeout

After reviewing functions, spend 5–10 minutes scheduling one callback with `setTimeout(callback, delayInMilliseconds)`. Pass a function rather than calling it immediately. Explain that 1000 milliseconds is one second, and the callback can run later than the requested delay. The remaining code continues; this is not a command to pause the entire program.

Run this plain JavaScript example in the browser console (no TypeScript build needed):

```javascript
console.log("1. Order received");
setTimeout(() => {
  console.log("3. Ready na ang order!");
}, 1000);
console.log("2. Taking the next order");
```

Expected order: 1, 2, then 3 after the timer becomes eligible and the callback can execute. Ask students to predict the order, change the delay, and explain: **“Naka-schedule ang callback; tuloy pa rin ang ibang code.”** Demonstrate saving the returned timer handle and passing it to `clearTimeout(handle)` to cancel pending work. Do not use a busy-wait loop or a string of executable code. A timer callback introduces scheduling; it is not itself a demonstration of DOM listener registration or Pub/Sub.

Use one of the existing quiz's code-trace items for this example; do not add an eleventh item or another graded exercise. Module 2 explains the event loop, zero-delay scheduling and promises; Module 5 revisits timer cleanup and debounce. This preview replaces part of the opening demonstration rather than adding another full activity. Source: [MDN setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout), inspected 3 November 2026.

### 1.2 What event-driven programming means

Events influence program flow; initialization, registration, and reaction. Compare procedural steps, polling, request/response, and event-driven interaction. These approaches can coexist.


### 1.3 Vocabulary and event anatomy

Source, producer/publisher/emitter, consumer/subscriber/listener/handler, dispatcher, bus, channel, and broker. Introduce payload, event name, event ID, and timestamp as appropriate—not mandatory fields for every DOM event.


### 1.4 Events, commands, and queries

A domain event records something that happened; a command requests an action; a query asks for information. Domain naming in past tense versus API-defined names such as click. Immutability as a deliberate domain-event policy.


### 1.5 Observer and Pub/Sub preview

Direct subject-observer registration versus an intermediary channel; one event, several reactions. Preview decoupling without claiming it is automatic.


### 1.6 Environment and strict TypeScript workspace

Node/npm, editor, browser DevTools, package.json, tsconfig.json with strict enabled, explicit module format, run versus type-check commands. Supply the configuration and a minimal typed payload/function; deeper type-system work belongs to M06.


### 1.7 Benefits, costs, and fit

Extensibility, independent reactions, responsiveness with non-blocking work; harder tracing, lifecycle mistakes, errors, ordering, duplicates. Scalability and resilience need appropriate design. Use direct calls for simple operations where clearer.


**Guided program / exercise:** Baon/order mini-program: use a condition, loop, and function, then observe a teacher-provided event with two reactions.

**Expected evidence:** Explain source → handler → effect; edit a value and a callback; predict the delayed example's 1 → 2 → 3 order; explain that setTimeout does not pause subsequent statements; run/check the prepared workspace.

**Depth and pacing:** Core: compressed refresher and event vocabulary. The 60-minute opening prioritizes a runnable first example; use the extra 30 minutes for setup support. Provide a catch-up reference for students needing more basics.


## Module 2: The JavaScript Event Loop, Concurrency, and Async Primitives

**Assessment plan:** One coding activity. Submit an output-order experiment with a prediction, actual trace and handled rejection; no claim that await makes CPU work parallel. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Prelim. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 2.1 Engine versus host

V8 call stack/heap as the selected Node engine example; browser Web APIs versus Node/libuv facilities. JavaScript engines do not alone provide every timer/network API.


### 2.2 Execution mechanics

Run-to-completion, tasks/macrotasks, promise microtasks, queueMicrotask, rendering opportunities, and timer delay thresholds. Avoid presenting one universal host queue.


### 2.3 Promises and async/await introduction

Pending/fulfilled/rejected; then/catch/finally; async functions returning promises; await yielding the current async function; try/catch. First use a fixed simulated delay and deliberate failure.


### 2.4 Node-specific phases and scheduling

Timers, poll, check, pending/close callbacks; setImmediate and nextTick. Explain module-format/context-sensitive ordering; do not teach nextTick as an ordinary browser microtask.


### 2.5 Non-blocking I/O, concurrency, and parallelism

Overlapping waiting versus executing CPU work simultaneously; promises do not move arbitrary CPU loops off-thread.


### 2.6 Starvation and event-loop lag

Long synchronous tasks and unbounded microtasks; bounded demonstration, interval-based lag observation, yielding, and worker preview.


**Guided program / exercise:** Predict and run a log-order experiment; simulate order preparation while another action remains usable.

**Expected evidence:** Explain synchronous/microtask/timer output and handled rejection; identify a blocking operation.

**Depth and pacing:** Core: stack, scheduling, small promise/await example. Phase internals and lag monitoring are guided traces or extension; M05 develops async composition.


## Module 3: Client-Side DOM Events and Interactive Interfaces

**Assessment plan:** 10-item quiz. Trace click registration, event target and page update; distinguish script placement, bubbling and preventDefault. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Prelim. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 3.1 HTML, script placement, and the first event listener

Begin with a complete `index.html`: one button, one paragraph for output, and an inline `<script>` placed after those elements near the end of `<body>`. Select the button with `document.getElementById`, register `addEventListener('click', handler)`, and change the paragraph's `textContent` inside the handler. Trace selection → registration → click → callback → visible change. Explain why passing a function differs from calling it immediately, and check that the selected element exists.

Then move the same JavaScript into `app.js` and introduce `<script src="app.js" defer></script>` as an alternative loading arrangement. Distinguish an inline script block from an inline HTML `onclick` attribute. Browser TypeScript will need a build/output step; this first HTML exercise uses plain JavaScript. Introduce event type, target/currentTarget, and function identity only after the first click response works.


### 3.2 Input, forms, and accessible interaction

Click, input, change, submit, keyboard, pointer events; labels, native controls, validation, text conversion, safe feedback.


### 3.3 Propagation and default actions

Capture/target/bubble; cancelable/bubbles; preventDefault, stopPropagation, stopImmediatePropagation. Non-bubbling event cases require a suitable strategy.


### 3.4 Delegation and dynamic elements

Stable parent listener; closest/contains checks; Element narrowing; stable row IDs and nested click targets.


### 3.5 Listener options and disposal

once, passive, capture, signal; removeEventListener matching; grouped AbortController cleanup.


### 3.6 Custom events and browser lifecycle

CustomEvent/detail and synchronous dispatch; bubbles/composed where needed; DOMContentLoaded, visibilitychange/pagehide rather than relying on unload.


### 3.7 Other browser event sources

Resize/Intersection/MutationObserver, storage, BroadcastChannel, MessageChannel, postMessage, and requestAnimationFrame as a reference map.


**Guided program / exercise:** Stage 1: a complete HTML page with a button and JavaScript inside `<script>` that changes visible text. Stage 2: add a click counter or one validated order input. Stage 3, if time permits: grow the same program into a dynamic task board with delegated actions and a custom status event.

**Expected evidence:** Students can identify the HTML element, script, registration and handler, then change the response independently. For the form/list extension, new rows and keyboard submission work, invalid input is rejected, and cleanup prevents duplicate responses.

**Depth and pacing:** Core: script placement → select element → register click listener → update text → small independent modification. A form or counter is the next step. Delegation/custom events can use prepared examples or follow-up practice. Observer APIs, cross-window channels, drag/drop and Shadow DOM are demonstrations/reference; do not require the entire board in the introductory listener exercise.


## Module 4: In-Process Node.js Events and Native Event Sources

**Assessment plan:** One coding activity. Submit an order emitter with two listeners, one once listener and cleanup; include a deliberate error handled appropriately. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Prelim. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 4.1 EventEmitter fundamentals

on, emit, once, off/removeListener, registration order, synchronous listeners, ignored return values, and emit return meaning.


### 4.2 Managing listeners

Named references, prependListener, listenerCount/eventNames, max-listener warnings, disposal and duplicate registration.


### 4.3 Error and async-listener policy

Special error event, thrown listener failures, rejected async listeners, captureRejections, and explicit local recovery. Contrast browser dispatch exceptions.


### 4.4 Small event service design

Composition versus subclassing; OrderService with meaningful payloads; separate invoice/log/inventory reactions.


### 4.5 Promise and iterator helpers

events.once and events.on; waiting before emitting, abort handling, async-iterator buffering and lifecycle.


### 4.6 Other Node sources and shutdown

fs.watch, HTTP request events, child-process/worker messages, SIGINT/SIGTERM; stop accepting work, drain, dispose. A read-once file example is not continuous watching.


**Guided program / exercise:** Canteen order emitter with independent handlers and a once-only notice.

**Expected evidence:** Trace listener order, remove a handler, and demonstrate an intentional error without pretending every failure policy is identical.

**Depth and pacing:** Core: small emitter. File watchers, async iterators, HTTP lifecycle and graceful shutdown are staged demonstrations.


## Module 5: Async Patterns, Cancellation, and Race Conditions

**Assessment plan:** 10-item quiz. Choose sequential versus concurrent awaits; diagnose stale results and explain cancellation versus debouncing. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Prelim. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 5.1 Choosing a completion model

Callback → promise → async/await; one promise outcome versus repeated events; composing rather than wrapping everything.


### 5.2 Sequential versus concurrent work

Promise.all, allSettled, race, any; first-settled versus first-successful; failure behavior; no automatic sibling cancellation.


### 5.3 HTTP and data validation

Fetch response status, JSON parsing and shape checks; success/loading/empty/error/retry states; fixtures and network failure.


### 5.4 Cancellation and timeout policies

AbortController, pre-aborted signals, reason, timeout/any where supported; cancellation versus merely stopping waiting.


### 5.5 Stale-response protection

Request tokens/version checks and supported aborts; slow-old versus fast-new results; avoid unhandled abort rejections.


### 5.6 Debounce and throttle

Trailing/leading choices, closure-held timer state, clear/cancel behavior, first-call tests, visual update scheduling.


### 5.7 Async iteration and cleanup

Buffer bounds, producer/consumer rates, finally disposal; avoid leaking abort listeners in custom wrappers.


**Guided program / exercise:** Campus directory search with controlled response delays, then add debounce and cancellation in stages.

**Expected evidence:** Newest query wins; canceled work has an expected path; success/failure cleanup is observable.

**Depth and pacing:** Core: one guarded async flow. Iterator wrappers and all combinators need small separate demonstrations rather than one oversized app.


## Module 6: Type-Safe Event Systems in TypeScript

**Assessment plan:** One coding activity. Submit a typed event map with a valid payload, a compile-time invalid example and a rejected runtime payload. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Midterm. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 6.1 Strengthening the starter types

Payload interfaces/type aliases, optional properties, unions, strict null checking; compile-time versus runtime contracts.


### 6.2 DOM typings and narrowing

Element queries, EventTarget/null checks, target/currentTarget limitations, safe delegation, avoiding unverified assertions.


### 6.3 Event maps and generic APIs

Event-name → payload map; keyof, indexed access, mapped/conditional types; introduce one typed on/emit signature at a time.


### 6.4 Typed custom events and domain unions

CustomEvent<T>, declaration merging as an extension; discriminated unions and exhaustive handlers.


### 6.5 Typed emitter behavior

on/off/once, unsubscribe function, snapshot versus live iteration, reentrancy, listener error and async policies.


### 6.6 Node typing and runtime schemas

Compatible @types/node/EventEmitter support; handwritten guards first, Zod/Valibot as schema-library options; version payloads deliberately.


**Guided program / exercise:** Small typed order bus; intentionally send a wrong payload, then reject malformed external data at runtime.

**Expected evidence:** Type checks catch mismatches; runtime checks reject untrusted data; unsubscribe semantics are specified.

**Depth and pacing:** Core: typed records and one event map. A publishable generic library is a stretch, not a prerequisite for later architecture.


## Module 7: Core Patterns, State Machines, and Framework Connections

**Assessment plan:** 10-item quiz. Classify event/command/query; reject an invalid state transition and explain Observer versus Pub/Sub. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Midterm. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 7.1 Observer versus Pub/Sub in depth

References, intermediaries, subscription ownership, coupling and testing boundaries.


### 7.2 Mediator and event bus

Route messages deliberately; avoid a global bus that hides every dependency.


### 7.3 Commands, facts, and queries

Responsibility, acknowledgment, event notification versus event-carried state transfer, thin/fat payload trade-offs.


### 7.4 State machines

States, transitions, guards and invalid actions; pure reducers; correlation between incoming event and state change.


### 7.5 Framework and reactive connections

React event/effect cleanup, Vue/Angular handling as comparison; signals versus event streams, state versus occurrence.


### 7.6 Domain modeling

Event storming walkthrough and past-tense domain events; do not turn every direct function call into a message.


**Guided program / exercise:** Model waiting → preparing → ready → collected with explicit invalid-transition feedback.

**Expected evidence:** Draw the event flow and test valid/invalid transitions without a framework dependency.

**Depth and pacing:** Core: patterns and small machine. Framework APIs/signals are comparisons; do not switch the required stack to React or Python.


## Module 8: Reactive Programming and RxJS Streams

**Assessment plan:** One coding activity. Submit the prepared reactive search example with one operator change and subscription cleanup; compare its behavior with plain JS. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Midterm. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 8.1 Reactive vocabulary

Observable, observer, subscription, next/error/complete; cold/hot and unicast/multicast concepts.


### 8.2 Stream creation and transformation

fromEvent, map, filter, tap; connect existing DOM events to a stream.


### 8.3 Time and higher-order operators

debounceTime, distinctUntilChanged, switchMap versus concatMap/mergeMap/exhaustMap; cancellation depends on the underlying operation.


### 8.4 Error, lifetime, and sharing

catchError/finalize, takeUntil, subscription disposal, Subject/BehaviorSubject, share/shareReplay trade-offs.


### 8.5 Stream testing

Marble-diagram reading and virtual time; compare with the plain-JS implementation.


**Guided program / exercise:** Rebuild the familiar search box as a short RxJS pipeline using a prepared environment.

**Expected evidence:** Explain the selected operator and show disposed subscriptions stop reacting.

**Depth and pacing:** Practical introduction plus operator reference. Exact APIs/version and executable examples need verification; no claim that the earlier client-rendered docs shell verified every operator.


## Module 9: Client–Server Real-Time Events and Messaging Channels

**Assessment plan:** 10-item quiz. Select SSE versus WebSocket for a scenario; explain connection loss, validation and authentication boundaries. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Midterm. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 9.1 Transport selection

Polling/long polling, SSE, WebSocket and Socket.IO; one-way versus two-way needs; Socket.IO is not raw WebSocket.


### 9.2 Connection lifecycle

Open/message/error/close, intentional disposal, reconnect/backoff and connection state in the UI.


### 9.3 Message identity and safety

Validate messages, identify sender/session, sequence/replay considerations, authentication boundaries, origin checks.


### 9.4 Browser channels

BroadcastChannel, storage notifications and postMessage; targetOrigin and incoming origin/source/data checks.


### 9.5 Real-time deployment concerns

Heartbeats, disconnect recovery, slow consumers and scaling questions; distinguish simulation from actual transport.


**Guided program / exercise:** Campus live-announcement board using a local event fixture, then an instructor-provided SSE or WebSocket service.

**Expected evidence:** Messages update the board; disconnection and cleanup are visible; simulations are labeled.

**Depth and pacing:** Core: transport comparison and one local demonstration. Deployments and public echo endpoints are optional, not assumed stable.


## Module 10: Streams, Backpressure, Workers, and Background Work

**Assessment plan:** One coding activity. Submit a bounded stream/backpressure trace; a worker comparison is optional, not a second graded activity. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Midterm. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 10.1 Stream model

Readable/Writable/Transform; data/end/error/close/drain; choosing one consumption style.


### 10.2 Pipeline lifecycle

stream/promises pipeline, error forwarding, completion and resource cleanup.


### 10.3 Backpressure and bounded buffers

write false/drain; high-water marks; pause/resume; queue capacity and overflow policy.


### 10.4 Async iterables

for await, producer/consumer rates, cancel/return/finally behavior.


### 10.5 CPU work and workers

Web Workers versus worker_threads; message passing, serialization/transfer concepts, termination; chunk-and-yield alternative.


### 10.6 Scheduling and shutdown boundaries

Foreground timers versus OS background services; drain pending work before closing a worker or pipeline.


**Guided program / exercise:** A prepared log-processing pipeline and a short responsive-UI comparison.

**Expected evidence:** Identify the slow consumer, enforce a small buffer policy, and dispose resources.

**Depth and pacing:** Core: one pipeline/backpressure trace. Worker implementation is a prepared demonstration or stretch.


## Module 11: Testing and Debugging Event-Driven Programs

**Assessment plan:** 10-item quiz. Read a failing test, identify the faulty listener or cleanup and select a meaningful assertion. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Midterm. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 11.1 Test design

Normal/boundary/failure/recovery cases; assertions for handlers and pure transition functions.


### 11.2 Listener contract tests

Order, once, unsubscribe during dispatch, duplicate registration, reentrancy, throwing and rejecting listeners.


### 11.3 Async and timing tests

Dependency-injected clock/scheduler, fake timers, deterministic waits and cancellation; avoid fragile sleeps.


### 11.4 Tools and layers

Node test runner; Vitest/Jest as alternatives; unit versus integration; RxJS marble tests.


### 11.5 Debugging tools

Breakpoints, async stack traces, structured event timeline, listener/resource leaks, timer/CPU profiling.


### 11.6 Integration environments

Testcontainers/broker test idea; do not require Docker for the core test exercise.


**Guided program / exercise:** Test and repair the typed bus or state machine built earlier.

**Expected evidence:** Show a failing regression test, its repair, and passing normal/error/cleanup tests.

**Depth and pacing:** Core practical tests; profiling, marbles and container integration are selected demonstrations.


## Module 12: Distributed Messaging, Brokers, and Event Streaming

**Assessment plan:** One coding activity. Submit a local queue versus broadcast simulation and label its difference from a real persistent broker. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Pre-final. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 12.1 From local to distributed

Process/network boundaries, direct transports versus broker mediation; broker is an architectural option, not universally required.


### 12.2 Messaging models

Point-to-point/work queues, competing consumers, fan-out/fan-in, Pub/Sub and request/reply.


### 12.3 Broker concepts

Queue, exchange, routing key, topic, partition, consumer group and retention; terminology is product-specific.


### 12.4 RabbitMQ and Kafka comparison

Routing/queues versus retained partitioned logs and replay; JavaScript client walkthrough with a prepared service.


### 12.5 Other platforms

Redis Streams, NATS, Pulsar; SQS/SNS/EventBridge, Google Pub/Sub, Azure Service Bus as a comparative catalog.


**Guided program / exercise:** Route order notifications to several consumers in a local simulation and inspect one broker diagram.

**Expected evidence:** Choose queue versus Pub/Sub versus log for a stated need and explain the delivery path.

**Depth and pacing:** Architecture module with a runnable local model. Broker installation and multiple cloud accounts are optional.


## Module 13: Delivery Guarantees, Ordering, and Reliable Consumers

**Assessment plan:** 10-item quiz. Trace duplicate delivery, retry limits and a dead-letter outcome; distinguish idempotency from global exactly-once claims. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Pre-final. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 13.1 Guarantee scope

At-most-once, at-least-once and exactly-once claims; distinguish broker guarantees from end-to-end side effects.


### 13.2 Acknowledgment and failure windows

Crash before/after side effects and acknowledgment; redelivery scenarios.


### 13.3 Idempotency

Event IDs, deduplication, unique constraints, inbox records and bounded retention.


### 13.4 Ordering

Per-key/per-partition constraints; concurrent consumers, sequence numbers and late events.


### 13.5 Retries and poison messages

Bounded exponential backoff/jitter, retry budgets, dead-letter queues, inspection and replay.


### 13.6 Backlog policy

Consumer lag, queue depth, overflow, load shedding and throttling; never silently drop critical work.


**Guided program / exercise:** Deliver an order twice and inject a transient failure in a bounded local queue.

**Expected evidence:** The completed order side effect occurs once by explicit deduplication policy; retry count is bounded.

**Depth and pacing:** Core simulation plus architectural reasoning. Do not call a toy Set-based deduplicator a durable exactly-once system.


## Module 14: Reliable Publication, Outbox/Inbox, and Event Contracts

**Assessment plan:** One coding activity. Submit a small outbox/failure-window model plus version validation; label whether storage is simulated or persistent. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Pre-final. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 14.1 Dual-write problem

Business data committed but event not published, or event published before a failed business write.


### 14.2 Transactional outbox

Business update and pending event in one database transaction; relay/polling or CDC; delivery still may duplicate.


### 14.3 Inbox and consumer transaction

Record processed identity alongside local state where possible; coordinate acknowledgments.


### 14.4 Schema evolution

Versioned payloads, compatibility, optional/required fields, deprecation and contract tests.


### 14.5 Event envelopes and CloudEvents

ID, source, type, time, data; common envelope versus application payload; JSON Schema/Avro/Protobuf and registry overview.


### 14.6 Privacy and replay

Data minimization, sensitive fields, retention and replay access; migration and operational ownership.


**Guided program / exercise:** Trace the failure windows in an outbox diagram and validate two event-schema versions.

**Expected evidence:** Explain why a relay can republish and why consumer idempotency still matters.

**Depth and pacing:** Design exercise with a small local model. Database transaction/CDC production setup is an extension.


## Module 15: Event Sourcing, Replay, and Read Projections

**Assessment plan:** 10-item quiz. Rebuild state from a short event history; distinguish a projection from external side effects during replay. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Pre-final. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 15.1 Event store versus ordinary log

Append-only domain-event history as the source of state; logging alone is not event sourcing.


### 15.2 Aggregate lifecycle

Command validation, emitting a new event, applying events, version and expected-version checks.


### 15.3 Replay and projections

Pure replay to rebuild state; avoid repeating real external side effects; read projections/materialized views.


### 15.4 Snapshots and evolution

Snapshot purpose, schema changes/upcasting, historical interpretation.


### 15.5 Trade-offs and fit

Auditability/reconstruction versus complexity, querying, concurrency and data-lifecycle obligations.


**Guided program / exercise:** Replay a small in-memory canteen-account or inventory event history.

**Expected evidence:** Reconstructed state matches the expected result and replay does not resend a notification.

**Depth and pacing:** Core small replay exercise, architecture discussion for snapshots/concurrency. Avoid mandatory production database setup.


## Module 16: CQRS, Sagas, and Distributed Workflow Coordination

**Assessment plan:** One coding activity. Submit a small saga failure/compensation simulation; distinguish compensation from a perfect database rollback. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Pre-final. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 16.1 CQRS

Separate command/write and query/read models; projections and stale reads; does not require event sourcing.


### 16.2 Consistency and UI design

Eventual consistency where chosen; pending/confirmed/failed states rather than assuming immediate agreement.


### 16.3 Saga concepts

Sequence of local transactions, compensating actions, irreversibility and business semantics.


### 16.4 Orchestration versus choreography

Coordinator-directed steps versus services reacting; ownership and failure visibility.


### 16.5 Workflow recovery

Timeouts, retries, duplicates, idempotent compensation and manual recovery.


### 16.6 Architecture fit

Direct calls for simple work; avoid a distributed ball of mud or hidden temporal coupling.


**Guided program / exercise:** Paper or local simulated order → reserve → confirm workflow with a deliberate failure.

**Expected evidence:** Explain the read model and show a compensating action without claiming global rollback.

**Depth and pacing:** Architecture walkthrough with a minimal simulation. CQRS/Sagas are covered, not promised as mastered enterprise implementations.


## Module 17: Observability, Security, and Production Resilience

**Assessment plan:** 10-item quiz. Diagnose a structured event timeline and choose a useful metric, correlation ID and validation boundary. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Pre-final. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 17.1 Tracing an event

Event/correlation/causation IDs, structured logs, metrics and traces; find where an order stopped.


### 17.2 Operational signals

Throughput, processing latency, retry/error rates, queue depth and consumer lag.


### 17.3 OpenTelemetry introduction

Context propagation and traceparent across HTTP/messaging; sampling/PII caution; prepared trace diagram.


### 17.4 Security boundaries

Authenticate/authorize producers and consumers, broker/topic permissions, validate payloads, origin/source checks, tenant isolation, encryption and secret placement.


### 17.5 Resilience tools

Circuit breaker, bulkhead, rate limit, bounded queues, graceful shutdown; Opossum as an optional library example.


### 17.6 Maintenance practices

Dependency/version baseline, event documentation, compatibility, instrumentation overhead, incident/replay runbook.


**Guided program / exercise:** Follow a failed event through a structured log and repair a validation or retry policy.

**Expected evidence:** Locate the failure, explain the trusted boundary and propose a measurable recovery check.

**Depth and pacing:** Core log/security audit; distributed collectors and full dashboards are demonstrations, not mandatory infrastructure.


## Module 18: Integrated Solo Project Design and Architecture Checkpoint

**Assessment plan:** One coding activity. Submit one individual working feature, event-flow diagram and meaningful failure test; reuse an earlier checkpoint. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Pre-final. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 18.1 Scope and requirements

Select campus order board, notifier, log processor or similar; user story and acceptance criteria.


### 18.2 Architecture artifacts

Event-flow diagram, state model, event contracts, error/cancel/cleanup paths and test plan.


### 18.3 Implementation tiers

Core: local JS/TS system; extension: one real-time/broker/projection feature. No requirement to implement every researched technology.


### 18.4 Capstone ideas from the reports

Kanban board, typed emitter package, chat/whiteboard, e-commerce workflow, bank/inventory replay, video/log pipeline and microservice logistics as comparison/advanced routes.


### 18.5 Delivery evidence

Runnable prototype, README/setup, known limitations, labeled simulations, source attribution and individual progress log.


**Guided program / exercise:** Plan and extend an individual project seeded from earlier activities.

**Expected evidence:** Demonstrate one complete event path and a failure path; identify remaining risks before Finals.

**Depth and pacing:** Core project integration. Multi-service logistics/payment infrastructure is an advanced blueprint, not compulsory solo scope.


## Module 19: Finals Review, Summative Preparation, and Mock Practical

**Assessment plan:** 10-item quiz. Complete a cumulative practical-reasoning quiz; guided repair rehearsal is ungraded and introduces no new infrastructure. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Final. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 19.1 Review map

Events, typing, runtime order, browser/Node differences, async failures and cleanup.


### 19.2 Practical rehearsal

Trace unfamiliar but small code, repair a broken handler, add a tested behavior.


### 19.3 Architecture recap

Choose appropriate patterns and explain limits rather than install new systems.


### 19.4 Assessment preparation

Rubric, normal/failure/recovery evidence and individual explanation; summative exam remains a separate slot.


**Guided program / exercise:** Individual mock practical on familiar technology and personal project risk review.

**Expected evidence:** A working repair, test evidence and a concise explanation of why it works.

**Depth and pacing:** Review only; no new advanced technology.


## Module 20: Applied knowledge for the mini-capstone defense

Complete the [20 applied items and two defense essays](modules/EDP_M20.md).

## Module 21: Mini-capstone announcement and solo project readiness

**Assessment plan:** One coding activity. Submit a reproducible solo-project preparation package and explain an independent change; actual final practical is separate. Other exercises in this module are guided practice or optional extensions, not additional graded submissions.

**Period:** Final. **Prerequisites:** Earlier modules; introduce any new syntax used by the starter.


### 21.1 Project verification

Launch from documented instructions; check dependencies, data fixtures and own event flows.


### 21.2 Failure and recovery rehearsal

Invalid payload, duplicate event, cancellation or disconnect as applicable; resource disposal.


### 21.3 Final walkthrough

Explain personal implementation, chosen patterns and unimplemented extensions honestly.


### 21.4 Submission preparation

Source files, README, test results, event diagram, limitations and reflection. Actual practical exam occurs in its institutional slot.


**Guided program / exercise:** Individual demo rehearsal and troubleshooting of the student’s own project.

**Expected evidence:** Reproducible individual submission with success/failure/cleanup evidence.

**Depth and pacing:** Preparation only; does not replace the final practical exam.


## Source-report coverage crosswalk

| Imported topic family | Where it is retained |
| --- | --- |
| JS/TS source M1 foundations and vocabulary | M01, reinforced in M07 |
| Source M2 runtime, lag, starvation, Node scheduling | M02, M10–M11 |
| Source M3 DOM/listeners/propagation/delegation/custom events/channels | M03, M05, M09 |
| Source M4 EventEmitter/helpers/subclassing/watchers/streams/shutdown | M04, M10, M17 |
| Source M5 promises/iteration/cancel/races/errors | M02, M05, M10 |
| Source M6 DOM types/event maps/generic emitter/unions/runtime validation | M01 setup, M06 in depth, M14 contracts |
| Source M7 Observer/PubSub/mediator/commands/state machines/RxJS/signals | M01, M07–M08 |
| Source M8 transports/guarantees/retries/outbox/ES/CQRS/sagas/observability | M09, M12–M17 |
| Source M9 framework connections | M07 comparison; core remains framework-independent |
| Source M10 testing/debugging | M11, reinforced in M18–M20 |
| Source M11 best practices and pitfalls | Every lifecycle/error section; consolidated in M13–M14 and M17 |
| Source M12 capstone, cheat sheets, practice prompts | M18–M20; per-module traces and references |
| Production report type-safe emitter and RxJS search | M06, M08 |
| Production report brokers, outbox, aggregate replay and saga | M12–M16 |
| Production report Testcontainers, OpenTelemetry, Opossum | M11/M17 as guided/advanced tooling |
| Production report logistics/driver/payment microservices | M18 advanced blueprint; not a mandatory individual deployment |
| Fundamentals report delivery, schemas, event storming, CloudEvents | M07, M12–M14 |
| Fundamentals report bank/inventory/chat/video/log project options | M15 and M18 project routes |
| Python event bus and asyncio examples | Optional language comparison only; no Python setup requirement |

## Technical qualifications carried into the lessons

- Event-driven programs may have synchronous handlers. Node emit is synchronous; returned listener values are ignored. Browser dispatch exception handling differs from ordinary Node listener calls.
- A producer does not universally avoid waiting: in-process synchronous dispatch waits for synchronous listeners. Brokered delivery changes the relationship; say which model is meant.
- Event-driven design does not universally require eventual consistency, immutability enforced by the runtime, a broker, or microservices.
- await yields the current async function; heavy synchronous CPU work still blocks its thread.
- V8, browser APIs and Node/libuv are distinct parts of the execution environment. Browser and Node queue rules are not one interchangeable diagram.
- TypeScript strict checks do not validate external payloads. Validate runtime boundaries separately.
- Exactly-once claims require defined scope; deduplication/idempotency does not magically create a global exactly-once system.
- A compensating saga action is a business recovery step, not necessarily a perfect rollback.
- Supplied AI examples remain untested references. Rewrite incomplete snippets and verify cancellation, reentrancy, errors, resource lifetimes and module format before calling them runnable starters.

## Primary references and verification state

| Area | References | State |
| --- | --- | --- |
| JS fundamentals and browser behavior | [MDN JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide), [execution model](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model), [events](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events) | Specific language/event pages inspected in earlier research; verify selected code during authoring |
| Promises and cancellation | [Using promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises), [AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) | Inspected previously |
| Node events and scheduling | [Events](https://nodejs.org/api/events.html), [event loop](https://nodejs.org/learn/asynchronous-work/event-loop-timers-and-nexttick), [process scheduling](https://nodejs.org/api/process.html#when-to-use-queuemicrotask-vs-processnexttick) | Relevant pages inspected; events and loop rechecked for this revision |
| Strict typing | [strict option](https://www.typescriptlang.org/tsconfig/strict.html), [narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) | strict inspected this revision; narrowing previously inspected |
| Node streams/testing | [Streams](https://nodejs.org/api/stream.html), [test runner](https://nodejs.org/api/test.html) | Stream reference retrieved this revision; test runner previously inspected; examples not executed |
| RxJS | [Official overview](https://rxjs.dev/guide/overview) | Client-rendered shell only through the research tool; exact operators and version need direct verification during authoring |
| Brokers | [RabbitMQ tutorials](https://www.rabbitmq.com/tutorials), [Kafka introduction](https://kafka.apache.org/intro/) | Index/introduction inspected this revision; no broker installed or lab validated |
| Event format | [CloudEvents](https://cloudevents.io/) | Overview inspected; exact specification/SDK usage needs follow-up |
| Architecture | [Event sourcing](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing), [CQRS](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs), [Saga](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga) | Article text retrieved this revision, with site authorization notices also present; not an implementation audit |
| Observability | [OpenTelemetry primer](https://opentelemetry.io/docs/concepts/observability-primer/) | Reference page retrieved; actual JS instrumentation/version setup remains to be verified |

RabbitMQ JavaScript clients, RxJS operators, Zod/Valibot, Opossum, Socket.IO, framework-specific APIs, schema registries and Testcontainers require targeted version/API checks before executable lessons. No unsupported package-version baseline is adopted from the reports.

## Tomorrow's authoring handoff

This document is the authoritative EDP topic sequence for the next writing session, superseding the previous refresher-heavy contents. Keep Day 1's basics compact and revisit syntax through small reminders thereafter. The goal is broad source-aligned EDP coverage with understandable programs—not claiming enterprise mastery from a short demonstration.

For each module write a preview and 2–4 measurable targets; detailed explanations with natural Taglish support; a meaningful analogy; exact files/setup commands; complete starter code; an output trace; expected failure/cleanup behavior; an independent modification; troubleshooting; and source links. Keep examples scoped by the depth labels above. Include a short glossary/cheat sheet. Use the alternating 10-item quiz/coding policy above; extra drills are optional and ungraded.

Summatives and periodicals need separate assessment documents. The solo final project should demonstrate a coherent subset of the course, with a reproducible setup, tests, event-flow diagram and honest limitations. Full lesson text, code execution, TypeScript checking, browser verification and final scheduling remain pending.

## Optional persistence connection to ADET

EDP remains JavaScript/TypeScript in the browser and Node.js. Do not make database installation a prerequisite for Prelim or core broker simulations. A shared campus-order domain can connect both courses, but assess different skills: EDP event flow/reliability, ADET mobile UI/API integration.

For M14/M18 extensions, use a Node API with MongoDB or MySQL/MariaDB from the chosen local stack. A browser or mobile client never receives database credentials. In-memory outbox examples illustrate failure windows but are not durable or transactionally atomic. A real SQL outbox needs the domain write and outbox insert in the same database transaction; a MongoDB variant needs a design matched to its deployment and transaction capabilities, verified before coding. Polling/retry examples need bounds, IDs and deduplication. Database writes do not automatically emit application events.

New detail to carry into each lesson: explicit environment (browser/Node), sync versus async dispatch, success trace, one failure trace, resource cleanup, and a clear stop point for the 60-minute version. Use sample/fake user data. Do not require Kafka, RabbitMQ, tracing infrastructure and two databases for one solo project.
