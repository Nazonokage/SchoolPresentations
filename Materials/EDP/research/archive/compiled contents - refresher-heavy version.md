# Event-driven Programming — Compiled Contents

**Updated:** 2 November 2026. **Target:** 20 prepared modules. **Stack:** JavaScript, TypeScript, browser APIs, and Node.js. **Status:** consolidated table of contents and authoring specification; complete lesson text and tested starter programs are still to be written.

[Research hub](research/README.md) | [Technical corrections](research/TECHNICAL_REVIEW.md) | [Verified sources](research/VERIFIED_SOURCES.md)

## 1. Coverage and completion status

The collected research covers the main language foundations, browser events, asynchronous execution, Node events, reliability, testing, and advanced architecture topics. This document selects and sequences that material for this class. The research collection is sufficient to outline the course; it is not proof that all teaching content or code is complete.

| Work | Current status |
| --- | --- |
| AI-supplied reports and earlier research | Collected and preserved in the research hub |
| Core technical references | Identified and inspected; version-sensitive implementation details require checking during authoring |
| Deduplicated topic sequence | Compiled below into 20 modules |
| Full explanations, complete code, expected output, teacher notes | Pending lesson authoring |
| Type checks, runtime/browser checks, dependency baseline | Pending implementation and validation |
| Actual subject dates and exam assignments | Pending the institution's timetable |

## 2. Flexible period allocation

| Period | Prepared modules | Count | Main purpose |
| --- | --- | ---: | --- |
| Prelim | M01–M05 | 5 | Opening, explicit programming refresher, collections |
| Midterm | M06–M11 | 6 | TypeScript bridge, browser events, runtime model, promises |
| Pre-final | M12–M18 | 7 | Async applications, event systems, persistence, testing, integration |
| Final | M19–M20 | 2 | Review and individual practical-project preparation |
| **Total** | **M01–M20** | **20** | **Prepared content inventory** |

Five plus six plus seven plus two equals **20**. Using eight Pre-final modules while retaining the other counts would produce **21**; an eighth Pre-final topic should therefore be an optional extension or a subdivision of existing content, not an unannounced extra numbered module.

The user now permits combining related prepared modules when the schedule is hectic. This supersedes the previous strict one-module-per-day planning rule. It does not make two full beginner lessons fit into one short meeting: choose a smaller combined core and retain the remaining material as practice/reference. Do not rush language foundations solely to preserve numbering.

Classes meet twice weekly per subject, approximately 60–90 minutes each; Saturdays are excluded. The [calendar analysis](../Modern_2026_Course_Pack/CALENDAR_AND_CAPACITY.md) still applies to available contact days. Twenty prepared modules are a content inventory, not a promise of twenty classroom teaching dates. Summative and periodical exams remain separate assessments.

## 3. Prelim — Starting with understandable programs

### M01 — Welcome to Event-driven Programming; Variables and Values

**Guiding question:** Paano nagiging interactive ang isang ordinaryong program?

**Detailed contents**

1. Brief introductions: name, familiar app, one campus problem worth solving.
2. Course preview: a teacher-run canteen order board responding to clicks.
3. Plain-language vocabulary: input, processing, output, event, response.
4. Running a small JavaScript program in the prepared environment; finding console output and errors.
5. Variables and constants: let, const, meaningful names, reassignment.
6. Numbers, strings, booleans; basic arithmetic and template-literal output.
7. Distinguishing a numeric value from numeric-looking text.

**Students should demonstrate:** declare values, calculate a balance, and explain one changed output.

**Guided activity:** Baon Check: allowance minus lunch and fare. **Remix:** change expenses and personalize the output. **Evidence:** correct balance and a short value trace. **Extension:** experiment with string concatenation versus numeric addition.

**Source basis:** R1. The opening demo motivates later work; its event code is not yet assumed knowledge.

### M02 — Conditionals and Decisions

**Guiding question:** Paano pipili ng tamang response ang program?

**Detailed contents**

1. Comparison operators and boolean results.
2. if, else if, and else; mutually exclusive branches.
3. Logical AND/OR and combining conditions.
4. Assignment versus equality; prefer clear strict comparisons.
5. Boundary values: below, exactly equal to, and above a threshold.
6. Input assumptions and a helpful invalid-value message.

**Students should demonstrate:** write and trace a decision and test its boundaries.

**Guided activity:** Is my baon enough? **Remix:** add a savings requirement. **Evidence:** three cases covering below/equal/above the required amount. **Extension:** a menu of named choices using switch after the core if/else works.

**Prerequisite:** M01. **Source basis:** R2.

### M03 — Loops and Repeated Work

**Guiding question:** Bakit paulit-ulit magta-type kung puwedeng loop?

**Detailed contents**

1. Recognizing repeated statements.
2. A counted for loop: initialization, condition, update.
3. Iteration trace tables and an accumulator.
4. A short while-loop comparison; termination matters.
5. Off-by-one mistakes and avoiding infinite loops.
6. Separating repeated calculation from repeated display.

**Students should demonstrate:** predict iterations and compute a repeated total.

**Guided activity:** Five-day savings forecast. **Remix:** change the duration and daily amount. **Evidence:** a trace and correct total for zero, one, and several iterations. **Extension:** stop when a target amount is reached.

**Prerequisites:** M01–M02. **Source basis:** R3.

### M04 — Functions, Parameters, Scope, and Return Values

**Guiding question:** Paano gagawing reusable ang isang calculation?

**Detailed contents**

1. Defining and calling a named function.
2. Parameters versus arguments.
3. Returning a result versus printing a result.
4. Local variables and basic scope.
5. Early return for a simple invalid case.
6. Calling the same function with different inputs.
7. Separating calculation from display for later testing.

**Students should demonstrate:** write a reusable calculation and explain its returned value.

**Guided activity:** Canteen order calculator. **Remix:** add a discount parameter. **Evidence:** three calls with predicted results. **Extension:** arrow-function notation after ordinary function calls are understood.

**Prerequisites:** M01–M03. **Source basis:** R4.

### M05 — Arrays, Objects, and Small Data Models

**Guiding question:** Paano hahawak ng maraming orders nang maayos?

**Detailed contents**

1. Arrays as collections; length and zero-based indexing.
2. Objects as records; properties and meaningful field names.
3. An array of menu/order records with stable IDs.
4. Iterating records with for...of; keeping index and identity distinct.
5. Introducing find/filter through one familiar selection task.
6. A short callback preview: passing a function for another operation to call.
7. Updating data deliberately and checking a missing record.

**Students should demonstrate:** model a small menu and select an affordable item.

**Guided activity:** Budget-friendly canteen menu. **Remix:** add a dish and filter by budget. **Evidence:** normal, no-match, and duplicate-title cases. **Extension:** map/reduce after the loop-based solution is clear.

**Prerequisites:** M03–M04. **Source basis:** R5.

## 4. Midterm — Making programs respond to events

### M06 — TypeScript Bridge and Safe Data

**Detailed contents:** JavaScript versus TypeScript; static checking versus execution; inference and annotations; typed parameters and returns; object types and arrays; simple unions; unknown input and narrowing; explicit setup/build/check commands for the chosen runtime.

**Students should demonstrate:** identify a type error and separately reject invalid runtime data.

**Guided activity:** Typed canteen order record. **Remix:** add a valid status field and reject an unsupported status. **Evidence:** a corrected type-check result and normal/invalid data tests. **Extension:** typed event payloads; advanced generics are deferred.

**Prerequisite:** M05. **Source basis:** R6. Browsers require an appropriate JavaScript output/build route; the lesson must not imply they execute arbitrary TypeScript directly.

### M07 — Events, Callbacks, Handlers, and Remembered State

**Detailed contents:** source/event/handler/registration; passing a function versus calling it; minimal supplied HTML shell; selecting elements and checking their presence; click listeners; a small state variable; named callbacks; a closure that remembers its own counter; handler registration lifetime.

**Students should demonstrate:** trace input → handler → state → displayed output.

**Guided activity:** Campus help-request counter. **Remix:** create a second independent counter and Reset. **Evidence:** independent values with no accidental duplicate registration. **Extension:** factory function for counters.

**Prerequisites:** M04–M06. **Source basis:** R7–R8. An event-driven handler can execute synchronously.

### M08 — DOM Input, Forms, and Validation

**Detailed contents:** event object and type; input/change/submit; reading text values; conversion and validation; visible labels; native keyboard operation; preventDefault for the form's default action; rendering useful feedback; separating input capture from a pure calculation function.

**Students should demonstrate:** submit valid data by button or Enter and recover from an invalid field.

**Guided activity:** Canteen order form. **Remix:** quantity limits and a clear action. **Evidence:** no unwanted reload, valid total, and corrective error messages. **Extension:** live feedback while typing.

**Prerequisites:** M06–M07. **Source basis:** R7, R9.

### M09 — Propagation, Delegation, and Listener Cleanup

**Detailed contents:** capture/target/bubble; target versus currentTarget; matching an actionable ancestor; one delegated listener for dynamic rows; safe DOM narrowing; preventDefault versus stopPropagation; same-reference removal and capture matching; once and signal as listener options.

**Students should demonstrate:** handle a newly added row through its parent and remove the intended listener.

**Guided activity:** Dynamic errands board with delegated delete buttons. **Remix:** a completed action using the same parent listener. **Evidence:** nested button content works and repeated setup does not duplicate reactions. **Extension:** AbortController-based shared cleanup.

**Prerequisites:** M07–M08. **Source basis:** R7–R9. Do not present all events as bubbling events.

### M10 — Execution Order, Timers, and the Event Loop

**Detailed contents:** synchronous call stack; host scheduling; a timer callback; delay as a scheduling threshold rather than an exact appointment; microtask introduction through a teacher-provided promise example; predictable logging; start/stop timer controls; clearTimeout/clearInterval; long synchronous work and responsiveness.

**Students should demonstrate:** explain a short output trace and stop work they started.

**Guided activity:** Study countdown or reaction timer. **Remix:** prevent duplicate starts and reset safely. **Evidence:** repeatable start/stop behavior and a simple ordering explanation. **Extension:** browser versus Node scheduling comparison after naming the runtime/module format.

**Prerequisite:** M09. **Source basis:** R10. Promise syntax is previewed here and explained in M11; do not require constructing promises for this module's core exercise.

### M11 — Promises and Expected Failures

**Detailed contents:** pending/fulfilled/rejected; one settled outcome; then/catch/finally; returning chained work; simulated asynchronous completion; successful versus unsuccessful operations; avoiding unhandled rejections; cleanup regardless of outcome.

**Students should demonstrate:** trace success and failure through a promise chain.

**Guided activity:** Simulated milk-tea preparation. **Remix:** reject an unavailable item and show recovery advice. **Evidence:** both outcomes end in a clear UI/log state. **Extension:** Promise.all/allSettled overview; implementation moves to M12.

**Prerequisite:** M10. **Source basis:** R11. The simulation must be labeled; it is not a real API.

## 5. Pre-final — Async applications and dependable event systems

### M12 — Async/Await and Concurrent Work

**Detailed contents:** async functions return promises; await pauses the current async function; try/catch/finally; translating the familiar chain; independent sequential versus concurrent requests; Promise.all; a brief partial-failure comparison with allSettled; concurrency versus CPU parallelism.

**Students should demonstrate:** implement an awaited success/failure path and explain a timing trace.

**Guided activity:** Load simulated menu and campus notices. **Remix:** compare sequential and concurrent starts. **Evidence:** correct results and handled failure, with no claim that Promise.all automatically cancels siblings. **Extension:** allSettled result rendering.

**Prerequisite:** M11. **Source basis:** R11–R12.

### M13 — Fetch, JSON, and Trust Boundaries

**Detailed contents:** client/server request and response; GET and a small fixture endpoint; HTTP status checks; JSON parsing; payload shape validation; loading/success/empty/error states; retry as a user action; safe text rendering; missing network/local fixture fallback.

**Students should demonstrate:** distinguish an HTTP failure from valid data and reject malformed payloads.

**Guided activity:** Campus announcement loader. **Remix:** category selection and retry. **Evidence:** normal, empty, unsuccessful-response, and malformed-data results. **Extension:** a teacher-provided local Node fixture service, not student deployment infrastructure.

**Prerequisites:** M06, M12. **Source basis:** R13.

### M14 — Cancellation, Stale Results, and Event Frequency

**Detailed contents:** older requests completing later; cancellation versus ignoring stale results; AbortController/signal; checking already-aborted signals in wrappers; expected abort handling; debounce as waiting for a pause; cleanup of pending timers; throttle as a contrasting policy.

**Students should demonstrate:** prevent an older search from overwriting a newer result.

**Guided activity:** Campus directory search with deliberately varied delays. **Remix:** add a debounced trigger after the stale-result guard works. **Evidence:** deliberate slow-old/fast-new case and cleanup on reset. **Extension:** throttle comparison and timeout composition. These are multiple techniques; the core exercise prioritizes one guarded search flow.

**Prerequisites:** M09, M12–M13. **Source basis:** R8, R14.

### M15 — Custom Events and Publish/Subscribe

**Detailed contents:** producer/subscriber separation; CustomEvent detail payload; EventTarget registration and dispatch; one event with multiple subscribers; stable event names; payload checking; synchronous dispatch; unsubscribe; event notification versus command/request terminology.

**Students should demonstrate:** add and remove independent reactions without changing the publisher.

**Guided activity:** Canteen order-added bus updating a count and activity log. **Remix:** add a subscriber, then dispose it. **Evidence:** only active subscribers react. **Extension:** a simple typed event map; declaration merging and generic emitter libraries remain advanced references.

**Prerequisites:** M06, M09, M12. **Source basis:** R15. Distinguish browser dispatch exception behavior from Node's behavior.

### M16 — Node.js EventEmitter and Runtime Differences

**Detailed contents:** Node program entry and module format; absence of browser document/window; EventEmitter on/emit/once/off; synchronous dispatch and listener order; ignored return values; error event handling; async listener rejection policy; listener counts and cleanup; comparison with browser EventTarget.

**Students should demonstrate:** run and explain a complete small Node emitter program.

**Guided activity:** Order-status broadcaster. **Remix:** add a once-only notification and remove another listener. **Evidence:** expected event log and a deliberate error path. **Extension:** captureRejections with its documented behavior; nextTick/setImmediate details are teacher reference.

**Prerequisites:** M11–M12, M15. **Source basis:** R16. Do not use undefined handler identifiers or claim emit awaits async handlers.

### M17 — Persistent State, Transitions, and Recovery

**Detailed contents:** explicit state and valid transitions; pure state-update function; events versus stored state; localStorage save/load; JSON serialization; validating restored data; missing/corrupt data; duplicate action handling; app reset and listener lifetime; client storage limitations and minimal personal data.

**Students should demonstrate:** restore a valid checklist and reject an impossible transition or invalid saved record.

**Guided activity:** Save-and-resume campus task board. **Remix:** a clear-all confirmation and recovery message. **Evidence:** reload persistence, invalid JSON recovery, and no doubled handlers. **Extension:** a short in-memory job queue or idempotent completion rule; no distributed database is required.

**Prerequisites:** M05–M06, M09, M15. **Source basis:** R6, R8, R17.

### M18 — Testing, Debugging, and Solo Project Integration

**Detailed contents:** reproducible bug reports; normal/boundary/failure cases; assertions for pure transition functions; a small Node test-runner example; event logs; expected versus actual order; testable scheduling through injected dependencies where needed; review of cleanup and invalid payloads; individual project scope, event-flow sketch, and acceptance criteria.

**Students should demonstrate:** test one rule, diagnose one event bug, and propose a manageable solo project.

**Guided activity:** Repair a task/order board and test its transition rule. **Remix:** add a regression case. **Evidence:** passing meaningful tests and a short personal project plan. **Extension:** a simulated real-time feed or worker demonstration only if time remains; neither becomes a final-project requirement.

**Prerequisites:** M12–M17. **Source basis:** R18 and prior topics. This is the flexible integration unit when class dates are limited. Summative assessment remains separate.

## 6. Finals — Two preparation modules only

### M19 — Review and Mock Practical Rehearsal

**Detailed contents:** revisit event flow, state, async operations, validation, and cleanup; read a rubric; run a familiar starter; identify a broken handler or stale result; practice a small timed modification; prepare the final summative; check the student's own acceptance criteria.

**Students should demonstrate:** independently trace and repair a familiar program.

**Activity:** an individual mock practical using previously taught techniques. **Evidence:** repaired behavior, a short explanation, and a list of remaining project issues. Provide feedback before the final assessment. No new advanced library or infrastructure is introduced.

**Prerequisites:** taught portions of M01–M18. **Source basis:** course synthesis.

### M20 — Solo Project Readiness and Troubleshooting

**Detailed contents:** test the individual's project; rehearse normal/failure/recovery flows; verify setup instructions; identify simulations and limitations; review source attribution; prepare code walkthrough and troubleshooting demonstration; package files and test instructions.

**Students should demonstrate:** launch their own work, explain a key event sequence, and diagnose a known failure.

**Activity:** personal readiness check and final demonstration rehearsal. **Evidence:** runnable individual project, concise README, test evidence, and honest limitations. The actual final practical exam uses its institution-assigned slot and is not counted as this module.

**Prerequisite:** M19 and the student's developing project. **Source basis:** course synthesis.

## 7. Short-schedule grouping options

Prepared module numbers remain stable even if related sections are taught together. Record what was actually delivered and adapt assessment coverage accordingly.

| Situation | Possible grouping | What to protect |
| --- | --- | --- |
| Only four Prelim content meetings | M01 + M02: short opening, one budget program introducing values and decisions | Keep dedicated loop and function practice; retain M05's collections introduction |
| Only five Midterm content meetings | M07 + M08: one supplied form demonstrates registration, input, and response | Keep TypeScript bridge, delegation/cleanup, runtime model, and promise basics accessible |
| Pre-final loses a meeting | M17 + selected M18: test the same saved-state transition function | Reduce optional features, provide prepared test setup, begin project proposal earlier |
| More time is available in Pre-final | Expand M18's integration activity over an extra meeting or use one optional survey | Do not relabel this as a mandatory 21st module |

A combined meeting uses a reduced core, not two complete 60–90-minute lessons. The instructor may instead move material to another available day. Independent reference work is not silently counted as a formal class session.

## 8. Advanced topics retained from the research

| Collected topic | Placement and reason |
| --- | --- |
| Web Workers / worker_threads | Optional responsiveness survey after M10/M18; additional setup and messaging concepts |
| SSE / WebSocket / BroadcastChannel / postMessage | Optional external-event survey after local event patterns; label simulations and validate messages |
| Async iterators, Node streams, backpressure | Teacher/reference extension after M16; avoid complex buffering wrappers in core starters |
| RxJS and marble testing | Advanced reference; plain callbacks/promises first |
| Generic typed emitter library | Advanced TypeScript extension after M15–M16; simple typed records suffice for core |
| Kafka, RabbitMQ, Redis Streams, cloud event services | Future distributed-systems study; no required broker setup |
| Event sourcing, CQRS, sagas, outbox/inbox, delivery guarantees | Architecture survey; distinct from basic event-driven programming |
| Distributed tracing and OpenTelemetry | Future observability topic; ordinary event logs suffice for this semester |

These preserve the breadth of the Gemini/Grok/Claude material without claiming that all of it fits a beginner semester. Imported AI reports remain idea sources; their code and production claims require verification.

## 9. Source map for lesson authoring

References below were inspected in the preceding research passes. The table maps coverage to primary sources; it does not claim a new exhaustive audit of each page or its examples.

| Ref | Sources | Main modules |
| --- | --- | --- |
| R1 | [MDN grammar and types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types) | M01 |
| R2 | [MDN control flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling) | M02 |
| R3 | [MDN loops](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration) | M03 |
| R4 | [MDN functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions) | M04–M05 |
| R5 | [TypeScript everyday types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html), [CMU JavaScript lab](https://dig.cmu.edu/datavis-fall-2024/labs/3/) | M05; exact Array API pages to check with the selected code |
| R6 | [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html), [Node TypeScript execution](https://nodejs.org/api/typescript.html) | M06, M17 |
| R7 | [MDN introduction to events](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events) | M07–M09 |
| R8 | [addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener), [removeEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/removeEventListener) | M07, M09, M14, M17 |
| R9 | [MDN events guide](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events) | M08–M09; check individual form/propagation APIs when writing code |
| R10 | [MDN execution model](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model), [Node event loop](https://nodejs.org/learn/asynchronous-work/event-loop-timers-and-nexttick) | M10; runtime-specific comparison |
| R11 | [MDN using promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) | M11–M12 |
| R12 | [MDN await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await), [allSettled](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled) | M12 |
| R13 | [MDN Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) | M13 |
| R14 | [MDN AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) | M14; debounce/throttle implementations need explicit policy tests |
| R15 | [CustomEvent](https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent), [dispatchEvent](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/dispatchEvent) | M15 |
| R16 | [Node Events](https://nodejs.org/api/events.html), [Node microtask/nextTick comparison](https://nodejs.org/api/process.html#when-to-use-queuemicrotask-vs-processnexttick) | M16 |
| R17 | [MDN localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) | M17 |
| R18 | [Node test runner](https://nodejs.org/api/test.html) | M18 |

For university PDF references and access limitations, use the [online collection](../Modern_2026_Course_Pack/ONLINE_SOURCE_COLLECTION.md). For all six imported AI reports, use the [research hub](research/README.md). Their advanced topic suggestions are represented in section 8; inaccurate generalizations are covered in the [technical review](research/TECHNICAL_REVIEW.md).

## 10. Requirements before calling the course complete

Each lesson will need a full explanation, natural Taglish support, measurable targets, exact file/run instructions, complete starter code, expected result, code trace, independent modification, troubleshooting, and direct references. Console examples must run; TypeScript must type-check; browser activities must be exercised; failure and cleanup behavior must be checked. Record the actual dependency baseline and any unverified platform behavior.

This compiled table of contents supersedes the earlier EDP 17- and 23-module inventories. ADET's content count is not changed by this EDP-only compilation. Actual period dates and assessment requirements still come from the institution and instructor.
