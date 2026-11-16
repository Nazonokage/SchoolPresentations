**Research date:** November 2, 2026 (sources inspected via official sites, MDN, Node.js docs, Expo/React Native docs, and targeted searches; no invented URLs, page numbers, or licenses).

This assembles primary documentation, teaching outlines, calendar/assessment notes, technical accuracy points, and a handoff for another AI to produce Markdown modules. Core activities use free, local, or Expo Go-friendly tools; no mandatory paid APIs, cloud accounts, or special hardware. Prefer depth and runnable labs (explain → complete starter → run → trace → modify) over quizzes. Relatable Philippine-college contexts: baon calculator, canteen orders, campus announcements, study timers, task trackers.

**Important feasibility note (honest capacity limit):** 23 modules per subject with only 2 in Finals requires ~21 teaching days before Finals + summative exams. With 2 meetings/week, no Saturdays, and the given calendar (semester start Dec 1 2026; resume Jan 4 2027; Prelim exams Jan 13–15; Midterm Feb 8–10; College Week Feb 15–19; Pre-final Mar 15–17; Final Apr 14–16; end Apr 16), a strict 7/7/7/2 split is tight or short after holidays, breaks, and exam windows. Do not invent dates, add Saturdays, merge modules, skip exams, or treat homework as class days. Flag shortfall to instructor; possible adjustments (instructor-approved only): trim optional/stretch topics, move lighter modules earlier, or reduce depth on advanced emerging-tech experiments. Exact weekdays unassigned—do not invent them.

---

### A. SOURCE REGISTER

Sources are primary or high-quality public materials actually inspected or confirmed via official landing pages. “Inspected” = content retrieved/verified in this research; “snippet” = search result only. No paywalled full textbooks reproduced. Licenses noted only when explicit.

**Core / Official (priority)**

1. **Expo Documentation (TypeScript guide, development builds, Expo Go, SDK, libraries)**  
   - Organization: Expo  
   - Updated: ongoing (pages checked 2026; e.g., TypeScript guide, development-builds FAQ/intro)  
   - Landing: https://docs.expo.dev/  
   - Key pages: https://docs.expo.dev/guides/typescript/, https://docs.expo.dev/develop/development-builds/introduction/, https://docs.expo.dev/develop/development-builds/faq/, https://docs.expo.dev/workflow/using-libraries/, SDK reference  
   - Format: HTML (Markdown available for agents)  
   - Access: free, public  
   - License: documentation generally reusable with attribution (check site)  
   - Supports: ADET (all Expo/React Native modules, TypeScript setup, Expo Go limits, permissions, device features, delivery)  
   - Why useful: Official, current, beginner-to-intermediate path from create-expo-app + Expo Go to development builds; explicit limits of Expo Go (no custom native, limited push/links, etc.).  
   - Notes: Prefer over third-party tutorials. Expo Go is for development/playground, not production.

2. **React Native Documentation (Components, Props, State, Layout, Core APIs)**  
   - Organization: Meta / React Native  
   - Updated: ongoing (2026 pages)  
   - Landing: https://reactnative.dev/docs/  
   - Key: https://reactnative.dev/docs/components-and-apis, /props, /state, /intro-react, /view, /layout-props, etc.  
   - Format: HTML  
   - Access: free  
   - Supports: ADET (components, props, state, events, lists, navigation basics, styling)  
   - Why useful: Primary source for RN primitives; pairs with Expo.  
   - Notes: New Architecture mentions exist; stick to stable core for beginners.

3. **TypeScript Handbook**  
   - Organization: Microsoft / TypeScript team  
   - Updated: ongoing (Handbook intro checked ~Nov 2026)  
   - Landing: https://www.typescriptlang.org/docs/handbook/intro.html  
   - Key sections: Basics, Everyday Types, Narrowing, Functions, Object Types, etc.  
   - Format: HTML  
   - Access: free  
   - License: open (docs site)  
   - Supports: Both subjects (TypeScript fundamentals after JS refresher; types do not replace runtime validation)  
   - Why useful: Official, progressive, non-framework-specific.  
   - Notes: Does not teach full JS; students need prior JS basics.

4. **MDN Web Docs – JavaScript Guide, Promises, Execution model, DOM Events**  
   - Organization: Mozilla  
   - Updated: ongoing (2026)  
   - Landing: https://developer.mozilla.org/en-US/docs/Web/JavaScript/  
   - Key: Using promises, Promise, Execution model / event loop, DOM events, event bubbling/delegation (also Spanish/other locales useful for Tagalog-support context)  
   - Format: HTML  
   - Access: free  
   - Supports: EDP (events, handlers, event loop, microtasks/tasks, promises, async/await, fetch, DOM); ADET (async patterns)  
   - Why useful: Authoritative, clear diagrams/explanations of event loop, tasks vs microtasks, propagation.  
   - Notes: Browser-focused; distinguish from Node.

5. **Node.js Events / EventEmitter documentation**  
   - Organization: Node.js  
   - Landing: https://nodejs.org/api/events.html (and GitHub source)  
   - Format: HTML / Markdown  
   - Access: free  
   - Supports: EDP (Node EventEmitter, pub/sub patterns, cleanup)  
   - Why useful: Official; shows synchronous listener invocation by default; AbortController integration examples.  
   - Notes: Not interchangeable with browser EventTarget in all cases.

**Additional useful inspected / high-value**

6. Expo tutorial / build-a-screen and related workflow pages (docs.expo.dev/tutorial/...) – practical RN + Expo UI patterns. Supports ADET UI/forms/layouts.  
7. React TypeScript Cheatsheet (community, GitHub typescript-cheatsheets/react) – referenced by Expo; practical component typing. Supports ADET.  
8. MDN / WHATWG DOM event model references (bubbling, capture, target vs currentTarget, stopPropagation). Supports EDP DOM modules.  
9. Example repositories (e.g., older Expo+TS templates on GitHub) – useful for starter structure if licenses clear (MIT common); verify current Expo SDK compatibility before assigning. Prefer official create-expo-app.  
10. University-style public materials / open notes on JS event loop (e.g., MIT-style readings, Turing School notes on bubbling/delegation) – pedagogical value for EDP; treat as secondary to MDN.

**Calendar-related (for planning only)**  
Prompt-provided Iloilo collegiate dates used as authoritative. Search returned various PH university calendars (UP Visayas trimestral, USC, others) and holiday lists; none exactly matched the attached description as a single public PDF in results. Treat prompt dates as primary; verify any local holidays/Dinagyang-style suspensions with institution.

**Outdated / incompatible flags**  
- Pure Android/Java/XML or old Kotlin-only materials: preserve conceptual ideas (UI planning, lifecycle thinking, permissions) but rewrite for RN/Expo + TS.  
- Pre-Expo-Router or very old Expo CLI instructions: prefer current docs.expo.dev.  
- Tutorials claiming “Expo Go is enough for production” or “await freezes the app”: incorrect—correct via primary sources.  
- Any source mixing browser `document` APIs directly into React Native without clarification.

**Unverified / not opened**  
Some search-result PDFs or older GitHub examples; mark as secondary and prefer live official HTML.

---

### B. TWO SEPARATE 23-MODULE RESEARCH OUTLINES

**Shared pedagogical pattern (both subjects):**  
Explain concept → provide complete runnable starter → students run/trace → guided modification → independent tweak → discuss result + common mistakes. 60 min core + optional 30 min extension. Coding activities preferred. Start both with explicit programming refresher (variables/constants, types, operators, conditionals, loops, functions/params/returns) then arrays/objects before heavy framework or async work. Do not assume prior React/TS/promises knowledge.

#### ADET – Application Development and Emerging Technologies (React Native + Expo + TypeScript)

**Period mapping suggestion (provisional, adjust for shortfall):** Prelim ~ Modules 1–7; Midterm 8–14; Pre-final 15–21; Final 22–23 (review/project prep only).

1. **Title:** Programming Refresher – Variables, Types, Operators, Conditionals (Prelim)  
   Prerequisites: None (or basic computer literacy).  
   Outcomes: Declare/use variables & constants; apply operators and if/else; predict simple program flow.  
   Coverage: let/const, number/string/boolean, arithmetic/comparison/logical, if/else/else-if, basic console output.  
   Guided activity: Baon calculator (fixed allowance, simple expense check).  
   Independent: Add tax or tip percentage.  
   Observable: Correct remaining balance printed.  
   Mistakes: Reassigning const, loose equality surprises.  
   60 min core + 30 min: more operators / nested conditions.  
   Sources: TypeScript Handbook basics + MDN JS fundamentals.  
   Core; optional stretch: switch.

2. **Title:** Loops, Functions, Parameters, Return Values (Prelim)  
   Prerequisites: Module 1.  
   Outcomes: Write for/while loops; define/call functions with params and returns.  
   Coverage: for, while, function declarations/expressions, scope intro, return.  
   Activity: Study-timer helper (loop countdown simulation, function for remaining minutes).  
   Independent: Add break/continue or parameter for interval.  
   Result: Correct iterated output.  
   Mistakes: Off-by-one, missing return.  
   Sources: MDN + Handbook.  
   Core.

3. **Title:** Arrays and Objects; Simple Data Modeling (Prelim)  
   Prerequisites: 1–2.  
   Outcomes: Create/manipulate arrays & objects; access properties/methods.  
   Coverage: Array methods (push, map, filter basics), object literals, nesting for canteen items.  
   Activity: Canteen order list (array of objects: name, price, qty).  
   Independent: Total price calculator.  
   Result: Printed summary.  
   Mistakes: Mutating vs copying, undefined property access.  
   Sources: MDN + Handbook Everyday Types.  
   Core.

4. **Title:** TypeScript Fundamentals for Beginners (Prelim)  
   Prerequisites: 1–3.  
   Outcomes: Annotate basic types; use interfaces/type aliases for data shapes; understand compile-time checking.  
   Coverage: Basic types, interfaces for Order/Baon, optional/strict, why types ≠ runtime validation.  
   Activity: Type the canteen order objects; fix intentional type errors.  
   Independent: Add union type for payment method.  
   Result: tsc passes; clear error messages on misuse.  
   Mistakes: Treating types as runtime guards.  
   Sources: TypeScript Handbook + Expo TypeScript guide.  
   Core.

5. **Title:** Intro to Expo + Expo Go + Project Setup (Prelim)  
   Prerequisites: 1–4.  
   Outcomes: Create Expo project with TS template; run on Expo Go; understand folder structure and limitations.  
   Coverage: create-expo-app, Expo Go vs development builds, basic App.tsx, hot reload.  
   Activity: Hello Campus app that displays student name + baon remaining.  
   Independent: Change colors/text.  
   Result: Runs on phone via Expo Go.  
   Mistakes: Expecting full native modules in Expo Go.  
   Sources: Expo docs (get-started, TypeScript, development-builds FAQ).  
   Core.

6. **Title:** React Components, JSX, Props (Prelim)  
   Prerequisites: 5.  
   Outcomes: Create functional components; pass and consume props; nest components.  
   Coverage: Function components, JSX, props (typed), composition.  
   Activity: Reusable CanteenItem component receiving name/price.  
   Independent: Add quantity prop + display.  
   Result: Multiple items render correctly.  
   Mistakes: Mutating props, forgetting key later.  
   Sources: React Native docs (props, intro-react).  
   Core.

7. **Title:** State and Basic Events (Prelim)  
   Prerequisites: 6.  
   Outcomes: Use useState; handle press events; update UI from state.  
   Coverage: useState, onPress/Pressable, controlled simple values.  
   Activity: Baon tracker – add/subtract expense buttons.  
   Independent: Reset button + validation (no negative).  
   Result: Live balance updates.  
   Mistakes: Direct state mutation, missing setter.  
   Sources: RN State + Pressable docs.  
   Core. (Summative practical possible here.)

8. **Title:** Layouts, StyleSheet, Flexbox Basics (Midterm)  
   Prerequisites: 7.  
   Outcomes: Style with StyleSheet; apply flex layout; responsive simple screens.  
   Coverage: StyleSheet.create, flexDirection, justify/align, padding/margin.  
   Activity: Campus announcement card layout.  
   Independent: Two-column or stacked variant.  
   Result: Visually consistent screen.  
   Mistakes: Inline styles everywhere, ignoring platform differences.  
   Sources: RN Layout Props, View, StyleSheet.  
   Core.

9. **Title:** Forms, TextInput, Simple Validation (Midterm)  
   Prerequisites: 8.  
   Outcomes: Controlled inputs; basic client-side validation; feedback messages.  
   Coverage: TextInput, onChangeText, error state, disabled buttons.  
   Activity: Canteen order form (item + qty) with required checks.  
   Independent: Price range or numeric validation.  
   Result: Form rejects bad input and shows message.  
   Mistakes: Uncontrolled inputs, no user feedback.  
   Sources: RN TextInput + Expo form patterns.  
   Core.

10. **Title:** Lists, FlatList / map, Keys (Midterm)  
    Prerequisites: 9.  
    Outcomes: Render dynamic lists efficiently; use keys; basic CRUD display.  
    Coverage: FlatList vs map, keyExtractor, renderItem.  
    Activity: Task tracker list from array of tasks.  
    Independent: Toggle complete status.  
    Result: Scrollable list updates.  
    Mistakes: Missing/unstable keys, heavy work in render.  
    Sources: RN List views.  
    Core.

11. **Title:** Navigation Basics (Expo Router or React Navigation intro) (Midterm)  
    Prerequisites: 10.  
    Outcomes: Multi-screen app; pass simple params; typed routes awareness.  
    Coverage: File-based or stack navigation, Link/navigate, params.  
    Activity: Announcement list → detail screen.  
    Independent: Add a “New” screen.  
    Result: Navigation works without crash.  
    Mistakes: Hard-coded routes, untyped params.  
    Sources: Expo Router / typed-routes docs.  
    Core (keep simple).

12. **Title:** Async/Await, Promises Intro, Fetch Basics (Midterm)  
    Prerequisites: 11 + prior JS.  
    Outcomes: Write async functions; await promises; handle simple fetch + JSON.  
    Coverage: Promise states, async/await (does not freeze whole app), try/catch, fetch to public JSON.  
    Activity: Load mock campus menu from local JSON or public endpoint.  
    Independent: Loading/error states.  
    Result: Data appears after “network” delay.  
    Mistakes: Assuming await blocks UI thread entirely.  
    Sources: MDN Promises + Expo networking.  
    Core.

13. **Title:** Local Persistence (AsyncStorage or expo-secure-store / SQLite lite) (Midterm)  
    Prerequisites: 12.  
    Outcomes: Save/load simple data offline; handle first-run.  
    Coverage: Key-value store, JSON serialize, offline-first thinking.  
    Activity: Persist baon history or task list.  
    Independent: Clear-all + reload.  
    Result: Data survives app restart (Expo Go).  
    Mistakes: Storing secrets, no error handling.  
    Sources: Expo SDK storage packages.  
    Core.

14. **Title:** Debugging, Console, Error Boundaries Basics, Maintainable Structure (Midterm)  
    Prerequisites: 13.  
    Outcomes: Use console/debugger; organize folders; basic testing mindset.  
    Coverage: Expo debugging tools, component structure, simple unit checks.  
    Activity: Fix seeded bugs in a small canteen app.  
    Independent: Add a log for every state change.  
    Result: Cleaner console + working app.  
    Sources: Expo + RN debugging guides.  
    Core. (Summative possible.)

15. **Title:** Device Features & Permissions (Camera / Location / Sensors – Expo modules) (Pre-final)  
    Prerequisites: 14.  
    Outcomes: Request permissions; use one Expo device API safely; handle denial.  
    Coverage: expo-camera or sensors/location (choose one simple), permission flow, Expo Go limits.  
    Activity: Campus “photo of baon” or simple step counter simulation.  
    Independent: Graceful fallback UI.  
    Result: Feature works or shows clear “permission denied”.  
    Mistakes: Assuming always granted; using APIs needing dev builds without warning.  
    Sources: Expo SDK + permissions docs.  
    Core (label simulations).

16. **Title:** Security, Privacy, Mock Auth Concepts (Pre-final)  
    Prerequisites: 15.  
    Outcomes: Distinguish mock login from real auth; never embed secrets; basic privacy practices.  
    Coverage: Client vs server secrets, mock token flow, privacy labels.  
    Activity: Mock login screen that “protects” a task list (local only).  
    Independent: Logout + clear storage.  
    Result: Demo only; clearly labeled mock.  
    Mistakes: Hard-coding API keys.  
    Sources: Expo security notes + general best practice.  
    Core.

17. **Title:** CRUD with Local State + Persistence + Lists (Pre-final)  
    Prerequisites: 16.  
    Outcomes: Full create/read/update/delete cycle in one app.  
    Coverage: State + storage + FlatList + forms together.  
    Activity: Complete canteen order manager (add/edit/delete/persist).  
    Independent: Search/filter.  
    Result: Data persists and UI stays consistent.  
    Mistakes: Race conditions on save, stale UI.  
    Sources: Prior modules + Expo storage.  
    Core.

18. **Title:** Accessibility & Polish (Pre-final)  
    Prerequisites: 17.  
    Outcomes: Add basic a11y labels; improve contrast/feedback.  
    Coverage: accessibilityLabel, roles, simple focus.  
    Activity: Make previous canteen form more accessible.  
    Independent: Screen-reader test notes.  
    Result: Labels present; no obvious blockers.  
    Sources: RN Accessibility.  
    Core / optional depth.

19. **Title:** Emerging Tech Experiment – Connected Data or Simple AI-Assisted Feature (Pre-final)  
    Prerequisites: 18.  
    Outcomes: Integrate one safe experiment (e.g., public API data or rule-based “suggestion” clearly labeled non-AI).  
    Coverage: Fetch + display; or simple rule engine; label simulations.  
    Activity: “Suggested baon items” from rules or public menu API.  
    Independent: Toggle feature off.  
    Result: Feature works; clearly not a trained model if rule-based.  
    Mistakes: Claiming real AI without model; leaking keys.  
    Sources: Expo + MDN fetch.  
    Optional/stretch if schedule tight.

20. **Title:** Expo Go Limits, Development Builds Overview, Delivery Concepts (Pre-final)  
    Prerequisites: 19.  
    Outcomes: Explain why/when to leave Expo Go; high-level EAS or local build idea; store vs internal.  
    Coverage: FAQ differences, config plugins intro, no full production build required in class.  
    Activity: Document limitations of current project + one change that would need a dev build.  
    Independent: Research one native module.  
    Result: Written comparison.  
    Sources: Expo development-builds FAQ/intro.  
    Core.

21. **Title:** Integration Review & Mini Capstone Checkpoint (Pre-final)  
    Prerequisites: 1–20.  
    Outcomes: Combine prior skills into a coherent small app; identify gaps.  
    Coverage: Full flow review.  
    Activity: Expand task tracker or canteen into a 3–4 screen personal project seed.  
    Independent: Add one new feature from earlier list.  
    Result: Runnable multi-feature app.  
    Sources: All prior.  
    Core. (Summative practical.)

22. **Title:** Final Project Preparation & Review (Final)  
    Prerequisites: All.  
    Outcomes: Clarify individual project requirements; review common pitfalls; plan timeline.  
    Coverage: Rubric walkthrough, debugging checklist, Expo Go vs build reality.  
    Activity: Project proposal + architecture sketch + risk list.  
    Independent: Start implementation.  
    Result: Approved plan.  
    Sources: Course rubric + Expo.  
    Core (no new advanced tech).

23. **Title:** Project Work Support, Troubleshooting, Exam Prep (Final)  
    Prerequisites: 22.  
    Outcomes: Resolve blockers; prepare for practical exam; finalize individual deliverable.  
    Coverage: Office-style troubleshooting, code review of own work, final polish.  
    Activity: Individual build + demo prep.  
    Independent: Complete and submit.  
    Result: Working individual project ready for assessment.  
    Sources: Prior + debugging.  
    Core.

#### EDP – Event-driven Programming (plain JS/TS, browser APIs + Node.js)

**Period mapping:** Same provisional 7/7/7/2 split; same capacity warning.

1. **Title:** Programming Refresher – Variables, Types, Operators, Conditionals (Prelim)  
   (Nearly identical to ADET 1; use browser console or simple HTML+JS.)  
   Activity: Baon calculator in browser console or script tag.  
   Sources: MDN JS Guide.  
   Core.

2. **Title:** Loops, Functions, Parameters, Returns (Prelim)  
   Same as ADET 2; browser or Node.  
   Activity: Study timer simulation with setTimeout intro (still sync-first).  
   Core.

3. **Title:** Arrays, Objects, Higher-order Basics (Prelim)  
   Same spirit as ADET 3.  
   Activity: Canteen order array processing.  
   Core.

4. **Title:** TypeScript Fundamentals (after JS) (Prelim)  
   Same as ADET 4; focus on event-handler typing later.  
   Core.

5. **Title:** Events, Handlers, Callbacks, Scope & Closures Intro (Prelim)  
   Prerequisites: 1–4.  
   Outcomes: Attach simple listeners; understand callback + closure for state.  
   Coverage: addEventListener, this/arrow, closure over counters.  
   Activity: Click counter on a campus button.  
   Independent: Multiple independent counters.  
   Result: Counts update correctly without global pollution.  
   Mistakes: Losing this, accidental globals.  
   Sources: MDN events.  
   Core.

6. **Title:** DOM Events, Forms, Propagation Basics (Prelim)  
   Prerequisites: 5.  
   Outcomes: Handle form submit; preventDefault; observe target vs currentTarget.  
   Coverage: Form events, bubbling intro.  
   Activity: Canteen order form that logs without page reload.  
   Independent: Disable submit until valid.  
   Result: No full reload; data captured.  
   Mistakes: Forgetting preventDefault.  
   Sources: MDN forms + events.  
   Core.

7. **Title:** Event Propagation, Capture, Delegation (Prelim)  
   Prerequisites: 6.  
   Outcomes: Explain capture/target/bubble; implement delegation for dynamic lists.  
   Coverage: Phases, stopPropagation, event.target matching.  
   Activity: Dynamic task list – one listener on parent handles all delete buttons.  
   Independent: Add “edit” via same delegation.  
   Result: Works for newly added items.  
   Mistakes: Attaching to every child, stopping propagation incorrectly.  
   Sources: MDN bubbling/delegation + DOM Standard concepts.  
   Core. (Summative possible.)

8. **Title:** Event Loop, Tasks, Microtasks, Timers (Midterm)  
   Prerequisites: 7.  
   Outcomes: Predict order of sync, setTimeout, Promise.then / queueMicrotask.  
   Coverage: Call stack, task queue, microtask queue; why Promise before setTimeout(0).  
   Activity: Console-order prediction lab + visual timer.  
   Independent: Nested microtasks.  
   Result: Correct predicted vs actual log order.  
   Mistakes: Thinking setTimeout(0) is immediate or faster than microtasks.  
   Sources: MDN Execution model + Using promises.  
   Core.

9. **Title:** Promises Deep Dive & Error Handling (Midterm)  
   Prerequisites: 8.  
   Outcomes: Create/chain promises; handle rejection; convert callback to promise.  
   Coverage: new Promise, then/catch/finally, Promise.resolve/reject.  
   Activity: Simulated canteen API that sometimes fails.  
   Independent: Retry once.  
   Result: Clean success/error paths.  
   Mistakes: Unhandled rejections, nesting hell.  
   Sources: MDN Promise.  
   Core.

10. **Title:** Async/Await, Sequential vs Concurrent (Midterm)  
    Prerequisites: 9.  
    Outcomes: Rewrite promise chains with async/await; run independent work concurrently with Promise.all.  
    Coverage: await pauses only the async function; not the whole app.  
    Activity: Load two independent mock data sources (menu + announcements).  
    Independent: Compare sequential vs parallel timing.  
    Result: Correct data + observed time difference.  
    Sources: MDN + event-loop notes.  
    Core.

11. **Title:** Fetch, Validation, Cancellation, Stale Responses (Midterm)  
    Prerequisites: 10.  
    Outcomes: Use fetch + AbortController; ignore stale responses; validate JSON shape.  
    Coverage: AbortSignal, race conditions on fast typing/search.  
    Activity: Searchable campus announcement list with cancel on new keystroke.  
    Independent: Add timeout.  
    Result: No stale data overwrites newer results.  
    Mistakes: No abort, trusting all JSON.  
    Sources: MDN Fetch + AbortController.  
    Core.

12. **Title:** Debouncing & Throttling (Midterm)  
    Prerequisites: 11.  
    Outcomes: Implement or use simple debounce/throttle for high-frequency events.  
    Coverage: Input events, scroll/resize patterns.  
    Activity: Live baon search that only fires after pause.  
    Independent: Throttle a resize logger.  
    Result: Far fewer network/console calls.  
    Mistakes: Wrong delay, missing cleanup.  
    Sources: MDN + common patterns.  
    Core.

13. **Title:** Custom Events & Simple Pub/Sub (Midterm)  
    Prerequisites: 12.  
    Outcomes: Create/dispatch CustomEvent; build lightweight pub/sub.  
    Coverage: CustomEvent, dispatchEvent, listener management.  
    Activity: Campus “announcement bus” – publisher and multiple subscribers.  
    Independent: Once-only listener.  
    Result: Decoupled modules react to events.  
    Mistakes: Memory leaks (not removing listeners).  
    Sources: MDN CustomEvent.  
    Core.

14. **Title:** Node.js EventEmitter (Midterm)  
    Prerequisites: 13.  
    Outcomes: Use EventEmitter in Node; contrast with browser; basic cleanup.  
    Coverage: on/emit/once/removeListener, error events.  
    Activity: Simple Node “canteen queue” emitter that logs order status changes.  
    Independent: Max listeners warning demo.  
    Result: Synchronous listener calls observed; cleanup works.  
    Sources: Node.js events docs.  
    Core. (Summative possible.)

15. **Title:** Persistence, Cleanup, Workers Intro (Pre-final)  
    Prerequisites: 14.  
    Outcomes: Save event-driven state; remove listeners; optional Worker for heavy work.  
    Coverage: localStorage + events, removeEventListener, Worker basics (message events).  
    Activity: Persistent task list that survives reload + cleanup on unmount simulation.  
    Independent: Offload a calculation to Worker.  
    Result: No leaks; data persists.  
    Sources: MDN Storage + Workers.  
    Core.

16. **Title:** Testing Event-Driven Behavior (Pre-final)  
    Prerequisites: 15.  
    Outcomes: Write simple tests for handlers and async flows (console or lightweight runner).  
    Coverage: Spy on callbacks, fake timers, assert order.  
    Activity: Test the debounce or order emitter.  
    Independent: Add failure case.  
    Result: Passing tests for expected sequence.  
    Sources: General testing practices + MDN.  
    Core / optional depth.

17. **Title:** Introductory Real-Time Communication Concepts (WebSocket or SSE simulation) (Pre-final)  
    Prerequisites: 16.  
    Outcomes: Understand event-driven real-time pattern; implement simple mock or public echo.  
    Coverage: WebSocket events or EventSource; reconnect thinking.  
    Activity: Mock “campus live announcements” via simple WebSocket echo or polling fallback.  
    Independent: Handle disconnect UI.  
    Result: Messages appear as events.  
    Mistakes: Blocking UI on network.  
    Sources: MDN WebSocket / EventSource.  
    Optional if schedule tight; label as intro.

18. **Title:** Queues, Sequential Processing, Backpressure Awareness (Pre-final)  
    Prerequisites: 17.  
    Outcomes: Process events in order without dropping critical work.  
    Coverage: Simple in-memory queue + EventEmitter or async iterator.  
    Activity: Order processing queue that handles bursts.  
    Independent: Drop or delay low-priority.  
    Result: Ordered completion.  
    Sources: Node streams/events concepts + MDN.  
    Core / stretch.

19. **Title:** Integration – Browser + Node Patterns Side-by-Side (Pre-final)  
    Prerequisites: 18.  
    Outcomes: Reuse event patterns across environments; document differences.  
    Coverage: Shared mental model, environment-specific APIs.  
    Activity: Same “task completed” event in browser DOM and Node EventEmitter.  
    Independent: Bridge via simple message.  
    Result: Consistent behavior description.  
    Sources: MDN + Node.  
    Core.

20. **Title:** Error Boundaries in Event Systems & Resilience (Pre-final)  
    Prerequisites: 19.  
    Outcomes: Isolate failures; keep system running.  
    Coverage: try/catch in listeners, unhandledrejection, process-level in Node.  
    Activity: Inject error in one handler; ensure others still fire.  
    Independent: Logging strategy.  
    Result: Partial failure does not crash whole demo.  
    Sources: MDN + Node.  
    Core.

21. **Title:** Capstone Checkpoint – Event-Driven Mini System (Pre-final)  
    Prerequisites: 1–20.  
    Outcomes: Design and implement a small multi-component event-driven app.  
    Coverage: All prior patterns.  
    Activity: Campus study-group notifier or canteen order status board (browser + optional Node).  
    Independent: Add one advanced pattern (debounce or custom event).  
    Result: Runnable system with clear event flow.  
    Sources: All.  
    Core. (Summative.)

22. **Title:** Final Project Preparation & Review (Final)  
    Same spirit as ADET 22: individual project plan, rubric, common event-driven pitfalls (leaks, races, assuming every handler is async).  
    Core.

23. **Title:** Project Work, Troubleshooting, Practical Exam Prep (Final)  
    Same as ADET 23.  
    Core.

---

### C. ASSESSMENT AND CALENDAR PLAN

**Formative (every module):** In-class coding activity + independent modification + observation of result. Low-stakes; focus on “does it run and match expected?” and discussion of mistakes.

**Summative exams:** One before each periodical (Prelim/Midterm/Pre-final). Practical-heavy: given a starter, implement or fix event/component behavior, explain order of execution, or complete a small CRUD/event flow. Written short questions on concepts (event loop order, props vs state, Expo Go limits, etc.).

**Periodical exams:** Institution-scheduled (Jan 13–15, Feb 8–10, Mar 15–17, Apr 14–16). Align coverage to modules taught by then.

**Practical assessment coverage suggestions**  
- Prelim: Refresher + basic components/events + simple state or DOM handlers.  
- Midterm: Lists/forms/navigation or event loop + promises + fetch + debouncing.  
- Pre-final: Full small app (CRUD + persistence or event-driven system) + device/real-time intro.  
- Final: Individual practical project defense + short practical exam on troubleshooting.

**Solo final-project requirements (achievable, individual)**  
- ADET: Multi-screen Expo app (Expo Go sufficient for core) with local persistence, forms/validation, list+CRUD, at least one device feature or mock external data, clear mock-auth if present, README with setup and limitations. No private keys.  
- EDP: Browser (and optional Node) event-driven system with custom events or EventEmitter, async flows with cancellation/debounce, persistence/cleanup, and a short design note on event flow.  
Rubric dimensions (example weights): Correctness & completeness (30%), Event/component design & clarity (25%), Error handling & resilience (15%), Code organization & TypeScript usage (15%), Documentation & demo (15%). Deduct for secrets in client, unlabeled simulations, or Expo Go treated as production.

**Scheduling uncertainty:** Exact meeting days unknown. College Week (Feb 15–19) – do not assume cancellation unless stated. Year-end break and holidays reduce available slots. 21 content modules before Finals is ambitious; prioritize core over stretch (emerging AI experiments, deep Workers, full real-time). Instructor must approve any reduction or reordering. Finals meetings: project support + summative + practical exam only—no new advanced topics.

---

### D. TECHNICAL ACCURACY NOTES

- Event-driven ≠ every handler is asynchronous. Many listeners (DOM click, EventEmitter.emit) run synchronously.  
- `await` pauses only the current async function; the event loop continues (UI stays responsive; other tasks/microtasks can run).  
- TypeScript is compile-time; it does not replace runtime validation of user input, API JSON, or permissions.  
- Browser APIs (document, window, DOM events) and Node.js APIs (EventEmitter, process, fs) are not interchangeable; teach the distinction explicitly.  
- Expo Go is a development client/playground, not a production deployment vehicle; many native modules and configurations require development builds.  
- Device features often need explicit permissions and may be limited or unavailable in Expo Go.  
- Mock login / local token is not real authentication; never ship private service credentials in client code.  
- Rule-based suggestions or simple heuristics are not an AI model; label them clearly.  
- Simulations and fallback/mock data must be labeled so students do not confuse them with live production systems.  
- Always prefer official docs for current behavior (Expo SDK version alignment, RN New Architecture notes, etc.).

---

### E. HANDOFF SUMMARY

**Recommended sources to read first**  
1. Expo TypeScript + development-builds FAQ/intro  
2. React Native Props / State / Core Components  
3. TypeScript Handbook (Basics → Everyday Types → Functions)  
4. MDN: Using promises, Execution model, DOM event bubbling/delegation  
5. Node.js EventEmitter page  

**Proposed folder structure**  
```
ADET/
  00-source-register.md
  modules/
    01-programming-refresher-variables...
    ...
    23-project-support...
  assessments/
  projects/
EDP/
  (parallel structure)
shared/
  calendar-notes.md
  technical-accuracy.md
  activity-templates/
```

**Decisions supported by evidence**  
- Start both subjects with explicit JS refresher before TS/frameworks/async.  
- Expo Go first, then explain limits and development builds.  
- Event loop + microtasks before heavy async/await and fetch cancellation.  
- Individual final projects; Finals limited to 2 modules of prep/support.  
- Prefer coding labs over quizzes; use campus-relatable scenarios.  

**Questions still unresolved**  
- Exact institution calendar PDF details and whether College Week cancels classes.  
- Precise meeting weekdays and any forced make-up policy.  
- Whether the college already has Expo/Node lab machines or students use personal devices exclusively.  
- Preferred navigation library depth (Expo Router vs simpler).  
- Exact weight of Tagalog support vs pure English materials.

**Sources / claims needing verification**  
- Any specific third-party example repos for current Expo SDK.  
- Local Iloilo holiday suspensions beyond prompt dates.  
- Whether institution provides free public JSON endpoints or prefers fully local mocks.

**Concise checklist for the AI that will write the Markdown lessons**  
- [ ] One module = one teaching day; do not combine.  
- [ ] Begin every early module with explicit refresher elements before relying on them.  
- [ ] Follow explain → complete starter code → run → trace → modify → explain.  
- [ ] Include 2–4 measurable outcomes, guided activity, independent modification, expected result, common mistakes, 60+30 timing, core vs stretch.  
- [ ] Cite only verified sources; prefer official docs.  
- [ ] Label all mocks/simulations; never put secrets in client code.  
- [ ] Address technical accuracy notes explicitly where relevant (await, Expo Go, TS vs runtime, browser vs Node).  
- [ ] Keep activities free of mandatory paid services.  
- [ ] Flag any schedule pressure and keep Finals modules as review/project only.  
- [ ] Use natural English with space for Tagalog clarification notes where helpful for Philippine students.  
- [ ] Preserve useful Android/Java conceptual ideas only as high-level parallels, not as code to copy.

This research inventory is ready for module authoring. Adjust depth or drop stretch topics only with instructor approval if the calendar proves too short.