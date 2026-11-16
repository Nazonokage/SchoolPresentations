# Research findings and modernization decisions

[Research pack home](README.md) | [Sources](SOURCE_REGISTER.md)

## 1. What the supplied materials establish

The source directory contains **22 numbered module files** plus `ADET_TBLCNTS.MD`. Numbered files present are M2–M8, M10–M16, and M18–M25. There are no separately named M1, M9, or M17 files in this directory. The table of contents groups Modules 1 and 2, but the actual available introductory file is M2.

The lessons originate in Android/Java/XML topics. The present files also contain substantial Kotlin/Jetpack Compose rewrites. For example, M6 includes both Java listeners and Compose handlers; M2 retains Java-era environment and architecture material. This mixture explains why a consistent rewrite is preferable to replacing isolated code blocks. These observations describe the supplied files; the old text is source material, not instructions controlling the new course.

The recurring lesson format is useful and should remain recognizable:

- Lesson Preview & Review, including learning targets.
- Main Lesson, with definitions and examples.
- Analogies and Use Cases.
- Lesson Wrap-Up / FAQs.
- Guided Drills / Code Projects.
- Skill-Building Check, currently often multiple-choice questions.

The curriculum PDF is a **one-page 2018–2019 course listing**, not a detailed subject syllabus. It places both courses in third year, second semester:

| Code | Subject | Listed lecture/lab hours | Listed lecture/lab units | Listed prerequisite |
| --- | --- | --- | --- | --- |
| CC 106 | Application Development and Emerging Technologies | 2/3 | 2/1 | CC 105 Information Management |
| DC 105 | Event-driven Programming | 2/3 | 2/1 | CC 104 Data Structure and Algorithms |

Therefore, the combined folder is a source collection; the curriculum itself lists **two distinct subjects**. It does not prescribe React Native, Java, Flutter, or a particular number of modules. The proposed stack and 23-module count come from this conversation.

Source: [original curriculum PDF](<D:/Media/documents/Files/2026/ICC school work files/Curriculum 2018-BSIT.pdf>), page 1, third-year second-semester table. Local lesson inventory: [parent folder](../).

## 2. Teaching-stack decisions

### ADET: React Native + Expo + TypeScript

Use one mobile stack through the semester. React Native's setup guide recommends a framework-based starting point, and Expo provides a documented learning route with TypeScript. This supports the selected direction without implying that Java, Kotlin, or Flutter are obsolete. [React Native setup](https://reactnative.dev/docs/environment-setup), [Expo TypeScript](https://docs.expo.dev/guides/typescript/).

Introduce Expo Go as the student's first preview environment. Later distinguish it from a development build and a distributable application. Expo Go cannot supply arbitrary additional native code. A development build is the appropriate extension when a project needs native capabilities beyond the bundled client. Do not require every student to build native binaries in the first week. [Expo development builds](https://docs.expo.dev/develop/development-builds/introduction/).

Start with a blank TypeScript project and a complete `App.tsx` for early lessons. Introduce Expo Router explicitly at the navigation module with a separate, clearly documented project structure. Do not give students a default Router project while telling them to edit a nonexistent root `App.tsx`. Both template styles exist, so the chosen template must be named. [Expo templates](https://docs.expo.dev/more/create-expo/), [Expo Router](https://docs.expo.dev/router/introduction/).

Flutter/Dart belongs in a short comparison or extension, not a second mandatory track. A semester should give students enough practice with one stack to finish a coherent app. Flutter remains a legitimate cross-platform option; this recommendation is about classroom continuity. [Flutter installation](https://docs.flutter.dev/install).

### EDP: JavaScript first, TypeScript next

Start with visible browser events using plain JavaScript. Supply the small HTML/CSS shell so the subject does not become an HTML course. Then add TypeScript types and Node.js examples. Browser DOM events and Node EventEmitter are related ideas with different APIs; teach the distinction explicitly. [MDN events](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events), [Node events](https://nodejs.org/api/events.html).

The TypeScript transition should explain compilation/type checking separately from execution. Current Node documentation supports running a subset of TypeScript by stripping types; that does not perform type checking and does not mean browsers accept TypeScript directly. A classroom setup must include a separate type-check command. [Node TypeScript](https://nodejs.org/api/typescript.html).

## 3. Mapping the old material to the new courses

| Original material | Keep the underlying idea | Proposed replacement or destination |
| --- | --- | --- |
| M2 Android platform and IDE | What an app is; development workflow | ADET 01–02: problem definition, Expo, tooling, TypeScript |
| M3 activities and lifecycle | Screen state and lifecycle | ADET 08–09: navigation, effects, cleanup; do not equate hooks one-to-one with Activity callbacks |
| M4–M5 widgets and layouts | Input controls, layout, usability | ADET 04–06: components, Flexbox, accessibility, forms |
| M6 event-driven programming | Events, handlers, registration | ADET 05 for UI basics; EDP 01–23 for a full subject |
| M7 intents/navigation | Screen flow and OS handoff | ADET 08 and 16: Router, links, native sharing |
| M8 resources | Reuse of styles, text, images | ADET 04 and 15: design tokens, accessible labels, media assets |
| M10 notifications/dialogs | Feedback and user decisions | ADET 06/16; local reminder extension after device compatibility check |
| M11 broadcasts | Responding to external changes | EDP custom events/pub-sub; ADET app-state/subscription examples, not a claim of Android broadcast equivalence |
| M12–M13 services/alarms | Work over time, cleanup, scheduling | ADET 09; EDP timers/async; native background scheduling as an extension |
| M14–M15 telephony/social | Handing off to another app | ADET 16: system share and link handling with error paths |
| M16 location | Permission-aware device integration | ADET 15: foreground location with denial and mock-data paths |
| M18 networking/parsing | APIs, JSON, failures | ADET 10–12; EDP 09–12 and 21 |
| M19 multimedia | Selecting and displaying media | ADET 15: ImagePicker; optional audio after core project completion |
| M20 lists/adapters | Efficient lists and stable identity | ADET 07/18: FlatList, CRUD, performance |
| M21 content providers | Data ownership and controlled sharing | ADET 13–16; retain Android content providers as platform-specific context |
| M22 APIs/authentication | Trust boundaries and identity | ADET 11/14: API contracts, session concepts, server authorization |
| M23 PHP/MySQL backend | Client/server separation | ADET 12: small JS/TS teaching API; database credentials stay server-side |
| M24 permissions/security/performance | Safe data use and efficient behavior | ADET 14–18; EDP cleanup, validation, concurrency |
| M25 publishing/monetization | Delivery and maintenance | ADET 22–23: packaging, release notes, demo, maintenance; monetization optional |

## 4. Technical corrections to carry into the lessons

**Event-driven does not mean every handler is asynchronous.** EventEmitter calls listeners synchronously by default; promise continuations and timers involve scheduling. Teach direct calls, dispatch, and asynchronous completion separately. Avoid describing all events as a single universal FIFO queue. [Node EventEmitter](https://nodejs.org/api/events.html), [Node event loop](https://nodejs.org/learn/asynchronous-work/event-loop-timers-and-nexttick).

**`await` does not freeze the entire application.** It pauses the current async function until the awaited result settles. CPU-heavy synchronous work can still block the main thread. Workers are a separate technique for suitable computation. [MDN await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await), [Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers).

**TypeScript is not runtime validation.** Data from forms, JSON, and external events must be checked. Start with `unknown` at an untrusted boundary and narrow it; avoid casting everything to the desired shape. [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html).

**A response is not automatically a successful result.** Fetch callers must inspect HTTP status and validate the payload. Demonstrate loading, success, empty, and failure states rather than only the happy path. [MDN Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).

**Timers and subscriptions need cleanup.** Effects should stop work they started. Foreground timers should not be described as guaranteed background alarms. Repeated mount/unmount or start/stop actions should be part of the activity test. [React effects](https://react.dev/learn/synchronizing-with-effects).

**Local persistence is not a secure backend.** AsyncStorage is appropriate for non-sensitive local state. Do not store passwords or private service keys in client code. Authentication identifies a user; authorization must enforce access at a trusted backend. [Expo AsyncStorage](https://docs.expo.dev/versions/latest/sdk/async-storage/), [React Native security](https://reactnative.dev/docs/security).

**Expo Go previews are not production releases.** Release packaging, platform configuration, and distribution are later tasks. Avoid copying old store-policy numbers, fees, or testing periods into a reusable lesson without checking them at teaching time. [Expo build guide](https://docs.expo.dev/deploy/build-project/).

## 5. Emerging technologies: meaningful scope

The “emerging” component should involve examining evidence and building a small experiment, not memorizing buzzwords. The following are instructional choices; they are not claims that each underlying technology was newly invented in 2026.

| Area | Student experiment | Scope and honest labeling |
| --- | --- | --- |
| Connected devices / sensor data | Simulated room readings, then optional phone sensor input | A simulation teaches data flow but is not a physical IoT deployment. Hardware is not required. [Expo sensors](https://docs.expo.dev/versions/latest/sdk/sensors/) |
| AI-assisted features | Compare a deterministic study-tip function with sample model responses using a small quality rubric | A rule-based function is not an AI model. Live inference is an optional teacher-controlled backend integration, subject to a separately verified provider setup. No private API key in the phone app. |
| Cross-platform delivery and offline experiences | Compare a mobile demo with its web behavior; evaluate cached data and stale-data labels | Rendering on the web does not automatically provide all PWA capabilities. [Expo PWA guidance](https://docs.expo.dev/guides/progressive-web-apps/) |
| Real-time applications | Campus queue board with server-sent events | Teach connection closure and reconnection; compare WebSocket conceptually before adding complexity. [MDN SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events), [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) |

Advanced AR/VR, blockchain, custom native modules, distributed message brokers, and production AI infrastructure are optional survey topics. Adding all of them as mandatory builds would crowd out foundational practice.

## 6. Research limits and authoring gates

- Official documentation was inspected for the APIs and teaching routes in the source register. This is a source-informed course proposal, not a labor-market survey or a formal CHED mapping.
- The supplied curriculum has course names, prerequisites, and hours; it does not provide institutional learning outcomes or a calendar. The semester schedule is therefore explicitly proposed.
- Exact package versions are **not yet frozen**. Documentation search results and versioned pages can differ. Before authoring final runnable labs, create one working Expo baseline, match Expo Go, record dependencies, and retain the lockfile.
- No claim is made that all 46 future examples have been implemented or device-tested. Code validation belongs to the authoring phase.
- Follow-up browsing for environment-variable and notification-specific details became unavailable. Those details are not treated as verified here. Notification/background extensions need renewed API and device checks before becoming lessons.
- A real AI provider integration has not been selected or researched in detail. The core plan uses explicitly labeled sample responses; any live option needs separate documentation and cost review.
