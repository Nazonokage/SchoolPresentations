# EDP — Complete teaching modules

**Current finals sequence:** M19 rehearsal, [M20 defense quiz and essays](EDP_M20.md), then [M21 solo mini-capstone announcement and readiness](EDP_M21.md). Alternating assessments apply through M19. If finals has only two teaching meetings, assign M20 as individual preparation between M19 and M21. Keep summative and periodical exam time separate.

Twenty authored Markdown lessons based on the compiled contents. Read [setup](../examples/README.md) first and consult the [validation report](../instructor/VALIDATION.md) for what was actually tested. These are classroom materials, not production deployments.

| Module | Lesson | Period | Assessment |
| --- | --- | --- | --- |
| 01 | [Module 1: Foundations of Event-Driven Programming and Day-One Refresher](EDP_M01.md) | Prelim | 10-item quiz |
| 02 | [Module 2: The JavaScript Event Loop, Concurrency, and Async Primitives](EDP_M02.md) | Prelim | Coding activity |
| 03 | [Module 3: Client-Side DOM Events and Interactive Interfaces](EDP_M03.md) | Prelim | 10-item quiz |
| 04 | [Module 4: In-Process Node.js Events and Native Event Sources](EDP_M04.md) | Prelim | Coding activity |
| 05 | [Module 5: Async Patterns, Cancellation, and Race Conditions](EDP_M05.md) | Prelim | 10-item quiz |
| 06 | [Module 6: Type-Safe Event Systems in TypeScript](EDP_M06.md) | Midterm | Coding activity |
| 07 | [Module 7: Core Patterns, State Machines, and Framework Connections](EDP_M07.md) | Midterm | 10-item quiz |
| 08 | [Module 8: Reactive Programming and RxJS Streams](EDP_M08.md) | Midterm | Coding activity |
| 09 | [Module 9: Client–Server Real-Time Events and Messaging Channels](EDP_M09.md) | Midterm | 10-item quiz |
| 10 | [Module 10: Streams, Backpressure, Workers, and Background Work](EDP_M10.md) | Midterm | Coding activity |
| 11 | [Module 11: Testing and Debugging Event-Driven Programs](EDP_M11.md) | Midterm | 10-item quiz |
| 12 | [Module 12: Distributed Messaging, Brokers, and Event Streaming](EDP_M12.md) | Pre-final | Coding activity |
| 13 | [Module 13: Delivery Guarantees, Ordering, and Reliable Consumers](EDP_M13.md) | Pre-final | 10-item quiz |
| 14 | [Module 14: Reliable Publication, Outbox/Inbox, and Event Contracts](EDP_M14.md) | Pre-final | Coding activity |
| 15 | [Module 15: Event Sourcing, Replay, and Read Projections](EDP_M15.md) | Pre-final | 10-item quiz |
| 16 | [Module 16: CQRS, Sagas, and Distributed Workflow Coordination](EDP_M16.md) | Pre-final | Coding activity |
| 17 | [Module 17: Observability, Security, and Production Resilience](EDP_M17.md) | Pre-final | 10-item quiz |
| 18 | [Module 18: Integrated Solo Project Design and Architecture Checkpoint](EDP_M18.md) | Pre-final | Coding activity |
| 19 | [Module 19: Finals Review, Summative Preparation, and Mock Practical](EDP_M19.md) | Finals | 10-item quiz |
| 20 | [Module 20: Applied Knowledge and Mini-Capstone Defense Preparation](EDP_M20.md) | Finals | 20-item quiz + 2 essays |
| 21 | [Module 21: Mini-capstone announcement and solo project readiness](EDP_M21.md) | Finals | Solo mini-capstone |

Odd modules through M19 use quizzes; even modules through M18 use coding activities; M20 and M21 are described in the table above. Guided practice remains ungraded. Summative and periodical exams need their own dates and assessment papers. [Instructor guide](../instructor/TEACHING_GUIDE.md) · [Coverage map](../instructor/COVERAGE_MAP.md)

## How the modules connect

| Block | Modules | Builds on | Leads to |
| --- | --- | --- | --- |
| Foundations | M01–M03 | Basic programming | M04 (Node events), M05 (async) |
| Node events and async | M04–M05 | M01–M03 | M06 (types), M07 (patterns) |
| Types, patterns, reactive | M06–M08 | M04–M05 | M09 (network), M11 (tests) |
| Real-time, streams, testing | M09–M11 | M03–M08 | M12 (brokers) |
| Messaging and reliability | M12–M16 | M04, M07, M09, M11 | M17 (production), M18 (project) |
| Production and project | M17–M18 | M11–M16 | M19–M21 (finals) |
| Finals | M19–M21 | M18 | Final practical (separate instructions) |

Each module’s **Before class** line names the exact modules it needs, and its **Next connection** line names what follows.

## Optional extensions added in this revision

| Module | New example | What it shows | Extra setup |
| --- | --- | --- | --- |
| M09 | `ws-demo.mjs` | Two-way WebSocket messaging with validation on both sides | `npm install --save-exact ws`; Node 22 or newer |
| M14 | `m14-webhook.mjs` | Webhook signature check, stale-timestamp rejection and deduplication | None (built-in `node:crypto`) |
| M17 | `m17-resilience.mjs` | Bounded retry and a small circuit breaker | None |

Changed examples that replace earlier files: `m06.ts` (adds a union demo), `m07.mjs` (records accepted facts), `m08.mjs` (imports operators from `rxjs`) and `m12.mjs` (adds redelivery and an invalid-offset case). Re-run `node m12.mjs` and the others once on your verified runtime before distributing them.

## Toolchain note

The pack’s verified baseline is Node 24, which moved to Maintenance LTS in October 2026 and is supported into 2028; Node 26 is the Active LTS line. Do not change the baseline without re-running the validation report. TypeScript 6 and 7 and RxJS 7 are covered in the module text where relevant.

## Instructor materials

The [quiz answer key](../instructor/QUIZ_ANSWER_KEY.md) covers every 10-item quiz and the M20 quiz and essays. Keep it out of the student pack.
