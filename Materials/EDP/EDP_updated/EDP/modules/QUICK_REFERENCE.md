# EDP quick reference and glossary

[Module index](README.md)

| Term | Plain meaning | Remember |
| --- | --- | --- |
| Callback | Function passed for another operation to invoke | Pass the function; do not accidentally call it during registration |
| Event | Reported occurrence | UI names and domain-event names follow their own contracts |
| Command | Request to do something | It can be rejected |
| Query | Request for information | It should not secretly change domain state |
| Payload | Data carried with an event | Validate external data at runtime |
| Listener | Function reacting to an occurrence | Its owner must define cleanup |
| Observer | Subject notifies registered observers | It need not be asynchronous |
| Pub/Sub | Publications routed through topics/channels | A bus does not remove contract coupling |
| Promise | One eventual fulfillment or rejection | Await or return it; handle failure |
| Concurrency | Overlapping progress | It does not guarantee CPU parallel execution |
| Backpressure | Capacity feedback toward a producer | Define bounded buffers and overflow policies |
| Subscription | Active observation of a stream | Unsubscribe when its owner ends |
| State machine | States and allowed transitions | Reject invalid actions even if the UI hides them |
| Idempotency | Repetition without an extra unintended effect | Stable IDs and atomic durable handling may be needed |
| Outbox | Pending publication recorded with a business change | Relay delivery may still duplicate |
| Inbox | Consumer record of received/processed IDs | Record it atomically with the intended effect |
| Projection | Readable view derived from events | It can lag; rebuilding should avoid side effects |
| Snapshot | Derived state at a known sequence | It shortens replay; it is not a replacement for schema rules |
| CQRS | Separate write and read responsibilities | Does not inherently require separate services/databases |
| Saga | Multi-step workflow with local commits and recovery | Compensation can fail or be imperfect |
| Correlation ID | Context connecting related work | It is not proof of identity |
| SSE | Server streams text events over one HTTP response | One direction only; reconnects but has no replay unless you build it |
| WebSocket | Two-way messages over one upgraded connection | Validate every message in both directions |
| At-least-once | Delivery that avoids loss but may repeat | Consumers must be idempotent |
| Dead-letter queue | Holding place for messages that exceeded their retries | A place to inspect and replay, not a trash bin |
| Backoff and jitter | Growing, slightly randomized delay between retries | Prevents many clients retrying together |
| Circuit breaker | Stops calling a failing dependency for a while | Probes recovery; it does not finish the business recovery |
| Event envelope | Metadata (ID, type, source, version) around the data | Schema version is not the package version |
| Webhook | HTTP callback sent to you by another service | Verify the signature and timestamp, then deduplicate by event ID |
| Type guard | Runtime check that narrows a type | A wrong guard lies to the compiler |
| Discriminated union | Variants told apart by a field such as `type` | Add a `never` check so a missing case fails to compile |

## Small syntax reminders

```javascript
const food = 'Bread';
let count = 0;
function add(a, b) { return a + b; }
if (count === 0) console.log('No orders');
for (const price of [25, 35]) console.log(price);
const handle = setTimeout(() => console.log('Later'), 1000);
clearTimeout(handle);
```

Browser listener pattern: select a real element, register `addEventListener(type, handler)`, update with `textContent`, and remove with the same handler reference or an AbortSignal. Node emitter pattern: `on`, `emit`, `once`, `off`; remember the special unhandled `error` event behavior. These are different APIs.

`preventDefault` cancels a cancelable default action; `stopPropagation` affects propagation. `event.target` identifies the origin; `event.currentTarget` identifies the current listener target. `await` yields that async function; it does not move a CPU loop into a worker.

## Debugging order

1. Confirm runtime, current folder and command.
2. Read the first useful error and identify its file/line.
3. Check whether the listener was registered before the occurrence.
4. Trace the payload and validate its shape.
5. Check the current state and whether the action is allowed.
6. Inspect promise rejection, stale response or duplicate delivery.
7. Dispose resources and repeat the test with a fresh instance.
8. For input from outside your process (network, webhook, JSON), verify the sender and validate the shape before trusting any field.

Use the full lesson and its linked documentation for environment-specific details; this sheet is a reminder, not a replacement for them.
