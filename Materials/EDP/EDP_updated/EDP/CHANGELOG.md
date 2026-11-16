# EDP course revision: changelog

Scope: all 21 modules, README, Quick Reference, plus new instructor answer key and example files. Original structure (A–D sections, Taglish recaps, predict → run → explain → modify) is kept.

## Whole-course changes
- **Before class** now names the exact modules each lesson builds on (it was the same vague sentence in 17 modules).
- **Scope** is module-specific: core versus optional/reference reading.
- **Exit reflection** is a module-specific question instead of one copied prompt.
- **Next connection** names what the next module does and why (it was one copied sentence).
- **Rubrics** for the coding modules (M02, 04, 06, 08, 10, 12, 14, 16, 18, 21) now name the module's own evidence.
- Removed instructor-facing wording that leaked into student text ("source reports", "documentation site only returns a JavaScript loading shell").
- New `instructor/QUIZ_ANSWER_KEY.md`: all ten 10-item quizzes (M01, 03, 05, 07, 09, 11, 13, 15, 17, 19), the M20 quiz and both essay rubrics.
- README: prerequisite map, list of new extensions, toolchain note. Quick Reference: 11 new terms and one debugging step.

## Module changes
| Module | Change |
| --- | --- |
| M01 | TypeScript companion moved to an optional take-home; run block now only `node m01.mjs`. |
| M06 | Added a discriminated-union demo to `m06.ts` (with `never` exhaustiveness check) and a browser DOM-narrowing snippet. Note on TypeScript 6/7 defaults. |
| M07 | `m07.mjs` now records accepted facts, so "commands ask, events tell" is visible in output. Removed the Python aside. |
| M08 | `m08.mjs` imports operators from `rxjs` (7.2+ style). Version note rewritten. |
| M09 | Optional `ws-demo.mjs` (WebSocket, both directions, validated). Quiz item 4 replaced to cover it. |
| M12 | `m12.mjs` rewritten: crash and redelivery, offline subscriber, invalid-offset rejection. Task, expected output, rubric and troubleshooting updated. This was the one coding activity with no real failure case. |
| M14 | New "webhook is an inbox at the edge" section and optional `m14-webhook.mjs` (HMAC check, stale timestamp, dedupe). Added a `node:crypto` reference. |
| M17 | New `m17-resilience.mjs` (bounded retry and a small circuit breaker) so learning target 3 has code. |
| M20 | Restructured into the A–D layout with learning targets, a worked defense example, an essay rubric and the scoring table. |
| M21 | Header order fixed (announcement now follows the title block). Table module references corrected (idea 1: M07; idea 6: M01, M05, M11). Added idea 11 (webhook receiver), a fresh-install check, and a rubric written for the capstone. |
| M02–05, 10, 11, 13, 15, 16, 18, 19 | Whole-course changes only (plus one wording cleanup each in M16 and M18). |

## Corrections to my earlier review
- EDP_M21.md *was* on disk; I wrongly said it hadn't come through. It is reviewed and updated.
- I said the rubric asks for a failing case even where the task has none. Only M12 actually lacked one; the other coding tasks already had a failure case, so only their wording was tightened.

## Checked
All changed or new example code was run (Node 22.23 in my sandbox): `m06.ts` (plus a TypeScript 5.9 strict typecheck, and the two commented-out lines were confirmed to fail), `m07`, `m08` (RxJS 7.8.2), `m12`, `m14-webhook`, `m17-resilience`, `ws-demo` (ws 8.x). The code blocks inside the lessons are identical to those files.

## Needs your action (I could not see these)
1. **Copy the 7 files in `examples/` into your pack**, replacing `m06.ts`, `m07.mjs`, `m08.mjs`, `m12.mjs` and adding `m14-webhook.mjs`, `m17-resilience.mjs`, `ws-demo.mjs`.
2. **Add `ws`** to the pack's `package.json` (`npm install --save-exact ws`) and commit the lockfile, or leave `ws-demo.mjs` as a teacher demo.
3. **Re-run your validation on Node 24** (I tested on 22) and update `VALIDATION.md`. Node 24 entered Maintenance LTS in October 2026; Node 26 is now Active LTS. Moving the baseline is your call.
4. `examples/server.mjs`, `m09.html`, the diagrams in `visuals/` and the checked screenshots are unchanged. The `m12`, `m14` and `m17` captured-output images, if you have any, should be re-captured.
5. Left alone on purpose: the "Visual Guide & HTML Presentation Notes" boilerplate repeated in each module. Consider moving the shared lines into `visuals/README.md`.
