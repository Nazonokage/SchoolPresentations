# EDP Module 12: Distributed Messaging, Brokers, and Event Streaming

[Module index](README.md) | [Setup and commands](../examples/README.md)

**Period:** Pre-final · **Meeting:** 60–90 minutes · **Assessment:** Coding activity

## A. Lesson Preview & Review

Two kitchen workers should share orders, but both inventory and analytics should hear about each completed order. Those are different delivery models.

**In a nutshell:** Compare work queues, Pub/Sub and retained logs. We will run a small example, explain its behavior and change one part ourselves.

**Learning targets**

1. Compare work queues, Pub/Sub and retained logs.
2. Explain what changes when events cross a network.
3. Build a local model and label its limits.

**Before class:** M04 (`EventEmitter`), M07 (Observer versus Pub/Sub) and M09 (a real network connection changes the failure model). No broker installation is needed; the example is a local model.

**60-minute route:** 5 minutes preview, 15 explanation/demo, 30 coding, 10 review. For 90 minutes, add 15 guided exploration and 15 debugging/feedback.

**Scope:** Core: the three delivery models, one crash-and-redeliver case and one rejected offset in the local model. Teacher demonstration only: a real RabbitMQ or Kafka tutorial.

## Visual Guide & HTML Presentation Notes

![Messaging model comparison: Producer → Queue or topic → Consumers → Replay position](../visuals/m12-guide.svg)

**What the sample image explains:** Use separate slides for competing consumers, broadcast and retained logs; do not imply identical guarantees.

**Suggested slides:**

1. Opening: show this diagram and ask students to predict the flow before revealing the explanation.
2. Concept: reveal one labeled stage at a time; connect it to the matching code rather than putting the whole lesson on screen.
3. Code/output: use a readable code panel beside a real output capture from the supplied example. Label input, expected output and any failure state.
4. Practice: keep the quiz or coding task readable and separate from its answer/explanation.

**Sample image to capture:** Run this module’s supplied program and capture the terminal with the meaningful result visible. Include a caption naming the command and the observed behavior; avoid invented output screenshots.

**Projector text:** use scalable text, minimum 16px everywhere; aim for 24–32px body text on classroom screens. Scale code and diagram labels too. Give a diagram its own slide when labels would become small. See the [visual guide and scalable presentation prompt](../visuals/README.md).

## B. Main Lesson

### Leaving one process changes the failure model

An in-process emit calls listeners in one runtime. A network message must be serialized, transmitted, received and processed elsewhere. A producer can time out without knowing whether a broker accepted its message. A consumer can fail after changing data but before acknowledging. There is no single shared call stack that tells every participant what happened.

A broker routes or stores messages between producers and consumers. It can reduce direct availability coupling, but becomes infrastructure that needs configuration, access control, monitoring and capacity planning. Broker availability does not guarantee consumer correctness. Start by identifying the delivery behavior required by the problem.

### Three models

In a work queue, competing consumers share jobs: typically one consumer handles a particular delivery, with redelivery possible after failure. In Pub/Sub, independent subscriptions receive relevant publications so several reactions can occur. In a retained log, events remain available according to retention settings and consumers track positions for replay. These are models, not rigid categories that each product can implement only once.

The simulation assigns four jobs round-robin to two worker labels and deliberately crashes one delivery: with no acknowledgment the job goes back on the queue and a different worker finishes it. It then broadcasts one event to an online and an offline subscriber, and slices a retained array at several offsets, including one invalid offset that is rejected. It demonstrates routing, redelivery and replay positions only. It has no network, real acknowledgments, persistence or actual parallel workers. A restart loses the arrays.

### Broker vocabulary

Queues hold pending deliveries; topics or exchanges help route publications. An acknowledgment records a delivery-processing decision at a defined point. Retention determines how long records remain available. Partitioning divides work and can define an ordering boundary. Consumer groups distribute consumption while independent groups can read the same retained data.

RabbitMQ's work-queue tutorial demonstrates explicit acknowledgment and delivery distribution. Kafka's introductory model emphasizes retained partitioned event streams. Their full capabilities overlap more than a simple “queue versus stream” slogan suggests. Compare configuration, client support, workload and operational needs before choosing.

### Platform comparison without installation overload

Redis Pub/Sub versus Redis Streams illustrates transient broadcast versus retained stream capabilities. NATS and JetStream, cloud queue/topic services such as SQS/SNS, Azure Service Bus and Google Pub/Sub, and MQTT-based IoT messaging have different guarantees and operational models. Treat this list as a research map: verify each product's current documentation before assigning exact API behavior or pricing.

For the core activity, annotate a diagram with producers, channels and consumers and trace one duplicate or offline-consumer case. A real RabbitMQ tutorial can be a teacher-prepared extension. Installing RabbitMQ and Kafka simultaneously is not required to understand the distinction.

## C. Analogy, Guided Program & Practice

### Everyday connection

A shared task tray gives one slip to one available worker. A public announcement informs several departments. An archive lets a new department read old announcements later.

### Run the complete example

Run commands from the `EDP/examples` folder. Install the pinned dependencies once with `npm ci`; most `.mjs` examples otherwise use only Node built-ins. See the setup guide for the verified runtime.

```powershell
node m12.mjs
```

Wait for completion and compare behavior with the expected trace before editing.

### File: `m12.mjs`

[Open runnable file](../examples/m12.mjs)

```javascript
// LOCAL MODEL ONLY: no network, no persistence, no real parallel workers.
// 1. Work queue: each job goes to ONE worker; an un-acknowledged job is redelivered.
const workers = ['Kitchen 1', 'Kitchen 2'];
const queue = ['A1', 'A2', 'A3', 'A4'];
const crashOnce = new Set(['Kitchen 2:A2']); // deliberate failure: worker dies before ack
const attempts = {};
const done = [];
let turn = 0;
while (queue.length > 0) {
  const job = queue.shift();
  const worker = workers[turn++ % workers.length];
  attempts[job] = (attempts[job] ?? 0) + 1;
  if (crashOnce.delete(`${worker}:${job}`)) {
    console.log('Queue:', worker, job, 'crashed, no ack -> redeliver');
    queue.push(job);
    continue;
  }
  console.log('Queue:', worker, job, 'ack');
  done.push(job);
}
console.log('Completed order:', done.join(','), '| A2 attempts:', attempts.A2);

// 2. Pub/Sub: every ONLINE subscriber gets its own copy; an offline one simply misses it.
const subscribers = [{ name: 'Invoice', online: true }, { name: 'Analytics', online: false }];
for (const { name, online } of subscribers) {
  console.log('PubSub:', name, online ? 'A1' : 'offline, missed A1');
}

// 3. Retained log: events stay; each consumer keeps its own offset and can catch up.
const retainedLog = ['created:A1', 'ready:A1', 'collected:A1'];
const offsets = { dashboard: 0, archive: 1, analytics: 0 }; // analytics was offline above
function replay(consumer, offset) {
  if (!Number.isInteger(offset) || offset < 0 || offset > retainedLog.length) {
    console.log('Rejected offset:', consumer, offset);
    return;
  }
  console.log('Replay:', consumer, retainedLog.slice(offset).join(',') || '(nothing new)');
}
for (const [consumer, offset] of Object.entries(offsets)) replay(consumer, offset);
replay('broken', 9); // failure case: offset outside the retained log
```

### Expected behavior and explanation checkpoint

Queue alternates between Kitchen 1 and Kitchen 2; Kitchen 2 crashes on A2 without an ack, so A2 is redelivered to Kitchen 1 and the completed order is A1,A3,A4,A2 with A2 attempts: 2. PubSub delivers A1 to the online Invoice subscriber while the offline Analytics subscriber misses it. Dashboard replays all three events, archive starts at the second, and analytics (which missed the broadcast) catches up from offset 0. Offset 9 is rejected.

Before editing, identify the producer/input, callback or consumer, state/output, and cleanup boundary in the code. Trace one value through the program. Explain which line changes the outcome rather than only reading the console aloud.

### Your independent change

Add a third worker and a third independent subscriber. Give a new replay consumer offset 2. Then make a different worker crash on a different job: predict which worker redelivers it and what the completion order becomes before you run. Keep the invalid-offset rejection. Explain each result and explicitly label the program a local model.

**Checkpoint:** Predict → run → explain → modify. *Hindi sapat na gumana dahil kinopya; dapat kaya mong sabihin kung bakit at baguhin ang isang behavior.*

### Troubleshooting and common mistake

A completion order of A1,A3,A4,A2 is correct: redelivery reorders completion, and a queue does not promise global order after a failure. A local array is not a durable queue. Broadcast to two listeners does not demonstrate competing-consumer load balancing. An offset represents a position, not proof that business processing succeeded.

If a command fails before any lesson output, check the working folder, filename, Node version and installed packages first. Distinguish setup errors from a deliberately rejected input or handled runtime failure.

### Sa madaling salita

Magkaiba ang paghahati ng trabaho at pagpapadala ng parehong balita sa maraming departamento. Piliin ang model ayon sa kailangan.

[Quick reference and glossary](QUICK_REFERENCE.md)

## D. Assessment, Wrap-Up & References

### One coding activity

**Task:** Add a third worker and a third independent subscriber. Give a new replay consumer offset 2. Then make a different worker crash on a different job: predict which worker redelivers it and what the completion order becomes before you run. Keep the invalid-offset rejection. Explain each result and explicitly label the program a local model.

**Submit one folder or archive containing:**

1. Your complete modified program and any files needed to run it.
2. A short README with the exact command and expected result.
3. Evidence of one successful case and one rejected/failing case (the crashed delivery and the rejected offset), plus a brief explanation of your independent change.

| Criterion | Points | Evidence |
| --- | ---: | --- |
| Required behavior | 4 | Core works (2); third worker, third subscriber and offset-2 consumer work (2) |
| Error/edge behavior | 2 | A worker crash is redelivered (job completes once) and an invalid offset is rejected (1); program and README label the work a local model (1) |
| Understanding | 2 | Explain event/data flow (1); explain your own change (1) |
| Reproducibility/readability | 2 | Commands/files are complete (1); names and small structure are understandable (1) |
| Total | 10 | One activity, no separate quiz |

### Wrap-up

Compare work queues, Pub/Sub and retained logs. Build a local model and label its limits.

**Exit reflection (ungraded):** Which result shows the difference between sharing work and broadcasting? What does the local model deliberately leave out?

**Next connection:** M13 asks what happens when delivery fails or repeats: guarantees, idempotency and dead letters.

### References and further reading

- [Official/reference documentation: www.rabbitmq.com](https://www.rabbitmq.com/tutorials/tutorial-two-javascript)
- [Official/reference documentation: kafka.apache.org](https://kafka.apache.org/intro/)

The prose and classroom code are original teaching examples informed by the references. Read [validation notes](../instructor/VALIDATION.md) before distributing a new toolchain version.
