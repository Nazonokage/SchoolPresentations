# ADET prepared starter

Entry: index.ts registers App.tsx. No Router routes or AI-agent configuration are included. Created with blank-typescript@sdk-58 and --no-agents-md on 2026-11-06 (Asia/Manila).

Preparation baseline: Node 24.18.1; npm 11.16.0. Course TypeScript is exactly 6.0.3. Direct dependency versions are exact in package.json; package-lock.json pins the transitive graph. Use this lockfile for reproduction, not an unpinned fresh install.

| Package | Installed version |
|---|---|
| expo | 58.0.23 |
| expo-status-bar | 58.0.4 |
| react | 19.3.0 |
| react-native | 0.88.1 |
| @types/react | 19.3.0 |
| typescript | 6.0.3 |

## Run

Use the parent START-LAB.cmd, or from this folder run `npm run typecheck` then `npm run offline`. Installed packages are supplied for the prepared Windows environment. Native client/device and network availability still need the smoke test in ../SMOKE-TEST.md.

A fresh online project uses:

```powershell
npx create-expo-app@latest ADET-M##-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
```

Copy the course manifest and lockfile if exact reproduction is required. Restore packages from the supplied cache using the parent RESTORE-OFFLINE.cmd. The package cache and installed node_modules are offline delivery assets, not source to upload to a student repository.

Do not run a selector against this starter: copy it to the student folder, then replace that copy's App.tsx with the announced lesson file. M05's real Router extension will have its own explicitly documented route layout after the opener batch is approved; the base lab will remain App.tsx.
