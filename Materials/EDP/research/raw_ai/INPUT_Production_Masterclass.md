Here is a comprehensive, production-grade course curriculum for **Event-Driven Programming (EDP) with JavaScript and TypeScript**.

This syllabus transitions from low-level execution mechanics and type-safe patterns to enterprise-grade distributed event architectures, stream processing, and event-sourcing patterns.

---

# Course Syllabus: Masterclass in Event-Driven Programming with JS/TS

* **Target Audience:** Intermediate-to-Advanced JavaScript/TypeScript Developers, Full-Stack Engineers, and Backend Systems Architects.
* **Prerequisites:** Sound understanding of ES6+ JavaScript, basic TypeScript generics, and asynchronous programming (`Promises`, `async/await`).
* **Tooling & Environment:** Node.js (v20+ LTS), TypeScript (v5+), RxJS, Socket.io, RabbitMQ / Apache Kafka (via Docker), Vitest / Jest, OpenTelemetry.

---

## Module 1: Event Loop Mechanics & Concurrency Engine

*Master the foundational runtime execution model that drives all non-blocking, event-driven JavaScript applications.*

### 1. Key Topics Covered

* **V8 Engine Execution Lifecycle:** Deep dive into the Call Stack, Memory Heap, and C++ bindings (`libuv` in Node.js / Browser Web APIs).
* **Queue Priority & Microtask vs Macrotask Scheduler:**
* **Macrotasks:** `setTimeout`, `setInterval`, `setImmediate`, I/O operations, DOM events.
* **Microtasks:** `Promise.then/catch/finally`, `process.nextTick`, `queueMicrotask`.
* **Render Queue:** Animation frame callbacks and browser frame budget allocation.


* **Event Loop Starvation & Lag:** Identifying event loop blocking caused by heavy CPU-bound computation vs long-running asynchronous queues.

### 2. Practical Code Pattern: Event Loop Lag Monitor

```typescript
export class EventLoopMonitor {
  private checkIntervalMs: number;
  private timer?: NodeJS.Timeout;

  constructor(checkIntervalMs: number = 1000) {
    this.checkIntervalMs = checkIntervalMs;
  }

  public start(onLagDetected: (lagMs: number) => void): void {
    let lastTime = Date.now();
    this.timer = setInterval(() => {
      const now = Date.now();
      const actualElapsed = now - lastTime;
      const lag = actualElapsed - this.checkIntervalMs;
      
      if (lag > 10) { // Threshold in ms
        onLagDetected(lag);
      }
      lastTime = now;
    }, this.checkIntervalMs);
  }

  public stop(): void {
    if (this.timer) clearInterval(this.timer);
  }
}

```

### 3. Lab / Hands-on Exercise

* **Task:** Build a microtask starvation simulator. Write a script that starves the event loop macrotask queue using recursive `process.nextTick` calls, analyze memory overhead, and re-architect it using `setImmediate` or `WorkerThreads` to restore non-blocking execution.

---

## Module 2: Type-Safe Event Architectures in TypeScript

*Eliminate event payload mismatch errors at compile time by building custom, strongly-typed event maps and emitters.*

### 1. Key Topics Covered

* **Type Maps & Generic Event Signatures:** Mapping string literal event names to structured interface payloads.
* **Type Inference & Utility Types:** Leveraging `keyof`, Index Access Types, Conditional Types, and Mapped Types for strict subscriptions.
* **Runtime Schema Validation:** Combining TypeScript types with Zod/Valibot to validate untrusted inbound runtime event payloads.

### 2. Practical Code Pattern: Zero-Dependency Type-Safe EventEmitter

```typescript
export type EventMap = Record<string, any>;

export class TypedEventEmitter<Events extends EventMap> {
  private listeners: {
    [K in keyof Events]?: Array<(payload: Events[K]) => void>;
  } = {};

  public on<K extends keyof Events>(event: K, listener: (payload: Events[K]) => void): void {
    if (!this.listeners[event]) {
      this.listeners[event] = [];
    }
    this.listeners[event]!.push(listener);
  }

  public emit<K extends keyof Events>(event: K, payload: Events[K]): void {
    const handlers = this.listeners[event];
    if (handlers) {
      handlers.forEach((listener) => listener(payload));
    }
  }

  public off<K extends keyof Events>(event: K, listener: (payload: Events[K]) => void): void {
    const handlers = this.listeners[event];
    if (handlers) {
      this.listeners[event] = handlers.filter((h) => h !== listener) as any;
    }
  }
}

// Usage Example
interface AppEvents {
  'user:registered': { userId: string; email: string; createdAt: Date };
  'order:placed': { orderId: string; amount: number };
}

const emitter = new TypedEventEmitter<AppEvents>();
emitter.on('user:registered', (data) => {
  console.log(`Welcome ${data.email}!`); // Fully typed payload
});

```

### 3. Lab / Hands-on Exercise

* **Task:** Refactor Node's native `events.EventEmitter` using TypeScript module augmentation / declaration merging to wrap existing legacy libraries with strict type checking.

---

## Module 3: Native In-Memory Event Systems

*Deep dive into Node.js `EventEmitter` and browser `EventTarget` / `CustomEvent` patterns for modular application decoupling.*

### 1. Key Topics Covered

* **Node.js `EventEmitter` Mechanics:**
* Synchronous vs Asynchronous listener invocation.
* Unhandled `'error'` event traps and process crashing behaviors.
* Memory Leak Prevention: Listener limits (`setMaxListeners`), `once()`, and teardown disposal patterns.


* **Browser DOM Events:**
* The 3-phase DOM event model: Event Capturing, Targeting, and Event Bubbling.
* High-performance UI patterns: Event Delegation and `CustomEvent` dispatching on `EventTarget`.



### 2. Lab / Hands-on Exercise

* **Task:** Build an In-Memory Order Fulfillment Pipeline. When an order is placed, emit custom events that trigger non-blocking sub-systems: Inventory Reservation, PDF Invoice Generation, Email Notification, and Fraud Detection. Handle failures cleanly using custom error events without unwinding the main process stack.

---

## Module 4: Reactive Programming & Stream Processing with RxJS

*Transition from discrete events to continuous, composable data streams using Functional Reactive Programming (FRP).*

### 1. Key Topics Covered

* **FRP Concepts:** Observables, Observers, and Subscriptions.
* **Subject Types:** `Subject`, `BehaviorSubject`, `ReplaySubject`, and `AsyncSubject` usage matrices.
* **Pipeable Operators:**
* Transformation: `map`, `scan`, `bufferTime`.
* Filtering: `filter`, `debounceTime`, `throttleTime`, `distinctUntilChanged`.
* Combination & Higher-Order Mapping: `switchMap`, `mergeMap`, `concatMap`, `exhaustMap`.


* **Backpressure Management:** Handling high-frequency telemetry/mouse/websocket events without blowing up memory.

### 2. Practical Code Pattern: Debounced Real-Time Search Stream

```typescript
import { Subject, of } from 'rxjs';
import { debounceTime, distinctUntilChanged, switchMap, catchError } from 'rxjs/operators';

interface SearchResult {
  query: string;
  results: string[];
}

export class ReactiveSearchService {
  private searchSubject = new Subject<string>();

  public searchResults$ = this.searchSubject.pipe(
    debounceTime(300), // Wait for user to stop typing
    distinctUntilChanged(), // Suppress identical consecutive queries
    switchMap((query) => this.fetchSearch(query)), // Cancel pending HTTP requests
    catchError((err) => {
      console.error('Search Stream Error:', err);
      return of({ query: '', results: [] });
    })
  );

  public onQueryInput(term: string): void {
    this.searchSubject.next(term);
  }

  private fetchSearch(query: string): Promise<SearchResult> {
    return fetch(`/api/search?q=${encodeURIComponent(query)}`).then((res) => res.json());
  }
}

```

### 3. Lab / Hands-on Exercise

* **Task:** Build a financial ticker dashboard using RxJS streams that consumes raw trade updates, computes rolling 5-second moving averages using `bufferTime` and `scan`, and dynamically throttles UI renders to 60fps.

---

## Module 5: Client-Server Real-Time Protocols

*Bridge the network gap by streaming events between backend services and frontend clients over persistent connections.*

### 1. Key Topics Covered

* **Protocol Selection Matrix:**
* **WebSockets:** Full-duplex bidirectional state sync.
* **Server-Sent Events (SSE):** Lightweight HTTP-based unidirectional data streaming.
* **WebTransport:** Low-latency UDP/QUIC-based streams.


* **Socket.io Typing Architecture:** Defining `ServerToClientEvents` and `ClientToServerEvents` interface contracts.
* **Resilience Patterns:** Heartbeat ping/pong, automatic reconnection exponential backoff, state reconnection catch-up buffers, and room broadcasting.

### 2. Lab / Hands-on Exercise

* **Task:** Implement an SSE notification endpoint in Express/Fastify with TypeScript, alongside a WebSocket multi-user collaborative room where user cursors and actions are broadcast to room participants with state reconciliation.

---

## Module 6: Distributed Event Brokers & Message Queues

*Decouple microservices using distributed, asynchronous message queues and event streaming platforms.*

### 1. Key Topics Covered

* **Broker Patterns:**
* **AMQP (RabbitMQ):** Topic/Fanout Exchanges, Message Queues, Smart Broker / Dumb Consumer logic.
* **Log Streaming (Apache Kafka / Redpanda):** Immutable commit logs, Partitioning key strategy, Consumer Groups, Offsets.


* **Reliable Delivery Guarantees:**
* At-most-once, At-least-once, and Exactly-once processing logic.
* Dead Letter Queues (DLQ) and Retry Policy Backoffs.
* The Transactional Outbox Pattern for atomic DB mutations and message publishing.



### 2. Practical Architecture Diagram: Outbox Pattern

```
┌──────────────────────────────────────────────────────────┐
│                      Microservice                        │
│                                                          │
│  ┌──────────────┐   Atomic Transaction   ┌────────────┐  │
│  │ State Update │ ──────────────────────>│ Outbox DB  │  │
│  └──────────────┘                        │   Table    │  │
│                                          └─────┬──────┘  │
└────────────────────────────────────────────────┼─────────┘
                                                 │
                                           Polling / CDC
                                                 │
                                                 ▼
                                     ┌──────────────────────┐
                                     │ Outbox Relay Worker  │
                                     └───────────┬──────────┘
                                                 │
                                        Publish Event
                                                 │
                                                 ▼
                                     ┌──────────────────────┐
                                     │ RabbitMQ / Kafka     │
                                     └──────────────────────┘

```

### 3. Lab / Hands-on Exercise

* **Task:** Spin up RabbitMQ via Docker. Implement a Distributed Payment Microservice in Node.js/TS that publishes `PaymentProcessed` events to a topic exchange, handles queue failures with a Dead Letter Queue (DLQ), and ensures idempotent consumer processing using Redis lock keys.

---

## Module 7: Enterprise EDP Patterns (Event Sourcing, CQRS & Saga)

*Architect complex business systems around domain events rather than mutative state tables.*

### 1. Key Topics Covered

* **Event Sourcing:** Storing system state as an immutable, append-only log of domain events (`OrderCreated`, `ItemAdded`, `PaymentCaptured`).
* **CQRS (Command Query Responsibility Segregation):** Decoupling Write Models (handling Commands) from Read Models (building optimized Read Projections).
* **Saga Orchestration vs Choreography:** Managing distributed multi-service transactions with compensating events to revert state on partial workflow failures.

### 2. Practical Code Pattern: Event-Sourced Aggregate Base

```typescript
export interface DomainEvent<T = any> {
  eventId: string;
  aggregateId: string;
  eventType: string;
  payload: T;
  timestamp: number;
  version: number;
}

export abstract class AggregateRoot {
  public id!: string;
  public version: number = 0;
  private uncommittedEvents: DomainEvent[] = [];

  protected applyChange(event: DomainEvent, isNew: boolean = true): void {
    this.mutate(event);
    if (isNew) {
      this.version++;
      event.version = this.version;
      this.uncommittedEvents.push(event);
    }
  }

  public loadFromHistory(history: DomainEvent[]): void {
    history.forEach((event) => {
      this.mutate(event);
      this.version = event.version;
    });
  }

  public getUncommittedEvents(): DomainEvent[] {
    return this.uncommittedEvents;
  }

  public markEventsAsCommitted(): void {
    this.uncommittedEvents = [];
  }

  protected abstract mutate(event: DomainEvent): void;
}

```

### 3. Lab / Hands-on Exercise

* **Task:** Build an Event-Sourced Bank Account aggregate in TypeScript. Implement commands (`DepositMoney`, `WithdrawMoney`) that generate events, rebuild account balances from event history, and create a Read Model projection in PostgreSQL or MongoDB.

---

## Module 8: Testing, Observability, & Production Engineering

*Ensure high reliability, visibility, and performance across complex event-driven workflows.*

### 1. Key Topics Covered

* **Event System Testing Strategies:**
* Unit testing custom EventEmitters and RxJS streams using Vitest / Marble Diagrams.
* Integration testing distributed message queues with Testcontainers.


* **Distributed Tracing & Context Propagation:**
* Injecting and extracting trace contexts (`traceparent` HTTP/AMQP headers) across microservice event boundaries using OpenTelemetry.


* **Production Security & Resilience:**
* Circuit Breakers (using Opossum library).
* Rate limiting high-frequency event ingress.



---

## Capstone Project Blueprint

### Real-Time Distributed Logistics & Delivery Tracking System

Students construct an end-to-end event-driven application:

```
┌─────────────────┐      WebSockets / SSE      ┌──────────────────┐
│  Driver App /   │ ─────────────────────────> │ Express/Fastify  │
│  Client Tracker │                            │ Gateway (TS)     │
└─────────────────┘                            └────────┬─────────┘
                                                        │
                                                 Emit Location
                                                        │
                                                        ▼
┌─────────────────┐     Topic Consumer         ┌──────────────────┐
│ Read Projection │ <───────────────────────── │ Apache Kafka /   │
│ Service (Redis) │                            │ RabbitMQ Broker  │
└─────────────────┘                            └────────┬─────────┘
                                                        │
                                              Trigger State Saga
                                                        │
                                                        ▼
                                               ┌──────────────────┐
                                               │ Billing & Driver │
                                               │ Microservices    │
                                               └──────────────────┘

```

#### Key Capstone Requirements:

1. **Frontend (React / Vite + TypeScript):** Subscribes to live driver coordinates via WebSockets, renders moving markers on a map, and utilizes RxJS to smooth out incoming telemetry.
2. **API Gateway (Node.js + TS):** Ingests driver geolocation updates, validates payloads using Zod, and pushes events into an AMQP/Kafka message broker.
3. **Microservices Architecture:**
* **Location Service:** Consumes raw updates and computes distance using spatial math.
* **ETA Calculation Service:** Computes remaining travel time using buffered stream averages.
* **Billing Saga Service:** Listens for `TripCompleted` events, triggers payment authorization, and handles compensating events (`RefundPayment`) if delivery validation fails.


4. **Observability:** Instrument all services with OpenTelemetry to trace a single event path from the driver's device through Kafka down to the billing service.