# EDP instructor answer key and scoring guidance

Prepared 3 November 2026. Distribute student module files separately from this instructor folder. Each odd-module quiz has exactly 10 items, one point each. Accept equivalent technically correct wording; give item-level feedback. Items 1–3 check concepts, 4–6 traces, 7–8 diagnosis, 9–10 application. Module 1 is diagnostic; actual grade weighting follows institutional policy.

## Module 01

1. **It reacts to an occurrence reported by a producer or dispatcher.**
2. **A command requests an action; an event reports something that happened.**
3. **1000.**
4. **60.**
5. **false, because 40 is less than 60.**
6. **A, C, B. The timer does not interrupt the current statements.**
7. **It calls show immediately and passes its return value instead of a callback.**
8. **No. The loop occupies the thread and prevents the callback from running.**
9. **Observer or Pub/Sub with two reactions and a documented payload.**
10. **Keep its returned handle and pass that handle to clearTimeout.**

## Module 02 — coding observation guide

Expected starting trace: A → B → C → D → Ready: A1 → Handled: Unavailable: A2 → Preparation finished. The numerical timer delays are not exact wall-clock promises.

Required student change: Add a successful A3 preparation after the handled failure by giving it its own try/catch scope. Explain why a statement after the rejecting await inside the original try does not run.

Award using the module rubric. Require a live explanation or a brief code walkthrough; screenshots alone do not prove the independent change. Do not penalize equivalent correct implementations. Teacher reference code is a starting point, not the completed student task.

## Module 03

1. **A callback for an event type on a target.**
2. **textContent.**
3. **No. Default action and propagation are separate concerns.**
4. **Hello, coder!**
5. **No. trim produces an empty string and the handler returns.**
6. **Yes. Its bubbling click reaches the delegated parent listener.**
7. **A wrong ID or running the script before that element exists.**
8. **It is a different function reference.**
9. **The form submit event.**
10. **Register them with a shared AbortSignal and abort its controller on disposal.**

## Module 04 — coding observation guide

Expected starting trace: A1 produces Invoice, Kitchen, First order bonus. A2 produces Kitchen only. The printer error is handled, Ready prints A2, and Remaining prints 0.

Required student change: Add an independent inventory listener, remove it after A1, and prove it does not run for A2. Keep the deliberate printer failure handled.

Award using the module rubric. Require a live explanation or a brief code walkthrough; screenshots alone do not prove the independent change. Do not penalize equivalent correct implementations. Teacher reference code is a starting point, not the completed student task.

## Module 05

1. **A quiet interval without another triggering input.**
2. **No. Cancellation is cooperative and cannot automatically undo committed effects.**
3. **Promise.allSettled.**
4. **No. Its request number is stale.**
5. **canteen.**
6. **No. It rejects, but cancellation requires separate support.**
7. **Create a fresh controller/signal for the new request.**
8. **fetch can fulfill with an HTTP error response; inspect response.ok/status.**
9. **No. Start both and await their results together when safe.**
10. **Cancel it when supported and retain a latest-request check before applying its result.**

## Module 06 — coding observation guide

Expected starting trace: Invoice: A1 60; Bad payload accepted: false. A3 prints no invoice because the listener was removed.

Required student change: Add a string reason to order.cancelled and a listener that displays it. Demonstrate one valid call, one intentionally invalid compile-time call (comment it afterward), and one invalid runtime payload.

Award using the module rubric. Require a live explanation or a brief code walkthrough; screenshots alone do not prove the independent change. Do not penalize equivalent correct implementations. Teacher reference code is a starting point, not the completed student task.

## Module 07

1. **A condition that must hold before allowing a transition.**
2. **Coordination among participating components.**
3. **An accepted fact/event, if the name is used honestly.**
4. **It is rejected and state stays waiting.**
5. **ready.**
6. **It is rejected in collected.**
7. **They can represent contradictory combinations unless extra rules prevent them.**
8. **Clients can be bypassed; the server must enforce valid actions too.**
9. **After accepting the command and establishing the corresponding state change.**
10. **Use focused topics, documented contracts/owners and traceable handler registration.**

## Module 08 — coding observation guide

Expected starting trace: Results: CANTEEN → Handled: Search unavailable → Search subscription closed. The c and ca prefixes are suppressed.

Required student change: Normalize terms with trim/lowercase before distinctUntilChanged, then show that equivalent consecutive terms do not produce repeated searches. Keep the error recovery and unsubscribe.

Award using the module rubric. Require a live explanation or a brief code walkthrough; screenshots alone do not prove the independent change. Do not penalize equivalent correct implementations. Teacher reference code is a starting point, not the completed student task.

## Module 09

1. **Server to client.**
2. **No. Socket.IO has additional protocol behavior.**
3. **text/event-stream.**
4. **A list item containing Order ready 1.**
5. **EventSource closes and new messages stop; status says Disconnected.**
6. **No. The sample has no durable history/resume implementation.**
7. **It lacks the intended HTTP origin; use the supplied local server URL.**
8. **Its shape, meaning, size or authorization may still be invalid.**
9. **SSE is suitable; explain that it streams server updates over HTTP.**
10. **Check the expected origin/source and validate the payload.**

## Module 10 — coding observation guide

Expected starting trace: Saved: ORDER A1 → Saved: ORDER A2 → Saved: ORDER A3 → Pipeline complete. Optional worker: Main thread remains available, then Worker result: 500000500000.

Required student change: Add one fourth record and a deliberate transform error for a chosen record. Verify that failure is reported and success is not falsely printed; document the successful prefix.

Award using the module rubric. Require a live explanation or a brief code walkthrough; screenshots alone do not prove the independent change. Do not penalize equivalent correct implementations. Teacher reference code is a starting point, not the completed student task.

## Module 11

1. **A check comparing observed behavior to an expected contract.**
2. **It checks interaction among actual connected components or boundaries.**
3. **To prevent shared listener/state contamination.**
4. **Once.**
5. **first:A1 followed by once:A1.**
6. **No. The expected failure can make assert.throws pass.**
7. **The test may finish before the asynchronous result or failure.**
8. **It is slow and timing-dependent; an explicit completion signal or controlled clock is more reliable.**
9. **Remove/dispose the listener, emit again and assert no reaction and/or zero owned listeners.**
10. **Temporarily remove that call, confirm the test fails, then restore it.**

## Module 12 — coding observation guide

Expected starting trace: Queue alternates A1–A4 between Kitchen 1 and Kitchen 2. PubSub prints A1 for Invoice and Analytics. Dashboard replays all three events; archive starts at the second.

Required student change: Add a third worker and a third independent subscriber. Give a new replay consumer offset 2. Explain each result and explicitly label the program a local model.

Award using the module rubric. Require a live explanation or a brief code walkthrough; screenshots alone do not prove the independent change. Do not penalize equivalent correct implementations. Teacher reference code is a starting point, not the completed student task.

## Module 13

1. **At-least-once, within its documented assumptions.**
2. **Repeating the same operation does not create an additional unintended effect.**
3. **Retain failed/poison messages for investigation and controlled repair/replay.**
4. **60, because the duplicate is skipped.**
5. **It is moved to the dead-letter array and processing returns.**
6. **The same message may be redelivered.**
7. **It is lost on restart and is not shared atomically with durable business writes.**
8. **A subsequent failure can lose work that the broker already considers handled.**
9. **Reject/quarantine or repair malformed input; bounded retries may help a transient outage.**
10. **Durable atomic deduplication plus the business change, typically with a uniqueness constraint/transaction.**

## Module 14 — coding observation guide

Expected starting trace: Commit cancelled → Received: A1 → Duplicate ignored: event-A1 → Orders: 1 Pending: 0. BAD never enters the committed model.

Required student change: Add a version-2 payload with a different field layout and normalize it explicitly into the same internal order ID. Reject an unsupported version and preserve duplicate detection.

Award using the module rubric. Require a live explanation or a brief code walkthrough; screenshots alone do not prove the independent change. Do not penalize equivalent correct implementations. Teacher reference code is a starting point, not the completed student task.

## Module 15

1. **The accepted domain-event history.**
2. **A derived view/state computed from events for a particular reading purpose.**
3. **Derived state at a known event sequence/version, used to shorten replay.**
4. **8.**
5. **8.**
6. **No. Each rebuild from the same starting state should give the same result.**
7. **Rebuilding state can resend the email; replay should not blindly repeat external effects.**
8. **It may be incomplete, mutable, unstructured or lack reconstruction guarantees.**
9. **Use an expected-version/concurrency check and handle conflict.**
10. **No. Use it when history/reconstruction needs justify its added complexity.**

## Module 16 — coding observation guide

Expected starting trace: A1 is reserved then compensated; A2 is reserved then confirmed. The read model shows cancelled/confirmed, and one reservation remains active.

Required student change: Add a simulated compensation failure that records compensation-pending instead of falsely claiming cancellation. Add a bounded retry or a manual-review record, and explain your choice.

Award using the module rubric. Require a live explanation or a brief code walkthrough; screenshots alone do not prove the independent change. Do not penalize equivalent correct implementations. Teacher reference code is a starting point, not the completed student task.

## Module 17

1. **Related work within a workflow/request context.**
2. **It aggregates measurements rather than describing only one occurrence.**
3. **No.**
4. **accepted.**
5. **rejected, not owner.**
6. **accepted: 1 and rejected: 1.**
7. **The caller can impersonate another actor; the server needs verified identity.**
8. **Logs would expose credentials to additional readers and retention systems.**
9. **Oldest pending message age, with processing latency and failure data as supporting signals.**
10. **Timeouts, limited safe retries and a circuit breaker/controlled recovery rather than unlimited attempts.**

## Module 18 — coding observation guide

Expected starting trace: Repeated ready is handled as Invalid transition; A1 remains ready; Events prints 2; cleanup leaves 0 listeners.

Required student change: Implement one personal feature such as cancellation from waiting or a collected transition from ready. Add a success test and a rejected-transition test, plus an updated diagram.

Award using the module rubric. Require a live explanation or a brief code walkthrough; screenshots alone do not prove the independent change. Do not penalize equivalent correct implementations. Teacher reference code is a starting point, not the completed student task.

## Module 19

1. **One eventual outcome rather than an ongoing sequence of values.**
2. **No; runtime validation remains necessary.**
3. **The failure window between committing business data and recording intent to publish its event.**
4. **A, C, B.**
5. **One.**
6. **The repeated transition is rejected and no extra history event is added.**
7. **It calls the handler immediately and supplies its return value, not the function.**
8. **Listener removal needs the original function identity.**
9. **A test or demonstration showing no later reactions and disposed owned resources/listeners.**
10. **Clearly label in-memory persistence limits, or implement and test durable storage if required.**

## Module 20 · Applied knowledge for the mini-capstone defense

1. The code invoked the handler instead of passing its reference.
2. The synchronous log precedes the scheduled callback.
3. Its pending callback is cancelled.
4. Register two listeners for the same accepted event.
5. It delays the return of emit and later synchronous listeners.
6. Duplicate registrations and lifecycle cleanup.
7. Delegate a bubbling click and identify the matching child.
8. It covers keyboard submission as well.
9. Compare a request ID with the latest one before applying results.
10. Debounce.
11. A runtime shape and business-rule check.
12. Reject the transition without emitting a collected fact.
13. Unsubscribe or use an equivalent lifecycle teardown.
14. Server-sent events with EventSource.
15. Backpressure and bounded buffering.
16. A work queue with competing consumers.
17. Stable operation ID and durable atomic deduplication with the effect.
18. The business change and intent to publish commit together.
19. Replaying history would repeat an external side effect.
20. Emit again and assert the callback count stays unchanged.

**Essays, 5 points each.** Award 2 for accurate subject principles, 1 for a concrete application, 1 for justified reasoning about the failure or alternative, and 1 for observable verification. Accept equivalent well-supported designs.

Essay 1: expect a named event and payload, two independent handlers, an explicit transition guard and post-disposal assertion. Essay 2: distinguish two callbacks on one dispatch from two deliveries of one ID. Expect registration counts or correlated traces and a targeted regression test.

## Module 21 — coding observation guide

Expected starting trace: PASS two orders; PASS first ready; PASS three domain events; PASS listeners cleaned. The separate test suite must also pass.

Required student change: Package your own project with README, event map, tests, personal feature and failure demonstration. Use the starter only as a reference, not as your unchanged final submission.

Award using the module rubric. Require a live explanation or a brief code walkthrough; screenshots alone do not prove the independent change. Do not penalize equivalent correct implementations. Teacher reference code is a starting point, not the completed student task.

