# EDP Module 13: Delivery Guarantees, Ordering, and Reliable Consumers

[Module index](README.md) | [Setup and commands](../examples/README.md)

**Period:** Pre-final · **Meeting:** 60–90 minutes · **Assessment:** 10-item quiz

## A. Lesson Preview & Review

The server successfully applies an order, but its acknowledgment is lost. The same message returns. Charging twice is not an acceptable retry strategy.

**In a nutshell:** Explain at-most-once and at-least-once trade-offs. We will run a small example, explain its behavior and change one part ourselves.

**Learning targets**

1. Explain at-most-once and at-least-once trade-offs.
2. Trace idempotency, bounded retries and dead letters.
3. Identify the limits of in-memory deduplication.

**Before class:** M12 (work queue, Pub/Sub, retained log), M05 (retries and cancellation) and M02 (`async/await` with timers).

**60-minute route:** 5 minutes preview, 25 explanation/demo, 15 guided code, 10 quiz, 5 feedback. For 90 minutes, add 15 minutes practice and 15 discussion/debugging.

**Scope:** Core: processed-ID set, bounded retries and a dead-letter array. Reference reading only: partitioning, ordering and real broker acknowledgments.

## Visual Guide & HTML Presentation Notes

![Reliable consumer: Receive ID → Check duplicate → Apply effect → Ack or retry](../visuals/m13-guide.svg)

**What the sample image explains:** Real deduplication and the business change need an atomic durable boundary; this model is in memory.

**Suggested slides:**

1. Opening: show this diagram and ask students to predict the flow before revealing the explanation.
2. Concept: reveal one labeled stage at a time; connect it to the matching code rather than putting the whole lesson on screen.
3. Code/output: use a readable code panel beside a real output capture from the supplied example. Label input, expected output and any failure state.
4. Practice: keep the quiz or coding task readable and separate from its answer/explanation.

**Sample image to capture:** Run this module’s supplied program and capture the terminal with the meaningful result visible. Include a caption naming the command and the observed behavior; avoid invented output screenshots.

**Projector text:** use scalable text, minimum 16px everywhere; aim for 24–32px body text on classroom screens. Scale code and diagram labels too. Give a diagram its own slide when labels would become small. See the [visual guide and scalable presentation prompt](../visuals/README.md).

## B. Main Lesson

### State the guarantee and its boundary

At-most-once delivery avoids some redelivery but can lose work. At-least-once aims to avoid loss under its assumptions but permits duplicates. “Exactly once” must specify the system boundary and operation: a broker feature does not automatically make every external email, payment or database write occur exactly once.

Consider process → save result → acknowledge. A crash between save and acknowledge can cause a duplicate delivery. Acknowledge → process risks losing the work if the consumer fails after acknowledging. These are failure windows, not merely bad luck. Draw them before choosing where acknowledgments happen.

### Idempotency protects the business effect

An idempotent operation can be repeated without creating an additional unintended effect. Setting a record to a known state may be naturally idempotent; incrementing a balance usually is not. A stable event or operation ID lets a consumer recognize repeated work. The same ID with different content should be treated as a contract violation, not silently accepted as a new event.

The example uses a Set and a running total. A1 fails once, then succeeds; a duplicate A1 is skipped. This demonstrates the logic in one sequential process. A real consumer needs the deduplication record and business change committed atomically, plus an appropriate uniqueness constraint. Otherwise concurrent workers can both pass the “not processed” check. Restarting this script clears its Set.

### Retry only when a retry can help

A temporary outage may recover. Malformed data or unauthorized requests usually need correction instead of endless retries. Use a limit, increasing delay and often jitter to avoid many consumers retrying together. The model retries three times with a small exponential delay. A2 is deliberately poison and moves to the dead-letter array.

A dead-letter queue is a place to inspect, repair and deliberately replay failures. It is not a trash bin or an automatic cure. Preserve IDs, reasons and useful metadata without leaking secrets. A replay plan should revalidate data and retain deduplication policy.

### Ordering and pressure

Parallel consumers and retries can reorder completion. Partition by a meaningful entity key when per-entity ordering matters, and use sequence/version checks where appropriate. Global ordering is expensive and often unnecessary. Queue depth alone is not enough to assess health: oldest-message age and processing latency help reveal stuck work.

Bound buffers and define overload behavior. More retries during an outage can make it worse. Today’s program is a small traceable model; broker acknowledgments, durable IDs and concurrent transaction tests belong to an explicitly configured extension.

## C. Analogy, Guided Program & Practice

### Everyday connection

A cashier marks a receipt number as paid. Seeing that same receipt again should not collect a second payment. The mark and the payment record must agree even if the cashier changes shifts.

### Run the complete example

Run commands from the `EDP/examples` folder. Install the pinned dependencies once with `npm ci`; most `.mjs` examples otherwise use only Node built-ins. See the setup guide for the verified runtime.

```powershell
node m13.mjs
```

Wait for completion and compare behavior with the expected trace before editing.

### File: `m13.mjs`

[Open runnable file](../examples/m13.mjs)

```javascript
import { setTimeout as delay } from 'node:timers/promises';
const processed = new Set(); const deadLetters = []; let total = 0;
async function consume(message) {
  if (processed.has(message.id)) { console.log('Duplicate:', message.id); return; }
  for (let attempt = 1; attempt <= 3; attempt++) {
    try {
      if (message.poison || (message.transient && attempt === 1)) throw new Error('Temporary service failure');
      total += message.amount; processed.add(message.id);
      console.log('Applied:', message.id, 'attempt', attempt); return;
    } catch (error) {
      console.log('Retry decision:', message.id, attempt);
      if (attempt === 3) { deadLetters.push(message); return; }
      await delay(5 * 2 ** (attempt - 1));
    }
  }
}
await consume({ id: 'A1', amount: 60, transient: true });
await consume({ id: 'A1', amount: 60 });
await consume({ id: 'A2', amount: 40, poison: true });
console.log('Total:', total, 'Dead letters:', deadLetters.length);
// In-memory sequential model only: a real consumer needs durable atomic deduplication.
```

### Expected behavior and explanation checkpoint

A1 retries once, applies on attempt 2, its duplicate is ignored; A2 reaches attempt 3 and is dead-lettered. Final total is 60 and dead-letter count is 1.

Before editing, identify the producer/input, callback or consumer, state/output, and cleanup boundary in the code. Trace one value through the program. Explain which line changes the outcome rather than only reading the console aloud.

### Your independent change

Predict the result if you remove the processed-ID check. Discuss what happens if the process restarts between applying the total and recording the ID.

**Checkpoint:** Predict → run → explain → modify. *Hindi sapat na gumana dahil kinopya; dapat kaya mong sabihin kung bakit at baguhin ang isang behavior.*

### Troubleshooting and common mistake

Marking processed before a failed business action can lose work. Marking it separately afterward can duplicate work. A Set is neither durable nor safe against independent concurrent processes.

If a command fails before any lesson output, check the working folder, filename, Node version and installed packages first. Distinguish setup errors from a deliberately rejected input or handled runtime failure.

### Sa madaling salita

Puwedeng maulit ang delivery. Dapat hindi umulit ang singil o ibang business effect dahil lang naulit ang message.

[Quick reference and glossary](QUICK_REFERENCE.md)

## D. Assessment, Wrap-Up & References

### 10-item quiz

One point per item. Answer after the explanation and guided practice. Give short answers; no extra graded coding submission today. The instructor keeps the answer key separately.

1. What delivery model permits duplicate deliveries while aiming to avoid loss?
2. What is an idempotent effect?
3. What is the purpose of a dead-letter destination?
4. A1 amount 60 succeeds and its identical ID returns. What total does the sample retain?
5. The poison message has a three-attempt limit. What happens after the third failure?
6. A consumer commits then crashes before acknowledgment. What can happen next?
7. Why is a process-local Set insufficient for restart-safe deduplication?
8. Why is acknowledging before doing the work risky?
9. How should malformed input differ from a temporary outage in retry policy?
10. Two workers might apply the same event simultaneously. What protects the effect?
### Wrap-up

Explain at-most-once and at-least-once trade-offs. Identify the limits of in-memory deduplication.

**Exit reflection (ungraded):** At which exact moment can a duplicate appear, and what protects the business effect when it does?

**Next connection:** M14 shows how to publish reliably in the first place: outbox and inbox.

### References and further reading

- [Official/reference documentation: www.rabbitmq.com](https://www.rabbitmq.com/docs/confirms)
- [Official/reference documentation: www.rabbitmq.com](https://www.rabbitmq.com/docs/dlx)

The prose and classroom code are original teaching examples informed by the references. Read [validation notes](../instructor/VALIDATION.md) before distributing a new toolchain version.
