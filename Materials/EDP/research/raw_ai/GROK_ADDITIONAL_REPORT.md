**Research date:** November 2, 2026. Sources inspected via official landing pages and documentation content (Expo, React Native, TypeScript, MDN, Node.js). No paywalled or invented material. CHED CMO 25 s. 2015 positions Applications Development and Emerging Technologies as a common course; exact institutional syllabi vary.

**A. SOURCE REGISTER**

1. **Using TypeScript (Expo)**  
   Organization: Expo. Updated ~Oct 2026.  
   Landing: https://docs.expo.dev/guides/typescript/  
   Format: HTML. Open access.  
   Supports: ADET (project setup, TypeScript migration, tsconfig, path aliases).  
   Useful: Official first-class TypeScript support, create-expo-app defaults, strict mode, type generation. Inspected. Current for SDK ~58.

2. **Create a project / Start developing / Tutorial series (Expo)**  
   Organization: Expo. Updated Oct 2026.  
   Landing: https://docs.expo.dev/get-started/create-a-project/, https://docs.expo.dev/get-started/start-developing/, https://docs.expo.dev/tutorial/introduction/  
   Format: HTML. Open.  
   Supports: ADET (setup, Expo Go, file structure, first changes, navigation intro).  
   Useful: Beginner-friendly, TypeScript template, Expo Router basics, universal (Android/iOS/web). Inspected.

3. **Expo Router documentation (Introduction, Navigation, Layouts, Common patterns, Notation)**  
   Organization: Expo. Updated 2026.  
   Landing: https://docs.expo.dev/router/introduction/, https://docs.expo.dev/router/basics/navigation/, related pages.  
   Format: HTML. Open.  
   Supports: ADET (file-based routing, Stack/Tabs, Link/router, params, typed routes).  
   Useful: Official replacement for older navigation patterns; deep-linking and universal routing. Inspected.

4. **React Native – React Fundamentals, Props, State, Core Components, Layout Props**  
   Organization: Meta / React Native. Updated 2026.  
   Landing: https://reactnative.dev/docs/intro-react, https://reactnative.dev/docs/props, https://reactnative.dev/docs/components-and-apis, https://reactnative.dev/docs/layout-props  
   Format: HTML. Open.  
   Supports: ADET (components, JSX, props, state/useState, View/Text/Pressable/ScrollView/FlatList, Flexbox).  
   Useful: Official core concepts; maps well to guided activities. Inspected. Note: some legacy class-component examples exist alongside hooks.

5. **TypeScript Handbook (The Basics, Everyday Types, etc.)**  
   Organization: Microsoft / TypeScript team. Continuously updated; handbook structure stable.  
   Landing: https://www.typescriptlang.org/docs/handbook/  
   Format: HTML (also referenced as downloadable in older announcements). Open / CC-influenced.  
   Supports: Both subjects (variables, types, functions, objects, narrowing, async typing).  
   Useful: Primary reference for TypeScript fundamentals without assuming prior TS knowledge. Inspected via handbook pages.

6. **MDN – Using promises, Promise, JavaScript execution model / Event Loop, DOM events, EventTarget.addEventListener**  
   Organization: MDN Web Docs (Mozilla). Updated 2026.  
   Landing: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model, https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Events, https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener  
   Format: HTML. Open.  
   Supports: EDP (events, handlers, event loop, microtasks/tasks, promises, async/await, DOM, forms, propagation).  
   Useful: Authoritative, browser-focused, clear diagrams/explanations of event loop and promises. Inspected.

7. **Node.js Events / EventEmitter**  
   Organization: Node.js. Current (v25/v26 docs).  
   Landing: https://nodejs.org/api/events.html  
   Format: HTML. Open (MIT-licensed Node).  
   Supports: EDP (EventEmitter, on/emit/once, sync vs async listeners, error handling, AbortSignal).  
   Useful: Official Node counterpart to browser events; shows differences. Inspected.

8. **CHED CMO No. 25, Series of 2015 (and related curriculum references)**  
   Organization: Commission on Higher Education (Philippines).  
   Landing/references: Various HEI syllabi and CourseHero/Scribd mirrors of the CMO; official CHED site lists related orders.  
   Format: PDF (original CMO). Access varies by mirror.  
   Supports: Both (course existence, common-course status for ADET-like subjects).  
   Useful: Confirms ADET as a required common course; outcomes emphasize application development and emerging tech. Partially inspected via secondary summaries; exact page numbers not re-verified here. Note: institutional implementations differ; forthcoming CMO revisions mentioned in 2026 AI-related announcements.

9. **Attached legacy outline (ADET_TBLCNTS.MD)**  
   Author: Course materials (modernized Android/Kotlin/Compose).  
   Format: Markdown.  
   Supports: Concept mapping only (lifecycle → state, events → handlers, lists → LazyColumn/FlatList equivalents, notifications, services → background/WorkManager analogs, networking → fetch/Retrofit-style, security/publishing).  
   Useful: Preserves useful concepts (activities/lifecycle, event-driven UI, data lists, background work, permissions, APIs) while shifting stacks. Treat as reference, not template.

Additional secondary but useful inspected pages: Expo blog/SDK notes (native modules, type generation), React TypeScript CheatSheet (community, for component typing), freeCodeCamp/MDN-aligned promise handbooks (for beginner explanations). Avoid SEO-only tutorials as primary sources.

**Unverified/restricted:** Specific Iloilo collegiate PDF (user-supplied dates used instead); full paywalled university syllabi; exact page numbers in older printed textbooks.

**B. TWO SEPARATE 23-MODULE RESEARCH OUTLINES**

**ADET – Application Development and Emerging Technologies**  
Stack: React Native + Expo (Expo Go primary), TypeScript.  
Approach: Explain → complete starter → run (Expo Go / web) → trace → modify → explain. Relatable Philippine campus activities (baon, canteen, announcements, study timers, task trackers).  
Core vs stretch noted. First modules build programming foundations explicitly.

**Prelim (Modules 1–7 suggested)**  
1. **Programming Refresher: Variables, Constants, Types, Operators** (Prelim)  
   Prerequisites: None / basic computer literacy.  
   Outcomes: Declare and use let/const; distinguish primitive types; apply operators; explain mutability.  
   Coverage: JS/TS variables, number/string/boolean/null/undefined, arithmetic/comparison/logical, template literals. Introduce TypeScript type annotations lightly.  
   Activity: Baon calculator (fixed budget, compute remaining after expenses).  
   Independent mod: Add tax or tip percentage.  
   Observable: Console or simple Text output of remaining amount.  
   Mistakes: Reassigning const, forgetting types, string vs number coercion.  
   60 min core + 30 min extension (more operators or early interface).  
   Sources: TypeScript Handbook Basics; Expo TS guide. Core.

2. **Conditionals, Loops, Functions (Parameters & Return)** (Prelim)  
   Prerequisites: Module 1.  
   Outcomes: Write if/else and switch; for/while loops; define/call functions with typed params/returns.  
   Coverage: Control flow, early return, pure functions.  
   Activity: Canteen order total with discounts (if student ID) and loop over items.  
   Mod: Add free item threshold.  
   Result: Correct total printed/displayed.  
   Mistakes: Off-by-one, missing return, scope issues.  
   Sources: TS Handbook, MDN JS. Core.

3. **Arrays, Objects, and Simple Data Modeling** (Prelim)  
   Prerequisites: 1–2.  
   Outcomes: Create/manipulate arrays and objects; map data to UI-friendly shapes.  
   Coverage: Array methods (map/filter/find basic), object literals, interfaces/types.  
   Activity: Campus announcement list (title, date, priority).  
   Mod: Filter by priority.  
   Result: Filtered list displayed.  
   Mistakes: Mutating vs new arrays, undefined property access. Core.

4. **Project Setup, Expo Go, and First Screen** (Prelim)  
   Prerequisites: 1–3.  
   Outcomes: Create Expo TS project; run on Expo Go/web; edit and see Fast Refresh.  
   Coverage: create-expo-app, app.json, src/app structure, Expo Go limitations.  
   Activity: Hello + personal baon status screen.  
   Mod: Change theme colors.  
   Result: Live update on device/emulator.  
   Sources: Expo Create/Start/TS guides. Core. Note Expo Go is not production.

5. **React Components, JSX, Props** (Prelim)  
   Prerequisites: 4.  
   Outcomes: Build functional components; pass and type props; compose UI.  
   Coverage: Function components, JSX rules, props (typed), children.  
   Activity: Reusable “AnnouncementCard” and “BaonSummary” components.  
   Mod: Add optional badge prop.  
   Sources: RN React Fundamentals / Props. Core.

6. **State with useState and Basic Events** (Prelim)  
   Prerequisites: 5.  
   Outcomes: Manage local state; handle press/change events; update UI reactively.  
   Coverage: useState, Pressable/TextInput, controlled inputs, event handlers (lambdas).  
   Activity: Study timer (start/pause/reset) or interactive baon tracker.  
   Mod: Persist last value in state only.  
   Mistakes: Mutating state directly, missing key on lists later. Sources: RN State. Core.

7. **Layouts with Flexbox, View, Text, StyleSheet** (Prelim)  
   Prerequisites: 5–6.  
   Outcomes: Arrange UI with Flexbox; style consistently; support basic accessibility.  
   Coverage: flexDirection, justify/align, StyleSheet.create, safe areas.  
   Activity: Canteen menu layout (rows/columns of items).  
   Mod: Responsive-ish stacking.  
   Sources: RN Layout Props / View. Core.

**Midterm (Modules 8–14)**  
8. **Forms, Validation, Controlled Components**  
   Outcomes: Build forms; validate input; show errors.  
   Activity: Student registration / order form (name, course, items).  
   Mod: Required fields + simple regex.  
   Mistakes: Uncontrolled inputs, no error state. Core.

9. **Lists and FlatList / ScrollView (CRUD basics – Read)**  
   Outcomes: Render dynamic lists efficiently; keyExtractor.  
   Activity: Task tracker list from array of objects.  
   Mod: Empty state. Sources: RN lists. Core.

10. **Navigation with Expo Router (Stack & Tabs basics)**  
    Outcomes: File-based routes; navigate with Link/router; pass params.  
    Activity: Home → Task detail → Settings tabs.  
    Mod: Dynamic [id] route. Sources: Expo Router docs. Core.

11. **Async/Await Introduction and Timers**  
    Outcomes: Write async functions; use setTimeout/setInterval safely; understand non-blocking.  
    Activity: Study timer with async tick simulation.  
    Note: await does not freeze the whole app. Core (ties to event loop later in EDP).

12. **HTTP, Fetch, JSON, Simple API Integration**  
    Outcomes: Fetch data; parse JSON; handle loading/error states.  
    Activity: Load mock campus announcements (public JSON or local mock).  
    Mod: Retry button. Mistakes: Missing error handling, treating response as data. Core. No private credentials.

13. **Local Persistence (AsyncStorage or Expo SecureStore light)**  
    Outcomes: Save/load simple data offline.  
    Activity: Persist task list or baon history.  
    Mod: Clear data. Core (label offline behavior).

14. **Debugging, Console, Error Boundaries basics, Maintainable Structure**  
    Outcomes: Use console/debugger; organize folders; basic testing mindset.  
    Activity: Fix seeded bugs in prior activity. Core.

**Pre-final (Modules 15–21)**  
15. **Permissions and Device Features (Camera/Location light, with Expo)**  
    Outcomes: Request permissions; use simple device APIs; handle denial.  
    Activity: Photo attachment for task or location-tagged announcement (mock fallback).  
    Note: Expo Go limits; some need dev builds. Sources: Expo docs. Core + stretch for advanced sensors.

16. **Authentication Concepts (Mock Login + Secure Storage)**  
    Outcomes: Implement mock auth flow; store token securely; protect routes.  
    Activity: Simple login → protected task list.  
    Note: Mock is not real auth; no real credentials. Core.

17. **Security, Privacy, and Client-Side Best Practices**  
    Outcomes: Avoid hard-coded secrets; validate inputs; understand data minimization.  
    Activity: Audit prior project for leaks. Core.

18. **Emerging Tech Experiment 1: AI-assisted or Connected Data (rule-based or public API)**  
    Outcomes: Integrate a simple external service or rule-based “smart” feature; label simulations.  
    Activity: “Smart baon suggester” (rules) or public weather for outdoor study.  
    Note: Rule-based ≠ AI model. Stretch options clear. Core light + stretch.

19. **Testing Basics and Maintainable Code**  
    Outcomes: Write simple unit tests or manual test plans; extract components.  
    Activity: Test pure functions from baon calculator. Core.

20. **Expo Go Limits, Development Builds, Delivery Concepts**  
    Outcomes: Explain Expo Go vs development/production builds; basic EAS awareness (no mandatory paid).  
    Activity: Document limitations of current project. Core.

21. **Project Architecture Review and Solo Project Kickoff**  
    Outcomes: Plan personal final project; map requirements to learned modules.  
    Activity: Proposal + wireframe + data model. Core.

**Finals (Modules 22–23 only – review/prep)**  
22. **Review, Troubleshooting Common Issues, Summative Prep**  
    Outcomes: Diagnose frequent errors; complete practice scenarios.  
    No new advanced tech.  

23. **Final Practical Project Support and Exam Prep**  
    Outcomes: Polish individual project; prepare demo and reflection.  
    Solo only.

**EDP – Event-driven Programming**  
Stack: Plain JS then TypeScript; browser APIs + Node.js. No mandatory frontend framework.  
Same teaching approach and campus activities.

**Prelim (1–7)**  
1. **JS Refresher: Variables, Constants, Types, Operators** – identical structure to ADET 1, pure browser/Node console or simple HTML. Core. Sources: MDN + TS Handbook.  
2. **Conditionals, Loops, Functions** – same. Core.  
3. **Arrays & Objects** – same. Core.  
4. **Introduction to Events, Handlers, Callbacks, Scope, Closures**  
   Outcomes: Register handlers; understand this/scope; basic closures.  
   Activity: Button click that updates baon display via closure.  
   Sources: MDN EventTarget. Core. Note: Event-driven ≠ every handler is async.  
5. **DOM Events, Forms, Propagation, Delegation**  
   Outcomes: addEventListener; preventDefault/stopPropagation; event delegation.  
   Activity: Canteen order form with live total and delegated list clicks. Core.  
6. **Event Loop, Tasks, Microtasks, Timers**  
   Outcomes: Predict output order; distinguish macrotask/microtask.  
   Activity: Trace setTimeout vs Promise.resolve vs sync code with campus announcement “queue”.  
   Sources: MDN Execution model + Using promises. Core. Explicit: await does not freeze the whole application.  
7. **Promises Fundamentals**  
   Outcomes: Create/consume promises; then/catch/finally; Promise.all vs allSettled.  
   Activity: Simulated sequential vs parallel “fetch” of study resources. Core.

**Midterm (8–14)**  
8. **Async/Await and Error Handling**  
   Outcomes: Rewrite promise chains; try/catch with await; typed Promises.  
   Activity: Async study timer with error injection. Core. TS does not replace runtime validation.  
9. **Sequential vs Concurrent Work**  
   Outcomes: Control concurrency; race conditions awareness.  
   Activity: Parallel vs sequential mock API calls for announcements. Core.  
10. **Fetch, Validation, Cancellation, Stale Responses**  
    Outcomes: Use AbortController; validate responses; ignore stale.  
    Activity: Searchable campus directory with cancel on new keystroke. Core.  
11. **Debouncing and Throttling**  
    Outcomes: Implement debounce/throttle for input/scroll.  
    Activity: Live search of tasks or canteen items. Core.  
12. **Custom Events, Pub/Sub, State Transitions**  
    Outcomes: dispatchEvent; simple EventTarget-based bus; model state machines lightly.  
    Activity: Task status machine (todo → doing → done) with custom events. Core.  
13. **Node.js EventEmitter**  
    Outcomes: Create emitters; on/once/emit; error events; differences from DOM.  
    Activity: Node-based “campus announcement broadcaster”.  
    Sources: Node.js events.html. Core. Browser and Node APIs are not interchangeable.  
14. **Persistence, Cleanup, Memory Leaks**  
    Outcomes: Remove listeners; AbortSignal; localStorage or simple file in Node.  
    Activity: Cleanup on page unload / process exit. Core.

**Pre-final (15–21)**  
15. **Workers and Off-Main-Thread Basics (light)**  
    Outcomes: Introduce Web Workers or worker_threads conceptually; when to use. Stretch-heavy.  
16. **Queues and Background-like Patterns**  
    Outcomes: Simple in-memory queue with events. Core light.  
17. **Testing Event-Driven Behavior**  
    Outcomes: Test handlers, simulate events, assert order. Core.  
18. **Introductory Real-Time (WebSockets or Server-Sent Events mock)**  
    Outcomes: Connect to public echo or mock; handle open/message/close/error.  
    Activity: Live campus announcement feed simulation. Core + stretch.  
19. **Integration Patterns and Error Recovery**  
    Outcomes: Combine fetch + events + cleanup. Core.  
20. **Security & Privacy in Event-Driven Clients**  
    Outcomes: No secrets in client; sanitize; origin checks. Core.  
21. **Solo Project Architecture & Kickoff** – parallel to ADET.  

**Finals (22–23)**  
22. Review + common pitfalls (event loop order, missing removeEventListener, unhandled rejections).  
23. Solo project support + practical exam prep.

**C. ASSESSMENT AND CALENDAR PLAN**

- **Formative:** In-class guided activities + independent modifications (observable results, code walk-throughs). Prefer coding over quizzes.  
- **Summative exams:** Before each periodical (practical + short conceptual). Cover cumulative skills of the period.  
- **Periodical exams:** Institutional (Prelim/Midterm/Pre-final/Final).  
- **Practical coverage suggestions:**  
  - Prelim: Refresher + basic components/events + simple interactive screen/list.  
  - Midterm: Forms, navigation/lists (ADET) or async/fetch/debounce (EDP), persistence.  
  - Pre-final: Full mini-app or event system with error handling, permissions/mock auth or real-time.  
  - Final: Individual project only.  

**Solo final project (both subjects):**  
Requirements (achievable): Working app/system using majority of core modules; local data; at least one async/external or event source; clear README with setup, limitations, and “what is simulated”; individual demo + short reflection. No group work.  
Rubric sketch: Functionality (40%), Code quality & TypeScript usage (20%), Correct use of events/async/state (20%), Documentation & honesty about limitations (10%), Demo & troubleshooting (10%).  

**Calendar feasibility (user-supplied Iloilo dates, research date Nov 2 2026):**  
- Classes: Dec 1 2026 start → year-end break → resume Jan 4 2027.  
- Prelims Jan 13–15, Midterms Feb 8–10, College Week Feb 15–19 (do not assume automatic cancellation), Pre-finals Mar 15–17, Finals Apr 14–16, end Apr 16.  
- Two meetings/week, ~60–90 min, one module per meeting, no Saturdays, summative before each periodical, Finals only two modules.  

Rough capacity: From Dec 1 to mid-April, accounting for break, exam weeks, and College Week uncertainty, realistic teaching days before Finals are closer to 18–20 than the 21 needed for a strict 7/7/7/2 split of 23 modules. Shortfall exists.  

Honest adjustments (instructor-approved only): Drop or merge lowest-priority stretch topics (e.g., advanced workers, full EAS, heavy AI experiment); move some review into exam-prep windows; compress early refresher if students already strong; treat College Week case-by-case. Do not invent Saturdays, skip exams, or count homework as class days. Exact weekday schedule unknown—do not invent dates.

**D. TECHNICAL ACCURACY NOTES**

- Event-driven programming does not require every handler to be asynchronous; many DOM and EventEmitter listeners run synchronously.  
- `await` yields only the current async function; the rest of the application (event loop) continues.  
- TypeScript provides static checking only; runtime validation (forms, API responses) is still required.  
- Browser APIs (DOM, fetch, workers) and Node.js APIs (EventEmitter, fs, worker_threads) are not interchangeable; teach differences explicitly.  
- Expo Go is a development client, not a production deployment vehicle; some native modules and permissions require development builds.  
- Device features often need explicit permissions and may be limited or unavailable in Expo Go.  
- Mock login / mock tokens are teaching tools, not real authentication or authorization.  
- Rule-based “smart” features or simple heuristics are not AI models; label them clearly.  
- Client-side code must never contain private API keys or service credentials; use public mocks or environment proxies for learning.  
- Any simulated or fallback data must be clearly labeled in UI and documentation.

**E. HANDOFF SUMMARY**

**Recommended sources to read first:**  
Expo TS + Create/Start + Router basics; React Native React Fundamentals/Props/State; TypeScript Handbook Basics/Everyday Types; MDN Using promises + Execution model + addEventListener; Node.js Events page.

**Proposed folder structure:**  
```
ADET/
  00-sources.md
  modules/
    01-...md (research outlines only)
  activities/
  final-project-spec.md
EDP/
  (parallel)
shared/
  calendar-notes.md
  assessment-rubrics.md
  technical-accuracy.md
```

**Decisions supported by evidence:**  
- Start both with explicit programming refresher before frameworks/async.  
- Expo + TypeScript is officially well-supported and beginner-accessible via Expo Go.  
- File-based Expo Router is current recommended navigation.  
- MDN + Node official docs are the correct primary references for events/event-loop/promises.  
- Solo final projects; Finals limited to two modules.  
- Core activities stay free of paid services/hardware.

**Unresolved questions:**  
- Exact meeting weekdays and whether College Week cancels classes.  
- Institutional lab machine setup (Node, Expo, Android/iOS simulators).  
- Student prior exposure to JS (affects refresher depth).  
- Whether a light backend mock server is allowed for ADET/EDP final projects.  
- Forthcoming CHED CMO details for computing programs (AI emphasis noted but not yet binding).

**Claims needing verification:**  
- Exact number of available teaching days once weekdays are assigned.  
- Any school-specific holiday list beyond the supplied dates.  
- Current Expo SDK number and any breaking changes after research date.

**Checklist for the AI that will write the Markdown lessons:**  
- Follow explain → complete starter code → run → trace → modify → explain.  
- Keep activities free of paid APIs/accounts/special hardware; label all mocks/simulations.  
- Explicitly teach foundations before using them.  
- Include common beginner mistakes and observable success criteria.  
- Respect 60-min core + optional 30-min extension.  
- Cite only verified sources; preserve technical accuracy notes.  
- Tagalog-friendly explanations welcome but primary language English.  
- One module = one teaching day; do not combine.  
- Final two modules = review/project support only.  
- Flag any stretch content clearly.  
- Produce runnable TypeScript examples that match the chosen stack.