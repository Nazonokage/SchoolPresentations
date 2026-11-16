# Technical review of imported EDP research

[Research home](README.md) | [Verified sources](VERIFIED_SOURCES.md)

## Findings supported by official references

1. **Error propagation depends on the API.** The JS/TS report broadly says handler errors do not propagate to an emitter's caller. Browser dispatchEvent reports listener exceptions separately, but Node EventEmitter invokes ordinary listeners directly and synchronously. Do not teach one blanket rule. [Browser dispatch](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/dispatchEvent), [Node events](https://nodejs.org/api/events.html).
2. **nextTick ordering needs context.** The report's unconditional “nextTick before promise microtasks” statement omits top-level ESM behavior. Node documents different top-level CJS/ESM ordering. Every ordering exercise must name the runtime and module format. [Node process scheduling](https://nodejs.org/api/process.html#when-to-use-queuemicrotask-vs-processnexttick).
3. **Listener removal uses identity and capture matching.** Keep the same function reference and capture setting. An AbortSignal can provide a shared lifetime for supported listener registrations. [addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener), [removeEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/removeEventListener).
4. **Already-aborted signals matter.** A promise-based wrapper should check the signal before registering work and reject an unsettled operation appropriately. Merely listening for a future abort misses an already-aborted signal. [AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal).
5. **EventEmitter does not await return values.** Async listener failures need a deliberate policy; captureRejections is an option with documented behavior, not automatic awaiting. [Node events](https://nodejs.org/api/events.html).
6. **Message data is a trust boundary.** Cross-window messaging requires appropriate targetOrigin and validation of incoming origin/source/data. It is not just another arbitrary event payload to trust. [postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage).

## Code-review concerns to verify with focused tests before reuse

These are observations from the supplied code, not claims that its entire course was executed or exhaustively audited.

- The EventEmitter snippet calls off with a handler identifier that was not declared in that snippet. Future starters must be complete, with all variables defined.
- The nextClick promise wrapper does not check a pre-aborted signal and does not remove the abort listener after a successful click. Design explicit cleanup for every settle path.
- The eventsOf async generator accumulates abort listeners while waiting and needs careful exit/disposal behavior. Do not use this advanced wrapper as the beginner cancellation example.
- The typed custom emitter isolates synchronous failures by throwing later in a microtask. That deferred throw can still become an uncaught failure; it is not a general production resilience guarantee. Async rejections also require separate handling.
- A shorthand throttle based on an initial timestamp can suppress its first call depending on timing. Specify leading/trailing behavior and test the chosen policy.
- Delegation snippets assume target is an Element and that ancestor lookup succeeds. Narrow target and check the selected row/ID. A type assertion alone does not validate DOM shape.
- A downloader example needs HTTP status validation; a fulfilled fetch promise can still represent an unsuccessful response.
- Abort/retry search examples must handle expected cancellation without throwing a new unhandled rejection from an async event listener. Define request cleanup and stale-result policy.
- Shutdown examples that call process.exit immediately after a partial drain may end before outstanding work finishes. Keep server lifecycle code out of the required beginner path until it is implemented and verified.

## Architectural overstatements to remove

Events crossing process boundaries do not always require a broker; direct protocols can carry events. Event-driven code does not universally imply eventual consistency, automatic resilience, or non-blocking handlers. Broker delivery guarantees, duplicate handling, and event-sourced state require system-specific definitions. Treat the production reports as topic suggestions rather than evidence of those guarantees.

No package version baseline has been approved or tested. Do not copy “Node 22 LTS recommended” or TypeScript 5.x from an unsearched report as a current classroom requirement. Resolve versions when authoring executable code.
