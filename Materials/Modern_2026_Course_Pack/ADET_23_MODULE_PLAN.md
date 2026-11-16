# Application Development and Emerging Technologies: 23-module plan

[Research pack home](README.md) | [Teaching blueprint](TEACHING_BLUEPRINT.md) | [Sources](SOURCE_REGISTER.md)

**Stack:** React Native + TypeScript + Expo. Introduce Expo Go in Module 01. **Status:** researched outline; full lesson files and code are the next phase.

**Course outcome:** Build, explain, test, and demonstrate a small mobile application that addresses a student need, manages state and data, handles failures, uses device features responsibly, and evaluates a contemporary technology extension.

Students are expected to know variables, conditions, loops, and functions from prior programming courses. Modules 02–03 provide a language bridge. React is introduced here rather than assumed. The order below is sequential; early starter programs are independent, while the later project integrates selected features.

## Phase 1 — Make something work, then understand it

| No. | Topic and learning target | Fun guided build | Independent change and evidence | Research basis |
| --- | --- | --- | --- | --- |
| 01 | From a campus problem to the first app: user story, acceptance criteria, Expo tooling, Expo Go | Campus Buddy with Help and Reset buttons | Add two offices; show first successful phone preview and explain the user need | S01–S04 |
| 02 | TypeScript basics: values, types, objects, functions, return values | Baon calculator | Add savings; predict a negative balance; demonstrate and fix a type error | S05 |
| 03 | Arrays, object models, map/filter/reduce, immutable data | Affordable canteen menu | Add a budget filter and total; handle no affordable meals | S05–S06 |
| 04 | JSX, reusable components, props, styles, Flexbox, accessibility basics | Student-card wall | Create reusable office cards; check large text and readable contrast | S04, S07 |
| 05 | State, event handlers, functional updates, derived values | Milk-tea order counter | Enforce a maximum quantity and change size pricing without inconsistent totals | S04 |
| 06 | Controlled forms, validation, helpful feedback | Split-the-merienda bill | Handle blank text, zero people, decimals, and an optional service charge | S05–S06 |

## Phase 2 — Build useful application behavior

| No. | Topic and learning target | Fun guided build | Independent change and evidence | Research basis |
| --- | --- | --- | --- | --- |
| 07 | CRUD, stable IDs, FlatList, empty states | Campus errands list | Add, complete, filter, and delete tasks; duplicate titles must remain distinct | S08 |
| 08 | Navigation, screen hierarchy, route parameters, return flow | Campus office directory with list/detail screens | Add a route and test an invalid ID; use an explicitly introduced Expo Router project | S09 |
| 09 | Effects, timers, lifecycle, cleanup | Study focus timer | Repeatedly start/pause; demonstrate cleanup and explain background limitations | S10 |
| 10 | Promises and async/await in a mobile UI | Simulated canteen order with loading/success/error states | Add a retry action; deliberately trigger failure; identify the simulation | S11–S12 |
| 11 | HTTP, JSON, fetch, status checks, runtime payload validation | Campus announcements reader | Handle empty data, malformed data, and a failed request; provide a local fixture fallback | S13, S06 |
| 12 | Client/server architecture, API contracts, basic create/read integration | React Native client plus a small Node teaching API | Submit a fictional lost-and-found report; validate on both client and server | S13, S18 |
| 13 | Persistence, loading saved data, offline behavior, stale information | Saved study checklist | Restart without losing tasks; handle invalid saved JSON and label cached content | S14 |
| 14 | Security and privacy: identity, authorization, storage boundaries, minimal data | Session-flow prototype and safe/unsafe data-storage comparison | Document where a real server must enforce access; never label a mock login as secure authentication | S15–S17 |

## Phase 3 — Test the app and explore contemporary features

| No. | Topic and learning target | Fun guided build | Independent change and evidence | Research basis |
| --- | --- | --- | --- | --- |
| 15 | Device integration: image selection, foreground location, permissions | Photo-based campus note with optional location | Handle denied permission and canceled selection; offer a sample-photo/location path | S19–S20 |
| 16 | Sharing, external-app handoff, feedback, platform differences | Share a study-session invitation | Handle unavailable destinations and canceled actions; optional local-reminder extension only after compatibility verification | S21; feature-specific docs to recheck |
| 17 | Debugging, test cases, pure functions, regression thinking | Fix a deliberately broken budget calculator | Submit a reproducible bug, a repair, and tests for normal and invalid input | S22, S05 |
| 18 | App organization, reducers, list performance, maintainability | Refactor the errands app into clear responsibilities | Keep behavior unchanged while separating data rules from UI; compare before/after traces | S23, S08 |
| 19 | Offline-first decisions and mobile/web comparison | Campus information app with a visible cached-data badge | Compare native and web behavior; write an update/conflict policy; do not promise automatic synchronization | S14, S24 |
| 20 | Connected-device concepts and event streams | Simulated room comfort monitor; optional phone sensor | Mark stale readings, reject malformed data, unsubscribe correctly; label simulated versus physical data | S25, S10 |
| 21 | AI-assisted feature evaluation and responsible integration design | Study-tip lab comparing rules with clearly labeled sample model outputs | Score relevance, correctness, privacy, and usefulness; add human correction and fallback behavior | S15 for client trust boundary; live model provider research pending |
| 22 | Integration, packaging, release notes, Expo Go versus builds | Assemble and test the capstone release candidate | Run a defined acceptance checklist; document limitations and deployment steps; paid store publication is not required | S03, S26 |
| 23 | Capstone demonstration, usability feedback, maintenance | Campus Companion or an approved student-life app | Demo success/failure/offline flows, explain one technical decision, and implement one peer-feedback improvement | Course synthesis |

## Project scope

Recommended project: **Campus Companion**, built from a manageable selection of earlier activities. Required features: a clear user need, at least two connected screens, a validated form, a persistent list, useful empty/error/loading states, and accessible labeling. Include one meaningful external-data or device integration with a fallback.

The emerging-technology experiment may be a separate small prototype. It need not be forced into the final app when it does not help the user. Grade the reasoning and evidence, not how many technologies students name.

A backend can use a teacher-provided local service. Students should understand requests, responses, and validation without being required to deploy production infrastructure or buy services. The mobile setup guide must distinguish a physical phone's network address from the computer's `localhost`.

## Intended level of depth

The final modules should teach why each technique is needed, show a complete runnable example, trace its behavior, introduce an intentional failure, and ask students to modify it. A list of links or isolated snippets will not count as a complete lesson. Each module should fit approximately three contact hours, with integration and support time allocated separately.
