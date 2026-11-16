> **Updated pacing decision:** 17 modules per subject, split 4 Prelim / 5 Midterm / 6 Pre-final / 2 Finals. This document retains the earlier research inventory; see [current pacing](../Modern_2026_Course_Pack/AGREED_PACING.md).

# EDP: research inventory before module authoring

Updated 2 November 2026. [Consolidated research](../Modern_2026_Course_Pack/RESEARCH_DOSSIER.md) | [Calendar analysis](../Modern_2026_Course_Pack/CALENDAR_AND_CAPACITY.md)

This is a proposed 23-topic inventory, not completed lessons or an assigned timetable. The 7/7/7/2 grouping preserves two Finals preparation modules; actual available teaching dates remain insufficient for some or all period allocations. Resolve the calendar gap before promising a dated syllabus. One module uses one teaching day; summatives and periodicals have separate slots.

The first six units deliberately establish the language foundations. Each subject teaches its own refresher even when students take both. ADET uses console exercises before introducing mobile tooling; EDP then applies the same language to browser and Node events.

| Unit | Proposed period | Research topic | Guided activity candidate | Evidence of understanding |
| --- | --- | --- | --- | --- |
| 01 | Prelim | Variables, constants, types, and operators | Baon balance calculator | Predict number versus string output; change one expense |
| 02 | Prelim | Conditionals and decisions | Fare/meal eligibility checker | Test boundaries, equality, and an invalid choice |
| 03 | Prelim | Loops and repeated work | Print a five-day study plan | Trace the counter and stop condition; avoid infinite loops |
| 04 | Prelim | Functions, parameters, and return values | Reusable order-total function | Call it with different inputs; distinguish return from console output |
| 05 | Prelim | Arrays, objects, and data modeling | Small canteen menu | Select an affordable meal; keep stable item identifiers |
| 06 | Prelim | TypeScript bridge and runtime checks | Typed budget or order records | Show a type error, then validate an unknown input separately |
| 07 | Prelim | Events, handlers, callbacks, and closures | Independent click counters | Register functions; trace which state each closure remembers |
| 08 | Midterm | DOM forms, propagation, and delegation | Dynamic canteen order board | Prevent unwanted submission; distinguish target/currentTarget |
| 09 | Midterm | Execution model, tasks, microtasks, and timers | Output-order tracing lab | Explain synchronous output before queued callbacks |
| 10 | Midterm | Promises and rejection handling | Simulated order preparation | Return chained work and handle deliberate failure |
| 11 | Midterm | Async/await and concurrent work | Two simulated campus data requests | Compare sequential versus concurrent independent operations |
| 12 | Midterm | Fetch, validation, and cancellation | Campus directory search | Check status/schema; cancel supported work or reject stale results |
| 13 | Midterm | Debouncing, throttling, and timer cleanup | Search request counter | Choose a timing policy and clean up pending timers |
| 14 | Midterm | Custom events and pub/sub | Class announcement bus | Publish a payload, subscribe twice, and remove one subscriber |
| 15 | Pre-final | Node.js EventEmitter and runtime differences | Order-status emitter | Trace synchronous dispatch; handle errors and remove listeners |
| 16 | Pre-final | Persistence and listener lifetime | Save-and-resume checklist | Recover invalid JSON; prevent duplicate subscriptions |
| 17 | Pre-final | Testing event-driven rules | Queue-state transition tests | Test repeatable event outcomes without fragile real-time sleeps |
| 18 | Pre-final | Queues, state transitions, and recovery | Sequential print-job simulator | Reject impossible transitions and avoid duplicate completion |
| 19 | Pre-final | Real-time patterns and external event sources | Simulated live campus board | Label local simulation; compare SSE/WebSocket as extensions |
| 20 | Pre-final | Security, validation, and reliable handlers | Audit and repair an event payload flow | Handle expected failures locally; document trust boundaries |
| 21 | Pre-final | Solo project kickoff and integration checkpoint | Individual event-flow diagram and prototype | Identify events, state, async work, cleanup, and recovery |
| 22 | Final | Finals review and practical rehearsal | Repair duplicate handlers or a stale response | Apply established patterns with an event log |
| 23 | Final | Finals project readiness and troubleshooting | Individual reliability rehearsal | Demonstrate normal, failure, recovery, and cleanup behavior |

## Depth and source policy

Use a 60-minute core and optional 30-minute extension. One row may name related concepts, but its final lesson must select one small guided behavior. Broader API coverage remains teacher reference. Use the dossier's source map to retrieve exact technical details when writing.

For early units, give a single complete console file and an output trace. For later units, provide the smallest complete runnable program appropriate to the runtime. Do not assume a previous lab was completed correctly. Each activity needs a normal case, an edge/failure case, and an independent modification.

Scope reductions and optional demonstrations do not create more class days. The proposed numbering supersedes the older outlines for discussion, but is still subject to instructor review after the timetable is assigned.
