LESSONS = {
11: {
'hook':'The program worked during the demo. Can you prove it still works after a listener is removed or an operation fails?',
'targets':['Write assertions for listener order and cleanup.', 'Await asynchronous tests correctly.', 'Diagnose a failure using a small reproducible trace.'],
'lesson':'''### Test a contract, not a screenshot of success

A useful test states an observable promise: a once listener runs once, invalid input is rejected, or cleanup prevents later reactions. Arrange a fresh instance, perform an action, and assert a result. Independent instances prevent one test's listeners from leaking into another. A test that only runs code without checking anything may pass while behavior is wrong.

The supplied suite uses built-in node:test and strict assertions. The first test captures listener order in an array, removes a callback and emits again. Comparing the entire trace proves both order and absence of later calls. The listener count checks teardown. Test one important contract per focused case; avoid assertions about internal variable names that do not matter to users.

### Async tests must finish at the right time

An async test must return or await its asynchronous work. Otherwise the test can finish before the failure occurs. Register events.once before emitting, then await the resulting promise. Prefer an event or injected scheduler over an arbitrary long sleep. A test that depends on “this should take exactly 10 ms” is fragile on busy machines.

Fake timers or virtual schedulers can model time deterministically, but they must match the environment and API. Restoring mocked clocks after each test is essential. Promise microtasks and timer queues are not identical, so advancing a fake timer may not settle every async continuation automatically. Use the test tool's documented behavior.

### Negative cases are part of correctness

The third test asserts that an unhandled EventEmitter error throws. Because the failure is expected and captured by assert.throws, the suite can pass. For an async rejection, use an asynchronous rejection assertion instead; assert.throws only observes synchronous throws. Add cases for duplicate registration, malformed payloads, missing IDs and cleanup after failure.

Mutation checking can be simple: temporarily remove off from the implementation and confirm the relevant test fails, then restore it. If the test still passes, it may not exercise the intended contract. Do not leave intentionally broken production code in the completed starter.

### Diagnose before adding machinery

Use browser breakpoints to inspect target/currentTarget and call stacks. In Node, inspect logs or a debugger and reduce the example until the error is reproducible. Add event IDs and a short timeline rather than printing entire private objects. A duplicate message may originate from duplicate registration, retry delivery or two producers; those require different fixes.

Unit tests isolate logic. Integration tests verify contracts across actual components. End-to-end tests exercise a complete user path. A Docker/Testcontainers broker test can be useful later, but the core course does not require students to install several services just to test a listener. Browser automation and RxJS virtual-time tests are appropriate extensions after the basic assertions are understood.
''',
'analogy':'A checklist before a bus trip covers brakes and emergency exits, not only whether the engine starts. Failure-path tests check the exits of our program.',
'trace':'All three m11 tests pass. Removing bus.off in the first test creates an extra first:A2 entry and causes the trace assertion to fail.',
'change':'During guided practice, add an assertion that a known payload reaches two listeners unchanged. Restore all deliberate faults before running the full suite.',
'pitfall':'An async callback launched without returning its promise can fail after the test finishes. Tests that share a global emitter can contaminate one another.',
'sources':['https://nodejs.org/api/test.html','https://nodejs.org/api/assert.html','https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Debugging_JavaScript']},
12: {
'hook':'Two kitchen workers should share orders, but both inventory and analytics should hear about each completed order. Those are different delivery models.',
'targets':['Compare work queues, Pub/Sub and retained logs.', 'Explain what changes when events cross a network.', 'Build a local model and label its limits.'],
'lesson':'''### Leaving one process changes the failure model

An in-process emit calls listeners in one runtime. A network message must be serialized, transmitted, received and processed elsewhere. A producer can time out without knowing whether a broker accepted its message. A consumer can fail after changing data but before acknowledging. There is no single shared call stack that tells every participant what happened.

A broker routes or stores messages between producers and consumers. It can reduce direct availability coupling, but becomes infrastructure that needs configuration, access control, monitoring and capacity planning. Broker availability does not guarantee consumer correctness. Start by identifying the delivery behavior required by the problem.

### Three models

In a work queue, competing consumers share jobs: typically one consumer handles a particular delivery, with redelivery possible after failure. In Pub/Sub, independent subscriptions receive relevant publications so several reactions can occur. In a retained log, events remain available according to retention settings and consumers track positions for replay. These are models, not rigid categories that each product can implement only once.

The simulation assigns four jobs round-robin to two worker labels, broadcasts one event to two subscriber labels, and slices a retained array at two offsets. It demonstrates routing and replay positions only. It has no network, acknowledgments, persistence, consumer crashes or actual parallel workers. A restart loses the arrays.

### Broker vocabulary

Queues hold pending deliveries; topics or exchanges help route publications. An acknowledgment records a delivery-processing decision at a defined point. Retention determines how long records remain available. Partitioning divides work and can define an ordering boundary. Consumer groups distribute consumption while independent groups can read the same retained data.

RabbitMQ's work-queue tutorial demonstrates explicit acknowledgment and delivery distribution. Kafka's introductory model emphasizes retained partitioned event streams. Their full capabilities overlap more than a simple “queue versus stream” slogan suggests. Compare configuration, client support, workload and operational needs before choosing.

### Platform comparison without installation overload

Redis Pub/Sub versus Redis Streams illustrates transient broadcast versus retained stream capabilities. NATS and JetStream, cloud queue/topic services such as SQS/SNS, Azure Service Bus and Google Pub/Sub, and MQTT-based IoT messaging have different guarantees and operational models. Treat this list as a research map: verify each product's current documentation before assigning exact API behavior or pricing.

For the core activity, annotate a diagram with producers, channels and consumers and trace one duplicate or offline-consumer case. A real RabbitMQ tutorial can be a teacher-prepared extension. Installing RabbitMQ and Kafka simultaneously is not required to understand the distinction.
''',
'analogy':'A shared task tray gives one slip to one available worker. A public announcement informs several departments. An archive lets a new department read old announcements later.',
'trace':'Queue alternates A1–A4 between Kitchen 1 and Kitchen 2. PubSub prints A1 for Invoice and Analytics. Dashboard replays all three events; archive starts at the second.',
'change':'Add a third worker and a third independent subscriber. Give a new replay consumer offset 2. Explain each result and explicitly label the program a local model.',
'pitfall':'A local array is not a durable queue. Broadcast to two listeners does not demonstrate competing-consumer load balancing. An offset represents a position, not proof that business processing succeeded.',
'sources':['https://www.rabbitmq.com/tutorials/tutorial-two-javascript','https://kafka.apache.org/intro/']},
13: {
'hook':'The server successfully applies an order, but its acknowledgment is lost. The same message returns. Charging twice is not an acceptable retry strategy.',
'targets':['Explain at-most-once and at-least-once trade-offs.', 'Trace idempotency, bounded retries and dead letters.', 'Identify the limits of in-memory deduplication.'],
'lesson':'''### State the guarantee and its boundary

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
''',
'analogy':'A cashier marks a receipt number as paid. Seeing that same receipt again should not collect a second payment. The mark and the payment record must agree even if the cashier changes shifts.',
'trace':'A1 retries once, applies on attempt 2, its duplicate is ignored; A2 reaches attempt 3 and is dead-lettered. Final total is 60 and dead-letter count is 1.',
'change':'Predict the result if you remove the processed-ID check. Discuss what happens if the process restarts between applying the total and recording the ID.',
'pitfall':'Marking processed before a failed business action can lose work. Marking it separately afterward can duplicate work. A Set is neither durable nor safe against independent concurrent processes.',
'sources':['https://www.rabbitmq.com/docs/confirms','https://www.rabbitmq.com/docs/dlx']},
14: {
'hook':'Saving an order and announcing it are two actions. What if the order is saved but the application crashes before publishing its event?',
'targets':['Explain the dual-write failure window.', 'Model outbox publication and inbox deduplication.', 'Validate a versioned contract and distinguish a model from a transaction.'],
'lesson':'''### The dual-write problem

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
''',
'analogy':'Write the order and its “send announcement” slip into one bound ledger entry. A messenger may deliver the slip twice, so the recipient keeps a receipt-number register.',
'trace':'Commit cancelled → Received: A1 → Duplicate ignored: event-A1 → Orders: 1 Pending: 0. BAD never enters the committed model.',
'change':'Add a version-2 payload with a different field layout and normalize it explicitly into the same internal order ID. Reject an unsupported version and preserve duplicate detection.',
'pitfall':'Deleting an outbox entry before confirmed publication can lose work. A relay retry can duplicate delivery. Copy-on-write in JavaScript does not prove database crash safety.',
'sources':['https://microservices.io/patterns/data/transactional-outbox.html','https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md']},
15: {
'hook':'Instead of storing only “8 items left,” keep the accepted stock changes that explain how the inventory reached eight.',
'targets':['Rebuild state from a sequence of domain events.', 'Separate replay from external side effects.', 'Explain projections, snapshots and concurrency risks.'],
'lesson':'''### History as the source of state

Event sourcing stores accepted domain events as the authoritative history from which state is derived. An ordinary debug log is not automatically an event store: logs can be incomplete, unstructured, rotated or unsuitable for deterministic reconstruction. A broker retained log also is not automatically an application's aggregate event store.

The example receives 10 units, reserves 3 and releases 1. Evolving state through that sequence gives 8. The evolve function validates the quantity and event type, then returns the next stock value. Unknown events are rejected instead of quietly ignored, because ignoring them could produce a misleading state.

### Decide before recording

A command asks to reserve stock. Load relevant history, reconstruct current state, check the business rule, and append a fact only when accepted. With concurrent writers, both could read the same old state and over-reserve. An expected version or equivalent concurrency check prevents blindly appending against an obsolete history.

Events need identity and ordering rules for their aggregate. Do not assume timestamps alone establish a safe total order across machines. Store the domain information necessary for reconstruction without treating mutable external services as part of the replay function.

### Projection and replay

A projection transforms events into a useful read model, such as current stock or daily reservations. Different projections can answer different questions. Rebuilding a projection should not resend emails or charge customers: those are live side effects with their own delivery policies. The pure evolve function contains no network calls, which makes repeated replay predictable.

Read models can lag behind the event store. The interface should show pending status where appropriate instead of claiming immediate consistency. A projection consumer also needs duplicate and version handling if delivery can repeat.

### Snapshots and evolution

A snapshot records derived state at a known sequence. Resume replay after that sequence rather than starting from the beginning. It is an optimization, not a replacement for deciding how old events remain interpretable. Our snapshot at sequence 2 holds 7; applying the remaining release yields 8 again.

Changing an old event's meaning can change every future replay. Use explicit schema evolution or carefully designed upcasting rather than rewriting history casually. Privacy, retention, audit and deletion requirements need deliberate design because immutable historical records complicate removal of personal information.

For simple CRUD, storing current state may be sufficient and clearer. Choose event sourcing when reconstructable history, audit or multiple projections justify the additional complexity. The local array teaches replay mechanics, not durable append-only storage or optimistic-concurrency implementation.
''',
'analogy':'A bank statement lists transactions that explain a balance. Re-reading the statement should calculate the balance, not execute all the transfers again.',
'trace':'Rebuilt stock: 8; From snapshot: 8; Replay again: 8. Replaying is deterministic and sends no external notification.',
'change':'Add a valid receipt event and calculate both full replay and snapshot replay by hand. Then try a reservation greater than available stock and explain the rejection.',
'pitfall':'Side effects inside evolve run again on every replay. A snapshot with the wrong sequence can double-apply an event. A mutable log with missing records is not a reliable source of truth.',
'sources':['https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing']},
16: {
'hook':'A reservation succeeds but payment fails. The workflow needs a recovery action, not a claim that all services can share one easy rollback.',
'targets':['Distinguish command and query models.', 'Trace a saga success and compensation path.', 'Explain why compensation is not necessarily a perfect rollback.'],
'lesson':'''### CQRS separates responsibilities

Command Query Responsibility Segregation separates the model used to change state from the model used to read it. A command model enforces rules; a query model serves useful views. They can share one database or use separate stores. CQRS does not inherently require event sourcing, microservices or a message broker.

Our status map is the write-side model; an array of ID/status records is a tiny read projection. In this script the projection is built immediately. In distributed applications it can update later, so a successful command may not instantly appear in every query. Show pending/processing states and define how the UI reconciles them.

### A saga is a workflow of local steps

A saga coordinates operations that cannot use one shared local transaction. Each participant commits its own work. If a later step fails, compensating actions attempt to reach an acceptable business outcome. Reserving inventory can be compensated by releasing it; sending a notification cannot literally be unsent. A refund is a new business operation, not erasure of the original payment.

The example reserves an ID, marks it pending, then either confirms payment or releases the reservation and marks it cancelled. A Set deletion is idempotent in this model. We intentionally simulate payment failure without using a real payment service. The catch path represents one known recovery rule, not “ignore every unknown error.”

### Orchestration versus choreography

An orchestrator explicitly chooses the next step and tracks progress. Choreography lets services react to events and publish further events. Orchestration can make the workflow easier to see; choreography can reduce central coordination but hide cycles and dependencies. Neither eliminates coupling: participants must still agree on contracts and outcomes.

Write down correlation ID, current step, completed steps and retry decisions. A real workflow must persist progress so restart does not forget which actions occurred. Commands and compensations need stable IDs because retries can happen on both forward and recovery paths.

### Failure during recovery

What if releasing inventory fails? The workflow is not simply cancelled and forgotten. It may need a retry, a compensation-pending state or a manual operator action. Use timeouts, deadlines and bounded retries, and distinguish retryable infrastructure errors from a business refusal. A circuit breaker can limit calls into a failing dependency, but does not complete the business recovery by itself.

The sample handles two orders sequentially with in-memory data. It illustrates concepts without distributed transactions or crash recovery. Keep the core activity to one successful and one compensated path. A logistics/payment microservice design from the source reports is an optional architecture diagram, not a required solo deployment.
''',
'analogy':'Booking a trip may reserve a room before a flight. If the flight fails, cancelling the room is a separate action that may have its own fee or failure—not time travel.',
'trace':'A1 is reserved then compensated; A2 is reserved then confirmed. The read model shows cancelled/confirmed, and one reservation remains active.',
'change':'Add a simulated compensation failure that records compensation-pending instead of falsely claiming cancellation. Add a bounded retry or a manual-review record, and explain your choice.',
'pitfall':'Catching a failure and labeling success hides unfinished recovery. Separate read models can lag. A saga cannot promise that irreversible actions are perfectly undone.',
'sources':['https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs','https://learn.microsoft.com/en-us/azure/architecture/patterns/saga']},
17: {
'hook':'“Something broke” is not enough information to repair an event-driven system. We need to connect an action, its reactions and the point where it was rejected.',
'targets':['Interpret structured logs and basic metrics.', 'Explain trace/correlation context and security boundaries.', 'Choose bounded recovery instead of unlimited retries.'],
'lesson':'''### Evidence that explains behavior

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
''',
'analogy':'A parcel tracking number follows one package through several depots. The daily depot volume counter answers a different question. You need both to investigate one lost package and a system-wide backlog.',
'trace':'E1 is accepted, E2 is rejected as not owner, metrics are accepted:1/rejected:1. The rejected action never reaches the success branch.',
'change':'Explain what would happen if actor.id came directly from an unverified request body. Add a malformed input during ungraded practice and inspect the rejection reason.',
'pitfall':'A correlation ID is not an authentication token. Retrying unauthorized input will not repair it. Logging entire payloads can expose data that the application otherwise protects.',
'sources':['https://opentelemetry.io/docs/concepts/observability-primer/','https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker']},
18: {
'hook':'Your final project needs a clear working story, not a collection of every library mentioned this semester.',
'targets':['Define a manageable individual project and acceptance criteria.', 'Integrate events, state rules, validation and cleanup.', 'Produce setup instructions, an event diagram and meaningful tests.'],
'lesson':'''### Choose a small vertical slice

A vertical slice connects input, decision, state change and visible evidence. The supplied board accepts an order, moves it to ready, records an event and rejects an invalid repeated transition. That is a coherent slice even without a remote broker. Your own project must add a meaningful personal feature or domain adaptation; submitting the unchanged teacher starter does not demonstrate independent work.

Possible domains include a clinic queue, library reservation, study timer, campus notification board or inventory tracker. A chat app adds connection handling; a payment/logistics architecture adds much more operational responsibility. Choose scope from the time and machines available, not from the length of the source reports.

### Write requirements that can be checked

For each core action, write one successful case and one rejected case. Example: “A nonblank item with a new ID creates one order”; “a repeated ID does not overwrite the original order.” Identify actor, command, emitted fact, payload, state and handler. Include one cleanup rule and one failure/recovery behavior.

Draw input → validation → command decision → state change → event → reaction. Label browser, Node, API and database boundaries when present. If storage is in memory, say that restart loses data. MongoDB or SQL is optional for EDP, and must sit behind the server boundary if used. A browser client should never contain database credentials.

### Read the starter's design

createBoard owns an emitter and a Map. add validates strings and uniqueness before inserting; ready checks the current state before replacing the record. It emits a copy after the change. list and history return copies so a caller cannot directly edit the stored objects. close removes the owned history listener. This is deliberately a local domain model, not an authenticated API or durable event store.

The history is a teaching audit trail. It is not a full event-sourcing implementation: it contains snapshots and does not rebuild the Map. Explain that distinction in your project write-up. Likewise, observing local events does not prove network resilience or database atomicity.

### Deliver evidence incrementally

Use small Git commits or saved checkpoints with meaningful notes. Keep installation commands, Node/package versions, sample data and non-secret configuration in a README. Run tests for valid behavior, rejected input, invalid transitions and cleanup. Screenshots can support a demo but cannot replace runnable files.

Suggested core tier: local JS/TS app with an event flow and tests. Extension tier: API, SSE or persistent data. Architecture tier: diagram brokers, outbox or sagas and explain which are actually implemented. You may share a campus domain with ADET, but EDP assessment focuses on event behavior and reliability rather than mobile styling.
''',
'analogy':'A food stall that reliably serves one complete meal is a better first delivery than an unfinished mall with twenty restaurant signs.',
'trace':'Repeated ready is handled as Invalid transition; A1 remains ready; Events prints 2; cleanup leaves 0 listeners.',
'change':'Implement one personal feature such as cancellation from waiting or a collected transition from ready. Add a success test and a rejected-transition test, plus an updated diagram.',
'pitfall':'A proposal with many features but no complete path is not an integrated project. A screenshot-only submission is difficult to reproduce. Declaring an in-memory history “durable” is inaccurate.',
'sources':['https://nodejs.org/api/events.html','https://nodejs.org/api/test.html']},
19: {
'hook':'Finals preparation is the time to repair familiar mistakes and explain your own choices—not install a new architecture.',
'targets':['Diagnose callback, cleanup and input-validation errors.', 'Explain one event path and its failure behavior.', 'Prioritize final project repairs using evidence.'],
'lesson':'''### Revisit the complete event path

Start with a user action or producer, follow the payload to validation, observe the accepted state change, then identify every reaction. Mark which steps run synchronously and which resume later. State what happens on failure and who owns cleanup. If you cannot point to the responsible handler, simplify the example before adding another abstraction.

Review setTimeout versus blocking, promise versus repeated event stream, browser listener versus Node emitter, and type checking versus runtime validation. These distinctions explain many practical mistakes. Browser propagation and Node special error events have different rules; name the environment when giving an answer.

### A controlled repair rehearsal

The supplied m19 file is the corrected version. On a separate copy, the teacher can introduce one fault at a time: change on('ready', handle) to on('ready', handle()), replace the off callback with a new arrow function, or remove trim from the input check. Predict the symptom before running. Restore the fix and explain why it works.

Do not pile several hidden faults into the first practice. One clear defect lets the student connect evidence and cause. After each repair, run a regression check to make sure the existing behavior still works. A symptom such as two reactions may come from duplicate listeners or duplicate messages; inspect the path instead of assuming one cause.

### Architecture recap in ordinary language

A queue shares work; Pub/Sub fans out reactions; a log can support replay. Idempotency protects repeated processing. An outbox links a business commit to pending publication. Event sourcing reconstructs state from accepted facts. CQRS separates write/read responsibilities. A saga coordinates local steps and compensations. None is automatically required by a small event-driven program.

Choose one architecture trade-off from your project and explain why a simpler alternative was or was not sufficient. For example, in-memory storage may be acceptable for a clearly labeled demonstration but cannot meet a requirement to survive restart. Honesty about that limit is more useful than naming a database that is not actually connected.

### Prepare for the actual assessment

Today's 10-item quiz checks taught concepts. Guided repair is practice, not a second graded coding task. The summative before the periodical and the actual final practical have their own timetable slots. Use quiz feedback to choose repairs: first failures that block the main path, then data correctness, then usability and optional polish.

Rehearse explaining a function, changing one rule and demonstrating one failure case. Record the starter code and references you used so you can distinguish your own decisions from the starter. No new framework, broker or deployment service is introduced in this finals module.
''',
'analogy':'Before a performance, musicians rehearse difficult passages and check instruments; they do not replace the entire arrangement backstage.',
'trace':'Calls: 1; Input accepted: false; Listener count: 0. Each output corresponds to one common repaired mistake.',
'change':'On a disposable copy, introduce one of the three listed faults, record its symptom, repair it, and describe the reason aloud. This is ungraded rehearsal.',
'pitfall':'Memorizing output without explaining the handler does not transfer to a new problem. A last-minute dependency upgrade can change behavior; retain the tested baseline for the practical.',
'sources':['https://nodejs.org/api/events.html','https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/removeEventListener']},
20: {
'hook':'Someone else should be able to run your project and understand what you built without guessing missing steps.',
'targets':['Package and rehearse a reproducible solo project.', 'Demonstrate successful behavior, rejected input and cleanup.', 'Explain personal work, tests and limitations clearly.'],
'lesson':'''### Verify the submitted artifact

Open the actual submission folder, not a separate working copy with uncommitted fixes. Follow its README from the beginning. Confirm entry points, package lockfile, commands and any required sample data. Document supported runtime versions and expected output. Do not include node_modules, private credentials, access tokens or real student data in the submission archive.

The m20 readiness script uses the starter board to check two orders, one transition, three history entries and listener cleanup. These checks illustrate a delivery gate; they are not a universal automatic grader for every student project. Adapt checks to your own acceptance criteria. The separate project tests cover rejected input and duplicate transitions.

### Rehearse a short, evidence-based walkthrough

Suggested five-minute sequence: state the user's problem; run the main path; show one deliberate invalid action; point to the responsible event handler and state rule; run a relevant test; explain one limitation. If the project includes a network service, show what the interface does when that service is unavailable. Do not claim a simulation demonstrates a production deployment.

Prepare one independent change that you can explain and implement, such as a new valid transition or validation rule. The instructor may ask a comparable modification during the actual practical. Understanding the data flow matters more than remembering every line verbatim.

### Evidence and documentation

Include a short architecture/event-flow diagram, a list of event names and payloads, setup instructions, tests, known limitations and references. State whether data survives restart. If using SQL or MongoDB, include a schema/seed or sample document process and a non-secret configuration template. If using only a local model, say so plainly.

Distinguish borrowed starter code, external libraries and your own additions. Explain the changes you wrote and how you checked them. A readable attribution section supports an honest discussion; it does not replace understanding the submitted implementation.

### Submission and final practical boundaries

This module's coding assessment is the preparation package and demonstration rehearsal. It is not a second name for the final practical exam. The actual exam instructions and institutional grading rules are issued separately. Do not reuse this preparation score as an exam score without an explicit instructor policy.

Use the final minutes to fix only defects that threaten the required path. Keep optional feature ideas in a future-work list. Back up the submission, run the documented checks once more and record the result. A small working system with clear limitations is an appropriate outcome for this course.
''',
'analogy':'Handing over a recipe means providing ingredients, quantities and steps—not just a photograph of the meal. A runnable project needs the same reproducibility.',
'trace':'PASS two orders; PASS first ready; PASS three domain events; PASS listeners cleaned. The separate test suite must also pass.',
'change':'Package your own project with README, event map, tests, personal feature and failure demonstration. Use the starter only as a reference, not as your unchanged final submission.',
'pitfall':'A project that runs only because of an undocumented global package is not reproducible. A successful setup on your machine does not prove a fresh installation works. Never archive secrets with the project.',
'sources':['https://docs.npmjs.com/cli/v11/commands/npm-ci','https://nodejs.org/api/test.html']}
}
