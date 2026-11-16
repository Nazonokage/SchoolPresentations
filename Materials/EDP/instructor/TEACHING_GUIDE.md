# EDP instructor teaching guide

**Current finals sequence:** M19 rehearsal, [M20 defense quiz and essays](../modules/EDP_M20.md), then [M21 solo mini-capstone announcement and readiness](../modules/EDP_M21.md). Alternating assessments apply through M19. If finals has only two teaching meetings, assign M20 as individual preparation between M19 and M21. Keep summative and periodical exam time separate.

Prepared 3 November 2026. Use [module index](../modules/README.md), [answer key](ANSWER_KEY.md), [coverage map](COVERAGE_MAP.md) and [validation report](VALIDATION.md) together.

## Structure and pacing

Each lesson follows the existing course's A. Preview, B. Main Lesson, C. Analogy/Program, D. Assessment/Wrap-Up structure. M01–05 are Prelim, M06–11 Midterm, M12–18 Pre-final, M19–21 Finals preparation. These are prepared chapters, not guaranteed dates. Retain separate summative-before-periodical slots; exclude Saturdays. Use the existing calendar/capacity analysis before assigning dates.

M01 refreshes variables, conditions, loops and functions together and introduces setTimeout/clearTimeout. Give the prepared workspace before class; do not spend the whole meeting installing. Its quiz is diagnostic. M03 must begin with the hello button and script block before showing the full form/list extension. Pause after selection, registration, click and text update so students can identify each step.

Odd lessons have one 10-item quiz; even lessons have one coding submission. Do not add graded drills on top. The first three quiz items check concepts, next three traces, next two debugging and last two decisions. Answer keys are instructor material. Use local grading policy for weightings; the proposed coding rubric is 10 points.

## Depth and shortening

Core: the smallest runnable behavior and its failure/cleanup rule. Guided extension: modify the same program. Reference: compare architectures or tools without installing them. Twenty modules can exceed available teaching slots; combine selected related core material and remove optional activities instead of accelerating through two full lessons. If one meeting combines modules, assign one primary assessment and explicitly reschedule or omit the other.

M01–02: prioritise callbacks and observable scheduling. M03: first button, then form. M04–05: emitter and latest-result correctness. M06–08: typed payloads, state rules, one reactive pipeline. M09–11: one transport, one stream and meaningful tests. M12–17: the local model plus a failure diagram; do not demand production brokers, databases, telemetry stacks or cloud accounts. M18: one personal feature. M19–21: repair, explanation and reproducible packaging only.

## Demonstrating understanding

Ask students to predict, run, point to the responsible handler and change one behavior. When they cannot explain it, return to the last working checkpoint and remove one abstraction. Use natural Taglish to clarify the mechanism, not to replace the technical vocabulary. Students who need longer syntax revision can use M01 as catch-up reading without turning every Prelim module into basic programming.

Require one personal modification for coding assessments. The teacher's reference programs are complete runnable baselines, not final answers to all student tasks. Check equivalent solutions against behavior and explanation. Offer an accessible text/console route where a complex interface is not the learning objective.

## Project and exam boundaries

The solo project requires a coherent event flow, validation, a state rule, failure handling, cleanup, tests and setup notes. A small local application is acceptable when limitations are declared. Optional SQL/Mongo persistence must be behind a server API and tested separately; no database install is required by these EDP core examples. The architecture survey is not a requirement to deploy every pattern.

M18's checkpoint, M20's readiness submission, the summative and final practical are distinct assessment events. Avoid awarding multiple marks for the same unchanged artifact. Write the actual exam papers separately according to institutional policy; this pack contains lesson quizzes and activity rubrics, not a claimed official exam.

## Maintenance

Read VALIDATION before claiming an environment is tested. Recheck dependencies when upgrading; repeat type checks and the behavior/browser suite after code changes. Browser UI and host networking differ from console tests. Keep simulations labeled, retain source provenance, and do not use copied AI reports as proof of correctness.
Maintenance: the earlier 20-lesson authoring scripts describe the original sequence. Preserve the published M20 assessment and M21 announcement when regenerating earlier lessons.
