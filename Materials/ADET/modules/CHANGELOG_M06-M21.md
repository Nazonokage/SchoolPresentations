# Change log — M06 to M21 and README

## What changed in every module
- Rewritten to the approved structure (A preview, B lesson, C analogy and code, D assessment, instructor notes).
- "In plain words" intro, concept table, predict-then-trace table, one misconception, three common mistakes.
- Conventional names (`setTasks`, `message`, `busy`, `callApi`), comments on non-obvious lines.
- "Install first" with `npx expo install`, and what is online-only.
- `node select.mjs` and the instructor-style figure text are gone. Setup points to M01 and the prepared starter.
- Quizzes: each item tests one stated idea; every quiz has an instructor answer key with a one-line reason. M20 keys name the lesson each item comes from, and the essays have a rubric.
- Coding modules (M06, M08, M10, M12, M14, M16, M18): three equal-point delivery modes plus a "before next meeting" handout. M21 is the capstone (see decisions).

## New or changed behavior
- **Practice server (M07, M08, M10, M16, M18):** API screens now run with no server. `request()` uses a small in-app fake server unless `EXPO_PUBLIC_API_URL` is set. A Stop/Start button rehearses a connection failure.
- **M12:** the core uses a practice camera (allow, cancel, deny). The real `expo-image-picker` version is an optional online extension.
- **M11:** the model now separates "not signed in" from "signed in but not allowed" (the old sample said Denied in both cases).
- **M09:** Restore reports "Nothing saved yet" for a missing key.
- **M10:** failed loads keep and label the last known count; retry is off in class so errors show at once.
- **M17:** test cases have names, and the lesson shows the `<=` to `<` mutation.
- **M21:** the readiness checklist is now `examples/M21` (the old text pointed to M20 files).

## Verified
- All 16 example files type-check (strict, SDK 58, TS 6). Lesson code blocks match the example files exactly.
- Practice server logic tested in Node.

## Not verified
- Anything on a physical phone or emulator; Expo Go behavior of each package; notification, camera, audio and share behavior; real APIs with these screens; the lab network route.

## Decisions for you
1. **M10 needs a package in the offline lab.** Pre-install `@tanstack/react-query` in the starter, or use Mode 3.
2. **M21 has no written alternative.** A capstone is not a single-concept trace. Decide what a student with no runnable route may submit.
3. **The real API in `examples/api`:** I did not see its README, so the modules only say how to point at it. Test it with these screens before relying on it.
4. **`examples/README.md` and `select.mjs`:** not rewritten here. The lessons no longer use them.
5. **M05:** not touched. Check that it matches this style.
