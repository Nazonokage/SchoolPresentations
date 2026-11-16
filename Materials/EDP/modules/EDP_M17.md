# EDP Module 17: Observability, Security, and Production Resilience

[Module index](README.md) | [Setup and commands](../examples/README.md)

**Period:** Pre-final · **Meeting:** 60–90 minutes · **Assessment:** 10-item quiz

## A. Lesson Preview & Review

“Something broke” is not enough information to repair an event-driven system. We need to connect an action, its reactions and the point where it was rejected.

**In a nutshell:** Interpret structured logs and basic metrics. We will run a small example, explain its behavior and change one part ourselves.

**Learning targets**

1. Interpret structured logs and basic metrics.
2. Explain trace/correlation context and security boundaries.
3. Choose bounded recovery instead of unlimited retries.

**Before class:** Earlier core lessons or their supplied runnable checkpoints. No database or broker installation is required for this lesson. Read the example filenames below and keep a clean copy before editing.

**60-minute route:** 5 minutes preview, 25 explanation/demo, 15 guided code, 10 quiz, 5 feedback. For 90 minutes, add 15 minutes practice and 15 discussion/debugging.

**Scope:** Prioritize the runnable core and learning targets. The later comparisons are reference reading or teacher demonstrations; do not attempt every extension in one meeting. Finals modules introduce no new infrastructure.

## Visual Guide & HTML Presentation Notes

![Observe and authorize: Validate shape → Check actor → Handle or reject → Log and metrics](../visuals/m17-guide.svg)

**What the sample image explains:** Correlation helps trace work; it does not authenticate the actor.

**Suggested slides:**

1. Opening: show this diagram and ask students to predict the flow before revealing the explanation.
2. Concept: reveal one labeled stage at a time; connect it to the matching code rather than putting the whole lesson on screen.
3. Code/output: use a readable code panel beside a real output capture from the supplied example. Label input, expected output and any failure state.
4. Practice: keep the quiz or coding task readable and separate from its answer/explanation.

**Sample image to capture:** Run this module’s supplied program and capture the terminal with the meaningful result visible. Include a caption naming the command and the observed behavior; avoid invented output screenshots.

**Projector text:** use scalable text, minimum 16px everywhere; aim for 24–32px body text on classroom screens. Scale code and diagram labels too. Give a diagram its own slide when labels would become small. See the [visual guide and scalable presentation prompt](../visuals/README.md).

## B. Main Lesson

### Evidence that explains behavior

A log records a discrete occurrence. A metric aggregates measurements such as counts or duration distributions. A trace connects work across operations through spans and context. These signals complement one another: an error count shows a problem is growing, while a correlated timeline helps explain a particular failure.

Our program emits structured JSON containing eventId, correlationId, outcome and reason. The event ID identifies one occurrence; the correlation ID groups a workflow. A causation ID can identify which earlier event or command directly caused the current event. These are related but distinct questions.

The example's correlation ID is fixed because it models one checkout. In a real service generate or accept context according to a trust policy and propagate it consistently. An arbitrary request header is not proof of identity. Do not store passwords, full tokens or unnecessary personal data in logs.

### Measure the useful failure signals

The counters show accepted and rejected actions. A live service also needs processing latency, queue depth, oldest pending age, retry/dead-letter counts and perhaps event-loop lag. Averages can hide slow tails; distributions/percentiles may better show user impact. Define units and avoid unbounded metric labels such as every user ID, which can create high cardinality.

OpenTelemetry supplies APIs, SDKs and conventions for collecting/exporting telemetry. A collector and visualization backend are separate pieces. Logging a correlationId field is not automatically a complete distributed trace. This lesson introduces the concepts; deploying an observability stack is a teacher demonstration or extension.

### Validate and authorize at the boundary

The handler first checks shape, then owner identity. Valid JSON is not sufficient: a correctly shaped action can still be unauthorized. In the local model the actor object is trusted by construction; a real server must derive it from a verified session or equivalent identity source, not accept actor.id from the user body.

Apply broker/topic permissions, payload size limits, schema checks and rate limits where appropriate. Do not broadcast all tenant data and hope clients filter it correctly. Secrets belong in protected server configuration; client bundles and telemetry are not secret stores.

### Resilience with limits

Timeouts bound waiting. Retries need safe operations and limits. A circuit breaker temporarily stops attempts to an unhealthy dependency and probes recovery according to policy. Bulkheads isolate resource pools so one failure does not exhaust everything. Opossum is one possible library, not a required or automatically correct configuration.

Graceful shutdown stops intake, drains bounded work and closes resources. Versioned contracts, dependency maintenance and replay rehearsals reduce operational surprises. Practice explaining one incident from evidence rather than adding retries until the symptom disappears.

## C. Analogy, Guided Program & Practice

### Everyday connection

A parcel tracking number follows one package through several depots. The daily depot volume counter answers a different question. You need both to investigate one lost package and a system-wide backlog.

### Run the complete example

Run commands from the `EDP/examples` folder. Install the pinned dependencies once with `npm ci`; most `.mjs` examples otherwise use only Node built-ins. See the setup guide for the verified runtime.

```powershell
node m17.mjs
```

Wait for completion and compare behavior with the expected trace before editing.

### File: `m17.mjs`

[Open runnable file](../examples/m17.mjs)

```javascript
const records = []; const metrics = { accepted: 0, rejected: 0 };
function log(eventId, outcome, reason) {
  const record = { eventId, correlationId: 'checkout-A1', outcome, reason };
  records.push(record); console.log(JSON.stringify(record));
}
function handle(input, actor) {
  if (!input || typeof input.id !== 'string' || typeof input.owner !== 'string') {
    metrics.rejected++; log('unknown', 'rejected', 'invalid shape'); return;
  }
  if (input.owner !== actor.id) { metrics.rejected++; log(input.id, 'rejected', 'not owner'); return; }
  metrics.accepted++; log(input.id, 'accepted', 'authorized');
}
handle({ id: 'E1', owner: 'student-1' }, { id: 'student-1' });
handle({ id: 'E2', owner: 'student-2' }, { id: 'student-1' });
console.log('Metrics:', JSON.stringify(metrics));
// actor is trusted only in this model; a real server derives it from verified identity.
```

### Expected behavior and explanation checkpoint

E1 is accepted, E2 is rejected as not owner, metrics are accepted:1/rejected:1. The rejected action never reaches the success branch.

Before editing, identify the producer/input, callback or consumer, state/output, and cleanup boundary in the code. Trace one value through the program. Explain which line changes the outcome rather than only reading the console aloud.

### Your independent change

Explain what would happen if actor.id came directly from an unverified request body. Add a malformed input during ungraded practice and inspect the rejection reason.

**Checkpoint:** Predict → run → explain → modify. *Hindi sapat na gumana dahil kinopya; dapat kaya mong sabihin kung bakit at baguhin ang isang behavior.*

### Troubleshooting and common mistake

A correlation ID is not an authentication token. Retrying unauthorized input will not repair it. Logging entire payloads can expose data that the application otherwise protects.

If a command fails before any lesson output, check the working folder, filename, Node version and installed packages first. Distinguish setup errors from a deliberately rejected input or handled runtime failure.

### Sa madaling salita

Sundan ang ebidensiya: aling event, aling workflow, anong result? Huwag isama ang password o token para lang mas maraming log.

[Quick reference and glossary](QUICK_REFERENCE.md)

## D. Assessment, Wrap-Up & References

### 10-item quiz

One point per item. Answer after the explanation and guided practice. Give short answers; no extra graded coding submission today. The instructor keeps the answer key separately.

1. What does a correlation ID group?
2. How does a metric differ from an individual log entry?
3. Is a correlation ID proof that a user is authenticated?
4. E1 belongs to student-1 and actor is student-1. What outcome is logged?
5. E2 belongs to student-2 but actor is student-1. What outcome is logged?
6. After those two calls, what are the sample counters?
7. Why is trusting actor.id directly from a request body unsafe?
8. Why should full tokens not be logged for easier debugging?
9. Which signal helps detect old stuck work besides queue length?
10. A dependency is persistently down. Suggest bounded resilience measures.
### Wrap-up

Interpret structured logs and basic metrics. Choose bounded recovery instead of unlimited retries.

**Exit reflection (ungraded):** What event or operation started the flow, what state changed, and what happens if that flow cannot complete? Name one assumption the sample deliberately makes.

**Next connection:** The next module builds on this core. Keep your working checkpoint; an independent starter is supplied if you need to restart.

### References and further reading

- [Official/reference documentation: opentelemetry.io](https://opentelemetry.io/docs/concepts/observability-primer/)
- [Official/reference documentation: learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker)

The prose and classroom code are original teaching examples informed by the references. Source reports are research inputs, not authority for unverified claims. Read [validation notes](../instructor/VALIDATION.md) before distributing a new toolchain version.
