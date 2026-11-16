# Event-Driven Programming in JavaScript & TypeScript

*A complete, hands-on course: from the event loop to event sourcing. Written from my own knowledge (web search was off), so double-check version-specific details against MDN, the Node.js docs and the TypeScript handbook.*

## Course overview

**Who it’s for:** developers who know basic JS/TS (functions, closures, promises) and want to truly understand how event-driven code works, in the browser, in Node, and across distributed systems.

**Outcome:** by the end you can reason about execution order, build typed event systems from scratch, avoid classic leaks and race conditions, and design event-driven architectures.

**Suggested pace:** 6 weeks, about 5–6 hours per week.

| Week | Modules | Deliverable |
| --- | --- | --- |
| 1 | 1–2 | Execution-order quiz + event loop notes |
| 2 | 3 | Browser project: delegation + custom events |
| 3 | 4–5 | Node pipeline with EventEmitter and async iterators |
| 4 | 6–7 | Typed event bus library with tests |
| 5 | 8–9 | Real-time app (WebSocket/SSE) + RxJS search box |
| 6 | 10–12 | Capstone: event-sourced order system |

**Setup:** Node 20+ (22 LTS recommended), TypeScript 5.x, a browser with DevTools, and optionally `vitest`, `ws`, `rxjs`.

---

## Module 1: Foundations

### 1.1 What is event-driven programming?

In **procedural** code you decide when things happen. In **event-driven** code, the flow is determined by *events*: things that happened (a click, a message arrived, a file changed, a payment succeeded). You register **handlers** (listeners/callbacks), and something else decides when to call them. This is **inversion of control**, sometimes called the Hollywood principle: *don’t call us, we’ll call you.*

### 1.2 Vocabulary

- **Event**: a record that something happened (a name/type plus data).
- **Emitter / publisher / producer**: the source of events.
- **Listener / handler / subscriber / consumer**: code that reacts.
- **Dispatcher / bus / broker**: routes events from emitters to listeners.
- **Event loop**: the runtime mechanism that picks up pending work and runs handlers.

### 1.3 Why use it?

- **Responsiveness:** UIs and servers wait for things without blocking.
- **Decoupling:** emitters don’t know who listens.
- **Scalability:** handle thousands of idle connections on one thread (Node’s model).
- **Extensibility:** add behavior by adding listeners.

### 1.4 Trade-offs (be honest about them)

- Control flow is harder to follow (“who handles this?”).
- Ordering and timing bugs (races, double handling).
- Leaks from forgotten listeners.
- Errors thrown in handlers don’t propagate to the emitter’s caller the way function calls do.

### 1.5 Comparison with other models

| Model | Who drives? | Example |
| --- | --- | --- |
| Request/response | Caller waits | `await fetch()` |
| Polling | Caller repeats | `setInterval(check)` |
| Event-driven | Source pushes | `button.addEventListener('click', …)` |
| Streaming/reactive | Source pushes a sequence | RxJS, async iterators |

**Exercise 1.1:** list five events in an app you use daily and name the emitter and the handler for each.

---

## Module 2: The JavaScript runtime and the event loop

JavaScript runs your code on a **single thread** (per realm/worker). Concurrency comes from the host environment (browser or Node) doing work off-thread and queuing callbacks.

### 2.1 The pieces

1. **Call stack:** the currently running synchronous code.
2. **Task (macrotask) queue:** `setTimeout`, I/O callbacks, UI events, `MessageChannel`, etc.
3. **Microtask queue:** promise reactions (`.then`, `await` continuations), `queueMicrotask`, `MutationObserver`.
4. **Rendering (browser):** style/layout/paint opportunities between tasks.

**The rule:** run one task; then drain the *entire* microtask queue; then (maybe) render; then pick the next task.

### 2.2 Predict the output

```js
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
queueMicrotask(() => console.log('4'));
console.log('5');
```

Output: `1, 5, 3, 4, 2`. Synchronous code first, then microtasks in order, then the timer task.

**Consequence:** a microtask that keeps scheduling microtasks can starve rendering and timers. Long synchronous work blocks *every* event handler (the UI freezes).

### 2.3 Node.js specifics

Node uses libuv. Each loop iteration has phases: **timers → pending callbacks → idle/prepare → poll (I/O) → check (`setImmediate`) → close callbacks**.

- `process.nextTick` callbacks run **before** promise microtasks, right after the current operation. Overusing them can starve I/O.
- `setImmediate` runs in the check phase. Inside an I/O callback, `setImmediate` always fires before a `setTimeout(…, 0)`. From the main module the order is not guaranteed.
- Since Node 11, microtasks are drained between each individual timer/immediate callback, matching browser behavior.

```js
import { readFile } from 'node:fs';
readFile(import.meta.filename, () => {
  setTimeout(() => console.log('timeout'), 0);
  setImmediate(() => console.log('immediate'));
  process.nextTick(() => console.log('tick'));
  Promise.resolve().then(() => console.log('promise'));
});
// tick, promise, immediate, timeout
```

### 2.4 Never block the loop

Bad: heavy CPU loops, `fs.readFileSync` in a server request path, giant `JSON.parse`. Fixes: chunk the work (yield with `setTimeout`/`scheduler.yield()` where available), use Worker Threads / Web Workers, or move it out of process.

**Exercise 2.1:** predict then run the output of a script mixing `nextTick`, `setImmediate`, `setTimeout`, `await`, and a `.then`. Explain each ordering.

**Exercise 2.2:** write a function that processes a 1,000,000-item array without freezing the UI by yielding every 1,000 items.

---

## Module 3: Events in the browser

### 3.1 The basics

```js
const btn = document.querySelector('#save');
function onSave(event) {
  console.log(event.type, event.target, event.currentTarget);
}
btn.addEventListener('click', onSave);
btn.removeEventListener('click', onSave); // same function reference needed
```

Avoid `onclick=` attributes and `element.onclick = fn` (only one handler, and mixes logic into markup).

### 3.2 Listener options

```js
el.addEventListener('scroll', handler, {
  passive: true,   // promise not to call preventDefault (smoother scrolling)
  once: true,      // auto-remove after the first call
  capture: false,  // listen in the capture phase
  signal: controller.signal, // remove when aborted
});
```

### 3.3 Propagation: capture, target, bubble

An event travels **down** from `window` to the target (capture), fires **at** the target, then travels **up** (bubble). By default listeners run on the bubble phase.

- `event.target`: the element that originated the event.
- `event.currentTarget`: the element the listener is attached to.
- `stopPropagation()`: stop moving along the path. `stopImmediatePropagation()`: also skip other listeners on the same element. Use sparingly; it breaks analytics and other code that relies on bubbling.
- `preventDefault()`: cancel the browser’s default action (form submit, link navigation). Only works if the event is `cancelable`.
- Not all events bubble: `focus`/`blur` don’t (use `focusin`/`focusout`), nor do `mouseenter`/`mouseleave` (use `mouseover`/`mouseout` or `pointerenter`).

### 3.4 Event delegation

Attach **one** listener to a stable ancestor instead of many on children. It works for dynamically added elements and uses less memory.

```js
document.querySelector('#todo-list').addEventListener('click', (e) => {
  const item = e.target.closest('[data-action]');
  if (!item || !e.currentTarget.contains(item)) return;
  const id = item.closest('li').dataset.id;
  if (item.dataset.action === 'delete') deleteTodo(id);
  if (item.dataset.action === 'toggle') toggleTodo(id);
});
```

### 3.5 Cleaning up with AbortController

```js
const controller = new AbortController();
const { signal } = controller;
window.addEventListener('resize', onResize, { signal });
window.addEventListener('keydown', onKey, { signal });
document.addEventListener('visibilitychange', onVis, { signal });

// later: removes all three at once
controller.abort();
```

This is the modern, leak-resistant pattern for components.

### 3.6 Custom events

```js
const cart = new EventTarget(); // constructible in modern browsers and Node
cart.addEventListener('item-added', (e) => console.log(e.detail));
cart.dispatchEvent(new CustomEvent('item-added', { detail: { sku: 'A1', qty: 2 } }));
```

On DOM elements, pass `{ bubbles: true, composed: true }` so the event bubbles up and crosses Shadow DOM boundaries (important for Web Components).

**Important:** `dispatchEvent` is **synchronous**; all listeners run before it returns.

### 3.7 Events you should know

- **Pointer events** (`pointerdown/move/up`) unify mouse, touch and pen. Prefer them over separate mouse/touch handlers.
- **Input/form:** `input` (every change), `change` (on commit), `submit`, `invalid`.
- **Lifecycle:** `DOMContentLoaded`, `load`, `visibilitychange`, `pagehide`. Prefer these over `unload`, which is unreliable and blocks bfcache.
- **Observers** are event-like APIs: `IntersectionObserver`, `ResizeObserver`, `MutationObserver`.
- **Messaging:** `postMessage`, `BroadcastChannel`, `MessageChannel`, `storage` event, `WebSocket`, `EventSource`.

### 3.8 Debounce and throttle

```js
export const debounce = (fn, ms) => {
  let t;
  return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), ms); };
};
export const throttle = (fn, ms) => {
  let last = 0;
  return (...args) => {
    const now = performance.now();
    if (now - last >= ms) { last = now; fn(...args); }
  };
};
```

Debounce = wait until activity stops (search box). Throttle = at most once per interval (scroll/resize). For visual updates, `requestAnimationFrame` is often better.

**Project 3 (browser):** build a Kanban board with drag-and-drop using pointer events and delegation. Components communicate only through custom events (`card:moved`, `column:changed`). Clean up with one `AbortController`.

---

## Module 4: Node.js EventEmitter and friends

### 4.1 EventEmitter

```js
import { EventEmitter } from 'node:events';

const bus = new EventEmitter();
bus.on('greet', (name) => console.log(`hi ${name}`));
bus.once('greet', (name) => console.log('first time only'));
console.log(bus.emit('greet', 'Ada')); // true (had listeners)
bus.off('greet', handler);              // alias of removeListener
```

Key behaviors:

- Listeners run **synchronously**, in **registration order**.
- `emit` returns `true` if there were listeners.
- `prependListener` puts one first. `listenerCount`, `eventNames`, `removeAllListeners` help introspection.
- **`'error'` is special:** emitting `'error'` with no listener **throws** (and can crash the process). Always attach an `'error'` handler to emitters that can fail (streams, sockets, child processes).
- Default `maxListeners` is 10 per event. Exceeding it prints a warning that usually signals a leak. Raise it deliberately, not blindly.
- `new EventEmitter({ captureRejections: true })` routes rejected async handlers to the `'error'` event.

### 4.2 Promise and async-iterator helpers

```js
import { once, on } from 'node:events';

// one-shot: wait for a single event
const [port] = await once(server, 'listening', { signal: AbortSignal.timeout(5000) });

// stream of events as an async iterator
const ac = new AbortController();
for await (const [msg] of on(emitter, 'message', { signal: ac.signal })) {
  if (msg.type === 'stop') ac.abort();
  handle(msg);
}
```

An aborted `on()` iteration throws an `AbortError`; catch it where appropriate.

### 4.3 Subclassing

```ts
import { EventEmitter } from 'node:events';

class Downloader extends EventEmitter {
  async start(url: string) {
    this.emit('start', url);
    try {
      const res = await fetch(url);
      this.emit('done', await res.arrayBuffer());
    } catch (err) {
      this.emit('error', err);
    }
  }
}
```

Prefer **composition** (hold an emitter, expose `on`) over inheritance when you want a smaller public surface.

### 4.4 Streams are event emitters

Readable/Writable/Transform streams emit `data`, `end`, `error`, `close`, `drain`. In modern code use `pipeline` (from `node:stream/promises`) instead of manual `.pipe()` chains, because it forwards errors and cleans up.

```js
import { pipeline } from 'node:stream/promises';
import { createReadStream, createWriteStream } from 'node:fs';
import { createGzip } from 'node:zlib';

await pipeline(createReadStream('in.log'), createGzip(), createWriteStream('in.log.gz'));
```

**Backpressure:** if `write()` returns `false`, wait for `'drain'`. Ignoring this is the most common cause of memory blow-ups.

### 4.5 Other Node event sources

`http.Server` (`request`, `connection`), `child_process` (`exit`, `message`), `process` (`SIGINT`, `uncaughtException`, `unhandledRejection`), `fs.watch`/`fs/promises.watch` (async iterator), `worker_threads` (`message`).

**Graceful shutdown pattern:**

```js
process.once('SIGTERM', async () => {
  server.close();           // stop accepting
  await drainQueues();      // finish in-flight work
  process.exit(0);
});
```

**Project 4 (Node):** build a log processor: `fs.watch` → parse lines (Transform stream) → emit typed events (`error-line`, `slow-request`) → listeners write alerts and metrics. Support clean shutdown.

---

## Module 5: Async patterns and events

### 5.1 Evolution

Callbacks → Promises → `async/await` → async iterators/streams/observables.

### 5.2 Promise vs event

A promise settles **once** (one result). An event can fire **many times** (or never). Use a promise for “this operation finishes”; use events/streams for “things keep happening.” Wrapping a one-shot event in a promise:

```js
const nextClick = (el, signal) => new Promise((resolve, reject) => {
  el.addEventListener('click', resolve, { once: true, signal });
  signal?.addEventListener('abort', () => reject(signal.reason), { once: true });
});
```

### 5.3 Async iteration over events

```js
async function* eventsOf(target, type, signal) {
  const queue = [];
  let wake;
  const push = (e) => { queue.push(e); wake?.(); };
  target.addEventListener(type, push, { signal });
  try {
    while (!signal.aborted) {
      while (queue.length) yield queue.shift();
      await new Promise((r) => { wake = r; signal.addEventListener('abort', r, { once: true }); });
    }
  } finally {
    target.removeEventListener(type, push);
  }
}
```

Note the buffering: producers can outpace consumers, so decide on a policy (drop, buffer limit, backpressure).

### 5.4 Cancellation

Use `AbortController`/`AbortSignal` everywhere: `fetch`, `addEventListener`, `events.once/on`, timers (`timers/promises`). Handy helpers: `AbortSignal.timeout(ms)` and `AbortSignal.any([a, b])`.

### 5.5 Race conditions

With concurrent handlers, a slow earlier response can overwrite a newer one.

```js
let controller;
input.addEventListener('input', async (e) => {
  controller?.abort();
  controller = new AbortController();
  try {
    const res = await fetch(`/search?q=${encodeURIComponent(e.target.value)}`, { signal: controller.signal });
    render(await res.json());
  } catch (err) {
    if (err.name !== 'AbortError') throw err;
  }
});
```

### 5.6 Error handling

An `async` listener returns a promise that the emitter ignores, so a throw becomes an **unhandled rejection**. Wrap handler bodies in try/catch (or use `captureRejections`), and add a global safety net (`unhandledrejection` in browsers, `process.on('unhandledRejection')` in Node) for logging, not for control flow.

**Exercise 5.1:** implement `typeahead(input)` returning an async iterable of results with debounce plus cancellation of stale requests.

---

## Module 6: TypeScript and events

### 6.1 DOM typings

```ts
const btn = document.querySelector<HTMLButtonElement>('#save');
btn?.addEventListener('click', (e) => {
  // e: MouseEvent (inferred from HTMLElementEventMap)
  console.log(e.clientX);
});

input.addEventListener('input', (e) => {
  const value = (e.target as HTMLInputElement).value; // target is EventTarget | null
});
```

Prefer `e.currentTarget` (typed to the element you attached to) over casting `e.target`. For delegation, narrow with `instanceof` or `closest`:

```ts
list.addEventListener('click', (e) => {
  if (!(e.target instanceof Element)) return;
  const row = e.target.closest<HTMLElement>('[data-id]');
  if (row) select(row.dataset.id!);
});
```

### 6.2 Typing custom DOM events (declaration merging)

```ts
interface CartDetail { sku: string; qty: number }

declare global {
  interface HTMLElementEventMap {
    'cart:item-added': CustomEvent<CartDetail>;
  }
}

el.addEventListener('cart:item-added', (e) => {
  e.detail.sku; // fully typed
});
```

### 6.3 Event maps

The core TypeScript pattern: one type mapping **event name → payload**, then generic methods constrained by `keyof`.

```ts
type AppEvents = {
  'user:login': { userId: string; at: Date };
  'user:logout': { userId: string };
  'app:ready': void;
};
```

### 6.4 Build a typed emitter from scratch

```ts
type Listener<T> = (payload: T) => void;
type Unsubscribe = () => void;

export class TypedEmitter<E extends Record<string, unknown>> {
  private listeners: { [K in keyof E]?: Set<Listener<E[K]>> } = {};

  on<K extends keyof E>(event: K, fn: Listener<E[K]>): Unsubscribe {
    (this.listeners[event] ??= new Set()).add(fn);
    return () => this.off(event, fn);
  }

  once<K extends keyof E>(event: K, fn: Listener<E[K]>): Unsubscribe {
    const off = this.on(event, (p) => { off(); fn(p); });
    return off;
  }

  off<K extends keyof E>(event: K, fn: Listener<E[K]>): void {
    this.listeners[event]?.delete(fn);
  }

  emit<K extends keyof E>(event: K, ...args: E[K] extends void ? [] : [payload: E[K]]): void {
    for (const fn of [...(this.listeners[event] ?? [])]) {
      try {
        fn(args[0] as E[K]);
      } catch (err) {
        queueMicrotask(() => { throw err; }); // isolate failing listeners
      }
    }
  }
}

const bus = new TypedEmitter<AppEvents>();
const off = bus.on('user:login', ({ userId }) => console.log(userId));
bus.emit('user:login', { userId: 'u1', at: new Date() });
bus.emit('app:ready');            // no payload needed
// bus.emit('user:login');        // error: payload required
// bus.emit('nope', 1);           // error: unknown event
```

Design choices worth noting: iterating a **copy** of the set so listeners can unsubscribe during emit; returning an **unsubscribe function** (great for cleanup); isolating listener errors so one bad handler doesn’t break the rest.

### 6.5 Discriminated unions for domain events

```ts
type DomainEvent =
  | { type: 'OrderPlaced'; orderId: string; total: number }
  | { type: 'OrderShipped'; orderId: string; carrier: string }
  | { type: 'OrderCancelled'; orderId: string; reason: string };

type Handlers = {
  [E in DomainEvent as E['type']]: (event: E) => void | Promise<void>;
};

function handle(e: DomainEvent, handlers: Partial<Handlers>) {
  const h = handlers[e.type] as ((e: DomainEvent) => unknown) | undefined;
  return h?.(e);
}

function describe(e: DomainEvent): string {
  switch (e.type) {
    case 'OrderPlaced': return `placed ${e.total}`;
    case 'OrderShipped': return `shipped via ${e.carrier}`;
    case 'OrderCancelled': return `cancelled: ${e.reason}`;
    default: { const _exhaustive: never = e; return _exhaustive; } // compile error if a case is missed
  }
}
```

The `never` check makes adding a new event a compile-time to-do list.

### 6.6 Typing Node’s EventEmitter

Recent `@types/node` versions let you pass a generic event map: `class Foo extends EventEmitter<{ ready: [] ; data: [Buffer] }>`, where each value is the **tuple of listener arguments**. Check the version of your typings; older ones are untyped (`any[]`).

### 6.7 Runtime validation

Types vanish at runtime. Events crossing a boundary (network, queue, `postMessage`) must be validated, e.g. with Zod or Valibot, then narrowed to your event types. Also **version** your event schemas (`type: 'OrderPlaced.v2'`).

**Project 1:** package your `TypedEmitter` as a library with `vitest` tests covering ordering, `once`, unsubscribe during emit, and listener errors.

---

## Module 7: Core patterns

### 7.1 Observer vs Pub/Sub

- **Observer:** subject holds its observers directly (`emitter.on`). Tight coupling; synchronous; in-process.
- **Pub/Sub:** publishers and subscribers know only a **topic** and a broker. Decoupled in space (and often time). Can cross processes.

### 7.2 Mediator / event bus

A central bus reduces point-to-point wiring, but a global bus becomes a hidden dependency graph. Keep topics **namespaced** (`orders:placed`), document them, and prefer scoped buses (per feature/component) over one global singleton.

### 7.3 Commands vs events vs queries

- **Command:** a request to do something; may fail; one handler (`PlaceOrder`).
- **Event:** a fact in the past tense; cannot be rejected; zero-to-many handlers (`OrderPlaced`).
- **Query:** asks for data, no side effects.

Name events in the **past tense** and keep them about business facts, not UI mechanics.

### 7.4 State machines

Events + explicit states prevent impossible states. XState is the standard JS library; the idea fits in a few lines:

```ts
type State = 'idle' | 'loading' | 'success' | 'error';
type Evt = 'FETCH' | 'RESOLVE' | 'REJECT' | 'RETRY';
const transitions: Record<State, Partial<Record<Evt, State>>> = {
  idle: { FETCH: 'loading' },
  loading: { RESOLVE: 'success', REJECT: 'error' },
  success: { FETCH: 'loading' },
  error: { RETRY: 'loading' },
};
const next = (s: State, e: Evt): State => transitions[s][e] ?? s;
```

### 7.5 Reactive streams with RxJS

An **Observable** is a lazy, cancellable stream of events that you can compose with operators.

```ts
import { fromEvent, debounceTime, map, distinctUntilChanged, switchMap } from 'rxjs';
import { ajax } from 'rxjs/ajax';

fromEvent<InputEvent>(input, 'input').pipe(
  map((e) => (e.target as HTMLInputElement).value.trim()),
  debounceTime(300),
  distinctUntilChanged(),
  switchMap((q) => ajax.getJSON(`/search?q=${encodeURIComponent(q)}`)), // cancels stale requests
).subscribe(render);
```

Flattening operators: `switchMap` (latest wins), `mergeMap` (all in parallel), `concatMap` (queue in order), `exhaustMap` (ignore while busy, ideal for submit buttons). Always **unsubscribe** (or use `takeUntil`) to avoid leaks.

### 7.6 Signals (a different take)

Frameworks (Solid, Angular, Vue refs, Preact signals) use **fine-grained reactivity**: state changes push updates to dependents automatically. It overlaps with events but models *current value over time* rather than *discrete occurrences*. A TC39 Signals proposal exists; check its current status before relying on it.

---

## Module 8: Event-driven architecture across systems

### 8.1 Transports in JS land

| Need | Tool |
| --- | --- |
| Server → browser stream (one way) | Server-Sent Events (`EventSource`) |
| Bidirectional real-time | WebSocket (`ws`, Socket.IO) |
| Third-party callbacks | Webhooks (HTTP POST to your endpoint) |
| Background jobs | BullMQ (Redis), pg-boss (Postgres) |
| Message brokers | RabbitMQ, NATS, Redis Streams |
| Durable event log at scale | Kafka (KafkaJS and similar clients) |
| Cloud | AWS SNS/SQS/EventBridge, Google Pub/Sub, Azure Service Bus |

A minimal WebSocket server:

```ts
import { WebSocketServer, WebSocket } from 'ws';

const wss = new WebSocketServer({ port: 8080 });
wss.on('connection', (socket) => {
  socket.on('message', (raw) => {
    for (const client of wss.clients) {
      if (client !== socket && client.readyState === WebSocket.OPEN) client.send(raw.toString());
    }
  });
  socket.on('error', console.error);
});
```

SSE in the browser is simpler when you only need server push and gets automatic reconnect:

```js
const es = new EventSource('/events');
es.addEventListener('order-updated', (e) => render(JSON.parse(e.data)));
```

### 8.2 Delivery guarantees

- **At-most-once:** may lose messages.
- **At-least-once:** may duplicate. The practical default in most brokers.
- **Exactly-once:** achieved in practice by at-least-once plus **idempotent consumers**.

```ts
async function onPaymentReceived(evt: { eventId: string; orderId: string }) {
  const firstTime = await db.processedEvents.insertIfAbsent(evt.eventId); // unique key
  if (!firstTime) return;          // duplicate: ignore
  await markOrderPaid(evt.orderId);
}
```

### 8.3 Ordering, retries, poison messages

- Ordering is usually guaranteed only **per partition/key** (e.g., per `orderId`), not globally.
- Retry with **exponential backoff and jitter**.
- After N failures, move the message to a **dead-letter queue** for inspection rather than blocking the stream.

### 8.4 The outbox pattern

Problem: you update the database *and* publish an event; one can succeed without the other. Solution: in the **same DB transaction**, write the state change and an `outbox` row. A separate relay reads the outbox and publishes, marking rows sent. You get reliable publishing with at-least-once semantics.

### 8.5 Event sourcing and CQRS

**Event sourcing:** store the sequence of events as the source of truth; current state is a fold over them.

```ts
type Account = { balance: number };
type AccountEvent =
  | { type: 'Deposited'; amount: number }
  | { type: 'Withdrew'; amount: number };

const apply = (s: Account, e: AccountEvent): Account =>
  e.type === 'Deposited' ? { balance: s.balance + e.amount } : { balance: s.balance - e.amount };

const rebuild = (events: AccountEvent[]) => events.reduce(apply, { balance: 0 });
```

Benefits: full audit trail, time travel, new read models by replaying. Costs: schema evolution, replay time (use snapshots), eventual consistency, and a learning curve. **CQRS** separates the write model from read models (projections built from events). Don’t adopt either unless you need the audit/replay properties.

### 8.6 Sagas

Long-running workflows across services (reserve stock → charge card → ship). Each step reacts to an event and emits the next; failures trigger **compensating actions** (refund, release stock). Two styles: **choreography** (services react to each other’s events) and **orchestration** (a coordinator directs steps). Choreography is simple at first but becomes hard to trace; orchestration is more explicit.

### 8.7 Observability

Propagate a **correlation ID** and trace context (OpenTelemetry) in every event’s metadata. A typical envelope:

```ts
interface EventEnvelope<T> {
  id: string;          // unique, for idempotency
  type: string;        // 'OrderPlaced.v1'
  occurredAt: string;  // ISO timestamp
  correlationId: string;
  causationId?: string; // id of the event/command that caused this
  data: T;
}
```

---

## Module 9: Frameworks and event handling

- **React:** uses a synthetic-event layer on top of native events (since React 17, attached at the root container). Handlers are props (`onClick`), and state updates are batched. Use `useEffect` with a cleanup function (or `AbortController`) for non-React event sources (`window`, WebSocket). A stale-closure bug is the classic trap: handlers capture the state from the render in which they were created.
- **Vue:** `defineEmits` plus `@event` for child → parent communication; props down, events up.
- **Web Components:** custom elements communicate outward via `CustomEvent` (`bubbles`, `composed`); read about retargeting of `event.target` across shadow roots.
- **Angular:** `@Output()` with `EventEmitter` (or the newer `output()` API) and RxJS everywhere.
- **Node frameworks:** Express middleware is callback-chained, Fastify has hooks/lifecycle events, NestJS provides an event-emitter module and microservice transports.

```tsx
function useWindowEvent<K extends keyof WindowEventMap>(type: K, handler: (e: WindowEventMap[K]) => void) {
  const ref = useRef(handler);
  ref.current = handler; // always the latest closure
  useEffect(() => {
    const ac = new AbortController();
    window.addEventListener(type, (e) => ref.current(e), { signal: ac.signal });
    return () => ac.abort();
  }, [type]);
}
```

---

## Module 10: Testing and debugging

### 10.1 Testing

- **Fake timers** for debounce/throttle (`vi.useFakeTimers()` in Vitest, `jest.useFakeTimers()` in Jest).
- Test emitters through public behavior: ordering, unsubscribe, errors, and `once` semantics.
- Await events with `events.once` plus a timeout signal so tests fail instead of hanging.
- In the DOM, use `@testing-library` and `userEvent` to dispatch realistic event sequences (`pointerdown` → `pointerup` → `click`).
- Assert **no leaks**: after teardown, `emitter.listenerCount('x') === 0`.

```ts
import { test, expect, vi } from 'vitest';

test('debounce fires once', () => {
  vi.useFakeTimers();
  const fn = vi.fn();
  const d = debounce(fn, 100);
  d(); d(); d();
  vi.advanceTimersByTime(100);
  expect(fn).toHaveBeenCalledTimes(1);
  vi.useRealTimers();
});
```

### 10.2 Debugging

- Chrome DevTools: Elements → **Event Listeners** pane; the console helpers `getEventListeners(el)` and `monitorEvents(el, 'click')`; Sources → **Event Listener Breakpoints**; Performance panel for long tasks and loop blocking.
- Node: `--trace-warnings` (shows where a max-listener warning came from), `--inspect`, `emitter.eventNames()`/`listenerCount()`, and `diagnostics_channel`/`async_hooks`/`AsyncLocalStorage` for tracing context across async boundaries.
- Log **event name, correlation ID and handler duration**. Slow handlers are your first suspect for lag.

---

## Module 11: Best practices and pitfalls

**Do**

1. Always provide a way to unsubscribe, and use it (return an unsubscribe function or accept an `AbortSignal`).
2. Keep handlers small and fast; offload heavy work.
3. Name events clearly (`domain:past-tense-fact`) and type their payloads.
4. Use delegation for lists and dynamic content.
5. Make consumers idempotent and handle duplicates and out-of-order delivery.
6. Validate and version events that cross trust or process boundaries.
7. Decide error and backpressure policies explicitly.

**Don’t**

1. Register a listener inside another listener or render path without cleanup (duplicate handlers).
2. Mutate shared event payloads (listeners will see each other’s changes). Freeze or copy.
3. Rely on listener order across modules; it’s an accident waiting to happen.
4. Emit events synchronously from constructors (no one has subscribed yet).
5. Build long chains where event A triggers B triggers C, with no one able to see the flow. Document it or switch to an explicit workflow.
6. Assume `emit` waits for async listeners. It doesn’t.
7. Use events where a plain function call is clearer. Not everything needs to be decoupled.

**Common bug checklist:** forgot `removeEventListener`; passed a different function reference; arrow function created inline on removal; `this` binding lost; async handler swallowing errors; stale closure; duplicate subscription on re-render; listener added after the event already fired (subscribe *before* triggering the work).

---

## Module 12: Capstone project

**Build an event-sourced order system in TypeScript.**

Requirements:

1. **Domain events** as a discriminated union (`OrderPlaced`, `PaymentCaptured`, `OrderShipped`, `OrderCancelled`) with a standard envelope (id, type, version, correlationId).
2. An **event store** (start with an in-memory append-only array, then SQLite/Postgres) with optimistic concurrency per aggregate.
3. **Command handlers** that validate and append events; **projections** that build read models (orders by status, daily revenue).
4. A **typed event bus** (from Module 6) delivering events to projections and a **saga** that handles payment failure with compensation.
5. **Idempotent consumers**, retries with backoff, and a dead-letter list.
6. A **real-time dashboard** via SSE or WebSocket that updates as events occur.
7. Tests: replay produces identical state, duplicate events are ignored, fake timers cover retries.
8. Stretch: swap the in-memory bus for NATS, Redis Streams or RabbitMQ without changing domain code; add OpenTelemetry tracing.

**Grading rubric (self-assess):** correctness of replay (25%), type safety and exhaustive handling (20%), failure handling and idempotency (25%), observability (10%), test quality (10%), code clarity (10%).

**Other projects along the way:** Project 1 (typed emitter library, Module 6), Project 3 (Kanban board, Module 3), Project 4 (log processor, Module 4), and a real-time chat with WebSocket plus SSE fallback (Module 8).

---

## Practice questions (with answers)

**Q1.** What prints?

```js
setTimeout(() => console.log('A'), 0);
Promise.resolve().then(() => console.log('B'));
process.nextTick(() => console.log('C'));
console.log('D');
```

**A1.** `D, C, B, A`. Sync first, `nextTick` before promise microtasks, then the timer.

**Q2.** Why does this leak, and how do you fix it?

```js
function mount() {
  window.addEventListener('resize', () => update());
}
```

**A2.** The anonymous listener can’t be removed and `mount` may run repeatedly. Pass an `AbortSignal` (or keep the function reference) and abort/remove on unmount.

**Q3.** What’s the difference between `event.target` and `event.currentTarget`?

**A3.** `target` is where the event originated; `currentTarget` is the element whose listener is currently running. They differ during bubbling/delegation.

**Q4.** What happens if you `emit('error', new Error('x'))` with no `'error'` listener in Node?

**A4.** The error is thrown; if uncaught it crashes the process.

**Q5.** Which RxJS operator for a search box, and why? Which for a Save button?

**A5.** `switchMap` (cancels stale requests so the latest query wins). `exhaustMap` for Save (ignore clicks while a save is in flight).

**Q6.** Why are idempotent consumers necessary?

**A6.** Most brokers deliver at-least-once, so duplicates will occur; idempotency makes repeats harmless and yields effectively-once processing.

**Q7.** When should you avoid event-driven design?

**A7.** When a direct call is simpler and the coupling is acceptable, when you need strict synchronous request/response semantics, or when the team can’t yet observe/debug asynchronous flows.

**Q8.** Why can `passive: true` improve scrolling?

**A8.** The browser knows the handler won’t call `preventDefault`, so it can scroll immediately without waiting for your code.

---

## Cheat sheet

| Task | Use |
| --- | --- |
| Remove many listeners at once | `AbortController` signal option |
| One-shot event as a promise | `events.once()` (Node) / custom `once: true` wrapper |
| Events as a stream | `events.on()` async iterator, RxJS `fromEvent` |
| Many dynamic children | Event delegation with `closest()` |
| Cross-component messaging (DOM) | `CustomEvent` with `bubbles` and `composed` |
| Cancel stale async work | `AbortController`, `switchMap` |
| Type event names/payloads | Event map plus `K extends keyof E` |
| Exhaustive event handling | Discriminated union plus `never` check |
| Reliable publish from DB | Outbox pattern |
| Duplicate deliveries | Idempotency key table |

---

## Further reading and resources

*Heads-up: I can’t search or browse a database right now, so these are from memory and I may have details wrong. Please verify titles, URLs and authors before relying on them.*

- **MDN Web Docs:** pages on *Event reference*, *Introduction to events*, *EventTarget*, *AbortController*, and *Using microtasks*.
- **Node.js docs:** *Events*, *The Node.js Event Loop, Timers, and process.nextTick()*, *Stream*, *Worker threads*.
- **TypeScript Handbook:** sections on generics, mapped types, discriminated unions, and declaration merging.
- **javascript.info:** the *Events* and *Event loop* chapters.
- **Philip Roberts’ talk “What the heck is the event loop anyway?”** (JSConf EU), a classic visual intro.
- **Jake Archibald’s “In The Loop”** (JSConf.Asia), a deeper look at tasks, microtasks and rendering.
- **RxJS documentation** (rxjs.dev) and the *Learn RxJS* site.
- ***Enterprise Integration Patterns*** (Hohpe and Woolf) for messaging patterns.
- ***Designing Data-Intensive Applications*** (Martin Kleppmann) for logs, streams and consistency.
- **Martin Fowler’s articles** on event sourcing, CQRS and “What do you mean by Event-Driven?”.
- **Microservices.io** (Chris Richardson) for saga and transactional outbox patterns.

**Next steps:** pick the first project, build it, and tell me where you get stuck. I can review your code, generate quizzes per module, or expand any section (WebSockets, RxJS, event sourcing) into its own deep-dive.
