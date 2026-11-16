# EDP Module 14: Reliable Publication, Outbox/Inbox, and Event Contracts

[Module index](README.md) | [Setup and commands](../examples/README.md)

**Period:** Pre-final · **Meeting:** 60–90 minutes · **Assessment:** Coding activity

## A. Lesson Preview & Review

Saving an order and announcing it are two actions. What if the order is saved but the application crashes before publishing its event?

**In a nutshell:** Explain the dual-write failure window. We will run a small example, explain its behavior and change one part ourselves.

**Learning targets**

1. Explain the dual-write failure window.
2. Model outbox publication and inbox deduplication.
3. Validate a versioned contract and distinguish a model from a transaction.

**Before class:** M13 (at-least-once delivery, idempotency, dead letters) and M06 (runtime validation of external data). Be ready to explain the difference between a model and a database transaction.

**60-minute route:** 5 minutes preview, 15 explanation/demo, 30 coding, 10 review. For 90 minutes, add 15 guided exploration and 15 debugging/feedback.

**Scope:** Core: copy-on-write outbox model, inbox deduplication and the versioned guard. Optional extension: the webhook receiver (`m14-webhook.mjs`). Reference reading only: CloudEvents and a real SQL/Mongo transaction.

## Visual Guide & HTML Presentation Notes

![Outbox publication: Domain write → Outbox record → Relay publishes → Inbox dedupes](../visuals/m14-guide.svg)

**What the sample image explains:** Domain write and outbox insert belong in one local transaction. Delivery can still duplicate.

**Suggested slides:**

1. Opening: show this diagram and ask students to predict the flow before revealing the explanation.
2. Concept: reveal one labeled stage at a time; connect it to the matching code rather than putting the whole lesson on screen.
3. Code/output: use a readable code panel beside a real output capture from the supplied example. Label input, expected output and any failure state.
4. Practice: keep the quiz or coding task readable and separate from its answer/explanation.

**Sample image to capture:** Run this module’s supplied program and capture the terminal with the meaningful result visible. Include a caption naming the command and the observed behavior; avoid invented output screenshots.

**Projector text:** use scalable text, minimum 16px everywhere; aim for 24–32px body text on classroom screens. Scale code and diagram labels too. Give a diagram its own slide when labels would become small. See the [visual guide and scalable presentation prompt](../visuals/README.md).

## B. Main Lesson

### The dual-write problem

Suppose code writes an order to SQL, then sends order.created to a broker. A crash between those actions leaves a real order with no announcement. Reversing the order can announce an order that never commits. A try/catch cannot roll back a message already delivered to another independent system.

The transactional outbox records the business change and a pending event in the same local database transaction. A relay later reads pending records and publishes them. This makes the intent to publish durable with the business change, but it does not remove duplicate publication. If sending succeeds and the relay crashes before marking sent, it sends again after restart.

### Read the model honestly

Our model clones an in-memory object, modifies both orders and outbox, then assigns the new object only if the simulated commit succeeds. A deliberate throw leaves the original object unchanged. This illustrates the all-or-nothing boundary; it is not durable storage, locking, isolation or a real database transaction.

The relay sends the same event twice to simulate lost acknowledgment. A consumer inbox remembers the event ID and ignores the duplicate. In a real database, inbox insertion and the consumer's business effect need their own atomic boundary. A uniqueness constraint prevents two workers from accepting the same ID concurrently.

SQL via a server API and MongoDB are optional persistence paths, not direct browser connections. Their transaction and deployment capabilities must be verified before replacing this model. Writing to a database does not automatically publish an application-level domain event unless that behavior is deliberately implemented.

### Evolve contracts without surprising readers

An event envelope contains routing/context metadata such as ID, type, source and version; data contains business facts. A schema version is not the same as the software package version. Adding an optional field can be compatible if consumers tolerate it. Renaming or changing the meaning of a required field often needs an explicit migration/version plan.

The guard here accepts only version 1 and an ID string. Extend it deliberately for version 2 rather than assuming every JSON object is compatible. Producer and consumer contract tests should include old and new samples. Avoid deleting required information before all relevant consumers can cope.

### Common envelopes and privacy

CloudEvents provides a common event description with required attributes such as id, source, specversion and type; its format version is distinct from the domain payload schema version. Our small envelope is not claimed to be a complete CloudEvents implementation. Use the actual specification when interoperability is required.

Events may persist for a long time and be replayed to new consumers. Minimize sensitive payloads, document retention and access, and avoid copying authentication tokens into history. Replay must not bypass authorization or blindly repeat external side effects.

### Optional extension: a webhook is an inbox at the edge

A webhook is an HTTP callback another service sends you when something happens, such as a payment provider reporting that an order was paid. It is the inbox problem arriving from outside: anyone can post to your URL, the sender retries when it does not get a quick success response, and a retry means the same event ID arrives again. A receiver therefore (1) verifies a signature computed over the exact raw body with a shared secret, using a constant-time comparison; (2) rejects timestamps outside a tolerance so a captured request cannot be replayed later; (3) parses and validates the body only after the sender is verified; (4) deduplicates by event ID, as in the inbox above; and (5) acknowledges quickly and does slow work afterward.

Every provider defines its own header names and signing recipe, so follow your provider’s documentation. `m14-webhook.mjs` uses a classroom recipe, not any provider’s. Its secret is hard-coded for the demo only; real secrets live in protected server configuration and are never committed or logged.

## C. Analogy, Guided Program & Practice

### Everyday connection

Write the order and its “send announcement” slip into one bound ledger entry. A messenger may deliver the slip twice, so the recipient keeps a receipt-number register.

### Run the complete example

Run commands from the `EDP/examples` folder. Install the pinned dependencies once with `npm ci`; most `.mjs` examples otherwise use only Node built-ins. See the setup guide for the verified runtime.

```powershell
node m14.mjs
node m14-webhook.mjs   # optional extension
```

Wait for completion and compare behavior with the expected trace before editing.

### File: `m14.mjs`

[Open runnable file](../examples/m14.mjs)

```javascript
// Model an atomic commit using copy-on-write, NOT a real database transaction.
let db = { orders: [], outbox: [] };
function placeOrder(id, fail = false) {
  const draft = structuredClone(db);
  draft.orders.push({ id });
  draft.outbox.push({ id: 'event-' + id, version: 1, type: 'order.created', data: { id } });
  if (fail) throw new Error('Commit cancelled');
  db = draft;
}
try { placeOrder('BAD', true); } catch (error) { console.log(error.message); }
placeOrder('A1');
const inbox = new Set();
function receive(event) {
  if (event.version !== 1 || typeof event.data?.id !== 'string') throw new Error('Unsupported contract');
  if (inbox.has(event.id)) { console.log('Duplicate ignored:', event.id); return; }
  console.log('Received:', event.data.id); inbox.add(event.id);
}
const pending = db.outbox[0];
receive(pending); // Simulate send succeeded but relay lost acknowledgment.
receive(pending); // Retry is expected.
db.outbox.shift();
console.log('Orders:', db.orders.length, 'Pending:', db.outbox.length);
```

### Optional file: `m14-webhook.mjs`

[Open runnable file](../examples/m14-webhook.mjs)

```javascript
// Webhook receiver model: verify the sender, reject stale deliveries, dedupe by event ID.
// Teaching model: the secret is hard-coded here; real secrets live in protected server config.
import { createHmac, timingSafeEqual } from 'node:crypto';
const SECRET = 'classroom-demo-secret';
const TOLERANCE_SECONDS = 300;
const seen = new Set();
const sign = (timestamp, body) => createHmac('sha256', SECRET).update(`${timestamp}.${body}`).digest('hex');

function receive({ timestamp, signature, body }, nowSeconds) {
  const expected = Buffer.from(sign(timestamp, body), 'hex');
  const given = Buffer.from(String(signature), 'hex');
  if (given.length !== expected.length || !timingSafeEqual(given, expected)) return 'Rejected: bad signature';
  if (Math.abs(nowSeconds - timestamp) > TOLERANCE_SECONDS) return 'Rejected: stale timestamp';
  const event = JSON.parse(body); // parse only AFTER the sender is verified
  if (seen.has(event.id)) return 'Duplicate ignored: ' + event.id;
  seen.add(event.id);
  return 'Accepted: ' + event.id;
}

const now = 1_800_000_000;
const body = JSON.stringify({ id: 'evt_1', type: 'payment.paid', orderId: 'A1' });
const good = { timestamp: now, signature: sign(now, body), body };
console.log(receive(good, now));                                   // first delivery
console.log(receive(good, now));                                   // sender retried
console.log(receive({ ...good, body: body.replace('A1', 'A9') }, now)); // tampered body
console.log(receive({ ...good, timestamp: now - 3600, signature: sign(now - 3600, body) }, now)); // replayed old request
```

### Expected behavior and explanation checkpoint

Commit cancelled → Received: A1 → Duplicate ignored: event-A1 → Orders: 1 Pending: 0. BAD never enters the committed model. Optional webhook demo: Accepted: evt_1 → Duplicate ignored: evt_1 → Rejected: bad signature → Rejected: stale timestamp.

Before editing, identify the producer/input, callback or consumer, state/output, and cleanup boundary in the code. Trace one value through the program. Explain which line changes the outcome rather than only reading the console aloud.

### Your independent change

Add a version-2 payload with a different field layout and normalize it explicitly into the same internal order ID. Reject an unsupported version and preserve duplicate detection.

**Checkpoint:** Predict → run → explain → modify. *Hindi sapat na gumana dahil kinopya; dapat kaya mong sabihin kung bakit at baguhin ang isang behavior.*

### Troubleshooting and common mistake

Deleting an outbox entry before confirmed publication can lose work. A relay retry can duplicate delivery. Copy-on-write in JavaScript does not prove database crash safety.

If a command fails before any lesson output, check the working folder, filename, Node version and installed packages first. Distinguish setup errors from a deliberately rejected input or handled runtime failure.

### Sa madaling salita

Sabay itala ang business change at balak na mag-publish sa isang transaction. Hiwalay pa rin ang delivery kaya posible pa rin ang duplicate.

[Quick reference and glossary](QUICK_REFERENCE.md)

## D. Assessment, Wrap-Up & References

### One coding activity

**Task:** Add a version-2 payload with a different field layout and normalize it explicitly into the same internal order ID. Reject an unsupported version and preserve duplicate detection.

**Submit one folder or archive containing:**

1. Your complete modified program and any files needed to run it.
2. A short README with the exact command and expected result.
3. Evidence of one successful case and one rejected/failing case (the unsupported version and the duplicate), plus a brief explanation of your independent change.

| Criterion | Points | Evidence |
| --- | ---: | --- |
| Required behavior | 4 | Core works (2); version-2 payload normalized into the same internal order ID (2) |
| Error/edge behavior | 2 | Unsupported version rejected (1); duplicate of a v2 event is still ignored (1) |
| Understanding | 2 | Explain event/data flow (1); explain your own change (1) |
| Reproducibility/readability | 2 | Commands/files are complete (1); names and small structure are understandable (1) |
| Total | 10 | One activity, no separate quiz |

### Wrap-up

Explain the dual-write failure window. Validate a versioned contract and distinguish a model from a transaction.

**Exit reflection (ungraded):** What is the failure window between saving an order and publishing its event? What can still duplicate even with an outbox?

**Next connection:** M15 rebuilds state from the events themselves: event sourcing and projections.

### References and further reading

- [Official/reference documentation: microservices.io](https://microservices.io/patterns/data/transactional-outbox.html)
- [Official/reference documentation: github.com](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md)
- [Official/reference documentation: nodejs.org](https://nodejs.org/api/crypto.html)

The prose and classroom code are original teaching examples informed by the references. Read [validation notes](../instructor/VALIDATION.md) before distributing a new toolchain version.
