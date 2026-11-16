# Teaching the ADET semester

**Current finals sequence:** M19 rehearsal, [M20 defense quiz and essays](../modules/ADET_M20.md), then [M21 solo mini-capstone announcement and readiness](../modules/ADET_M21.md). Use the explicit evidence table in modules/README.md; M03 and M04 are both coding. If finals has only two teaching meetings, assign M20 as individual preparation between M19 and M21. Keep summative and periodical exam time separate.

Start with the [student index](../modules/README.md), [environment setup](../examples/README.md), [answer key](ANSWER_KEY.md) and [validation record](VALIDATION.md). The mobile checkpoints share a shell. Select the lesson before class and keep a copy of student modifications before selecting another screen.

| Period | Chapters | Evidence before the periodical |
|---|---|---|
| Prelim | 00–05 | Explain and change a component, input and route |
| Midterm | 6–11 | Trace one task from list to API to database, handle invalid data |
| Pre-final | 12–18 | Add one suitable device capability and finish a personal vertical slice |
| Finals | 19–21 | Repair rehearsal and a runnable solo project presentation |

Two weekday meetings per week give 60–90 minutes each. Reserve a summative meeting before each periodical, including finals. Assign dates only after receiving the actual timetable. Twenty-two prepared lessons may require combining selected cores. If Prelim has only four content meetings, combine M03 form review with M04 component reuse and use M05 as a prepared navigation demonstration. Grade one task in that meeting. For a short pre-final, show notifications and media as instructor demonstrations and preserve the project integration lab.

**60-minute quiz meeting.** Spend 5 minutes on the campus problem, 20 on the concept and trace, 15 running and changing the screen, 15 on the ten questions and 5 reviewing a common error. M00 introduces app development with a quiz; M01 is the first coding meeting. **Coding meeting.** Spend 5 minutes predicting, 15 demonstrating, 30 on one individual change and 10 comparing a valid and failing case. At 90 minutes, spend the additional time on setup support, device testing and independent explanations. Avoid adding another graded drill.

Use one backend for an implementation. Pre-seed a private practice dataset and verify phone-to-PC reachability before M07. FastAPI serves HTTP for the SQL track while XAMPP/WampServer supplies the database. For MongoDB use the Node API. Both have the same JSON surface. M11 deliberately models local session behavior. An identity stored on a client is insufficient proof of ownership on either public API.

**Solo evidence.** For M18 require one personal change, the client/API/database diagram and a success/failure trace. M20 remains a 20-item quiz plus two essays; M21 carries the solo mini-capstone readiness requirements. The rehearsal checklist is a tool for students to record their evidence. Set separate summative and periodical papers and grade those in the assigned slots.

**Device preparation.** Rehearse permission denial and cancellation as well as success. A teacher device can demonstrate the camera and local reminders if students cannot grant permissions on lab devices. Keep a text alternative for the report and a visual label for audio. Use the offline visual assets on the projector. Record class timing and common blockers after the first delivery.
Maintenance: the earlier 20-lesson authoring scripts describe the original sequence. Preserve the published M20 assessment and M21 announcement when regenerating earlier lessons.


## Approved opener delivery — November 7, 2026

Use [OPENER_ANSWER_KEY.md](OPENER_ANSWER_KEY.md) for M00–M05. It supersedes old opening keys. M06–M21 keys remain in ANSWER_KEY.md until those batches are rewritten. Every coding module offers one graded activity in three equal-point modes; never grade all three. Copying the sample is guided practice.

Before class: verify Node/npm, student folder copies, installed dependencies, compatible native client, and the [five-minute smoke test](../offline-lab/SMOKE-TEST.md). The measured checks establish local compilation/bundling only. If no real display route works, use the written trace with its equivalent rubric. No new native package is needed in the opener core.

At the end of the preceding meeting, announce the next coding activity's laptop setup. Reuse its Before next meeting block on the LAST slide, with the actual date supplied by the teacher. M00 announces M01; M02 announces M03; M03 also announces M04. Students prepare their OWN laptop before class and bring it to do the activity. A module also carries its own reusable preparation block for the teacher to send earlier. M05's quiz needs no coding delivery modes.

The separate Router extension is optional online preparation. Core examples all use App.tsx. Do not run the old authoring generators over the rewritten lessons. The current opener generation sources are update_opener.py and opener_support.py; manual refinements and validation results must be preserved.
