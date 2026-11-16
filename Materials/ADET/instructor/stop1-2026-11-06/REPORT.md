# ADET stop 1: environment, corrections and offline evidence

Report completed November 7, 2026 (Asia/Manila). SDK/store evidence was collected November 6. This is the requested review checkpoint before full lesson authoring. The active lessons have not yet been replaced.

## 1. SDK and version decision

Both scaffolding tests used `create-expo-app@latest` with `--no-agents-md --no-install --yes`. These test template generation independently from package installation; the selected SDK 58 starter was subsequently installed and tested.

| Template argument | Generated Expo | React Native | React | TypeScript |
|---|---|---|---|---|
| `blank-typescript@sdk-57` | ~57.0.32 | 0.86.3 | 19.2.3 | ~6.0.3 |
| `blank-typescript` | ~58.0.23 | 0.88.1 | 19.3.0 | ~6.0.3 |

`--no-agents-md` worked with both templates. Neither probe generated AGENTS.md, CLAUDE.md or .claude/settings.json. No AI-agent configuration is part of the student starter.

The store/client decision was checked separately from the scaffolder:

- Android: Philippine Google Play application metadata reported Expo Go **58.0.5**. Expo's client metadata associates Android client 58.0.5 with **SDK 58**.
- iOS: Philippine Apple lookup reported Expo Go **58.0.5**, with release notes explicitly adding **SDK 58** support. The iOS simulator client listed by Expo is a different artifact; it is not the iPhone store version.
- Expo's download page identified SDK 58 as latest at inspection time.

Official evidence: [Expo Go](https://expo.dev/go), [Expo client metadata](https://exp.host/--/api/v2/versions), [Google Play](https://play.google.com/store/apps/details?id=host.exp.exponent&hl=en&gl=PH), [Apple Philippine lookup](https://itunes.apple.com/lookup?id=982107779&country=ph). Saved responses are alongside this report; see [sdk-evidence.json](sdk-evidence.json). Store availability can vary by rollout; this is a dated check, not a permanent compatibility promise.

**Selected course command:**

```powershell
npx create-expo-app@latest ADET-M##-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
```

The instructor supplies the actual module number and naming convention. This pins the SDK family; the distributed package.json and package-lock.json provide exact package reproduction. The course selects **TypeScript 6.0.3**, replacing the existing mobile project's ~5.9.3 during approved authoring.

Prepared starter baseline: **Node 24.18.1, npm 11.16.0**. Exact direct pins: expo 58.0.23, expo-status-bar 58.0.4, react 19.3.0, react-native 0.88.1, @types/react 19.3.0, typescript 6.0.3. See [starter README](../../offline-lab/starter/README.md). Source, manifest, lockfile and README were committed in the starter's own repository as **f75d930**; installed dependencies and cache are delivery assets, not committed source.

## 2. M00–M03 corrections prepared for review

Corrected reference copies are in [reviewed-opening](reviewed-opening/). These are correction-stage documents, not the final authored opener batch. Instructor answers still in these references will be separated during authoring.

| Lesson | Applied correction |
|---|---|
| [M00](reviewed-opening/ADET_M00.md) | House explicitly labeled an analogy; Hermes executes JavaScript rather than being another serial platform layer; shared code with platform differences; no student code. |
| [M01](reviewed-opening/ADET_M01.md) | SDK 58 command and no-agents flag; expo-constants removed from required offline checkpoint and retained only as optional online work; separate `npx tsc --noEmit`; Metro transpilation distinguished from type-checking; tunnel labeled online fallback; compact baon refresher covers variables, conditions, loops and functions with a worked trace. |
| [M02](reviewed-opening/ADET_M02.md) | Conditional removal unmounts; hiding/navigation blur need not unmount; AppState observes but does not pause this sample; OS termination does not guarantee cleanup; interval is not an accurate clock. Log instructions and quiz item 8 consistently identify React Native DevTools Console, with physical-device verification explicitly pending. |
| [M03](reviewed-opening/ADET_M03.md) | Raw text nodes belong in Text; string-valued props such as Button.title remain valid; exact validation is `username.trim() === "" || password === ""`; spaces-only password passes this demonstration; trace included; demonstration is not authentication. |

M01–M03 sample files all passed `tsc --noEmit` and local Metro Android bundle generation using the prepared starter. See [validation.json](validation.json) and the per-module logs. These checks establish compilation/bundling, not native UI correctness.

## 3. Offline-lab results

Read the EDP offline-lab pattern first. ADET now has [offline-lab/README.md](../../offline-lab/README.md), START-LAB.cmd, RESTORE-OFFLINE.cmd, a prepared starter with installed dependencies and lockfile, a populated npm-cache, and [SMOKE-TEST.md](../../offline-lab/SMOKE-TEST.md) with a five-minute checklist and actual-results form.

| Route/check | Measured outcome | Limit |
|---|---|---|
| Use the prepared installed dependencies | M01–M03 type checks and Android bundles passed with local Metro in offline mode. | USB transfer to a second PC has not been tested. |
| Reinstall from prepared cache | `npm ci --offline` installed **458 packages**, exit 0; restored project also passed `npm run typecheck`, exit 0. | Tested on this Windows/Node environment; not proof of another OS or architecture. |
| Phone connection / native screen / native logs | Not tested: `adb devices -l` returned no attached device. | No claim that a phone route works offline or that logs were observed on hardware. |
| Emulator route | Not tested. | A prepared native client is still required; iOS Simulator requires macOS. |

The isolated restore used this command from `offline-restore-check/`:

```powershell
npm ci --offline --cache '../../../offline-lab/npm-cache' --registry http://127.0.0.1:9 --no-audit --no-fund
npm run typecheck
```

See [offline-ci.log](offline-ci.log). The registry was deliberately unreachable and npm offline mode was enabled; the machine's network adapter was not disabled. An earlier attempt had an incorrect relative cache path and a Windows permission error; the successful retry used the correct cache path. No success claim relies on that failed attempt.

**Conclusion:** the prepared dependency route and cache-only restoration work for local compilation/bundling without fetching packages. End-to-end offline phone teaching remains a required classroom smoke test. `--offline` does not provide Wi-Fi, install Expo Go or bypass access-point isolation. `--tunnel` requires internet.

## 4. Layout and later authoring decisions

- Existing examples/mobile currently starts through index.js → App.tsx. Router packages and an app/office tree also exist, and the selector changes entry behavior for M05. This mixed layout must be normalized during authoring.
- The chosen core lab layout is index.ts → App.tsx, matching the prepared blank template. M05 still teaches Expo Router: its real Router extension must state its extra dependencies and separate route layout explicitly; the template-only lab uses a navigation simulation/paper trace. It must not silently switch the core starter's entry point.
- The starter was freshly scaffolded; instructor/opening-audit-*/opening-check was not copied into it or student examples.
- Existing examples/api requires a local MongoDB service plus prepared Node packages, or MySQL/MariaDB plus prepared FastAPI packages. It is not certified by this starter. Later core offline lessons will use deterministic mock data; real API startup and optional install commands will be documented separately.
- Camera, storage, maps, notifications, SQLite and similar package-dependent features use sample data/paper simulation in the template-only core lab, with explicit optional online extensions.
- Every coding lesson receives all three delivery modes and the equivalent 4/2/2/2 written rubric. The pre-class announcement goes at the end of the previous meeting's material: install named dependencies on **your own laptop before class**, bring that laptop, and perform the activity in the next meeting. No guessed calendar dates.

## 5. Approved authoring sequence and remaining work

No module renumbering has been applied at this checkpoint. The full pack remains scheduled for **22 lessons, M00–M21**. M00 quiz; M01 coding; M02 quiz; M03 coding; M04 coding; M05 quiz; M06 coding; M07 quiz; M08 coding. M09 onward retain their existing types. M20 remains 20-item quiz plus two essays; M21 remains solo mini-capstone.

After stop-1 review: author M00–M05, new examples and change log, then stop 2. After that approval: M06–M10, M11–M15, M16–M21, followed by all-course consistency checks and the 22-row README evidence table. M04 covers reusable components/props and a responsive accessible screen; M05 covers navigation. Old M04 interaction/forms/lifecycle content is absorbed into M02/M03. Later topics remain intact.

**Outstanding technical evidence:** a real device on a real network is needed to confirm rendering, connectivity and M02 console output. This requirement is not waived by compilation tests. The review copies disclose it rather than claiming it passed.

**Stop 1 reached.** Await the requested review before authoring the opener batch.
