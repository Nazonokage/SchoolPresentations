# ADET offline computer lab

Copy this entire prepared folder to the lab PC or your own laptop by USB. The code starts from blank-typescript and App.tsx. Node and VS Code must already be installed. The prepared native client or emulator must match SDK 58. No native device or classroom network has been validated yet.

## Start

Double-click START-LAB.cmd on Windows. It runs the local Expo CLI from starter with --offline. Or open a terminal in starter and run npm run typecheck, then npm run offline. Stop Metro with Ctrl+C. Use one copy of this starter per student. Do not overwrite a student's modified App.tsx while switching checkpoints.

## Prepared contents

- starter/: exact package versions, package-lock.json, source, assets and installed node_modules for the prepared Windows/Node environment.
- npm-cache/: cache populated during online preparation, for a separate offline reinstall route.
- RESTORE-OFFLINE.cmd: executes npm ci --offline --cache ../npm-cache --no-audit --no-fund inside starter. This replaces node_modules, so use it only when dependency restoration is intended.
- SMOKE-TEST.md: timed pre-class checklist and evidence form.

No instructor audit project is part of the starter. Do not copy instructor/opening-audit-*/opening-check to students.

## Online preparation on each student's laptop

At the end of the PREVIOUS meeting, announce the next coding module, required packages and these instructions. Students prepare their OWN laptop before the next class, bring it and do the activity on that laptop.

```powershell
npx create-expo-app@latest ADET-M##-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M##-LASTNAME
npx tsc --noEmit
npx expo start
```

Replace ## with the announced module number and LASTNAME with the instructor's naming convention. The SDK is pinned; use the distributed package.json and lockfile when exact package reproduction is needed. The course's exact TypeScript version is 6.0.3. --no-agents-md was tested successfully. This course uses no AI-agent files.

Bring a screenshot of the running app or the exact error. If home internet is unavailable, use campus Wi-Fi, mobile data or an agreed hotspot before class, or copy the prepared folder by USB. Any extra native-package exercise is optional online extension work; the core lab uses template packages and simulated inputs.

## How students see the result

A physical phone still needs a reachable PC over local Wi-Fi and a compatible Expo Go installed beforehand. --offline stops Expo CLI's online lookups; it does not create a network, install Expo Go or bypass router isolation. A prepared emulator is another route, pending an actual local test. iOS Simulator requires macOS/Xcode and is unavailable on the Windows preparation host. The blank template does not include React DOM/react-native-web; web preview is not promised as a zero-install alternative.

--tunnel is online-only and needs its tunnel tooling. It is not an offline fallback.

## Copying and submission

Copy starter with node_modules for the tested same-OS lab environment. Keep npm-cache if you want the offline reinstall route. Node installers, VS Code and native emulator/client installers are not included. Do not assume Windows node_modules works on macOS or Linux: prepare and smoke-test per platform.

Do not upload node_modules, npm-cache, .git, .expo or secrets as student source. Submit source, manifest, lockfile, README, essays and requested evidence. Repository names and dates follow the activity instructions, not a guessed deadline.

## API and package boundaries

The core starter has only the blank-template packages. Later API lessons will use deterministic mock data as the offline baseline. Existing examples/api is not bundled or certified by this starter: its real Node/MongoDB or FastAPI/SQL route requires separately prepared server dependencies and a running local database. Starting a server on the PC also requires using a reachable PC address from a phone. Real camera/storage/maps/notifications/SQLite integrations require separate documented online preparation and do not belong in the core no-new-install lab.

## Test record

See ../instructor/stop1-2026-11-06/REPORT.md for measured outcomes and limits. A successful local Android bundle is not a real-device test. Native log location, phone LAN behavior and emulator execution remain pending until actual hardware is available.
