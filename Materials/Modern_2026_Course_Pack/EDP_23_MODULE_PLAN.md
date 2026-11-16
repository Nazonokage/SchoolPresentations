# Event-driven Programming: 23-module plan

[Research pack home](README.md) | [Teaching blueprint](TEACHING_BLUEPRINT.md) | [Sources](SOURCE_REGISTER.md)

**Stack:** Plain JavaScript, then TypeScript; browser APIs and Node.js. No React, Angular, or Vue is required. Small HTML/CSS shells are provided for browser activities. **Status:** researched outline; full lesson files and code are the next phase.

**Course outcome:** Design and test programs whose behavior responds correctly to user input, timers, asynchronous results, and external events, including failure, cancellation, cleanup, and ordering concerns.

The sequence assumes basic programming but does not assume knowledge of JavaScript's runtime model. ADET and EDP may share vocabulary and scenarios; neither course's assessment depends on completing the other course's project.

## Phase 1 — See the event, trace the response

| No. | Topic and learning target | Fun guided build | Independent change and evidence | Research basis |
| --- | --- | --- | --- | --- |
| 01 | Events, event sources, listeners, handlers; program flow | Browser click counter | Add Reset and narrate input → handler → state → display | S27 |
| 02 | JS functions, callbacks, scope, closures, registration | Custom greeting buttons | Explain passing a function versus calling it; avoid accidental shared state | S27, S04 for comparison only |
| 03 | DOM event objects, target/currentTarget, forms, keyboard interaction | Canteen order form | Submit with Enter and button; prevent unwanted navigation; validate input | S27 |
| 04 | Propagation, capture/bubble, delegation | Clickable campus notice board | Handle a newly added row through the parent listener; explain nested-element targeting | S27 |
| 05 | Event-loop foundations, stack, tasks, microtasks | Predict-the-output ordering lab | Explain synchronous logs, promise continuation, and timer order without assuming all queues are identical | S28, S11 |
| 06 | Timers, scheduling, start/stop controls, cleanup | Reaction-time game | Reject premature clicks, stop old timers, and avoid multiple concurrent rounds | S28 |
| 07 | TypeScript bridge: typed state, unions, narrowing, DOM null checks | Typed traffic-light controller | Reject an invalid transition and handle a missing element without unsafe casting | S05–S06, S18 |

## Phase 2 — Asynchronous programs that handle real problems

| No. | Topic and learning target | Fun guided build | Independent change and evidence | Research basis |
| --- | --- | --- | --- | --- |
| 08 | Promises: pending/fulfilled/rejected and chaining | Simulated milk-tea preparation | Add a rejection path and a final cleanup message; do not hide errors | S11 |
| 09 | Async/await with try/catch/finally | Small TypeScript order program | Await a simulated order; test success and failure; explain that the whole runtime is not frozen | S12, S18 |
| 10 | Sequential versus concurrent work; Promise.all and allSettled | Compare three simulated canteen stalls | Measure start/end order; show partial failure without claiming promises automatically cancel siblings | S11, S29 |
| 11 | Fetch, response codes, JSON, runtime validation | Campus announcement loader | Test a missing route, invalid payload, and empty list against a local fixture service | S13, S06 |
| 12 | Cancellation, timeouts, stale responses | Search-as-you-type campus directory | Cancel old work or ignore outdated results so a slow earlier request cannot overwrite a newer one | S30 |
| 13 | Debounce, throttle, and backpressure concepts | Search suggestion counter and pointer-event meter | Compare immediate versus delayed handling; document the chosen policy | S28, S27; timing exercise is original |
| 14 | Custom events, pub/sub, listener lifetime | Decoupled classroom score board | Add two subscribers, unsubscribe one, and show that the remaining subscriber still works | S27; CustomEvent-specific reference to verify during authoring |
| 15 | State machines and reducers for event-driven behavior | Queue ticket status machine | Allow waiting → serving → done; reject impossible transitions and explain event versus state | S23, S06 |

## Phase 3 — External events, reliability, and integration

| No. | Topic and learning target | Fun guided build | Independent change and evidence | Research basis |
| --- | --- | --- | --- | --- |
| 16 | Node EventEmitter, synchronous dispatch, once/off, error handling | Canteen order event bus | Trace listener order and remove a listener; distinguish EventEmitter from DOM EventTarget | S31 |
| 17 | Persistence and restoring event-driven state | Save-and-resume browser checklist | Recover from invalid JSON; do not mistake local storage for secure or shared server storage | S32 |
| 18 | Workers and responsive computation | Number-crunching lab with a usable main UI | Compare blocking work with worker messages; terminate the worker when finished | S33 |
| 19 | Queues, bounded concurrency, retries, idempotency basics | Simulated print-job processor | Cap in-flight work, retry a transient failure, and avoid repeating a completed job | S11, S28; queue design is an original exercise |
| 20 | Testing and debugging event-driven programs | Tests for the queue/state machine | Assert transitions and error behavior; inject predictable timing rather than rely on fragile sleeps | S22 |
| 21 | Real-time server events, connection lifetime, reconnect behavior | Local campus queue board with SSE | Close subscriptions, handle disconnects, and compare SSE with a WebSocket use case | S34–S35 |
| 22 | Integration lab: event log, validation, cancellation, cleanup | Smart Canteen Queue prototype | Integrate selected patterns; show an event timeline and fix one race or duplicate-handler bug | Course synthesis |
| 23 | Capstone demo, explanation, and reliability review | Finish the queue board, study dashboard, or similar app | Demo normal use, a failure, recovery, and cleanup; explain one ordering decision using logs/tests | Course synthesis |

## Project scope

Recommended project: **Smart Canteen Queue**. Students generate orders, validate them, process events, display state, and handle simulated delays and failures. An event log should explain what happened in time order. A local SSE board is a stretch or team integration feature once the basic state machine works.

Required evidence: user-triggered events, an asynchronous operation, an error/recovery path, explicit cleanup, meaningful state transitions, and automated tests for a pure rule or transition function. Browser projects should retain native keyboard-operable controls. Server code must not assume browser-only APIs exist.

Do not require a message broker, paid cloud service, or external production API. Those may be compared conceptually after students understand local events and failure handling.

## Important boundaries to explain

- Event-driven architecture and asynchronous execution overlap but are not synonyms.
- Browser event propagation and Node EventEmitter have different behavior and methods.
- Type annotations do not make untrusted JSON safe.
- A timeout may stop waiting without canceling the underlying work; teach the actual cancellation mechanism used.
- Debouncing, throttling, cancellation, and bounded concurrency solve different problems.
- “It worked once” is weaker evidence than a repeatable normal/failure/recovery test.
