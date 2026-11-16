# Teaching blueprint: approachable, practical, and interesting

[Research pack home](README.md) | [ADET outline](ADET_23_MODULE_PLAN.md) | [EDP outline](EDP_23_MODULE_PLAN.md)

## 1. Course rhythm

Use **copy → run → trace → modify → explain**. Copying is the entry point, not the evidence that learning is complete.

1. Show a familiar problem: “Bakit dalawang order ang nasend?” or “Paano kung walang internet?”
2. Let students see the finished behavior before explaining every line.
3. Build a complete small starter together. Pause at meaningful checkpoints.
4. Trace the actual values and event sequence using the code, UI, or logs.
5. Change one requirement independently or in pairs.
6. Test a normal case and a failure/edge case.
7. Ask each learner to explain one important line or decision.

Avoid grading typing speed. Give students the full starter as a downloadable file as well as a Markdown code block. Allow pair programming, but rotate who types and ask both students to explain. Offer a core task and an optional stretch task so faster learners stay engaged without leaving beginners behind.

## 2. Final lesson structure

Preserve the source collection's recognizable structure while strengthening the practical work:

| Section | Required contents |
| --- | --- |
| A. Preview & Review | Familiar scenario, prerequisites, estimated time, 2–4 measurable targets |
| B. Main Lesson | Short definitions, reasons for the technique, a diagram or trace when useful, one common misconception |
| C. Analogy & Use Case | A natural Taglish explanation linked explicitly to the real technical behavior |
| D. Guided Coding | Exact filenames and commands, full imports and code, dependencies, incremental checkpoints |
| E. Expected Result & Code Walkthrough | Visible output or log sequence, explanation of the key lines, normal and failure cases |
| F. Gawin Mong Sarili | A small independent change, acceptance criteria, optional stretch, submission evidence |
| G. Troubleshooting & Wrap-Up | Likely mistakes, how to diagnose them, an explanation/demo prompt instead of a long quiz |
| H. Instructor Notes & Sources | Demonstration hints, rubric focus, source links, tested environment and limitations |

Technical identifiers stay in English. Explain them in Taglish without inventing awkward translations. Examples:

- **State:** “Ito ang data na kailangang maalala ng app habang nagbabago ang screen.”
- **Event handler:** “Ito ang function na tatakbo kapag nangyari ang event.”
- **Await:** “Hihintayin ng async function ang result bago ituloy ang kasunod nitong step; hindi ibig sabihin na frozen na ang buong app.”
- **Cleanup:** “Kung ikaw ang nag-start ng timer o listener, malinaw din dapat kung kailan mo ito ititigil.”

Analogies simplify one aspect of a concept. Follow them with the real rule so students do not mistake a restaurant waiter analogy for the actual event-loop implementation.

## 3. Proposed semester allocation

The curriculum lists 2 lecture and 3 laboratory hours for each subject. **Assumption for planning: an 18-week semester, approximately 90 contact hours per subject.** The institution's actual calendar must replace this assumption before the official syllabus is issued.

Each module has a nominal three-hour learning core, approximately one conceptual hour and two practical hours. Twenty-three modules use 69 hours. The remaining 21 hours support explanation, remediation, integration, assessment, and feedback. This can be distributed to match 36 lecture and 54 laboratory hours across the term; modules are not synonymous with weeks.

| Weeks | Module range in each course | Core hours | Flexible/support hours | Focus |
| --- | --- | ---: | ---: | --- |
| 1–3 | 01–04 | 12 | 3 | Setup, language bridge, first visible success |
| 4–6 | 05–08 | 12 | 3 | Interaction and structured state |
| 7–9 | 09–12 | 12 | 3 | Async behavior and data exchange |
| 10–12 | 13–16 | 12 | 3 | Persistence, boundaries, integration |
| 13–15 | 17–20 | 12 | 3 | Reliability, testing, technology experiments |
| 16–18 | 21–23 | 9 | 6 | Capstone integration, demo, feedback, buffer |
| **Total** | **23 modules** | **69** | **21** | **90 hours per course** |

Two courses together would be approximately ten contact hours per week under this assumption. Coordinate submission dates so both major demonstrations do not fall on the same day. Use the institutional examination weeks for practical demonstrations where permitted rather than inventing an extra week.

## 4. Assessment with fewer quizzes

Suggested weighting per subject, adjustable to school policy:

| Evidence | Weight | What is assessed |
| --- | ---: | --- |
| Guided-lab portfolio and selected remixes | 40% | Working behavior, meaningful modification, explanation, edge-case evidence |
| Two practical checkpoints | 20% | Each student can implement or debug a small change with reference materials |
| Final project | 30% | Coherent solution, correctness, robustness, and appropriate scope |
| Demo, reflection, and peer-feedback improvement | 10% | Ability to explain, test, and improve the work |

No weekly multiple-choice quiz is required. A short ungraded prediction question may start a lesson. Practical checkpoints can follow Module 08 and Module 16. Open-reference tasks test application of ideas rather than memorization of method names.

Use this 20-point rubric for a typical remix:

- Correct required behavior: 8 points.
- Meaningful independent change: 4 points.
- Input/error handling and test evidence: 4 points.
- Explanation and readable organization: 4 points.

A screenshot alone is not proof of correctness. Require code plus an explanation or short demonstration. AI-assisted code is allowed only with disclosure and verification; students remain responsible for tracing the changed behavior and correcting errors. This is a proposed classroom policy, not a statement of the institution's existing rules.

## 5. Infrastructure and access plan

**ADET minimum:** a development computer, editor, compatible Node/npm setup, and an Android/iOS device with a compatible Expo Go client where available. A supported web preview is a fallback for UI/data exercises, but it cannot prove native permissions or hardware features work. Pair learners when devices are limited. Internet is needed for initial package installation; prepare a working classroom baseline beforehand.

**EDP minimum:** editor, modern browser with DevTools, and Node.js for later modules. Browser activities use a local HTTP server where necessary; do not assume every feature behaves correctly when opened as a `file://` page. Keep runtime labels clear: browser JavaScript, Node JavaScript, or TypeScript with an explicit runner/checker.

Do not require paid APIs, cloud accounts, credit cards, store publication, or dedicated IoT boards for the core pass. When a feature depends on network or hardware, include a deterministic fixture or simulator and label it accurately. The fallback should teach the same core concept, while its limitations are stated.

For local APIs on a phone, document the computer's reachable local address, Wi-Fi/firewall checks, and the fact that `localhost` on the phone points to the phone. This setup detail must be tested on the classroom network before the related lab.

## 6. Keep the subjects distinct

| Shared concept | ADET emphasis | EDP emphasis |
| --- | --- | --- |
| Events | Responding to mobile interaction | Registration, dispatch, propagation, listener lifetime |
| Async/await | Loading/error/retry UX | Ordering, rejection, concurrency, cancellation |
| State | Consistent screens and application data | Explicit transitions and event histories |
| Persistence | Useful data after restarting | Restoring state and validating saved input |
| Testing | User journeys and pure domain rules | Timing-independent rules, cleanup, failure sequences |
| Final product | Usable campus/student mobile app | Reliable event-driven interactive program |

Reusing a canteen scenario reduces the effort of understanding the problem domain. The implementation and graded outcomes should still differ between courses.

## 7. Authoring and validation plan

Before calling the full course pack complete:

1. Produce exactly 23 numbered Markdown modules in each subject directory; keep supplementary guides separate from the count.
2. Resolve one documented dependency baseline; save a lockfile and exact setup commands.
3. Supply complete starter files, not code fragments requiring undisclosed prior changes.
4. Run TypeScript checks where relevant, execute console examples, and verify expected outputs.
5. Test browser interactions and representative mobile screens on the stated platform; exercise permission denial, canceled selections, and offline/error paths.
6. Identify any device/cloud feature that could not be verified rather than claiming blanket validation.
7. Check every local file link and code fence, and keep citations next to technical explanations.
8. Ensure every simulation is labeled and every extension has clear prerequisites.

The current research pack completes the initial planning pass. It does not replace these implementation checks.
