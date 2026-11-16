> **Updated pacing decision:** 17 modules per subject, split 4 Prelim / 5 Midterm / 6 Pre-final / 2 Finals. This document retains the earlier research inventory; see [current pacing](AGREED_PACING.md).

# Consolidated research dossier: ADET and EDP

Research updated **2 November 2026**. Current phase: research and planning, before writing the full teaching modules.

[ADET research plan](../ADET/RESEARCH_PLAN.md) | [EDP research plan](../EDP/RESEARCH_PLAN.md) | [Calendar calculations](CALENDAR_AND_CAPACITY.md) | [Source register](SOURCE_REGISTER.md) | [External-report review](external_research/REVIEW_NOTES.md)

## Confirmed classroom constraints

- Two meetings **per subject per week**, confirmed again after the phrase “two classes per day” was clarified.
- A meeting lasts approximately 60–90 minutes; Saturdays are excluded.
- One numbered module per teaching day.
- Prelim, Midterm, Pre-final, and Final periods, each with a summative before its periodical exam.
- Exactly two Finals modules/presentations, both devoted to review and project preparation.
- Individual final practical projects.
- Explicit language refresher at the beginning of both courses.
- Research first; full lessons and executable starter programs are a subsequent phase.

## Is 23 modules per subject feasible?

**It does not fit the ordinary weekday scenarios currently calculated while keeping all the above constraints.** The requested 23-topic inventory remains useful as research, but cannot yet be presented as a deliverable class timetable.

Twenty-three modules minus two Finals modules leaves **21 teaching days before Finals**. Add three earlier summative meetings: **24 ordinary meetings are needed before the Pre-final exam**, with periodical exams scheduled separately in their official windows.

Using the supplied school calendar and all ten possible Monday–Friday weekday pairs:

| College Week assumption | Module/studio days available before Finals, after reserving summatives | Required | Shortfall |
| --- | ---: | ---: | ---: |
| Reserve College Week for activities | 15–17 | 21 | 4–6 |
| Ordinary subject meetings continue during College Week | 17–19 | 21 | 2–4 |

With two Finals modules added, these scenarios support **17–19** or **19–21** numbered modules respectively. These are capacity bounds, not a final recommendation or assigned dates. They rely on the documented year-end-break assumption and on reserving 17 December for the year-end activity. Later school announcements may change the count.

The semester runs **1 December 2026–16 April 2027**. Periodical windows are 13–15 January, 8–10 February, 15–17 March, and 14–16 April. The uneven windows matter: a roughly monthly period does not guarantee four uninterrupted teaching weeks. See the complete [weekday comparison and exclusions](CALENDAR_AND_CAPACITY.md).

Possible resolutions are school-approved additional teaching dates, explicitly recognized asynchronous instructional dates, or fewer numbered core modules with extra topics retained as references. Do not silently combine modules, use Saturdays, remove summatives, or shift new advanced content into Finals. No scope change is approved merely by documenting these options.

## Language foundations and teaching sequence

Both subjects should establish the following progression before expecting framework or async fluency:

| Step | Teach and demonstrate | Beginner misconception to address | Activity candidate |
| --- | --- | --- | --- |
| Variables and types | let/const, numbers, strings, booleans, arithmetic, readable output | Text that looks numeric is not automatically numeric; const does not make an object's contents immutable | Baon balance |
| Conditionals | Comparisons, boolean expressions, if/else, boundary checks | Assignment versus comparison; overlapping or missing branches | Fare eligibility |
| Loops | Counter, continuation condition, update, trace table | Off-by-one errors; missing termination | Five-day study plan |
| Functions | Declaration, call, parameters, arguments, return, local scope | Printing a result is different from returning it | Reusable order calculator |
| Arrays and objects | Collections, records, IDs, iteration, basic selection | Position or title is not always stable identity | Canteen menu |
| TypeScript bridge | Annotations, object types, inference, unions, unknown and narrowing | Static type checks do not validate incoming runtime data | Typed order record |

Technical foundations: [MDN grammar and types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types), [control flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling), [loops](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration), [functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions), and [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html). These sources were inspected; the proposed teaching order is an instructional decision.

Start with small console programs, then connect familiar logic to mobile components or browser events. ADET and EDP can use different examples while teaching the same foundations. Do not require one subject's attendance as a prerequisite for understanding the other.

## ADET research decisions

React Native, Expo, and TypeScript remain the selected stack. Choose one explicit project template and document the actual entry file. The default Router structure and a blank App.tsx structure require different instructions. Avoid swapping between them without a migration explanation. [Expo project setup](https://docs.expo.dev/get-started/create-a-project/), [Expo TypeScript](https://docs.expo.dev/guides/typescript/).

Teach props and local state before effects, async data, or persistence. Use a counter before a timer so the first state lesson does not depend on interval cleanup. Introduce forms and lists before requiring a full task tracker. Route parameters should identify data and have a missing-record path.

Persistence and network access each need their own small example. A persistent checklist teaches save/load and invalid-data recovery. An announcement reader teaches status checks, JSON validation, and loading/error states. A local fixture keeps the lesson usable when internet fails. [AsyncStorage reference](https://docs.expo.dev/versions/latest/sdk/async-storage/), [MDN Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).

Private credentials must stay outside the distributed client. Expo's public environment variables are embedded in client code and are unsuitable for secrets. A .env file alone does not create a secure server boundary. [Expo environment variables](https://docs.expo.dev/guides/environment-variables/).

Keep a device integration small: image selection with a cancellation path or foreground location with permission denial. Do not require camera, maps, sensors, audio, and background tasks all in one core lesson. Expo Go compatibility is feature-specific; verify against the selected SDK and test on the intended device. Delivery concepts should distinguish Expo Go previews, development builds, and distributable builds. [Development builds](https://docs.expo.dev/develop/development-builds/introduction/).

For emerging technologies, grade an experiment and its limitations. Simulated connected-device readings can demonstrate validation and stale data. A rule-based suggestion engine can be compared with sample model responses, but must not be called an AI model. Live AI, custom native code, and real hardware remain optional until their setup and costs are researched separately.

## EDP research decisions

After the language bridge, teach registration and callbacks, then event objects and propagation. Provide the HTML shell so students spend their time on behavior. Use native buttons and form controls so keyboard operation remains straightforward.

Separate the browser runtime model from Node. Promise continuations, timers, direct calls, and event dispatch do not share one simple universal FIFO rule. The browser execution model is the right foundation for browser ordering exercises; Node-specific scheduling belongs with Node examples. [MDN execution model](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model).

Teach a deterministic promise success/failure example before async/await, then independent concurrent operations. Cancellation and stale-result protection are distinct requirements: stopping supported work and deciding whether a result is still relevant. A timeout that merely rejects a wrapper does not necessarily stop the underlying operation.

For Node EventEmitter, demonstrate synchronous listener invocation, once/off, and explicit error handling. Do not assume that emit awaits async listeners or that a thrown exception automatically permits every remaining listener to complete. Make the chosen recovery policy visible in the program. [Node Events](https://nodejs.org/api/events.html).

Testing should verify transitions, handler results, and failure paths. Use a known sequence or injected scheduling where appropriate instead of asserting fragile real-world delays. The built-in Node test runner is a possible low-dependency teaching tool; it does not itself prove mobile UI behavior. [Node test runner](https://nodejs.org/api/test.html).

Workers and live SSE/WebSocket servers are extensions to the core event/state/async sequence. A local event simulation must be labeled as such. A short topic list is not sufficient evidence that these integrations fit one beginner class meeting.

## Assessment and workload design

Use a repeatable 60-minute core: 5 minutes recap/prediction, 10 explanation, 20 guided coding, 10 tracing/debugging, 10 modification, and 5 minutes demonstration. Add a 30-minute extension only when the meeting allows it. Setup installation and large downloads should be arranged ahead of the relevant class where possible.

Each future lesson needs measurable outcomes, a complete runnable starter, expected output, a normal and edge/failure test, and one independent modification. Natural Taglish explanations should clarify the technical behavior rather than replace precise terminology.

Summatives are assessments of taught skills and occupy separate meetings. Periodical exams follow the institutional calendar. M22 and M23 are preparation modules, not the final practical exam itself. Begin project scope and data/event planning before Finals so the last period can focus on solo implementation, troubleshooting, and demonstration.

ADET project evidence should emphasize a coherent user flow, validated input, state/data handling, and failure recovery. EDP evidence should emphasize event registration, transitions, async behavior, cleanup, and recovery. Use a manageable subset of learned techniques; avoid requiring every feature in the syllabus.

## Evidence quality and remaining research

Three supplied Grok reports have been preserved in [external research](external_research/REVIEW_NOTES.md). Their claims of inspection, publication dates, licenses, SDK numbers, and CHED compliance are not automatically accepted. Direct official technical pages are stronger sources for implementation. The provided institutional calendar has already been inspected locally; it does not need to be rediscovered through public search.

A local file named `lec16.pdf` is also present. Initial inspection identifies a 36-page slide deck titled **Event-Driven Programming**, CSE 8B, Spring 2022; metadata lists Ben Ochoa. Only its opening pages and metadata were checked in this pass. Its download origin and reuse license remain unknown, and its technical contents have not yet been reviewed as a source. It is not currently used to support the lesson recommendations.

Remaining work: inspect any candidate downloadable material fully before citing relevant pages; verify its origin/license; resolve actual lab tooling and device access; select tested package versions; and finalize the timetable after weekday assignments. No formal CHED compliance mapping or live AI integration is claimed.

## Status of older plans

The new subject research inventories linked above supersede earlier numbered outlines for discussion. Older files remain as planning history. Their three-hour modules and 18-week/90-hour assumptions are obsolete for this instructor's stated schedule. The research inventory has 23 topics per subject, but the calendar question is still unresolved. Full teaching modules and their code have not been authored or validated.
