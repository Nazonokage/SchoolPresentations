# Application Development and Emerging Technologies — Compiled Contents

**Current finals sequence:** M19 rehearsal, [M20 defense quiz and essays](modules/ADET_M20.md), then [M21 solo mini-capstone announcement and readiness](modules/ADET_M21.md). Alternating assessments apply through M19. If finals has only two teaching meetings, assign M20 as individual preparation between M19 and M21. Keep summative and periodical exam time separate.

**Revision:** 3 November 2026. **Status:** lesson-plan specification. [Open the authored modules](modules/README.md) and [validation record](instructor/VALIDATION.md).

**Stack:** React Native + Expo + TypeScript. This 21-module working sequence combines the supplied 23-topic outline and three research reports. It retains their topic families with different practical depths. The previous 23-topic inventory is source material, not a requirement for 23 meetings.

| Period | Modules | Count |
| --- | --- | ---: |
| Prelim | 01–05 | 5 |
| Midterm | 06–11 | 6 |
| Pre-final | 12–18 | 7 |
| Finals | 19–21 | 3 |

This is the same flexible planning split as EDP, not an assigned timetable. Two meetings weekly, 60–90 minutes each, no Saturdays. Four Prelim teaching meetings can combine selected M04/M05 core material and defer extensions. Exams and school interruptions consume separate slots; consult the [calendar analysis](../Modern_2026_Course_Pack/CALENDAR_AND_CAPACITY.md).

## Database choices and course boundaries

Use **one backend track per implementation**: (A) Python/FastAPI REST API with MySQL/MariaDB through a local XAMPP/WampServer environment, or (B) Node.js/TypeScript REST API with MongoDB. Keep the same client-facing contract so the React Native lessons work with either. Backend scaffolds must be supplied; learning a full second server language is outside one mobile meeting.

XAMPP/WampServer are development stacks, not database names. XAMPP ships MariaDB, as described in its [official FAQ](https://www.apachefriends.org/faq_windows.html). The exact WampServer bundle/version must be checked before setup; its website could not be retrieved in this pass. Use prepared statements for SQL values ([FastAPI SQL guide](https://fastapi.tiangolo.com/tutorial/sql-databases/)); allowlist dynamic identifiers. The MongoDB driver runs in the Node backend ([official connection guide](https://www.mongodb.com/docs/drivers/node/current/connect/)), not inside the mobile client.

The architecture is **mobile app → HTTP API → database**. Never put database credentials in the app. React Native provides fetch for API calls ([networking documentation](https://reactnative.dev/docs/network)). Teach phone-versus-PC localhost explicitly. Use local development only for the lab, and plan a separately secured deployment if remote access is needed.

SQLite remains on-device storage; it does not replace the selected shared backend. Supabase/Firebase become optional architectural comparisons. EDP stays JS/TS-first: its core simulations do not require either database, and its optional persistent examples can use a Node API with the selected database.

## Learning scope

TaskTrail or a small campus-services app supplies familiar examples. Every lesson has an independent checkpoint so one broken lab does not block the next. Core means a small student implementation; comparison/demo means prepared code, a diagram or trace. Broad coverage is not a requirement for every student to build a production system. Prefer plain React state, styling and fetch before optional abstraction libraries.

## Assessment rhythm and realistic meeting plan

Updated 3 November 2026: alternate **odd modules = one 10-item quiz**, **even modules = one coding activity**. This replaces earlier suggestions of multiple assessed drills per lesson. Guided code-alongs remain in every module; they are learning time, not another graded submission. Module 1's quiz is diagnostic after the refresher, with feedback rather than a prerequisite barrier.

- Quiz blueprint: 3 concept/recognition items, 3 code/output traces, 2 error diagnoses, and 2 application decisions. One point each; prepare an answer key with brief explanations. Use only content already taught; M19 is cumulative revision. Allow about 10–15 minutes, adjusting accessibility accommodations as needed.
- Coding activity: one small individual deliverable, one meaningful modification, and one failure case. Suggested 10-point rubric: required behavior 4, handling errors/edge cases 2, explanation and independent change 2, reproducible setup/readability 2. This is a proposed classroom rubric, not an institutional grading policy.
- Optional challenges and extra drills are ungraded. Do not require a quiz AND a separate graded coding task in the same module. Do not count the same artifact again as the summative or periodical exam.
- At 60 minutes: quiz meeting = 5 recap + 25 explanation/demo + 15 guided practice + 10 quiz + 5 feedback; coding meeting = 5 recap + 15 explanation/demo + 30 coding + 10 review. At 90 minutes, add 15 minutes guided practice and 15 feedback/debugging. Setup-heavy lessons need prepared starters.
- Summative exams before each periodical retain their own scheduled slots. M19/M20 prepare students for the solo final practical; they are not the actual final exam.
- If two chapters share a shortened meeting, use one primary assessment and move or omit the other with a recorded adjustment. Never double the workload merely to preserve numbering. Twenty prepared modules do not guarantee twenty available teaching meetings.

Every full lesson will include a plain-language preview, 2–4 observable outcomes, prerequisites, numbered explanations, exact setup/files, complete runnable checkpoint, expected output, one common failure and repair, short Taglish support, and sources. Students should predict, run, explain, and independently change code. “Gumana” is the starting point; “kaya kong ipaliwanag at baguhin” is the understanding check.

## In a nutshell — discuss and create

| Module | Discuss | Create | Assessment |
| --- | --- | --- | --- |
| 01 — Expo ecosystem and Day-One refresher | Understand the mobile toolchain and refresh all essential syntax in one meeting. | A campus welcome screen and tiny baon calculation. | 10-item quiz |
| 02 — Components, props and state | Build a screen from reusable pieces and understand why state updates change it. | A reusable campus service card with a working counter. | Coding activity |
| 03 — Layout, assets and accessibility | Make mobile screens readable and usable on different devices. | A responsive, themed campus dashboard. | 10-item quiz |
| 04 — Interaction, forms and lifecycle | Turn input into validated state and clean up effects. | A task form with validation, editing and a character counter. | Coding activity |
| 05 — Navigation and application structure | Connect screens and separate temporary screen state from shared data. | A task list/detail route with a small tabs or stack layout. | 10-item quiz |
| 06 — Lists and shared client state | Keep a growing collection predictable and easy to interact with. | A searchable task list with add/edit/complete behavior. | Coding activity |
| 07 — HTTP, APIs and asynchronous data | Follow a request from the app to an API and back. | A read-only campus announcements screen. | 10-item quiz |
| 08 — Persistent CRUD through a database API | Store records on a server using one selected backend track. | A mobile create/list/update/delete task flow against a prepared API. | Coding activity |
| 09 — Local storage and offline behavior | Separate local persistence from server storage and cached data. | A task draft or preference that survives restart. | 10-item quiz |
| 10 — Server state and reliable mutations | Keep displayed server data consistent after changes and failures. | A cached list with a create/update mutation and recovery. | Coding activity |
| 11 — Authentication, authorization and secure sessions | Distinguish logging in from permission to access a record. | A prepared sign-in/session flow and ownership-check demonstration. | 10-item quiz |
| 12 — Hardware, permissions and attachments | Add a device feature while handling permission denial. | One image attachment with a preview and removable selection. | Coding activity |
| 13 — Notifications and background work | Understand user alerts and the limits of scheduled work. | A local reminder demonstration and lifecycle timeline. | 10-item quiz |
| 14 — Linking, sharing and location | Hand off to other apps and optionally display a location. | A shareable campus task or place with a safe external link. | Coding activity |
| 15 — Audio, video and app performance | Use media responsibly and diagnose slow interfaces. | A prepared audio or video player and a simple performance comparison. | 10-item quiz |
| 16 — Backend alternatives and emerging technologies | Compare architectures and try one carefully bounded emerging feature. | A client calling a prepared server-side helper with a deterministic fallback. | Coding activity |
| 17 — Testing, security and release planning | Check the app before distributing it. | A test checklist, defect investigation and release plan. | 10-item quiz |
| 18 — Solo project integration | Combine a manageable set of features into one coherent app. | A working vertical slice with UI, API and persistent data. | Coding activity |
| 19 — Finals rehearsal and repair | Review known skills and diagnose common practical mistakes. | A personal repair checklist and rehearsed project explanation. | 10-item quiz |
| **20 — Defense preparation** | Apply course principles to project scenarios | 20 quiz answers and two essays | Quiz and essays |
| 21 — Final project readiness and presentation | Package an individual project so someone else can run and assess it. | A runnable solo project, README and short demonstration. | Coding activity |

## Detailed module contents

## Module 1: Expo ecosystem and Day-One refresher

**Period:** Prelim. **Prerequisite:** Basic previous programming exposure; prepared starter.

**In a nutshell:** Understand the mobile toolchain and refresh all essential syntax in one meeting.

**What we will create:** A campus welcome screen and tiny baon calculation.

### 1.1 Opening demo and introductions

Opening demo and introductions: show the app students will gradually build; identify a useful campus problem.

### 1.2 JavaScript refresher

JavaScript refresher: let/const, values, operators, if/else, for/while, functions, parameters and returns; recognize arrays, objects and arrow callbacks.

### 1.3 TypeScript introduction

TypeScript introduction: simple annotations, inference and type checking versus runtime behavior; JSX as UI syntax.

### 1.4 React Native, Expo, Metro and Hermes roles

React Native, Expo, Metro and Hermes roles; native versus web UI; New Architecture/JSI as a brief conceptual overview.

### 1.5 Prepared create-expo-app workspace, package scripts and device connection

Prepared create-expo-app workspace, package scripts and device connection; Expo Go versus a development build; record tested versions during authoring.

**Evidence of understanding:** Change a value and explain the function result; identify which process serves the app.

**Assessment:** 10-item quiz using the shared blueprint; code-along is ungraded.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 2: Components, props and state

**Period:** Prelim. **Prerequisite:** M01–M01 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Build a screen from reusable pieces and understand why state updates change it.

**What we will create:** A reusable campus service card with a working counter.

### 2.1 View, Text, Image, Pressable and TextInput

View, Text, Image, Pressable and TextInput; imports, exports and component composition.

### 2.2 Typed props, interfaces, optional properties and children

Typed props, interfaces, optional properties and children; distinguish props from local state.

### 2.3 useState, event callbacks and functional updates

useState, event callbacks and functional updates; immutable array/object updates.

### 2.4 Conditional rendering, map and stable keys

Conditional rendering, map and stable keys; component rendering versus direct DOM mutation.

### 2.5 Read a compiler/runtime error and isolate a component

Read a compiler/runtime error and isolate a component; browser addEventListener is not the native component event API.

**Evidence of understanding:** Add a typed prop and reset button without mutating state directly.

**Assessment:** One coding activity using the shared rubric; submit the core result and a brief explanation.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 3: Layout, assets and accessibility

**Period:** Prelim. **Prerequisite:** M01–M02 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Make mobile screens readable and usable on different devices.

**What we will create:** A responsive, themed campus dashboard.

### 3.1 StyleSheet and Flexbox

StyleSheet and Flexbox: direction, alignment, spacing and sizing.

### 3.2 Safe areas, scrolling, keyboard overlap and small screens

Safe areas, scrolling, keyboard overlap and small screens; test large text.

### 3.3 Local/remote images, fonts and icons

Local/remote images, fonts and icons; loading and missing-asset behavior.

### 3.4 Color contrast, accessible labels, touch targets and light/dark appearance

Color contrast, accessible labels, touch targets and light/dark appearance; short localization examples.

### 3.5 NativeWind and Unistyles as comparisons after plain styling

NativeWind and Unistyles as comparisons after plain styling; choose one baseline, not three required styling stacks.

**Evidence of understanding:** Explain a layout problem and improve a label or contrast issue.

**Assessment:** 10-item quiz using the shared blueprint; code-along is ungraded.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 4: Interaction, forms and lifecycle

**Period:** Prelim. **Prerequisite:** M01–M03 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Turn input into validated state and clean up effects.

**What we will create:** A task form with validation, editing and a character counter.

### 4.1 TextInput, press/submit events, keyboard dismissal and controlled values.

TextInput, press/submit events, keyboard dismissal and controlled values.

### 4.2 Required fields, trimming, bounds and useful inline errors

Required fields, trimming, bounds and useful inline errors; prevent duplicate submission.

### 4.3 useEffect dependencies and cleanup

useEffect dependencies and cleanup; timers, subscriptions, focus and AppState distinctions.

### 4.4 Extract a custom hook only after duplicated behavior is visible.

Extract a custom hook only after duplicated behavior is visible.

### 4.5 React Hook Form and Zod as a prepared extension

React Hook Form and Zod as a prepared extension; compare schema validation with static TypeScript types.

**Evidence of understanding:** Reject an empty title and demonstrate timer/subscription cleanup.

**Assessment:** One coding activity using the shared rubric; submit the core result and a brief explanation.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 5: Navigation and application structure

**Period:** Prelim. **Prerequisite:** M01–M04 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Connect screens and separate temporary screen state from shared data.

**What we will create:** A task list/detail route with a small tabs or stack layout.

### 5.1 Expo Router file routes, layout files, stacks and tabs

Expo Router file routes, layout files, stacks and tabs; navigate/back behavior.

### 5.2 Dynamic route parameters and invalid/missing IDs

Dynamic route parameters and invalid/missing IDs; parse parameters before use.

### 5.3 Screen state versus shared state

Screen state versus shared state; preview Context, reducer and Zustand trade-offs.

### 5.4 Deep-link concepts and route guards

Deep-link concepts and route guards; hiding a screen is not server authorization.

### 5.5 Organize components, hooks and data services

Organize components, hooks and data services; retain complete independent lesson checkpoints.

**Evidence of understanding:** Trace a route parameter to a displayed record and explain an invalid route.

**Assessment:** 10-item quiz using the shared blueprint; code-along is ungraded.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 6: Lists and shared client state

**Period:** Midterm. **Prerequisite:** M01–M05 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Keep a growing collection predictable and easy to interact with.

**What we will create:** A searchable task list with add/edit/complete behavior.

### 6.1 FlatList/SectionList, item keys, empty states and list item components.

FlatList/SectionList, item keys, empty states and list item components.

### 6.2 Filtering, sorting and derived values

Filtering, sorting and derived values; avoid storing unnecessary duplicate state.

### 6.3 Lift state, useReducer/Context, then compare a small Zustand store.

Lift state, useReducer/Context, then compare a small Zustand store.

### 6.4 Refresh and pagination concepts

Refresh and pagination concepts; FlashList comparison only after a measured need.

### 6.5 Small gesture/animation demonstration

Small gesture/animation demonstration; preserve an accessible button alternative.

**Evidence of understanding:** Filter and update one item while retaining stable IDs.

**Assessment:** One coding activity using the shared rubric; submit the core result and a brief explanation.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 7: HTTP, APIs and asynchronous data

**Period:** Midterm. **Prerequisite:** M01–M06 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Follow a request from the app to an API and back.

**What we will create:** A read-only campus announcements screen.

### 7.1 HTTP methods, URLs, status codes, headers and JSON

HTTP methods, URLs, status codes, headers and JSON; request/response contracts.

### 7.2 fetch, async/await, try/catch/finally

fetch, async/await, try/catch/finally; check response status and validate response shape.

### 7.3 Loading/error/empty/success UI

Loading/error/empty/success UI; timeouts/cancellation and stale responses.

### 7.4 Phone localhost is the phone, not the teacher PC

Phone localhost is the phone, not the teacher PC; LAN address, server binding, firewall and network isolation troubleshooting.

### 7.5 Native versus browser CORS differences

Native versus browser CORS differences; platform transport restrictions and HTTPS; Axios as an optional alternative.

**Evidence of understanding:** Explain a failed request using status, response body and server logs.

**Assessment:** 10-item quiz using the shared blueprint; code-along is ungraded.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 8: Persistent CRUD through a database API

**Period:** Midterm. **Prerequisite:** M01–M07 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Store records on a server using one selected backend track.

**What we will create:** A mobile create/list/update/delete task flow against a prepared API.

### 8.1 React Native → HTTP API → database architecture

React Native → HTTP API → database architecture; credentials stay on the backend.

### 8.2 SQL track

SQL track: Python/FastAPI API with MySQL or MariaDB from a local XAMPP/WampServer setup; tables, IDs and parameterized values.

### 8.3 MongoDB track

MongoDB track: Node.js/TypeScript API with the official MongoDB driver; collections, documents, ObjectId and validated fields.

### 8.4 Shared endpoint contract and error format

Shared endpoint contract and error format; normalize database IDs to client strings.

### 8.5 Seed/reset data and inspect records

Seed/reset data and inspect records; authorization, indexes and transactions introduced as next-step design issues. Implement one track, compare the other.

**Evidence of understanding:** Create a record, restart the client, and show it persists; handle a missing ID.

**Assessment:** One coding activity using the shared rubric; submit the core result and a brief explanation.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 9: Local storage and offline behavior

**Period:** Midterm. **Prerequisite:** M01–M08 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Separate local persistence from server storage and cached data.

**What we will create:** A task draft or preference that survives restart.

### 9.1 Teaching focus 1

Transient state, persistent preferences, cached responses and authoritative server data.

### 9.2 AsyncStorage-style key/value baseline versus SQLite structured records

AsyncStorage-style key/value baseline versus SQLite structured records; serialization and schema migration concepts.

### 9.3 MMKV native-build requirements and trade-offs

MMKV native-build requirements and trade-offs; optional Drizzle comparison.

### 9.4 Offline indicators, saved drafts and a pending-write model

Offline indicators, saved drafts and a pending-write model; do not silently claim synchronization.

### 9.5 Conflict policy and duplicate submissions

Conflict policy and duplicate submissions; small last-updated example, not a complete offline sync engine.

**Evidence of understanding:** Choose storage for a preference versus a relational record and explain the choice.

**Assessment:** 10-item quiz using the shared blueprint; code-along is ungraded.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 10: Server state and reliable mutations

**Period:** Midterm. **Prerequisite:** M01–M09 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Keep displayed server data consistent after changes and failures.

**What we will create:** A cached list with a create/update mutation and recovery.

### 10.1 Why server state differs from client UI state

Why server state differs from client UI state; query keys and cache lifecycle.

### 10.2 TanStack Query after plain fetch

TanStack Query after plain fetch: loading, refetch and invalidation.

### 10.3 Mutation success/error handling, disabled duplicate actions and bounded retries.

Mutation success/error handling, disabled duplicate actions and bounded retries.

### 10.4 Optimistic UI and rollback as an extension

Optimistic UI and rollback as an extension; retry safety and server idempotency.

### 10.5 Network/focus integration and pagination

Network/focus integration and pagination; caching alone does not provide background/offline synchronization.

**Evidence of understanding:** Trigger a failed mutation and show understandable recovery without a duplicate record.

**Assessment:** One coding activity using the shared rubric; submit the core result and a brief explanation.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 11: Authentication, authorization and secure sessions

**Period:** Midterm. **Prerequisite:** M01–M10 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Distinguish logging in from permission to access a record.

**What we will create:** A prepared sign-in/session flow and ownership-check demonstration.

### 11.1 Mock login versus real identity

Mock login versus real identity; session expiration, logout and protected routes.

### 11.2 Server password hashing/verification and library-supported sessions

Server password hashing/verification and library-supported sessions; no home-made cryptography.

### 11.3 SecureStore for appropriate session material

SecureStore for appropriate session material; no database passwords or private API keys in client code.

### 11.4 Server ownership checks for every record action

Server ownership checks for every record action; demonstrate two test users and a denied request.

### 11.5 OAuth/AuthSession redirects, provider configuration and token concepts

OAuth/AuthSession redirects, provider configuration and token concepts; OAuth is not by itself an identity protocol, and access tokens are not always JWTs.

**Evidence of understanding:** Explain why changing a record ID must not reveal another user’s data.

**Assessment:** 10-item quiz using the shared blueprint; code-along is ungraded.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 12: Hardware, permissions and attachments

**Period:** Pre-final. **Prerequisite:** M01–M11 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Add a device feature while handling permission denial.

**What we will create:** One image attachment with a preview and removable selection.

### 12.1 Image picker versus camera

Image picker versus camera; permission requests at the point of use.

### 12.2 Denied/restricted permission states and a usable fallback.

Denied/restricted permission states and a usable fallback.

### 12.3 Files, URIs, uploads, MIME/size checks and server-side validation.

Files, URIs, uploads, MIME/size checks and server-side validation.

### 12.4 Contacts/media-library and sensor access as guided comparisons using sample data.

Contacts/media-library and sensor access as guided comparisons using sample data.

### 12.5 Development-build/platform labels

Development-build/platform labels; no assumption that every native module runs in Expo Go.

**Evidence of understanding:** Complete the core flow when permission is denied; validate one attachment constraint.

**Assessment:** One coding activity using the shared rubric; submit the core result and a brief explanation.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 13: Notifications and background work

**Period:** Pre-final. **Prerequisite:** M01–M12 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Understand user alerts and the limits of scheduled work.

**What we will create:** A local reminder demonstration and lifecycle timeline.

### 13.1 Alert/modal versus local notification versus remote push.

Alert/modal versus local notification versus remote push.

### 13.2 Permission, scheduling, received/tapped listeners and cleanup.

Permission, scheduling, received/tapped listeners and cleanup.

### 13.3 Push tokens and backend delivery

Push tokens and backend delivery; remote push development-build requirements must be checked by platform.

### 13.4 BackgroundTask and TaskManager

BackgroundTask and TaskManager; replace deprecated BackgroundFetch teaching.

### 13.5 OS scheduling, battery/network constraints and force-quit behavior

OS scheduling, battery/network constraints and force-quit behavior; jobs are not exact recurring timers.

**Evidence of understanding:** Classify local versus remote work and explain why a background job may not run immediately.

**Assessment:** 10-item quiz using the shared blueprint; code-along is ungraded.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 14: Linking, sharing and location

**Period:** Pre-final. **Prerequisite:** M01–M13 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Hand off to other apps and optionally display a location.

**What we will create:** A shareable campus task or place with a safe external link.

### 14.1 React Native text Share versus file Sharing

React Native text Share versus file Sharing; supported targets and cancellation.

### 14.2 Linking for web, dialer, SMS and email

Linking for web, dialer, SMS and email; validate destinations and handle unsupported URLs.

### 14.3 Incoming deep links and route parameters

Incoming deep links and route parameters; user confirmation for external actions.

### 14.4 Foreground location, accuracy and denied permission

Foreground location, accuracy and denied permission; static fallback coordinates.

### 14.5 Map markers, provider configuration and restricted keys

Map markers, provider configuration and restricted keys; background tracking/geofencing as demonstrations only.

**Evidence of understanding:** Share one item and handle a failed or unavailable handoff; maps are optional.

**Assessment:** One coding activity using the shared rubric; submit the core result and a brief explanation.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 15: Audio, video and app performance

**Period:** Pre-final. **Prerequisite:** M01–M14 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Use media responsibly and diagnose slow interfaces.

**What we will create:** A prepared audio or video player and a simple performance comparison.

### 15.1 expo-audio and expo-video rather than deprecated expo-av.

expo-audio and expo-video rather than deprecated expo-av.

### 15.2 Playback state, controls, loading/error UI and resource cleanup.

Playback state, controls, loading/error UI and resource cleanup.

### 15.3 Audio interruptions and app state

Audio interruptions and app state; captions/transcripts and accessible controls.

### 15.4 Hermes and development-versus-release behavior

Hermes and development-versus-release behavior; inspect before optimizing.

### 15.5 List rendering, image size and unnecessary updates

List rendering, image size and unnecessary updates; memoization only for an identified problem.

**Evidence of understanding:** Explain a playback failure and identify a measurable optimization.

**Assessment:** 10-item quiz using the shared blueprint; code-along is ungraded.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 16: Backend alternatives and emerging technologies

**Period:** Pre-final. **Prerequisite:** M01–M15 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Compare architectures and try one carefully bounded emerging feature.

**What we will create:** A client calling a prepared server-side helper with a deterministic fallback.

### 16.1 Compare custom SQL and MongoDB APIs with Supabase/Firebase

Compare custom SQL and MongoDB APIs with Supabase/Firebase; BaaS remains optional.

### 16.2 REST versus GraphQL and real-time updates

REST versus GraphQL and real-time updates; select by requirements.

### 16.3 Expo API routes require a server deployment

Expo API routes require a server deployment; secrets stay in its environment.

### 16.4 Rule-based API design and independent debugging

Rule-based API design: write and explain the decision logic, validate input, handle failures and keep server credentials private.

### 16.5 Teaching focus 5

Widgets, App Intents, Expo modules and experimental UI/server features as a short research comparison, not mandatory installs.

**Evidence of understanding:** Call the helper, handle its failure, and explain which code executes on the server.

**Assessment:** One coding activity using the shared rubric; submit the core result and a brief explanation.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 17: Testing, security and release planning

**Period:** Pre-final. **Prerequisite:** M01–M16 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Check the app before distributing it.

**What we will create:** A test checklist, defect investigation and release plan.

### 17.1 Unit tests for validation, component interaction tests and API integration checks

Unit tests for validation, component interaction tests and API integration checks; tool versions verified during authoring.

### 17.2 Failure matrix

Failure matrix: offline, denied permissions, expired session, empty database and malformed input.

### 17.3 Teaching focus 3

Server authorization, parameterized SQL, validated MongoDB queries and least-privilege credentials.

### 17.4 EAS Build/Submit/Update, signing and runtime compatibility

EAS Build/Submit/Update, signing and runtime compatibility; native changes may require a new build.

### 17.5 Store policies, privacy disclosures and RevenueCat/IAP/ads as research comparisons

Store policies, privacy disclosures and RevenueCat/IAP/ads as research comparisons; no required paid publishing or subscription integration.

**Evidence of understanding:** Trace a defect to client/API/database and justify a compatible update strategy.

**Assessment:** 10-item quiz using the shared blueprint; code-along is ungraded.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 18: Solo project integration

**Period:** Pre-final. **Prerequisite:** M01–M17 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Combine a manageable set of features into one coherent app.

**What we will create:** A working vertical slice with UI, API and persistent data.

### 18.1 Pick a small campus problem, acceptance criteria and a minimal data model.

Pick a small campus problem, acceptance criteria and a minimal data model.

### 18.2 Select one backend track

Select one backend track; diagram app/API/database and trust boundaries.

### 18.3 Integrate one core flow with validation and loading/error states.

Integrate one core flow with validation and loading/error states.

### 18.4 Use Git commits, setup notes, seed data and a small test checklist.

Use Git commits, setup notes, seed data and a small test checklist.

### 18.5 Optional native or emerging feature only after the core works

Optional native or emerging feature only after the core works; no requirement to integrate every library taught.

**Evidence of understanding:** Demonstrate one complete personal feature and explain an independent change.

**Assessment:** One coding activity using the shared rubric; submit the core result and a brief explanation.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 19: Finals rehearsal and repair

**Period:** Finals. **Prerequisite:** M01–M18 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Review known skills and diagnose common practical mistakes.

**What we will create:** A personal repair checklist and rehearsed project explanation.

### 19.1 Cumulative 10-item quiz based on taught UI/state/API/database/security topics.

Cumulative 10-item quiz based on taught UI/state/API/database/security topics.

### 19.2 Guided repair of a broken callback, invalid input and failed API request.

Guided repair of a broken callback, invalid input and failed API request.

### 19.3 Trace a user action through UI, API and database using evidence.

Trace a user action through UI, API and database using evidence.

### 19.4 Rehearse setup and explain design choices without adding a new framework.

Rehearse setup and explain design choices without adding a new framework.

### 19.5 Use feedback to prioritize remaining project defects

Use feedback to prioritize remaining project defects; summative and final exam are separate slots.

**Evidence of understanding:** Identify the cause of one failure and justify a fix; rehearsal is ungraded beyond the quiz.

**Assessment:** 10-item quiz using the shared blueprint; code-along is ungraded.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Module 20: Applied knowledge for the mini-capstone defense

Complete the [20 applied items and two defense essays](modules/ADET_M20.md).

## Module 21: Mini-capstone announcement and solo project readiness

**Period:** Finals. **Prerequisite:** M01–M19 core concepts or the supplied catch-up checkpoint.

**In a nutshell:** Package an individual project so someone else can run and assess it.

**What we will create:** A runnable solo project, README and short demonstration.

### 21.1 Run from a clean setup using documented versions and commands.

Run from a clean setup using documented versions and commands.

### 21.2 Teaching focus 2

Include schema/seed or sample documents, API contract and non-secret configuration example.

### 21.3 Demonstrate success, one invalid input and one failure/recovery path.

Demonstrate success, one invalid input and one failure/recovery path.

### 21.4 Explain personal contributions, borrowed code and references and known limitations.

Explain personal contributions, borrowed code and references and known limitations.

### 21.5 Submit the preparation artifact and rehearse the presentation

Submit the preparation artifact and rehearse the presentation; the actual final practical remains separate.

**Evidence of understanding:** Another person follows the README; the student explains and changes one behavior.

**Assessment:** One coding activity using the shared rubric; submit the core result and a brief explanation.

**Depth and pacing:** Implement only the small core result in class. Comparisons, alternative libraries, provider setup and advanced integrations are demonstrations or optional extensions. Supply configuration and service checkpoints before class.

## Source coverage crosswalk

| Original outline topics | New home |
| --- | --- |
| 1 Expo; 2 components/TS; 3 styling | M01–M03 |
| 4 events/state; 5 Router | M04–M06 |
| 6 APIs/query; 7 forms | M04, M07, M10 |
| 8 storage | M09 |
| 9 hardware; 19 contacts/media | M12 |
| 10 auth; 20 OAuth | M11 |
| 11 BaaS; 12 server routes and rule-based helpers | M16 |
| 13 EAS/OTA; 22 performance/security; 23 publishing/monetization | M15, M17, M20 |
| 14 notifications; 15 background | M13 |
| 16 linking/sharing; 17 location/maps | M14 |
| 18 audio/video | M15 |
| 21 PHP/MySQL REST; newly requested MongoDB option | M07–M08, M11, M17–M18 |
| Additional reports: hooks, lifecycle, lists, testing, offline, native experiments | M04, M06, M09–M10, M16–M17 |

## Research and authoring gates

Read the [topic synthesis](adet%20research%20folder%20JS/SYNTHESIS.md), [technical corrections](adet%20research%20folder%20JS/TECHNICAL_REVIEW.md), [source checks](adet%20research%20folder%20JS/SOURCE_CHECKS.md), and [preserved reports](adet%20research%20folder%20JS/README.md). Report 2 ends at Module 13; its claimed later chapters were not supplied.

Before producing runnable lessons: select and test Expo/RN/React/TS versions; label each native feature by Expo Go/development build/device/server requirements; test the selected database/API track; verify current third-party APIs. Keep corrected BackgroundTask and audio/video choices, native runtime limits on OTA, and server-side secret boundaries. No source snippet has been certified runnable by this contents revision.

Author exact quiz questions, answer keys and coding activity sheets later. Preserve complete code and expected outputs, but require one student-owned change. Final project scope: a small personal app with UI, validation, API persistence, error handling and a reproducible setup; advanced hardware and monetization features are optional; the core assessment focuses on explaining and implementing the taught principles.
