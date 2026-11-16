> **Current EDP plan:** [compiled contents: 20 modules](../compiled%20contents.md), split 5 / 6 / 7 / 2 with flexible grouping. This supersedes the earlier 17-module allocation below.

# EDP research synthesis and scope

[Research home](README.md)

## Agreed teaching constraints

Prepare a 17-module EDP inventory: 4 Prelim, 5 Midterm, 6 Pre-final, 2 Finals. Meetings occur twice weekly, last 60–90 minutes, and exclude Saturdays. One teaching module uses one day. Summative exams precede each periodical exam and occupy separate slots. Finals modules are review/preparation for an individual practical project.

The first four modules establish variables, conditionals, loops, and functions, with introductions and a motivating demonstration in the opening. Arrays/objects and a clear TypeScript bridge must precede code that depends on them. The later allocation remains provisional: the calendar may not allow six Pre-final teaching days. Preserve M15 as a flexible integration/rehearsal unit without introducing a dependency required for Finals.

## What the reports contribute

| Material | Useful contribution | Scope caution |
| --- | --- | --- |
| Earlier Grok research reports | Refresher, campus examples, period/exam constraints | Source and version claims require verification |
| Supplied JS/TS course | Rich DOM/EventEmitter examples, cancellation, typed payloads | Assumes functions, closures, and promises; some code has lifecycle/typing issues |
| Production masterclass paste | Topic inventory for reactive and distributed systems | Begins too advanced and ends with an unsuitable multi-service capstone |
| Fundamentals-to-architecture paste | Events/commands vocabulary, duplicate handling, reliability ideas | Generalizes distributed-system properties to all event-driven code |
| Official MDN/Node/TypeScript references | Exact runtime/API behavior and type checking | API references need teacher-designed explanations and examples |
| University PDF references | Visual explanations of sources, handlers, and callbacks | Java/pseudocode must be translated carefully; licenses remain unverified |

## Deduplicated topic bank

| Priority | Research topics | Appropriate learning evidence |
| --- | --- | --- |
| Required foundations | Variables, data types, conditions, loops, functions, arrays/objects, TypeScript basics | Predict, run, trace, and modify a small console program |
| Core EDP | Sources/handlers, registration, DOM input/forms, event objects, delegation | Interactive browser board using provided HTML/CSS |
| Core async | Runtime ordering, timers, promises, async/await, expected failures | Trace logs and demonstrate success/failure without blocking input |
| Core reliability | Listener cleanup, payload validation, stale results, simple testing | Repeat interactions without duplicate handlers; test invalid data |
| Small extension | CustomEvent or EventEmitter, debounce, cancellation, simple queues | One bounded example after its prerequisites |
| Teacher survey / optional | Workers, SSE/WebSocket, async iterators, streams/backpressure | Explain the need, optionally demonstrate a small isolated behavior |
| Advanced archive | RxJS, Kafka, RabbitMQ, event sourcing, CQRS, sagas, outbox, tracing infrastructure | Future learning only; no required installation or solo final-project dependency |

This is a topic bank, not a requirement for a separate module per row or technique. There are only 11 numbered teaching units after Prelim and before the two Finals preparation units. Do not attempt to fit every imported topic into them.

## Explanations to preserve

Teach event-driven programming through the relationship between a source, a registration, a handler, and changed state. Event-driven architecture adds concerns of systems and communication boundaries; a browser counter does not require a broker, eventual consistency, or an append-only event store.

A promise represents a single eventual outcome; event sources may deliver multiple notifications. Both can appear in the same program. A direct function call or request/response operation can also exist inside an event-driven application. These are compatible techniques, not mutually exclusive labels.

Past-tense event names are useful for domain facts such as orderCreated. Browser event names such as click and input follow the API; an application need not rename them. Payload immutability should be an explicit design choice, not asserted as a property enforced by all JavaScript event APIs.

## Activity bank

- Baon checker for variables and branches.
- Study-session counter for loops and function return values.
- Canteen order form for input, validation, and submit handling.
- Dynamic errands board for event delegation and stable IDs.
- Simulated order preparation for promises and async/await.
- Campus directory search for stale results, debounce, and cancellation.
- Local order-status broadcaster for CustomEvent or EventEmitter.

Choose one manageable solo final product, such as a campus task/order board. It should show user events, a small state model, an async operation, validation, cleanup, and failure recovery. Keep the HTML shell available and the backend optional. No React frontend, broker cluster, distributed payment flow, or cloud service is required.
