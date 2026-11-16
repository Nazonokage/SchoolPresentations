# Opener validation — November 7, 2026

## Executed checks

| Checkpoint | TypeScript 6.0.3, noEmit | Metro Android bundle | Native device |
|---|---|---|---|
| M01 baon | Pass | Pass | Not tested |
| M02 lifecycle | Pass | Pass | Not tested |
| M03 form | Pass | Pass | Not tested |
| M04 reusable cards | Pass | Pass | Not tested |
| M05 offline stack model | Pass | Pass | Not tested |
| M03 optional message timeout | Pass | Pass | Not tested |
| M05 actual Router extension | Pass | Pass | Not tested |

Core results: [validation.json](validation.json), check-opener.mjs and per-example logs. The harness temporarily copied each checkpoint into the installed blank starter and restored its original App.tsx afterward. Each bundle response was successful and contained the checkpoint's expected marker. This detects compilation/bundle failures; it is not an interaction test.

Router results: [router-validation.json](router-validation.json), check-router.mjs and router logs. A separate audit project contains the actual route files and config. Its node_modules junction points to existing examples/mobile dependencies; this avoids claiming a fresh minimal dependency install. Type checking used the course TypeScript 6.0.3 compiler. The Android bundle included the Home and detail routes. Installed versions were expo 58.0.23, Router 58.0.30, linking 58.0.16, constants 58.0.15, status-bar 58.0.4, React 19.3.0, React Native 0.88.1, screens 4.30.1 and safe-area-context 5.11.1.

Both harnesses recorded all results and restored the starter, but their process sessions remained open after the results were written. They were interrupted afterward to finish cleanup. Their individual compiler exit codes are 0; do not confuse that with an uninterrupted harness exit. Local ports 8291–8296 and 8301 were subsequently checked closed.

The stop-1 prepared-cache result still applies: npm ci --offline restored 458 packages with an unreachable registry, and the restored starter type-checked. No dependency changes were made to that starter in this batch.

## Static review

The final static-check record covers A–D sections, each quiz count, coding delivery modes, SDK-pinned scaffolding commands, module/example source agreement, local links and the 22-row module index. See [static-check.json](static-check.json).

## Device/classroom acceptance still required

Use offline-lab/SMOKE-TEST.md with an actual prepared phone or emulator before teaching. Record its SDK/client version and connection route. Check M02 mounted/unmounted logs in React Native DevTools, M03 keyboard/validation behavior, M04 larger fonts and screen reader labels, and M05 Back plus no-history navigation. Conditional removal, navigation blur and backgrounding are different tests.

A paper trace is the equal-point alternative when no native display route is available. No offline phone route, physical USB transfer to another PC, real custom-scheme deep link or accessible-screen certification has been asserted.

## Documentation inspected

- [Expo Router manual installation](https://docs.expo.dev/router/installation/) — explicit dependency command and entry configuration.
- [React Native window dimensions](https://reactnative.dev/docs/usewindowdimensions) — responsive values.
- [React Native accessibility](https://reactnative.dev/docs/accessibility) — platform-dependent assistive technology behavior.
- [React useEffect](https://react.dev/reference/react/useEffect) — setup, changed dependencies and cleanup.

Version choice remains grounded in the separate store/template evidence in the stop-1 report, not a cached documentation page's version selector.
