LESSONS = {
1: {
'hook': 'Imagine the canteen taking another order while your food is being prepared. The cashier does not freeze until your meal is ready. Today we connect familiar programming syntax to that kind of response.',
'targets': ['Trace variables, a condition, a loop and a function in one short program.', 'Identify a producer, listener and payload.', 'Predict delayed callback output and cancel a pending timer.'],
'lesson': '''### Values, decisions, repetition and functions

`const` binds a name that cannot be reassigned; it does not make every object stored there deeply immutable. Use `let` when a binding changes, such as a running total. In our program, `prices` is an array, `total` is a number, and the `for...of` loop visits each price. `total += price` means “add this price to the current total.” After two iterations, 25 + 35 gives 60.

An `if/else` selects a branch using a Boolean condition. `canAfford(100, 60)` returns true because the budget is at least the cost. A function receives parameters and may return a result; returning is different from printing. `console.log` displays something, while `return` makes a value available to the caller. A `while` loop repeats while a condition holds; unlike our bounded array loop, it needs a condition that eventually becomes false.

An object groups related properties: `{ id: 'A1', total: 60 }`. A function can itself be a value. Putting `invoice` in an array stores its function reference; writing `invoice(order)` calls it. That difference is the bridge to callbacks. *Ipinapasa natin ang gagawin; hindi pa natin ginagawa.*

### From direct calls to reactions

Procedural code says “do step A, then B.” Event-driven code also performs setup, but registers reactions that execute when a relevant occurrence is reported. The producer reports an occurrence; the listener handles it; the payload carries useful data. An order-created event may trigger both an invoice and a kitchen notice. Neither reaction is automatically asynchronous: our loop calls both listeners synchronously.

Observer commonly involves a subject holding listener references. Pub/Sub introduces a topic or channel between publishers and subscribers. These patterns reduce some direct dependencies, but they do not remove the need for agreed payloads and error policies. A command requests an action (`prepareOrder`); an event reports a fact (`order.created`); a query requests information (`getOrder`). A button click is a UI event with an API-defined name, not necessarily a past-tense domain name.

### Schedule a callback, not a frozen program

`setTimeout(callback, delay)` schedules a one-time callback. The delay is milliseconds: 1000 means one second. The code after the call continues immediately. A timer can execute later than requested when other work or host scheduling intervenes. Even zero delay does not interrupt the currently running JavaScript. Save the returned handle to cancel pending work with `clearTimeout(handle)`. Cancellation cannot undo a callback that already executed.

The example uses 50 milliseconds to keep classroom tests quick; change it to 1000 to observe the pause. The “Taking the next order” message appears before “Ready na ang order!” Do not implement delay using a busy loop: that keeps the thread occupied. Module 2 explains the scheduling model; today's goal is to see and describe the behavior.

### Workspace and fit

Run `.mjs` files with Node; use the browser for HTML/DOM examples. The supplied `m01-types.ts` adds an interface and typed function. Run the pack's type-check command before running TypeScript; execution alone is not a type check. `strict` helps find mistakes, but external data still needs runtime validation.

Events are useful when multiple independent reactions follow a change. For one simple calculation, a direct function call is often easier. More events can mean harder tracing and listener cleanup. Today’s emitter is deliberately a small loop; Node's established event API arrives in Module 4.
''',
'analogy':'A canteen bell announces that an order is ready. One person collects the food, another updates the board. The bell does not determine what each person must do, but they must understand what it means.',
'trace':'Total: 60 → Order accepted → Invoice: A1 → Kitchen: A1 → Taking the next order → Ready na ang order! The cancelled message never appears.',
'change':'Change the budget to 40, add a third price, and predict the branch and total before running. The sample still broadcasts its demonstration event after the affordability branch; explain how you would move publication inside the accepted branch for real ordering.',
'pitfall':'If the callback runs during registration, you likely wrote `setTimeout(fn(), 1000)` instead of passing `fn` or `() => fn()`. If a string price produces unexpected addition, inspect its type before calculating.',
'sources':['https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide','https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout','https://www.typescriptlang.org/tsconfig/strict.html']},
2: {
'hook':'A program prints A, B, C and D, but the source code mentions D before B. This is predictable scheduling—not random behavior.',
'targets':['Predict synchronous, promise and timer output in the supplied example.', 'Write and handle a promise using async/await.', 'Distinguish concurrency from CPU parallelism.'],
'lesson':'''### The engine and its host

JavaScript executes function calls on a call stack. A call adds a frame; returning removes it. Objects live in managed memory, often described as the heap. The engine executes language instructions, while the host supplies capabilities such as timers, files or networking. Browsers expose DOM/Web APIs; Node combines its own APIs with runtime infrastructure including libuv. Do not draw browser DOM work inside Node as though every environment were identical.

Ordinary synchronous code runs to completion before another queued callback can use that JavaScript thread. In our example the initial logs run first. Resolving a promise schedules its reaction; it does not run that reaction in the middle of the current statements. The timer callback becomes eligible later. For this particular example, the promise reaction precedes the zero-delay timer.

### Tasks and microtasks

Browser task sources include timers and input events. Promise reactions and `queueMicrotask` use the microtask mechanism. At a microtask checkpoint, queued microtasks are drained, including newly queued ones. A never-ending chain can prevent other work from progressing. Rendering opportunities depend on browser scheduling; “every timer causes a repaint” is not a valid rule.

Node has phases such as timers, poll, check and close callbacks. `setImmediate` relates to the check phase; `process.nextTick` has special Node scheduling behavior and can starve I/O if abused. The relative ordering of nextTick, promises, timers and immediate callbacks depends on context, including CommonJS versus ES modules. Our files are ES modules. Learn the measured trace first; do not memorize one global diagram as a guarantee for all contexts.

### A promise describes one eventual outcome

A promise starts pending and settles fulfilled or rejected. Its executor runs immediately when constructed. In `prepare`, the executor schedules a timer, then the timer later calls `resolve` or `reject`. Settling is different from a repeated event stream: one promise does not keep producing values.

An `async` function returns a promise. `await` suspends that function's continuation until the awaited result is available; it does not pause all JavaScript. Use `try/catch` around awaited operations to handle rejection, and `finally` for cleanup that should occur on either path. In the example A2 rejects, so its success log is skipped and the catch runs. A finally block is not proof of success.

### Concurrency, parallelism and responsiveness

Concurrency means operations can make progress during overlapping periods, such as waiting for two requests. Parallelism means work actually executes simultaneously. Writing `async` before a function containing a huge CPU loop does not move the loop to another thread. Use a worker for suitable CPU-heavy work, or break work into bounded pieces when appropriate.

Event-loop lag is the difference between when work could ideally run and when it gets an opportunity. Measure it rather than assuming a timer is an exact clock. A lag demonstration must use a short, bounded loop—never intentionally freeze classroom machines indefinitely. Worker and stream details return in Module 10.
''',
'analogy':'While the kitchen cooks, the cashier serves someone else. That is overlapping waiting. Two cooks working simultaneously illustrate parallel work. One cashier cannot perform an endless calculation and serve customers at the same instant.',
'trace':'A → B → C → D → Ready: A1 → Handled: Unavailable: A2 → Preparation finished. The numerical timer delays are not exact wall-clock promises.',
'change':'Add a successful A3 preparation after the handled failure by giving it its own try/catch scope. Explain why a statement after the rejecting await inside the original try does not run.',
'pitfall':'A rejected promise without a handler may terminate a Node process. A function that starts a promise but does not return or await it can appear complete before its work finishes.',
'sources':['https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model','https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises','https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick']},
3: {
'hook':'Make a plain HTML button respond before adding frameworks. The first success is simply seeing your own message appear when you click.',
'targets':['Connect a button to a handler inside a script block.', 'Handle form input safely and explain event propagation.', 'Remove a group of listeners and verify that responses stop.'],
'lesson':'''### The first listener, step by step

Open the supplied HTML file and first focus only on the hello button, message paragraph and their click handler. The script is below the elements, so they exist when selected. `getElementById('hello')` selects an element; `addEventListener('click', callback)` registers a function; a click invokes it; `textContent` changes the visible text. Registering a callback is not the same as calling it immediately.

An inline `<script>` block contains JavaScript. An `onclick` HTML attribute is a different arrangement and is not required. To split the file, move the script body into `app.js` and use `<script src="app.js" defer></script>` in the head. `defer` applies to that external classic script, not as a way to delay an inline classic script. Browsers do not type-check or directly execute ordinary TypeScript syntax in this exercise.

### Forms and accessible controls

A native button already supports keyboard activation. A form's submit event can arise from clicking its submit button or pressing Enter. Listen to submit rather than only the button's click so both routes work. `preventDefault()` suppresses the form's default navigation, but does not stop propagation. A label associates text with the input; `aria-live` makes status changes available to assistive technology without replacing clear visible feedback.

Read input, trim whitespace, validate, and only then create a row. HTML `required` helps but does not make all whitespace invalid. User text goes into text nodes or `textContent`, not into HTML markup. These choices prevent input from being interpreted as executable markup in this example.

### Propagation and delegation

Many events travel through capture, target and bubble phases. `target` identifies the originating target; `currentTarget` is the element whose listener currently runs. A list can keep one click listener while rows are added later. The handler narrows `event.target` to an Element, finds the closest matching button, and confirms it belongs to the list. This is event delegation.

Not all events bubble: for example, mouseenter/pointerenter differ from mouseover/pointerover. Select a suitable event or capture strategy rather than assuming delegation always works. `stopPropagation()` stops further propagation, while `stopImmediatePropagation()` also prevents later listeners on the same target. Neither automatically cancels a default action. Avoid stopping propagation without a clear need.

### Listener lifetime and other sources

The shared AbortController provides a signal to several listeners. Calling abort removes them together. A separately registered once-only stop button also disables the controls, preventing a now-unhandled form from navigating. With manual removal, retain the same callback reference and matching capture option; a new arrow function is a different function. A passive listener cannot cancel the default action with preventDefault.

The custom `order-added` event carries data in `detail`; dispatch is synchronous, not a promise. Its default does not bubble unless requested. Browser exceptions reported from listeners are not identical to catching an ordinary Node emit call. Later lessons compare channels such as BroadcastChannel and postMessage. Resize/Intersection/MutationObserver observe particular changes; requestAnimationFrame schedules visual work; visibilitychange and pagehide support lifecycle handling. They are not interchangeable replacements for click listeners.
''',
'analogy':'The HTML control is the doorbell, registration is connecting the wire, the click is a press, and the handler is the response. A disconnected wire explains why the same press stops doing anything.',
'trace':'Click Say hello → “Hello, coder!”; submit “Pandesal” → one row and “Added order 1”; press Collected → row removed; Stop listeners → controls disabled; reload restores the page.',
'change':'Change the hello message and add a count of successful orders. Keep blank submissions from incrementing it. The dynamic list is a guided extension if time remains after the first button.',
'pitfall':'A null element usually means a misspelled ID or early script execution. A page reload on submission suggests preventDefault is missing. Duplicate reactions suggest repeated listener registration.',
'sources':['https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events','https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener','https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent']},
4: {
'hook':'One order should notify the kitchen and receipt printer without the order creator containing both implementations.',
'targets':['Register, emit, remove and run a listener once with EventEmitter.', 'Explain synchronous ordering and handle an error deliberately.', 'Wait for an event without missing it and clean up listeners.'],
'lesson':'''### EventEmitter as an in-process dispatcher

Import EventEmitter from Node's built-in `node:events`; no npm package is needed. `on(name, listener)` registers; `emit(name, payload)` invokes matching listeners in registration order. These listeners run synchronously unless they themselves schedule later work. `emit` does not await an async listener's returned promise. Its Boolean return indicates whether the event had listeners, not whether the business operation succeeded.

An event name is a contract. Publishers and consumers must agree on both spelling and payload meaning. `order.created` carries an ID here; a real invoice may also require line items and currency. Decide whether the consumer gets enough information or must query a service. More information reduces follow-up requests but can spread sensitive or stale data.

### Lifetime, identity and once

`once` registers a listener removed after its first invocation. `off` removes a particular registered function. Save the reference to invoice so removal can find it. Registering the same callback repeatedly is not deduplicated for you. `listenerCount` and `eventNames` help diagnose leaks; increasing maximum listeners merely hides a warning if the real problem is forgotten cleanup.

Use removeAllListeners only when you own the emitter and all its listeners, as this standalone demonstration does. A shared service should expose targeted unsubscribe functions. Composition keeps a private emitter inside a service; subclassing EventEmitter exposes its interface. Choose according to the intended API rather than making every object an emitter.

### Three distinct failure paths

Emitting the special `error` event without a listener throws in ordinary EventEmitter use. Our explicit error listener records a printer failure. A synchronous listener that throws can interrupt emit; decide whether to catch around dispatch or isolate that reaction. An async listener can reject after emit returns. `captureRejections: true` routes supported rejected listener promises to error handling, but is not a transaction or universal rollback. Keep the error handler itself simple and do not create another unhandled rejected promise there.

The example emits an error deliberately; this is not evidence that every library uses the same error policy. A real order system must decide whether receipt failure invalidates the order or simply needs a retry.

### Awaiting and other Node sources

`events.once(emitter, name)` returns a promise for the next matching event's arguments. Create that promise before emitting, otherwise the event can be missed and the program can wait forever. `events.on` offers an async iterator, but a producer can outpace a consumer; stopping iteration and aborting work must be planned.

Node HTTP requests, worker messages and file watchers also produce events. `fs.readFile` reads once; `fs.watch` observes changes but behavior and reliability vary by platform. During shutdown, stop accepting work, drain bounded pending work, and close watchers/listeners. Process signals are environment-sensitive; use the lifecycle supported by the classroom host.
''',
'analogy':'The order service is a public-address microphone. Invoice and kitchen listen to the same announcement. Muting invoice does not remove the kitchen listener.',
'trace':'A1 produces Invoice, Kitchen, First order bonus. A2 produces Kitchen only. The printer error is handled, Ready prints A2, and Remaining prints 0.',
'change':'Add an independent inventory listener, remove it after A1, and prove it does not run for A2. Keep the deliberate printer failure handled.',
'pitfall':'If ready never resolves, registration may have happened after emit. If cleanup fails, check function identity. If an async listener fails later, a try/catch around emit alone is insufficient.',
'sources':['https://nodejs.org/api/events.html','https://nodejs.org/api/fs.html#fswatchfilename-options-listener']},
5: {
'hook':'A student types a new search, but an older slow result arrives afterward and overwrites it. Successful requests can still produce an incorrect interface.',
'targets':['Explain stale results and protect the latest request.', 'Cancel pending work and distinguish cancellation from failure.', 'Compare debounce, throttle and promise-composition choices.'],
'lesson':'''### Choose a completion model

A callback is a function another piece of code calls. A promise describes a single eventual outcome. An event emitter represents repeated named notifications. An async iterator exposes a sequence consumed over time. Pick the model that matches the information: wrapping a click stream in one promise only captures one occurrence.

Use sequential awaits when the second operation requires the first result. For independent work, start both operations before awaiting their combined result. `Promise.all` rejects when an input rejects, but does not automatically cancel the other work. `allSettled` reports every result. `race` settles from the first settlement; `any` needs one fulfillment and rejects only when all inputs reject. Do not confuse concurrent waiting with running a CPU loop in parallel.

### Latest request wins

The example increments `latestRequest` for each search. Each invocation captures its own request number. Before displaying a result, it compares its number with the current latest value. A stale result is ignored even if the transport could not be cancelled. This identity check protects correctness; cancellation helps avoid unnecessary work.

An AbortController has a signal that cooperative APIs observe. Aborting does not forcibly interrupt arbitrary JavaScript or undo server-side work already committed. Our simulation uses Node's abortable promise timer. We abort the previous controller, create a new one, then await a simulated response. AbortError is an expected cancellation path; unknown errors are rethrown.

### Debounce and throttle

Debounce waits for a quiet period before invoking work; each new input resets the timer. The three rapid terms in the example produce only the final announcement. Throttle limits invocation frequency over time and may retain leading/trailing calls depending on the chosen policy. A search field often benefits from debounce; a continuously updated scroll indicator may need throttle or animation-frame scheduling. Neither automatically prevents stale network responses.

The returned debounced function has a cancel method. Call it during disposal so it cannot update a destroyed interface. Decide whether a final queued action should be flushed or discarded; cancellation here discards it.

### Real HTTP and bounded lifetimes

With fetch, inspect `response.ok` before parsing; HTTP 404 does not itself behave like a network rejection. JSON parsing can fail, and parsed data can have the wrong shape. Validate it before using properties. A timeout needs a policy: cancel the request, show a retry option, and avoid retrying unsafe mutations blindly.

Async iteration can make consumption clearer, but does not guarantee an upstream producer has bounded buffering. Dispose generators/listeners and handle loop exits. For this lesson, request IDs, cancellation and debounce form the practical core; HTTP schema libraries and full concurrency limiters remain extensions.
''',
'analogy':'Calling a new number at the counter makes the previous slip obsolete. Cancelling a preparation may save work, but checking the slip number still prevents the wrong order from reaching the customer.',
'trace':'Cancelled: old → Show: NEW → Debounced: canteen. Earlier typed prefixes never reach the debounced callback.',
'change':'Remove the abort call but keep the request-number check; the old result must still not display. Then explain why restoring cancellation is useful.',
'pitfall':'Reusing an already-aborted controller immediately cancels later work. Catching every error and silently returning hides genuine failures. Promise.race alone does not stop the losing request.',
'sources':['https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal','https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise','https://nodejs.org/api/timers.html#timers-promises-api']},
6: {
'hook':'An invoice handler expects a numeric total, but receives the word “sixty.” Catch that mistake both while coding and when data arrives at runtime.',
'targets':['Define a typed event map and generic channel.', 'Reject malformed external data with a runtime guard.', 'Explain callback lifetime and compile-time versus runtime checks.'],
'lesson':'''### Describe payloads before broadcasting them

An interface or type alias describes the shape of a value for the compiler. `Order` contains a string ID and numeric total. The event map associates each name with its own payload. `keyof Events` represents allowed event names; `Events[K]` selects the corresponding payload type. A generic function preserves that relationship for a concrete call.

The mapped `Channels<M>` type creates a channel for every key in M. This avoids one untyped dictionary accepting any payload everywhere. Each `Channel<T>` stores listeners that accept T. The public on method returns an unsubscribe function, so callers do not need access to the Set itself. A snapshot of listeners is iterated: adding a new listener during dispatch affects a later emission, rather than extending the current iteration.

### Static checking is not external validation

Run `npm run typecheck`. Uncommenting the wrong total produces a compiler error. Node's ability to execute erasable TypeScript syntax does not perform these checks. JSON.parse returns data that must not be trusted merely because we want it to be an Order. Assign it to `unknown`, inspect it, and narrow it using `isOrder`.

The guard rejects null, checks primitive types, requires a nonempty ID and checks that total is finite and nonnegative. `typeof NaN` is number, so typeof alone is not enough for all numeric rules. A guard's claimed type predicate is a promise made by the programmer; a bad guard can lie. Schema libraries such as Zod/Valibot offer another approach, but their schemas still need correct business constraints.

### DOM and domain unions

In browser TypeScript, a selected element may be null or a general HTMLElement. Narrow with an instanceof check before reading input-specific properties. An event target is not automatically the input you expected. A domain union can discriminate between `{ type: 'created', ... }` and `{ type: 'cancelled', ... }`; switching on type then narrows the data. These patterns help make invalid states harder to express.

CustomEvent<T> describes detail for typed code, but does not validate messages crossing a trust boundary. The same is true of typed Socket.IO or emitter APIs. Incoming network data needs runtime checks irrespective of how carefully local interfaces were declared.

### Define behavioral contracts too

Our channel dispatch is synchronous, ignores returned listener results and propagates a thrown synchronous listener error. It is not EventEmitter and has no special error event. Type safety alone says nothing about retries, buffering, cancellation or async rejections. Document these choices alongside types. The unsubscribe demonstration emits A3 after removal and intentionally produces no invoice output.

Keep code checking and program execution as separate commands. The pack pins TypeScript and Node typings; upgrading either can expose new errors that should be reviewed rather than suppressed with broad any casts.
''',
'analogy':'The event map is a labeled delivery form: “order.created” needs an ID and amount. The type checker checks forms you fill out in the office; runtime validation checks parcels arriving from outside.',
'trace':'Invoice: A1 60; Bad payload accepted: false. A3 prints no invoice because the listener was removed.',
'change':'Add a string reason to order.cancelled and a listener that displays it. Demonstrate one valid call, one intentionally invalid compile-time call (comment it afterward), and one invalid runtime payload.',
'pitfall':'Using `as Order` on untrusted JSON suppresses doubt rather than checking data. A channel must not accept async listeners without an explicit rejection policy just because TypeScript allows a callback shape.',
'sources':['https://www.typescriptlang.org/docs/handbook/2/generics.html','https://www.typescriptlang.org/docs/handbook/2/narrowing.html','https://www.typescriptlang.org/docs/handbook/2/mapped-types.html']},
7: {
'hook':'An order cannot be collected before it is ready. Naming events is not enough; we also need rules for valid transitions.',
'targets':['Differentiate Observer, Pub/Sub and mediator.', 'Read and change a finite state machine.', 'Separate commands, facts and queries in a small domain.'],
'lesson':'''### Patterns solve different coupling problems

Observer lets a subject notify registered observers. Pub/Sub routes publications through topics or channels so publishers need not hold each consumer reference. A mediator centralizes collaboration rules between participants. An event bus can implement part of these patterns, but the existence of a bus does not automatically create a well-designed architecture.

Ask what must change when a new reaction is added. If the publisher contains every consumer's implementation, coupling remains high. If nobody can trace who handles a topic, an overly broad bus creates hidden dependencies. Keep event names specific, payloads documented and ownership clear.

### Commands ask; events tell

`prepare` requests a transition. It can be rejected. An `order.preparing` fact would only be published after accepting the transition. A query reads current status without changing it. Do not label an unapproved request as an already completed fact. When several effects must occur, decide which one establishes the fact and which are follow-up reactions.

State is the program's current condition; a transition maps a valid command in that state to another state. Our table permits waiting → preparing → ready → collected, with cancellation from waiting. Collected and cancelled are terminal in this tiny model. Undefined entries mean invalid actions, not “do whatever the UI requested.”

### Guards, actions and testable rules

A guard is a condition checked before allowing a transition, such as a payment requirement. An action is work performed because the transition happens. Keep pure transition decisions separate from side effects where possible so tests can explore rules without contacting a real service. A diagram helps identify missing cases: can a preparing order be cancelled, and if so what happens to inventory?

The sample mutates a single local state variable for readability. A larger design can return a new state from a pure reducer. UI controls should reflect allowed commands, but disabling a button is not a security boundary. Server-side rules must still reject invalid commands.

### Framework connections and domain modeling

React handlers update state, reducers encode transitions and effects manage external synchronization. Vue/Angular and signals-based systems offer other mechanisms to track dependencies and updates. Signals generally describe reactive value dependencies; domain events describe occurrences. Avoid pretending all frameworks share one lifecycle or that using a framework replaces explicit cleanup.

For a short event-storming exercise, write commands, events and actors on separate cards. Start with “student places order,” “order created,” and “kitchen starts preparation.” Mark where failure can occur and who owns the decision. This is a discussion tool, not a demand to deploy microservices. Python/asyncio can be compared conceptually if present in the source reports; required implementation remains JS/TS.
''',
'analogy':'A parcel has statuses: received, dispatched, delivered. You cannot truthfully announce delivery merely because someone pressed a button. The state machine enforces the story.',
'trace':'collect is rejected in waiting; waiting → preparing → ready → collected; another collect is rejected.',
'change':'Sketch a cancelled transition from preparing and specify its required recovery action before changing code. Explain why a direct jump to collected should remain rejected.',
'pitfall':'Many independent Boolean flags can describe impossible combinations such as ready and cancelled at once. One explicit state plus guards can make those combinations visible.',
'sources':['https://react.dev/learn/extracting-state-logic-into-a-reducer','https://developer.mozilla.org/en-US/docs/Web/API/EventTarget']},
8: {
'hook':'A search box produces many values over time. RxJS lets us describe how that sequence should be filtered, delayed and replaced.',
'targets':['Distinguish Observable, observer, subscription and Subject.', 'Build and explain a short RxJS operator pipeline.', 'Recover from an inner failure and unsubscribe cleanly.'],
'lesson':'''### A sequence instead of a single result

An Observable describes how values can be delivered over time. An observer receives next values, errors or completion. A subscription represents the active connection and its teardown. A Subject can receive values through next and distribute them to its subscribers. Our Subject stands in for input events so the example runs without a browser.

A cold source often starts work for each subscription; a hot source can produce independently of a particular subscriber. Do not assume all Observables share or replay their values. `fromEvent` can connect a browser target to a stream, `of` emits given values, and `timer` emits after a delay. `map` transforms values; `filter` keeps values matching a predicate. An Observable is not inherently faster or simpler than a short direct handler.

### Read the pipeline from input to result

`debounceTime(10)` waits for a quiet period. `distinctUntilChanged()` suppresses consecutive equal terms. `switchMap` subscribes to a new inner stream and unsubscribes the previous one. Here each inner stream is a timer representing a search. Because this source supports teardown, unsubscribing stops its pending timer.

For a promise-backed network request, unsubscription does not necessarily cancel the underlying operation. Use an abort-aware source if cancellation matters. Compare other flattening choices: concatMap serializes inner work, mergeMap permits concurrent work (configure bounds when appropriate), and exhaustMap ignores new starts while current inner work remains active. The right choice follows the business rule: discarding an old search may be correct, discarding a payment command may not be.

### Put recovery at the intended boundary

The map callback deliberately throws for the term error. `catchError` inside switchMap replaces that failed inner search with a friendly result. The outer input stream can then keep receiving future terms. Catching only outside can instead replace or end the entire search pipeline depending on what the replacement does. Error placement is part of program behavior, not cosmetic syntax.

`finalize` runs when the subscription terminates through completion, error or unsubscription. It is useful for cleanup but is not a signal that the search succeeded. Always retain and dispose subscriptions when their owning screen/service ends. Sharing with share/shareReplay has lifetime and caching consequences; only add it when multiple consumers need the same work.

### Testing time without guessing

The sample includes small waits to make its console trace easy to see, not as a guarantee for every machine under load. For precise operator tests, RxJS TestScheduler models virtual time; marble diagrams describe emissions, time and termination. Compare expected sequences, including errors and cancellation. The core activity is one pipeline and one independent change, not learning every operator at once.

The package is pinned to RxJS 7.8.2 in this pack. Its installed source and executed example are the verification baseline when the documentation site only returns a JavaScript loading shell.
''',
'analogy':'A water filter is a sequence of stages: let the flow settle, remove duplicates, then direct the newest request into a channel. Each operator changes what gets through or when.',
'trace':'Results: CANTEEN → Handled: Search unavailable → Search subscription closed. The c and ca prefixes are suppressed.',
'change':'Normalize terms with trim/lowercase before distinctUntilChanged, then show that equivalent consecutive terms do not produce repeated searches. Keep the error recovery and unsubscribe.',
'pitfall':'Forgetting subscribe means many Observable descriptions never execute. Nested manual subscriptions make cancellation harder to follow; use an appropriate flattening operator instead.',
'sources':['https://rxjs.dev/guide/overview','https://github.com/ReactiveX/rxjs/tree/7.8.2/src/internal/operators','https://rxjs.dev/guide/testing/marble-testing']},
9: {
'hook':'An announcement board should update without students repeatedly pressing Refresh. We will use a real local HTTP connection, not pretend that a local emitter crosses the network.',
'targets':['Select SSE versus WebSocket for a communication need.', 'Run a local SSE server and validate received messages.', 'Handle connection status and close the stream.'],
'lesson':'''### Choose the direction and lifetime

Polling asks the server for updates repeatedly. Server-sent events (SSE) keeps an HTTP response open so the server can stream text events to the client. WebSocket supports two-way messaging over an upgraded connection. Socket.IO is a higher-level protocol/library with its own handshake and behavior; a Socket.IO endpoint is not automatically compatible with a raw WebSocket client.

A one-way order board fits SSE. Interactive chat might use WebSocket, though client requests plus SSE can also solve some two-way application workflows. Decide from requirements, reconnect behavior, infrastructure and deployment constraints—not from which name sounds newer.

### The wire format and browser client

The server replies with `text/event-stream`. Each message has fields such as id, event and data, and ends with a blank line. The data field contains serialized JSON, but SSE itself is text framing. Our client listens for the custom announcement event, parses data and verifies that text is a string. It appends text safely and caps visible rows at 20.

EventSource emits open/error notifications and ordinarily reconnects after an interrupted connection. Our status shows that attempt rather than claiming successful recovery. Closing the source explicitly stops it. On the server, closing the request clears that connection's interval so disconnected users do not leave timers running.

### Delivery is not automatically durable

The example restarts its counter for each connection and retains no history. Although it sends IDs, it does not implement replay from Last-Event-ID. Reconnection can therefore miss or repeat business information. A production service needs stable IDs, a retention policy, resume semantics and an appropriate deduplication strategy. Transport connectivity is not equivalent to exactly-once business processing.

Validate messages and authenticate users on a real service. Decide how credentials are carried using supported mechanisms; do not put private secrets into URLs. Rate limits, connection limits, TLS, proxy buffering and idle timeouts matter for deployment. Keep this server bound to loopback for the classroom.

### Other communication channels

BroadcastChannel exchanges messages among compatible same-origin contexts; it is not an internet broker. MessageChannel connects two message ports. postMessage can communicate between windows/workers: validate origin, source and payload, and use a specific target origin when sending cross-window data. A worker message is another boundary requiring a clear data contract.

For today's core, start the supplied server, open the page, observe messages, stop the server to see reconnect status, then restart and finally press Disconnect. Full broker setup, remote hosting and authentication implementation are beyond this short lesson.
''',
'analogy':'SSE is a school announcement speaker: the office speaks and listeners receive. WebSocket is closer to a phone call where both ends can send messages during the connection.',
'trace':'Connected appears, followed by Order ready 1, 2, 3… Disconnect changes status and stops new rows. Restarting the server creates a fresh sequence; it does not recover missed history.',
'change':'Add a visible received-message count independent of the capped list. Explain whether reconnect duplicates should count as new business events.',
'pitfall':'Opening m09.html as a file gives the wrong origin for /events; use the local HTTP URL. A proxy that buffers responses can prevent timely updates even when server code is correct.',
'sources':['https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events','https://developer.mozilla.org/en-US/docs/Web/API/WebSocket','https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage']},
10: {
'hook':'A producer can generate records faster than a slow writer saves them. More memory is not a sustainable flow-control policy.',
'targets':['Build a readable-transform-writable pipeline.', 'Explain backpressure and completion/error handling.', 'Compare a worker with ordinary async waiting.'],
'lesson':'''### Streams process chunks

A Readable supplies chunks, a Writable accepts them, a Duplex does both, and a Transform changes input into output. Chunks may be bytes or, in object mode, JavaScript values. Processing incrementally avoids loading an entire large dataset before useful work can begin. It also creates a responsibility to handle errors and completion across the whole chain.

Our source yields three strings. A Transform uppercases each. The Writable simulates a slow save by calling its completion callback later. Calling done signals that this chunk has been handled; forgetting it stalls the pipeline, while calling it twice is a bug. Errors should be passed through the callback or supported promise interface, not swallowed.

### Backpressure is feedback

A writable can signal that its buffer is full enough for the producer to pause. With manual write calls, a false result means wait for drain before continuing. Pipeline handles flow coordination and errors for the linked streams. highWaterMark is a buffering threshold, not a universal hard memory cap; chunk sizes, object references and upstream behavior still matter.

The small example uses object mode and a low threshold so the behavior can be discussed without huge data. Slowing the sink should lengthen completion, not make us spin in a loop checking whether it is ready. A pipeline completion promise means the connected work finished or failed; do not print success immediately after starting it.

### Async iterables and bounded queues

`for await...of` consumes asynchronous sequences and can make flow readable. However, an upstream source can still buffer aggressively. Set queue limits and decide whether overflow should wait, drop, reject or coalesce. These policies depend on the data: dropping intermediate mouse positions may be acceptable; silently dropping payment records is not.

Cancellation should reach sources and destinations, and cleanup should release file handles/listeners. A long-running service should stop accepting new work and allow bounded drain time on shutdown. A service worker in the browser has an OS/browser-managed lifecycle and is not a guaranteed forever-running process.

### Workers for suitable CPU work

Awaiting a file read allows other work while I/O is pending. A heavy JavaScript loop still occupies its thread. A worker provides another JavaScript execution context and communicates through messages; data is usually cloned or deliberately transferred, and startup/communication has overhead. Shared memory requires careful synchronization, not ordinary unsynchronized writes.

The optional worker sums one million integers. Its purpose is to show message exchange and main-thread availability, not to claim that every calculation is faster in a worker. Measure realistic workloads before adding one. The core submission is the stream pipeline; the worker comparison is ungraded extension material.
''',
'analogy':'A slow cashier asks the queue attendant to admit fewer customers at a time. Backpressure communicates capacity upstream; it is not merely adding more waiting chairs.',
'trace':'Saved: ORDER A1 → Saved: ORDER A2 → Saved: ORDER A3 → Pipeline complete. Optional worker: Main thread remains available, then Worker result: 500000500000.',
'change':'Add one fourth record and a deliberate transform error for a chosen record. Verify that failure is reported and success is not falsely printed; document the successful prefix.',
'pitfall':'Ignoring write(false) in a manual loop can grow memory. Marking a CPU-heavy function async does not move its work off-thread. Exact worker/main output timing should not be inferred from line placement alone.',
'sources':['https://nodejs.org/api/stream.html','https://nodejs.org/api/worker_threads.html','https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers']}
}
