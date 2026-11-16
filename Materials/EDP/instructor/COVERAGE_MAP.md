# EDP compiled-contents coverage map

Every compiled subsection is mapped to its lesson below. Main-lesson prose explains the concepts; the runnable core implements a smaller subset. Advanced comparisons are reference/discussion, not an additional required installation or graded exercise.

## M01: Foundations of Event-Driven Programming and Day-One Refresher

[Lesson](../modules/EDP_M01.md)

- 1.1 Opening and programming refresher
- 1.1.1 First delayed callback: setTimeout
- 1.2 What event-driven programming means
- 1.3 Vocabulary and event anatomy
- 1.4 Events, commands, and queries
- 1.5 Observer and Pub/Sub preview
- 1.6 Environment and strict TypeScript workspace
- 1.7 Benefits, costs, and fit

## M02: The JavaScript Event Loop, Concurrency, and Async Primitives

[Lesson](../modules/EDP_M02.md)

- 2.1 Engine versus host
- 2.2 Execution mechanics
- 2.3 Promises and async/await introduction
- 2.4 Node-specific phases and scheduling
- 2.5 Non-blocking I/O, concurrency, and parallelism
- 2.6 Starvation and event-loop lag

## M03: Client-Side DOM Events and Interactive Interfaces

[Lesson](../modules/EDP_M03.md)

- 3.1 HTML, script placement, and the first event listener
- 3.2 Input, forms, and accessible interaction
- 3.3 Propagation and default actions
- 3.4 Delegation and dynamic elements
- 3.5 Listener options and disposal
- 3.6 Custom events and browser lifecycle
- 3.7 Other browser event sources

## M04: In-Process Node.js Events and Native Event Sources

[Lesson](../modules/EDP_M04.md)

- 4.1 EventEmitter fundamentals
- 4.2 Managing listeners
- 4.3 Error and async-listener policy
- 4.4 Small event service design
- 4.5 Promise and iterator helpers
- 4.6 Other Node sources and shutdown

## M05: Async Patterns, Cancellation, and Race Conditions

[Lesson](../modules/EDP_M05.md)

- 5.1 Choosing a completion model
- 5.2 Sequential versus concurrent work
- 5.3 HTTP and data validation
- 5.4 Cancellation and timeout policies
- 5.5 Stale-response protection
- 5.6 Debounce and throttle
- 5.7 Async iteration and cleanup

## M06: Type-Safe Event Systems in TypeScript

[Lesson](../modules/EDP_M06.md)

- 6.1 Strengthening the starter types
- 6.2 DOM typings and narrowing
- 6.3 Event maps and generic APIs
- 6.4 Typed custom events and domain unions
- 6.5 Typed emitter behavior
- 6.6 Node typing and runtime schemas

## M07: Core Patterns, State Machines, and Framework Connections

[Lesson](../modules/EDP_M07.md)

- 7.1 Observer versus Pub/Sub in depth
- 7.2 Mediator and event bus
- 7.3 Commands, facts, and queries
- 7.4 State machines
- 7.5 Framework and reactive connections
- 7.6 Domain modeling

## M08: Reactive Programming and RxJS Streams

[Lesson](../modules/EDP_M08.md)

- 8.1 Reactive vocabulary
- 8.2 Stream creation and transformation
- 8.3 Time and higher-order operators
- 8.4 Error, lifetime, and sharing
- 8.5 Stream testing

## M09: Client–Server Real-Time Events and Messaging Channels

[Lesson](../modules/EDP_M09.md)

- 9.1 Transport selection
- 9.2 Connection lifecycle
- 9.3 Message identity and safety
- 9.4 Browser channels
- 9.5 Real-time deployment concerns

## M10: Streams, Backpressure, Workers, and Background Work

[Lesson](../modules/EDP_M10.md)

- 10.1 Stream model
- 10.2 Pipeline lifecycle
- 10.3 Backpressure and bounded buffers
- 10.4 Async iterables
- 10.5 CPU work and workers
- 10.6 Scheduling and shutdown boundaries

## M11: Testing and Debugging Event-Driven Programs

[Lesson](../modules/EDP_M11.md)

- 11.1 Test design
- 11.2 Listener contract tests
- 11.3 Async and timing tests
- 11.4 Tools and layers
- 11.5 Debugging tools
- 11.6 Integration environments

## M12: Distributed Messaging, Brokers, and Event Streaming

[Lesson](../modules/EDP_M12.md)

- 12.1 From local to distributed
- 12.2 Messaging models
- 12.3 Broker concepts
- 12.4 RabbitMQ and Kafka comparison
- 12.5 Other platforms

## M13: Delivery Guarantees, Ordering, and Reliable Consumers

[Lesson](../modules/EDP_M13.md)

- 13.1 Guarantee scope
- 13.2 Acknowledgment and failure windows
- 13.3 Idempotency
- 13.4 Ordering
- 13.5 Retries and poison messages
- 13.6 Backlog policy

## M14: Reliable Publication, Outbox/Inbox, and Event Contracts

[Lesson](../modules/EDP_M14.md)

- 14.1 Dual-write problem
- 14.2 Transactional outbox
- 14.3 Inbox and consumer transaction
- 14.4 Schema evolution
- 14.5 Event envelopes and CloudEvents
- 14.6 Privacy and replay

## M15: Event Sourcing, Replay, and Read Projections

[Lesson](../modules/EDP_M15.md)

- 15.1 Event store versus ordinary log
- 15.2 Aggregate lifecycle
- 15.3 Replay and projections
- 15.4 Snapshots and evolution
- 15.5 Trade-offs and fit

## M16: CQRS, Sagas, and Distributed Workflow Coordination

[Lesson](../modules/EDP_M16.md)

- 16.1 CQRS
- 16.2 Consistency and UI design
- 16.3 Saga concepts
- 16.4 Orchestration versus choreography
- 16.5 Workflow recovery
- 16.6 Architecture fit

## M17: Observability, Security, and Production Resilience

[Lesson](../modules/EDP_M17.md)

- 17.1 Tracing an event
- 17.2 Operational signals
- 17.3 OpenTelemetry introduction
- 17.4 Security boundaries
- 17.5 Resilience tools
- 17.6 Maintenance practices

## M18: Integrated Solo Project Design and Architecture Checkpoint

[Lesson](../modules/EDP_M18.md)

- 18.1 Scope and requirements
- 18.2 Architecture artifacts
- 18.3 Implementation tiers
- 18.4 Capstone ideas from the reports
- 18.5 Delivery evidence

## M19: Finals Review, Summative Preparation, and Mock Practical

[Lesson](../modules/EDP_M19.md)

- 19.1 Review map
- 19.2 Practical rehearsal
- 19.3 Architecture recap
- 19.4 Assessment preparation

## M20: Finals Solo Project Readiness and Practical-Exam Support

[Lesson](../modules/EDP_M20.md)

- 20.1 Project verification
- 20.2 Failure and recovery rehearsal
- 20.3 Final walkthrough
- 20.4 Submission preparation

