# ADET runnable examples

## Updated opener M00–M05

M00 is paper-only. For M01–M05 copy the lesson's App.tsx into a separate student copy of [offline-lab/starter](../offline-lab/README.md). Core entry: index.ts → App.tsx. Use the pinned SDK 58 / TypeScript 6.0.3 baseline and lockfile, then `npx tsc --noEmit` and `npx expo start --offline`. Native client and local-network smoke tests are required before classroom use; only compilation and bundling are measured so far.

Fresh online preparation uses:

```powershell
npx create-expo-app@latest ADET-M##-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
```

Use the instructor's real module number and naming pattern. No extra packages for core M01–M05. M05's [real Router extension](M05/router-extension/README.md) is a separate online-prepared project with its own entry/configuration; the core M05 App.tsx is only a stack simulation.

## Existing later checkpoints — pending rewrite

M06–M21 retain their prior content until their approved batches. The existing mobile/ shell includes additional libraries and is NOT the template-only offline starter. examples/api also requires separate preparation; see its README. Do not claim those dependencies or databases are supplied by the starter.

The selector is instructor-only: `node select.mjs 01` through `20` copies a checkpoint over mobile/App.tsx. Save student changes first. It now always uses an App.tsx entry and does not switch M05 into Router. Use the separate extension for real Router navigation. M00 and M21 have no selectable executable checkpoint. Students should use independent folders and direct copy instructions from their lesson.

Do not distribute instructor audit projects as student examples. Do not submit node_modules, caches or secrets. Announce dependencies before the activity so students prepare their own laptop and bring it to the coding meeting.
