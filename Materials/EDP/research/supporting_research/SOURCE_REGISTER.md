# Source register

[Research pack home](README.md)

**Collection date:** 2 November 2026, Asia/Manila. Official framework/runtime documentation and MDN were used for technical research. Source IDs below are internal labels for the outlines, not external citation identifiers. Links point directly to the relevant documentation.

The entries identify the basis for a topic, not a claim that a complete lesson was copied from that source. Scenarios, assessments, and lesson sequencing are proposed instructional designs. Documentation at a `latest` or unversioned URL can change; freeze the classroom toolchain and check version-specific documentation during implementation.

## Local evidence

| Source | What was inspected | What it supports |
| --- | --- | --- |
| [Curriculum 2018-BSIT.pdf](<D:/Media/documents/Files/2026/ICC school work files/Curriculum 2018-BSIT.pdf>) | Extracted the complete one-page course listing, including the third-year table | Separate course codes, titles, prerequisites, listed hours/units |
| [Existing module folder](../) | Inventoried all 22 numbered files and the table of contents; reviewed the introduction, event-handling, networking, and lifecycle/activity material in more detail | Original teaching format, topic coverage, Java/Android roots, mixed Kotlin updates |
| [Original table of contents](../ADET_TBLCNTS.MD) | Reviewed its phases and missing-module note | Comparison against the replacement sequence; not assumed to be a verified technical authority |

## ADET and shared foundations

| ID | Documentation | Research use |
| --- | --- | --- |
| S01 | [React Native: Get Started](https://reactnative.dev/docs/environment-setup) | Framework-based mobile development starting point |
| S02 | [Expo: create-expo-app](https://docs.expo.dev/more/create-expo/) and [TypeScript guide](https://docs.expo.dev/guides/typescript/) | Explicit project template choice and TypeScript setup |
| S03 | [Expo: Start developing](https://docs.expo.dev/get-started/start-developing/) and [Development builds](https://docs.expo.dev/develop/development-builds/introduction/) | Expo Go preview workflow and development-build boundary |
| S04 | [React Quick Start](https://react.dev/learn) | Components, props, rendering, state, and event-handler foundations |
| S05 | [TypeScript Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html) | Values, typed functions, objects, arrays, and unions |
| S06 | [TypeScript Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) | Runtime checks and discriminated state models |
| S07 | [React Native Accessibility](https://reactnative.dev/docs/accessibility) | Accessible naming and platform-aware accessibility behavior |
| S08 | [React Native FlatList](https://reactnative.dev/docs/flatlist) | List identity, rendering, and performance considerations |
| S09 | [Expo Router introduction](https://docs.expo.dev/router/introduction/) | File-based navigation and the need for a consistent project structure |
| S10 | [React: Synchronizing with Effects](https://react.dev/learn/synchronizing-with-effects) | External synchronization and cleanup |
| S11 | [MDN: Using promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) | Promise composition, chaining, rejection, and concurrency concepts |
| S12 | [MDN: await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await) | What awaiting pauses and how async execution resumes |
| S13 | [MDN: Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) | Requests, HTTP status handling, and reading responses |
| S14 | [Expo: AsyncStorage](https://docs.expo.dev/versions/latest/sdk/async-storage/) | Non-sensitive local persistence; implementation needs the SDK-compatible package |
| S15 | [React Native Security](https://reactnative.dev/docs/security) | Client-side storage, secrets, and security boundaries |
| S16 | [Expo: Authentication](https://docs.expo.dev/guides/authentication/) | External authentication integration context; real provider setup is beyond the mock-login exercise |
| S17 | [Expo: SecureStore](https://docs.expo.dev/versions/latest/sdk/securestore/) | Platform-backed storage option and its documented limitations |
| S18 | [Node.js: TypeScript](https://nodejs.org/api/typescript.html) | Supported TypeScript execution and the separate need for type checking |
| S19 | [Expo: ImagePicker](https://docs.expo.dev/versions/latest/sdk/imagepicker/) | Media-selection workflow, cancellation, and platform configuration |
| S20 | [Expo: Location](https://docs.expo.dev/versions/latest/sdk/location/) | Foreground location and permissions; device testing required |
| S21 | [Expo SDK reference](https://docs.expo.dev/) | Entry point for integration planning; individual Share/Linking APIs must be checked during module authoring |
| S22 | [Node.js test runner](https://nodejs.org/api/test.html) | Repeatable tests for pure logic and event-driven behavior; not a claim of native UI-test coverage |
| S23 | [React: Extracting State Logic into a Reducer](https://react.dev/learn/extracting-state-logic-into-a-reducer) | State transitions and organized update logic |
| S24 | [Expo: Progressive web apps](https://docs.expo.dev/guides/progressive-web-apps/) | Mobile/web comparison and PWA-specific considerations |
| S25 | [Expo: Sensors](https://docs.expo.dev/versions/latest/sdk/sensors/) | Connected-data extension options; exact sensor APIs remain implementation work |
| S26 | [Expo: Build project](https://docs.expo.dev/deploy/build-project/) | Packaging and release workflow, distinct from opening a preview |

## Event-driven Programming

| ID | Documentation | Research use |
| --- | --- | --- |
| S27 | [MDN: Introduction to events](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events) | Handlers, event objects, default behavior, and propagation foundations |
| S28 | [Node.js event loop](https://nodejs.org/learn/asynchronous-work/event-loop-timers-and-nexttick) | Scheduling and non-blocking I/O; distinguish Node from browser-specific details |
| S29 | [MDN: Promise.allSettled](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled) | Reporting all outcomes when independent tasks can fail |
| S30 | [MDN: AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController) | Canceling supported operations through a signal |
| S31 | [Node.js Events](https://nodejs.org/api/events.html) | EventEmitter, synchronous listener calls, registration, removal, and errors |
| S32 | [MDN: localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) | Browser persistence and storage behavior |
| S33 | [MDN: Using Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) | Background computation and message-based communication |
| S34 | [MDN: Using server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) | Server-to-browser streaming and connection management |
| S35 | [MDN: WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) | Comparison with bidirectional real-time communication |

## Alternative-stack context

- [Flutter installation](https://docs.flutter.dev/install) and [simple state management](https://docs.flutter.dev/data-and-backend/state-mgmt/simple): inspected to inform the initial React Native/Flutter choice. Flutter is not required in the selected course.

## Remaining targeted research before implementation

1. Resolve and test an Expo SDK/Expo Go/package combination on the actual classroom platform; record versions rather than asserting “latest” as a reproducible baseline.
2. Check React Native Share/Linking, CustomEvent/EventTarget, debounce/throttle timing choices, and Node HTTP server details against their direct API pages when writing the exact code.
3. If local notifications are retained, verify current Expo Go/development-build and platform requirements. Remote push is not a core requirement.
4. Select a live AI provider only if the instructor wants that extension; then verify its API, server-side secret handling, cost, privacy, and classroom access separately.
5. Recheck platform release/distribution guidance when teaching the final module; do not carry forward fixed store-policy claims from the older files.

Some later web lookups failed because the browsing connection closed. The register separates inspected material from these remaining checks instead of claiming all optional integrations are already verified.
