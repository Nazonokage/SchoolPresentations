# EDP quiz answer key (INSTRUCTOR ONLY)

Do not include this file in the student pack. Answers are model answers: accept any response with the same idea. Item numbers match the current module files.

## M01: Foundations (10 items)

1. It reacts to a reported occurrence: it runs when the event is dispatched and receives the payload.
2. A command requests an action and can be rejected (`prepareOrder`); an event reports something that already happened (`order.created`).
3. 1000.
4. 60.
5. false (40 is less than 60).
6. A, C, B. The timer callback runs after the current synchronous code, even with a 0 ms delay.
7. `show()` runs immediately and its return value (probably `undefined`) is passed to `setTimeout`. Pass `show` or `() => show()`.
8. No. A timer cannot run until the thread is free, and a delay is a minimum, not an exact time.
9. Observer or Pub/Sub: publish one `order.created` event with separate kitchen and invoice listeners.
10. Keep the handle returned by `setTimeout` and call `clearTimeout(handle)` before it runs.

## M03: DOM events (10 items)

1. A callback (handler) for one event type on that element, to run when the event happens.
2. `textContent` (or a text node), not `innerHTML`.
3. No. `preventDefault` cancels the default action; `stopPropagation` stops propagation.
4. “Hello, coder!” in `m03.html` (the first page `m03-first.html` shows “Hello, coder! Kaya mo ito.”).
5. No. The trimmed text is empty, so the page shows “Enter a food name.” and adds no row.
6. Yes, with event delegation: the listener is on the parent list and uses `event.target.closest(...)`.
7. A misspelled ID, or the script ran before the element existed.
8. It is a different function object, so it does not match the registered one. Removal needs the same reference (and the same capture option).
9. The form’s `submit` event.
10. One `AbortController`: pass its `signal` to every listener and call `abort()` when the screen is destroyed.

## M05: Async patterns (10 items)

1. A quiet period after the last input before it runs the work.
2. No. Aborting is cooperative and cannot undo work the server already committed.
3. `Promise.allSettled`.
4. No. Result 1 is stale and is ignored.
5. “canteen”.
6. No. `Promise.all` rejects, but the other operations keep running unless they are cancelled.
7. Create a new `AbortController` for each request.
8. `fetch` rejects mainly on network failure; an HTTP 404 still resolves, so check `response.ok`.
9. No. Start both and await them together (`Promise.all` or `allSettled`).
10. Ignore it (and ideally abort it) by checking the request ID before displaying anything.

## M07: Patterns and state machines (10 items)

1. A condition checked before a transition is allowed (for example, payment received).
2. The collaboration rules between participants.
3. An accepted fact. A request would be a command such as `createOrder`.
4. It is rejected (“Rejected: collect in waiting”) and the state stays `waiting`.
5. `ready`.
6. It is rejected (“Rejected: collect in collected”); `collected` is terminal.
7. Independent flags allow impossible combinations (ready and cancelled together). One explicit state makes them visible.
8. Disabling a button is not a security boundary. The server must validate transitions itself.
9. Only after the prepare command was accepted and the transition happened.
10. Use specific event names, documented payloads and clear owners, or split the bus into narrower topics; keep a list of who handles what.

## M09: Real-time channels (10 items)

1. Server to client.
2. No. Socket.IO has its own protocol and handshake.
3. `text/event-stream`.
4. The server replies with an error message (“text must be a string”) and the connection stays open. Messages are just data: shape must be validated on both sides.
5. The stream closes, the status shows “Disconnected” and no new rows appear (the server clears that connection’s timer when the request closes).
6. No. The counter restarts and there is no history or `Last-Event-ID` replay.
7. A `file://` page has the wrong origin, so `/events` does not reach the server. Use `http://127.0.0.1:4173/m09.html`.
8. Valid JSON can still have the wrong shape or hostile content. Validate fields and render with `textContent`.
9. SSE (server-sent events).
10. Check `event.origin` and `event.source`, validate the payload shape, and use a specific `targetOrigin` when sending.

## M11: Testing (10 items)

1. A check that a result equals the expected value; the test fails otherwise.
2. An integration test exercises real components together; a unit test isolates one piece.
3. To stop listeners and state leaking from one test into another.
4. Once.
5. `['first:A1', 'once:A1']`.
6. No. `assert.throws` passes when the expected error is thrown.
7. The test can finish before the failure happens, so the failure is missed or reported later.
8. It is slow and still flaky on a busy machine. Wait for the event or promise instead.
9. After removal, emit again, assert the listener was not called, and assert `listenerCount` is 0.
10. Mutation check: temporarily remove the cleanup call, confirm the test fails, then restore it.

## M13: Delivery guarantees (10 items)

1. At-least-once.
2. Repeating the operation does not create an additional unintended effect.
3. To hold messages that could not be processed so they can be inspected, repaired and deliberately replayed.
4. 60.
5. It is added to the dead-letter list and `consume` returns; the total does not change.
6. The broker redelivers because there was no acknowledgment. The consumer must detect the duplicate.
7. It is lost on restart and not shared between processes.
8. If the consumer crashes after acknowledging but before doing the work, the work is lost.
9. Malformed input needs correction (reject or dead-letter, do not retry endlessly). A temporary outage can use bounded retries with backoff and jitter.
10. An atomic, durable deduplication record (for example a unique constraint committed in the same transaction as the effect).

## M15: Event sourcing (10 items)

1. The accepted sequence of domain events.
2. A read-oriented view derived from events.
3. Derived state at a known sequence, so replay can resume after it.
4. 8.
5. 8.
6. No. The same history gives the same result.
7. Replay would resend the email every time. Replay should only compute state.
8. A log may be incomplete, unstructured or rotated, so it cannot reliably rebuild state.
9. An expected-version (optimistic concurrency) check when appending.
10. No. Plain current-state storage is often clearer; use event sourcing when history, audit or several projections justify the cost.

## M17: Observability, security, resilience (10 items)

1. The related events and actions that belong to one workflow.
2. A metric aggregates measurements (counts, durations); a log records one occurrence.
3. No. It is context for tracing, not authentication.
4. Accepted (authorized).
5. Rejected with the reason “not owner”.
6. accepted 1, rejected 1.
7. The client could claim any identity. The actor must come from a verified session or equivalent.
8. Logs are copied and read widely; a leaked token is a breach. Log minimal or redacted data.
9. Age of the oldest pending message (and processing latency).
10. Timeouts, bounded retries with backoff, a circuit breaker (in `m17-resilience.mjs` it opens after two failures and skips calls), bulkheads, a dead-letter or manual-review path, alerts and graceful degradation.

## M19: Finals review (10 items)

1. A promise is one eventual outcome; an event stream is repeated notifications.
2. No. Interfaces exist only at compile time; fetched JSON needs runtime validation.
3. The dual-write problem: it records the business change and the pending event together so the event is not lost.
4. A, C, B.
5. 1.
6. The second `ready` throws “Invalid transition”; the order stays `ready`.
7. `handle()` calls the function immediately and registers its return value, not the function.
8. A new wrapper is a different function, so `off` does not match the original handler.
9. A trace or test showing `listenerCount` is 0 and no reaction occurs after removal.
10. State plainly that it is in-memory and loses data on restart; do not call it durable.

## M20: Applied quiz (20 items) and essays

| # | Model answer | From |
| ---: | --- | --- |
| 1 | The handler was called (`handle()`) instead of passed (`handle`), so it ran at registration. | M01, M03 |
| 2 | The synchronous log. | M02 |
| 3 | It is cancelled and its callback will not run (unless it already ran). | M01 |
| 4 | Register separate listeners on one event; the order code should not call both. | M04 |
| 5 | Synchronous listeners run inside `emit`, so `emit` does not return (and the thread is blocked) until it finishes. | M04 |
| 6 | Duplicate registration: check `listenerCount`, guard the setup, use `off`/`once`. | M03, M04 |
| 7 | Event delegation: a listener on the parent using `event.target.closest(...)`. | M03 |
| 8 | Submit covers both clicking the button and pressing Enter. | M03 |
| 9 | Compare the request ID or token with the latest before displaying (and abort the old one). | M05 |
| 10 | Debounce. | M05 |
| 11 | Runtime validation of the data (a guard or schema). | M06 |
| 12 | Reject the command: no state change and no fact emitted. | M07 |
| 13 | Unsubscribing (`subscription.unsubscribe()` or an equivalent teardown). | M08 |
| 14 | SSE. | M09 |
| 15 | Backpressure: pause on `write()` returning false and resume on `drain`, or use `pipeline`. | M10 |
| 16 | A work queue (competing consumers). | M12 |
| 17 | An idempotency or operation ID with durable, atomic deduplication. | M13 |
| 18 | So the business change and the pending event commit together, leaving no dual-write window. | M14 |
| 19 | Replay would repeat side effects; the reducer should be pure. | M15 |
| 20 | Emit after removal and assert the listener was not called and `listenerCount` is 0 (ideally with a mutation check). | M11 |

**Essay 1 (5 points)** looks for: a named producer, payload, two reactions and a state rule (2); one accepted and one rejected trace (1); which reaction is synchronous and how cleanup is proven (1); specifics from the student’s own project (1).

**Essay 2 (5 points)** looks for: duplicate registration shows one delivery (one receive or emit line) triggering the handler twice, with `listenerCount` above expected; redelivery shows two separate deliveries of the same event ID with a normal `listenerCount` (2); the repair matches the cause: remove the extra registration or deduplicate by ID (1); a repeatable test (1); clarity (1).
