# Stop 2 — M00–M05 opener authored

November 7, 2026, Asia/Manila. Stop 1 was approved. This batch updates the **actual modules folder**, not only review copies. Per the approved process, stop here for review before M06–M21 authoring.

## What changed

| Module | Evidence type | Delivered lesson |
|---|---|---|
| M00 | 10-item quiz | Code-free app-development introduction, house analogy explicitly labeled, shared-code/platform differences, accurate Hermes role diagram and paper requirements trace |
| M01 | Individual coding | Tool roles, SDK-pinned setup, compact baon refresher covering variables/conditions/loops/functions, separate type-check, independent budget modification |
| M02 | 10-item quiz | Screens/state/effect lifecycle, conditional unmount versus blur/hiding, cleanup and dependency trace, AppState limitations; quiz item 8 agrees with DevTools instructions |
| M03 | Individual coding | Basic layout and controlled form, exact validation including spaces-only password, early-return trace, show-password activity and optional complete timeout comparison |
| M04 | Individual coding | Typed reusable cards, independent state, capacity/leave behavior, responsive width/font-scale rule and accessible labels/status; optional local-asset/theme discussion |
| M05 | 10-item quiz | Routes, stacks/tabs, dynamic IDs, invalid route data, guards versus authorization; template-only stack model plus separately configured real Expo Router extension |

All six use the A–D structure, plain-language explanations, Taglish analogy, trace/prediction, common mistakes, local text diagrams, references and instructor notes. Coding modules M01/M03/M04 have three delivery modes and equivalent 4/2/2/2 rubrics. Their laptop announcements specify personal-laptop preparation before class, folder/repository names, actual dates supplied by the instructor and last-slide placement. M03 and M04 intentionally remain consecutive coding modules.

## Example and supporting changes

- examples/M00 now contains the paper-only activity pointer; M01–M05 contain matching copyable App.tsx files and setup READMEs.
- M03/App.timeout.tsx preserves the absorbed form-feedback/effect-cleanup comparison as optional ungraded work.
- M05/router-extension contains complete route files, setup command, dependency list, entry/configuration instructions and invalid-ID/no-history behavior. Extra packages are isolated from the core offline starter.
- examples/mobile is confirmed as an App.tsx shell. Its inactive old app/ route files were preserved in the before/ backup and removed from the active shell. The instructor-only selector no longer switches M05 to a Router entry.
- Student quiz solutions moved to instructor/OPENER_ANSWER_KEY.md with one-line reasons. ANSWER_KEY.md now points to it for M00–M05 and preserves the later keys.
- Root README and modules/README now list all **22 lessons and their evidence types**, with an explicit partial-migration status. The teaching guide and examples index agree with the approved sequence.
- The prepared starter and its committed lockfile are retained; no audit project was copied into student source.

## Numbering and topic mapping

Added M00. M01–M05 keep their numeric IDs but their content is reorganized: old M01 feeds M00/M01; old M02 components/props and old M03 responsive/accessibility work feed new M04; old M04 forms/lifecycle feeds new M02/M03; M05 remains navigation. **No M06–M21 renumbering or topic changes.** M20 and M21 lesson files remain unchanged in this batch.

## Validation and limits

See [VALIDATION.md](VALIDATION.md). All five core apps, the M03 timeout extension and the separate Router source passed TypeScript checking and Android bundle generation. Router checking reused existing installed dependencies; it is not a fresh-install claim. No real phone, emulator navigation, TalkBack/VoiceOver or classroom Wi-Fi result is claimed.

The previous mobile/ shell still contains the later modules' extra libraries and older TypeScript manifest; it is labeled as a legacy instructor shell pending later-batch normalization, not the recommended starter. All rewritten core lessons use the SDK 58 / TypeScript 6.0.3 prepared starter. M06–M21 lessons, examples and their cross-references still require their scheduled rewrite and final all-course consistency pass.

## Review boundary

**M00–M05 are updated; M06–M21 are not yet rewritten.** After stop-2 approval, continue M06–M10, M11–M15 and M16–M21 without additional approval stops unless technically blocked. Preserve M20's 20-item quiz/two essays and M21's solo capstone. Then finish all-course setup, dependencies, assessment, naming and cross-reference consistency.

Original files changed in this batch are retained under before/. Authoring pipeline for this batch: opener_support.py (imports update_opener.py), refine_opener.py, then finish_opener.py. Do not run an older generator over the new modules. Validation scripts and measured results are stored here separately from student examples.
