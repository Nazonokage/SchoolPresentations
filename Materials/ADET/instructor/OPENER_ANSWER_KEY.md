# M00–M05 instructor keys and coding criteria

Instructor distribution only. Quiz answers are one point each; accept equivalent explanations. The coding assessment totals 10, using the lesson's 4/2/2/2 rubric in any delivery mode. Guided practice is ungraded.

## M00 — 10-item quiz

1. A — Application software performs a user task.
2. B — Requirements identify the problem before building.
3. B — Separate native implementations require separate maintenance.
4. A — Swift is used for native iOS development.
5. B — These React Native mobile components map to native views.
6. B — Hermes executes JavaScript on the device.
7. B — Expo provides a framework and tools around React Native.
8. A — Expo Go hosts compatible development projects.
9. D — A spreadsheet macro is not one of the three taught mobile approaches.
10. C — Testing includes incorrect and empty input.

## M01 — coding / written alternative

Budget 80 with prices 25, 35, 15 leaves 5. Budget 75 leaves 0 and selects Change, because >= includes zero. Check an individual modification, a meaningful failure and repair, command explanations and reproducible evidence. A misspelled import should be restored before final submission. For the paper route: original balances are -10, 0, 20 for budgets 50, 60, 80; with added 15 they become -25, -15, 5. Require an ordered trace, not only final numbers. No extra-package installation is graded.

## M02 — 10-item quiz

1. A — A screen presents one task's UI.
2. B — The effect runs after commit; development checks may repeat setup/cleanup.
3. A — The returned function cleans up the effect's resource.
4. B — background reports that state; it does not implement pausing.
5. A — Activity is an approximate Android comparison, not a one-to-one mapping.
6. Its local state is discarded — a new instance starts from its initial state.
7. AppState — it observes whole-app status, not individual navigation focus.
8. React Native DevTools Console — terminal forwarding varies. This is the documented target, not a claimed physical-device observation.
9. To release the interval — otherwise callbacks can continue unnecessarily after removal.
10. Mount, update, unmount — distinguish render/commit and effect setup/cleanup when discussing the trace.

## M03 — coding / written alternative

Expect showPassword/setShowPassword state initialized false; secureTextEntry={!showPassword}; a button that toggles via a functional update. For the refined validation, test username.trim() first and return after its message, then check password === "". Spaces-only passwords pass the specified demo rule. Grade the explanation that this is validation, not authentication. Use invented credentials only. Written evidence must trace at least the four requested inputs and show the state change and missing-setter failure.

## M04 — coding / written alternative

Registrar uses OfficeCard with capacity 4; it is not a pasted third implementation. Leave can use setVisitors(current => Math.max(0, current - 1)); readable equivalents count. Library and Clinic remain independent. Trace two joins then one leave as 0 → 1 → 2 → 1; at zero, another leave remains zero. Width/font rule is row only if width >= 700 AND fontScale <= 1.3. Accept truthful hardware limitations and the equivalent paper route, not fabricated screenshots.

## M05 — 10-item quiz

1. A — A route names a destination.
2. B — _layout supplies the navigator.
3. B — Brackets identify the dynamic segment.
4. A — Tabs select peer sections.
5. B — Navigation guards cannot authorize server data access.
6. [Home] — Back removes the pushed top entry.
7. Office not found — an unknown ID is not a known record.
8. No — a mounted screen can lose focus without being removed.
9. No — the array model has no external URL handling.
10. Home — replace the destination when no previous history exists.
