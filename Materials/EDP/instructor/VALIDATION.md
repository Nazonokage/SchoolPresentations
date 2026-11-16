# EDP lesson-pack validation

Checked 3 November 2026. Scope: the authored EDP lessons and their supplied core examples.

## Passed checks

- 20 student modules with A–D lesson structure, runnable code, expected behavior, independent changes, troubleshooting, assessments and sources.
- 10 quizzes × 10 questions = 100 questions, with a separate instructor answer key; 10 alternating coding activities with rubrics.
- 19 console entry points executed successfully with assertions for expected output and ordering. See [console results](console-results.json).
- TypeScript 5.9.3 strict checking passed for the typed companion and typed event channels.
- Five Node tests passed: listener order/removal, awaiting before dispatch, expected error behavior, project state transitions, and rejected inputs/caller isolation.
- Headless Microsoft Edge browser checks passed on all four pages: minimal first click, order form/list, RxJS search and real local SSE. Checks covered keyboard submission, whitespace rejection, delegated actions, cleanup, reactive error recovery and disconnect behavior. No page JavaScript errors were observed. See [browser results](browser-results.json).
- Embedded lesson source blocks were checked against their runnable files, and local lesson links were checked.

## Tested environment

Node.js 24.18.1, TypeScript 5.9.3, @types/node 24.10.0, RxJS 7.8.2. The browser test reported Edge 156.0.4314.58. These are observed test versions, not claims about current release recommendations. package-lock.json records the installed dependencies. Dependency installation required network access; the classroom examples use local inputs afterward.

Official documentation was consulted alongside the existing research. The RxJS documentation website returned a JavaScript shell, so the pinned installed RxJS source and executed behavior were also inspected. Generic Node documentation may describe a newer version than the tested runtime; the supplied APIs were actually run on the version above.

## Limits and classroom checks still needed

- The lessons have not been piloted with students or timed in a live 60–90-minute class. Use the core/extension boundaries and prepared environments.
- Console timing checks assert meaningful output order, not exact millisecond deadlines. No high-load, long-duration or production reliability test is claimed.
- Browser tests cover local Edge, not every mobile/browser/device combination. Visual inspection confirmed the simple order-board page; styling is deliberately minimal so event behavior remains visible.
- Brokers, database transactions, cloud services, full OpenTelemetry instrumentation and production authentication are explained or simulated, not deployed and certified here.
- M12–M17 local models have explicit in-memory/sequential limitations. They do not prove durability, distributed exactly-once effects or security of a public service.
- The SSE sample has no durable replay, authentication or production reconnection guarantee. Stop/restart status is a classroom exploration; the automated check verifies message receipt and explicit disconnect.
- Actual summative and periodical examination papers, institutional grading weights and final calendar dates are separate instructor decisions.

The material is ready for instructor review and lesson delivery preparation. Preserve these limits when presenting the examples and rerun the relevant checks after editing code.
