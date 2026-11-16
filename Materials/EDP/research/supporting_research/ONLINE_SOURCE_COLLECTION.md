# Online source collection for ADET and EDP

Collected **2 November 2026**. Scope: online evidence and teaching references only. No new teaching modules authored in this pass. Current target remains [17 modules per subject](AGREED_PACING.md).

## How to read this register

**Inspected** means the page or PDF text was retrieved, not that every example was executed or every linked file reviewed. **Discovery only** means the landing page lists material whose contents could not be retrieved. Public access does not establish permission to reproduce or redistribute a work. Unless explicitly verified below, reuse licenses and precise last-update dates remain unconfirmed.

University slides support teaching explanations and examples. Official language/runtime/framework documentation remains the implementation reference for contemporary APIs. Publication years below describe the course offering or source label, not a claim that the material was updated this year.

## 1. Programming refresher: direct language references

| Source | Organization / format | Relevant coverage | Status and intended use |
| --- | --- | --- | --- |
| [Grammar and types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types) | MDN / HTML | Declarations, scope, primitive values, type conversion | Inspected in the preceding research pass; basis for variables and value tracing |
| [Control flow and error handling](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling) | MDN / HTML | Conditional branches and exceptions | Previously inspected; select conditionals first, defer exception depth |
| [Loops and iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration) | MDN / HTML | Loop forms and termination | Previously inspected; basis for short trace-table exercises |
| [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions) | MDN / HTML | Function definitions, calls, parameters, scope | Previously inspected; distinguish return values from printing |
| [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/) | TypeScript team / HTML | Language-learning entry point | Landing page found in this pass; specific everyday-types/narrowing pages were inspected earlier |

Use small console examples before browser or mobile plumbing. This is a proposed teaching choice rather than a requirement imposed by MDN. Do not give students a massive API-reference reading assignment in place of a refresher.

## 2. ADET: contemporary mobile development

### A01 — React Fundamentals

- Organization: React Native project. Format: HTML.
- Direct source: [React Fundamentals](https://reactnative.dev/docs/intro-react).
- Status: inspected this pass, including components, JSX, props, and state sections.
- Teaching use: explain how plain functions connect to components, how data enters through props, and how interaction changes state. Offers JavaScript and TypeScript views.
- Limits: this is a foundation reference, not the full semester. Keep React Native components distinct from browser HTML elements.

### A02 — Official Expo tutorial

- Organization: Expo. Format: HTML with linked source repository.
- Landing: [Using React Native and Expo](https://docs.expo.dev/tutorial/introduction/).
- Status: introduction and chapter list inspected. The linked complete repository was listed but not inspected or downloaded in this pass.
- Coverage: TypeScript-enabled project, navigation, layouts, image selection, modal/list UI, gestures, saving an image, and platform differences.
- Teaching use: select a small visual demonstration to make the opening interesting; revisit individual chapters after the language and component foundations.
- Limits: its self-paced time estimate is not a reliable classroom estimate for students refreshing programming. Do not assign the whole project as a single 60-minute introduction. Match commands and dependencies to the classroom version later.

### A03 — React learning entry point

- Organization: React project. Format: HTML.
- Source: [Quick Start](https://react.dev/learn).
- Status: found again this pass; inspected in the earlier collection.
- Teaching use: parent/child components, data-driven rendering, and interaction concepts.
- Limits: browser elements in React examples must be adapted to React Native rather than pasted directly into mobile UI.

The earlier [source register](SOURCE_REGISTER.md) supplies the inspected references for Expo setup, navigation, accessibility, persistence, device APIs, security, and deployment. This file records additions and access findings rather than pretending all those pages were newly reviewed today.

## 3. Downloadable university teaching references

### U01 — University of Washington: HTML and TypeScript

- Course: CSE 331, Software Design & Implementation, Summer 2023.
- Direct PDF: [lec16-html-js.pdf](https://courses.cs.washington.edu/courses/cse331/23su/lectures/lec16-html-js.pdf).
- Format: PDF, 48 pages. Text retrieved and inspected; screenshot retrieval failed, so visual layout has not been verified.
- Verified relevant printed pages: **6** introduces callback categories; **9** lists event sources; **10** discusses observers; **11–15** develops an event-loop illustration.
- Teaching use: distinguish code supplied as a callback from ordinary input data, then show listener registration and event processing.
- Limits: mixes Java material, conceptual pseudocode, HTML, and TypeScript. Its simplified loop is not a complete browser scheduling specification. Use MDN/Node for task and microtask details; do not carry its equivalence between asynchronous callbacks and event-driven programming into a universal definition.
- Access: retrieved without login. Author and redistribution license not established in this pass; attribute the course and institution.

### U02 — UC San Diego: Event-Driven Programming

- Instructor/course: Ben Ochoa, CSE 8B, Spring 2022.
- Landing: [official course page](https://cseweb.ucsd.edu/classes/sp22/cse8B-a/).
- Direct PDF: [Lecture 16](https://cseweb.ucsd.edu/classes/sp22/cse8B-a/lec16.pdf).
- Format: PDF, 36 pages. PDF text inspected this pass. The course page explicitly links Lecture 16 as Event-Driven Programming.
- Verified relevant printed pages: **3–7** introduce events, sources, and objects; **12–18** show handler registration and a button example; **29–31** cover Java lambda-based handlers.
- Teaching use: a conceptual bridge from the original Java-oriented material: identify source, event, registration, and response, then write a fresh JavaScript/TypeScript example.
- Limits: Java/JavaFX syntax and interfaces are not the EDP implementation target. Do not require handler classes merely because this source does. No redistribution license was verified.
- Local relationship: the title, page count, course identifier, and term match the existing [lec16.pdf](lec16.pdf). This establishes a plausible official source match, not a cryptographic identity check.

### U03 — University of Maryland: Spring 2026 JavaScript course resources

- Course: CMSC335, Web Application Development with JavaScript.
- Landing: [official schedule and resource index](https://www.cs.umd.edu/class/spring2026/cmsc335/schedule.shtml).
- Status: public index inspected. It lists PDFs and code ZIPs for introductory JS, events, promises, event loop, storage, and debugging.
- Useful as: an instructor's topic-discovery list and an example of pairing explanations with runnable source files.
- Important access distinction: indexed does not mean publicly retrievable. No PDF content from the following entries was used as evidence:

| Listed file | Direct target exposed by the index | Access result |
| --- | --- | --- |
| JavaScriptI.pdf | [Week03 JavaScriptI](https://www.cs.umd.edu/class/spring2026/cmsc335/prot/lectures/Week03/JavaScriptI.pdf) | HTTP 401 Unauthorized |
| Events.pdf | [Week04 Events](https://www.cs.umd.edu/class/spring2026/cmsc335/prot/lectures/Week04/Events.pdf) | Retrieval failed / cache miss; access not verified |
| EventLoop.pdf | [Week07 EventLoop](https://www.cs.umd.edu/class/spring2026/cmsc335/prot/lectures/Week07/EventLoop.pdf) | Retrieval failed / cache miss; access not verified |
| Promises.pdf | [Week07 Promises](https://www.cs.umd.edu/class/spring2026/cmsc335/prot/lectures/Week07/Promises.pdf) | Retrieval failed / cache miss; access not verified |

The code ZIP contents and their licenses were not inspected. Do not depend on these files for a student assignment or attempt to bypass access controls.

## 4. University activity reference in HTML

### U04 — Carnegie Mellon: Introduction to JavaScript lab

- Course collection: Data Vis 2024. Organization: Carnegie Mellon University.
- Source: [Lab 3: Introduction to JS](https://dig.cmu.edu/datavis-fall-2024/labs/3/).
- Format/access: public HTML, inspected. Linked slide contents were not inspected.
- Coverage: primitive values, arrays/objects, DOM manipulation, and responses to user actions. Activities include generating navigation and implementing a theme preference.
- Teaching use: study how a visible improvement motivates a programming technique. A theme switch or generated menu can be adapted into an original campus-themed EDP exercise.
- Limits: assumes prior HTML/CSS labs and a local server. Provide our own complete shell instead of inheriting its previous-lab requirements. Later Svelte/D3 course units are outside our selected stack. License not verified.

## 5. Failed, outdated, or unverified download leads

| Candidate | Result | Decision |
| --- | --- | --- |
| [Historical official TypeScript Handbook PDF](https://www.typescriptlang.org/assets/typescript-handbook.pdf) | Returned 404 | Use current HTML handbook; do not advertise this as a working download |
| [University of Toronto JavaScript/event slides](https://www.cs.toronto.edu/~mashiyat/csc309/Lectures/javascriptsept28.pdf) | Search discovered it; direct retrieval failed | Candidate only; content and page references unverified |
| [University of Virginia JS objects/events slides](https://cs4640.cs.virginia.edu/fall2023/lectures/21-JavaScript-Objects-Events.pdf) | Direct retrieval blocked by unavailable robots information | Candidate only; do not cite specific contents |

No verified DOCX source was collected in this pass. PDFs are not inherently more current or more suitable than official HTML references. Search result crawl dates are not publication dates.

## 6. Recommended reading order for the instructor

1. MDN refresher pages for the four Prelim foundations.
2. React Native React Fundamentals for the mobile mental model.
3. Expo tutorial introduction and selected relevant chapters.
4. Washington PDF pages 6 and 9–15 for callback/event illustrations.
5. UCSD PDF pages 3–7 and 12–18 for the old-to-new conceptual bridge.
6. The existing official references for promises, execution model, AbortController, EventEmitter, and testing.

The opening could show the same simple campus interaction in both courses: ADET asks how to build the useful screen; EDP asks which event causes which response. This is an original teaching suggestion, not a copied university exercise.

## 7. Collection status

Two university PDF texts are now accessible and inspected at relevant sections, alongside a public university lab and an indexed resource collection with access limitations. Links are recorded here; no new remote PDFs or ZIPs were downloaded to the workspace in this pass. The existing local UCSD-named PDF predates this collection pass.

Next source collection should target short official examples for safe input handling, async cancellation, and device-permission denial, plus clearly licensed starter repositories. Keep material aligned with the current **4 / 5 / 6 / 2** pacing proposal and defer detailed lesson authoring.
