**Acknowledged.** The attached `ADET_TBLCNTS.MD` is treated strictly as reference material (legacy/modernized Android → Kotlin + Jetpack Compose). Useful concepts are preserved and adapted to the required stacks only:

- **ADET**: React Native + Expo + TypeScript (Expo Go first).
- **EDP**: plain JavaScript/TypeScript + browser APIs + Node.js (no mandatory frontend framework).

No full modules are written. The research inventory, outlines, assessment notes, technical accuracy points, and handoff are refined below to incorporate the TOC’s phase structure and concept list while staying faithful to the selected stacks, beginner sequencing, calendar constraints, and quality rules.

**Research date remains November 2, 2026.** Primary sources are still the official Expo, React Native, TypeScript Handbook, MDN, and Node.js docs previously registered. The Android TOC is used only for conceptual mapping (e.g., Activity lifecycle ideas → component mount/unmount + state; XML widgets → RN core components; Broadcast/Service ideas → limited background + event patterns; etc.).

---

### Updated Concept Mapping from Attached TOC (Preserve → Adapt)

| Android TOC Phase / Module | Useful Concept to Preserve | ADET Adaptation (RN + Expo + TS) | EDP Adaptation (JS/TS + browser/Node) |
|----------------------------|----------------------------|----------------------------------|---------------------------------------|
| Foundations & Modern UI (1–5, 8) | Platform overview, UI building blocks, layout, resources/theming | Expo project + Expo Go; View/Text/TextInput/Pressable/Image; StyleSheet + Flexbox; assets & basic theming | Browser DOM elements + CSS; simple HTML structure as “screen” |
| Event-Driven (6) | User actions → handlers, state response | onPress / Pressable + useState; typed event handlers | addEventListener, callbacks, closures, DOM events |
| Navigation & Lists (7, 20) | Screen transitions, data passing, efficient lists | Expo Router or React Navigation basics; FlatList + keys + typed data | Multi-page or SPA-style with custom events / history; dynamic lists via delegation |
| Background / System Events (10–13) | Notifications, dialogs, system listeners, scheduled work | Expo Notifications (where Expo Go allows), Alert, limited background; label limits clearly | Timers, CustomEvent, EventEmitter; no true OS services |
| Hardware & Integrations (14–16, 19) | Telephony/share, location, maps, multimedia | Expo modules (camera, location, sensors, image, AV) + permissions; Sharesheet-style via Linking | Browser geolocation, Media APIs, share via Web Share API (where available) |
| Data / Networking / APIs (18, 21–23) | JSON, HTTP, local data sharing, backend connection | fetch + JSON; AsyncStorage / expo-sqlite; mock or public APIs only; no private keys | fetch / Node http; localStorage or simple files; EventEmitter for data events |
| Security / Permissions / Publish (24–25) | Runtime permissions, performance, secure practices, delivery | Expo permissions flow; never embed secrets; Expo Go vs development builds vs EAS overview | Input validation, AbortController, cleanup of listeners; no client secrets |

Modules 9 and 17 remain skipped as in the TOC. All “modern update” Kotlin/Compose specifics are replaced by the RN/Expo or pure JS/TS equivalents. Industry-standard claims are avoided unless directly supported by the primary docs.

---

### Refined ADET 23-Module Research Outline (incorporating TOC phases)

**Prelim (≈ Modules 1–7)** – Foundations + UI + basic interaction (maps to TOC Phase 1 + start of Phase 2)

1. Programming refresher – variables, constants, types, operators, conditionals  
2. Loops, functions, parameters, return values  
3. Arrays & objects; simple data modeling (canteen / baon structures)  
4. TypeScript fundamentals (annotations, interfaces; compile-time only)  
5. Expo + Expo Go project setup, folder structure, limitations  
6. React components, JSX, props (maps TOC widgets → RN core components)  
7. State + basic events / Pressable (maps TOC event-driven + Compose state ideas)

**Midterm (≈ 8–14)** – Layout, forms, lists, navigation, async, persistence (TOC Phase 2 + networking start)

8. Layouts, StyleSheet, Flexbox (Row/Column/Box equivalents)  
9. Forms, TextInput, simple validation + feedback  
10. Lists / FlatList, keys, basic CRUD display  
11. Navigation basics (Expo Router or stack; typed routes awareness)  
12. Async/await, Promises, fetch + JSON (maps TOC networking)  
13. Local persistence (AsyncStorage or equivalent) + offline thinking  
14. Debugging, structure, maintainable code

**Pre-final (≈ 15–21)** – Device features, security concepts, integration, emerging (TOC Phases 3–6 concepts, adapted)

15. Device features & permissions (one Expo module: camera/location/sensors; Expo Go limits explicit)  
16. Security, privacy, mock-auth concepts (no real secrets; label mocks)  
17. Full local CRUD + lists + persistence integration  
18. Accessibility & polish  
19. Emerging-technology experiment (connected public data or clearly-labeled rule-based feature; not claimed AI model)  
20. Expo Go limitations, development builds overview, delivery concepts (maps TOC publishing ideas at high level)  
21. Integration review / mini-capstone checkpoint

**Final (22–23 only)** – Review & individual project support (no new advanced tech)

22. Final project preparation & review  
23. Project work, troubleshooting, practical-exam support

**Guided activities** remain baon calculator, canteen orders, campus announcements, study timers, task trackers. Each module still specifies prerequisites, 2–4 outcomes, concept order, guided + independent work, observable result, common mistakes, 60 min core + optional 30 min, core vs stretch, and supporting primary sources.

---

### Refined EDP 23-Module Research Outline (event focus, using TOC “Event-Driven” as conceptual anchor)

**Prelim (1–7)**  
1–4. Same programming + TS refresher as ADET (shared foundation).  
5. Events, handlers, callbacks, scope, closures  
6. DOM events, forms, preventDefault, target vs currentTarget  
7. Propagation, capture, bubbling, delegation (dynamic lists)

**Midterm (8–14)**  
8. Event loop, tasks, microtasks, timers  
9. Promises + error handling  
10. Async/await; sequential vs concurrent (Promise.all)  
11. Fetch, validation, AbortController, stale-response handling  
12. Debouncing & throttling  
13. Custom events + simple pub/sub  
14. Node.js EventEmitter (on/emit/once/removeListener, cleanup)

**Pre-final (15–21)**  
15. Persistence, listener cleanup, Workers intro  
16. Testing event-driven behavior (order, fakes)  
17. Introductory real-time (WebSocket/EventSource concepts or simulation)  
18. Simple queues / ordered processing  
19. Browser vs Node event patterns side-by-side  
20. Resilience (isolate handler errors, unhandledrejection)  
21. Integration checkpoint – small event-driven system

**Final (22–23)**  
22. Project preparation & review  
23. Solo project support + practical exam prep

---

### Assessment, Calendar & Feasibility (unchanged substance, reinforced)

- Formative: every module’s coding activity + modification.  
- Summative practical before each periodical.  
- Periodicals per institution calendar (Prelim Jan 13–15 2027, Midterm Feb 8–10, Pre-final Mar 15–17, Final Apr 14–16).  
- Solo individual final projects only.  
- **Capacity shortfall remains real**: 21 content modules before Finals + summatives is tight against Dec 1 2026 start, year-end break, holidays, and College Week (Feb 15–19). Do not add Saturdays, merge modules, or treat homework as class days. Instructor must approve any reduction of stretch topics (e.g., deep emerging-tech or full real-time).  

Final projects stay realistic and free of mandatory paid services or private credentials.

---

### Technical Accuracy Notes (reinforced with TOC context)

- Event-driven does **not** mean every handler is asynchronous (TOC event module → RN onPress and DOM listeners are often sync).  
- `await` does not freeze the whole application.  
- TypeScript does not replace runtime validation.  
- Browser and Node APIs are not interchangeable.  
- Expo Go is not production delivery (maps TOC publishing module at conceptual level only).  
- Device features need permissions; many require development builds beyond Expo Go.  
- Mock login ≠ real authentication; client code must never contain private service credentials.  
- Rule-based output is not an AI model; simulations must be labeled.  
- Android-specific lifecycle/Broadcast/Service/WorkManager ideas are taught only as high-level parallels, never as code to copy.

---

### Handoff Summary (updated)

**Read first**  
Expo TypeScript + development-builds docs, React Native Props/State/Components, TypeScript Handbook, MDN event loop/promises/DOM events, Node EventEmitter. Use the attached TOC only for the concept-preservation table above.

**Folder structure** (unchanged)  
`ADET/` and `EDP/` each with `modules/`, `assessments/`, `projects/`; shared calendar and accuracy notes.

**Evidence-supported decisions**  
- Explicit programming refresher first in both subjects.  
- Map TOC UI/event/navigation/list/networking/permission concepts to RN/Expo or pure JS/TS equivalents.  
- Keep Finals to two review/project modules.  
- Prefer runnable campus-themed labs.

**Still unresolved**  
Exact weekday assignments, whether College Week cancels classes, lab-device availability, preferred navigation depth, and the precise public calendar PDF details.

**Checklist for the Markdown-writing AI**  
- Treat the Android TOC as reference only; never generate Kotlin/Compose or Java/XML code as the teaching target.  
- Preserve the conceptual progression (foundations → interaction → data/async → device/security → integration) while using the required stacks.  
- One module per teaching day; start with variables/conditionals/loops/functions before heavy use.  
- Explain → complete starter → run → trace → modify → explain.  
- Label every mock, simulation, and Expo Go limitation.  
- Cite only verified primary sources.  
- Keep activities free of paid APIs and private keys.  
- Flag schedule pressure; Finals modules contain no new advanced technology.

This refined research inventory now fully incorporates the forgotten TOC while remaining aligned with the original constraints and selected stacks. Ready for the next AI to produce the Markdown modules.