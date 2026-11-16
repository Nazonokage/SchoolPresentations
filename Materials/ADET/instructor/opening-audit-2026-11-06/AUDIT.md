# ADET opening review and overlap audit

Date: 2026-11-06 (Asia/Manila). Status: Tasks 1–2 review stage. Current student modules have not been deleted, overwritten or renumbered. Submitted references are saved here as *_submitted.md; they are preserved verbatim. The test project is isolated in opening-check/.

## Scope and evidence

Read the course README, all 21 student modules, module index and the textual source/configuration in examples (excluding installed dependencies, generated caches and binary assets). inventory.json records 60 inspected files with hashes, headings and imports. Existing M01–M05 samples and the selector confirm the overlaps below. The inventory is not a claim that all later code was executed.

The attached prompt explicitly requires stopping after Task 1 findings and the Task 2 overlap table. Changes to the remaining lessons and renumbering await approval. No AI-agent teaching is proposed.

## Task 1: technical and teaching findings

| Reference | Finding | Recommended correction |
|---|---|---|
| M00 | The house diagram suggests Hermes is a serial layer between React Native and all native UI. It is a conceptual simplification, not the runtime call graph. | Show app JavaScript executed by Hermes, React Native coordinating native views, and Expo libraries exposing supported services. Label the house as an analogy. |
| M00 | “Write once” and “same steps every time” overstate portability and process. | Say shared code with platform-specific differences; development revisits design, implementation and testing. |
| M00 | Its paper exercise correctly needs neither installation nor code. | Keep this exception to the coding-lesson setup structure. Keep all 10 quiz questions; add one-line explanations to their keys. |
| M01 | The supplied 57→58/default57/phone57 version note is not established by the official page returned in this audit. That page contains a different transition note and an older update date. | Use the fresh project's actual package versions and the test scope below. Do not infer the installed Expo Go version from create-expo-app. |
| M01 | The default-template file path may change. Moving App.tsx code into one route is not a complete migration instruction. | Standardize this course on blank-typescript and inspect the actual entry files. Keep Router setup for the navigation lesson. |
| M01 | “No extra packages” conflicts with the assessed expo-constants installation. | Use only template imports for the offline checkpoint. Move adding expo-constants to optional online homework or pre-install it explicitly. |
| M01 | --tunnel is presented as a connectivity fix without its internet and additional-tool requirements. | Label tunnel as an online fallback. Use --offline only with packages and client prepared, plus a functioning local connection. |
| M01 | The iPhone account instruction and alternative Expo Go installation steps need a platform-specific pre-class check. | Do not promise arbitrary Expo Go versions on a physical iPhone or a universally required sign-in flow; verify the actual chosen client and document it. |
| M01 | Fast Refresh does not guarantee every edit preserves state or avoids a reload. | Describe it as development refresh behavior, with possible remounts/full reloads. |
| M01 | “TypeScript warns before running” may imply Expo refuses type-invalid code. | Teach a separate npx tsc --noEmit check; Metro transpilation does not replace it. |
| M02 | useEffect is described as always after the screen draws. | Teach effect setup after commit; avoid an unconditional after-paint claim. Explain dependency cleanup and Strict Mode's extra development setup/cleanup cycle. |
| M02 | Hiding a component is equated with unmounting. | In this sample, conditional removal unmounts Timer. Visual hiding or a navigation blur does not necessarily unmount a component. |
| M02 | AppState changes are observed but do not pause the timer. | Label background pause as a desired extension, not demonstrated behavior. The sample only stops the interval on unmount. |
| M02 | onDestroy is loosely equated with cleanup when the system closes the app. | OS termination does not guarantee JavaScript cleanup. Remove any promised cleanup-on-kill behavior. Keep Android comparisons short and explicitly approximate. |
| M02 | Metro terminal logs are promised in instructions and quiz item 8. | Direct students to the React Native DevTools Console; describe terminal forwarding as environment-dependent. Update item 8 and its answer together. |
| M02 | The code uses an interval as a seconds counter. | Explain that callback timing may be delayed or suspended; it is not an accurate elapsed-time clock. |
| M02 | A whole-app lifecycle demo cannot be certified by a browser or successful bundle. | Verify foreground/background behavior on an actual supported native device before teaching it as observed. |
| M03 | The sample is input validation, not authentication, and already says so. | Keep that distinction. secureTextEntry obscures the display; it does not authenticate or encrypt the password. |
| M03 | A spaces-only password passes password === "". | State the exact validation rule. Do not silently trim real passwords. Add an edge-case trace showing this behavior if retained. |
| M03 | “All text must be inside Text” is overly broad. | Say raw rendered text nodes must be inside Text; props such as Button.title and TextInput.placeholder accept strings. |
| M01–M03 | M02/M03 depend on the M01 folder, and none supplies all three requested delivery modes. | In the later authoring batch, add fresh-project setup, prepared offline instructions, pre-class fallback and an equal-point written alternative. |
| M00–M03 | Core JS variables/conditions/loops/functions refresher is no longer fully represented. | Keep a compact refresher in the first hands-on meeting or its prepared reference, using the existing baon trace. Do not add coding to M00. |

## Version and execution record

Node observed: v24.18.1. npm observed: 11.16.0. Fresh create-expo-app resolved blank-typescript@sdk-58, with manifest expo ~58.0.23, react 19.3.0, react-native 0.88.1 and TypeScript ~6.0.3. This differs from the existing course project's TypeScript ~5.9.3. All three submitted App.tsx samples passed tsc --noEmit (exit 0). Each started a local Expo Metro server with --offline and successfully returned an Android development bundle containing its expected sample text. See validation.json and per-module typecheck/Metro logs. The runner invokes the installed Expo and TypeScript CLIs directly through Node, equivalent to the local binaries resolved by npx expo start and npx tsc --noEmit, without another package download. M00 has no executable sample.

A successful Metro bundle confirms transformation and module resolution, not a rendered native UI, reliable Fast Refresh, keyboard behavior, screen-reader support or lifecycle transitions. iOS Simulator cannot run on this Windows host. adb devices -l returned an empty device list. No Android native UI test could be performed. A physically disconnected-network test was not performed: --offline local bundling alone does not prove the classroom phone route. Web dependencies are absent from the fresh blank template, so browser execution was not tested. These are explicit outstanding Task 1 checks. The package installation reported five moderate dependency advisories; no automatic force-upgrade was applied.

## Task 2: overlap table — approval required before changes

| Existing module | What it covers | Overlap with proposed M00–M03 | Recommended action |
|---|---|---|---|
| Old M01: Expo ecosystem and refresher | Tool roles, first screen, variables/conditionals/loop/function baon trace | New M00 ecosystem and new M01 tools/setup | **Merge/trim:** move definitions to M00 and practical setup to new M01; retain the short JS refresher as first-hands-on supporting material. |
| Old M02: Components, props and state | Typed props, reusable Cards, independent counters, functional state updates | New M02 components/state and new M03 controlled state | **Trim/keep:** preserve props, reusable components, functional updates and state ownership in a focused follow-on lesson; omit repeated introductory View/Text definitions. |
| Old M03: Layout, assets and accessibility | Responsive width, dark mode, spacing, assets and accessibility | New M03 basic Flexbox and labels | **Trim/move:** retain responsive layout, assets and deeper accessibility after the basic form; merge its essential practice with the follow-on components lesson if keeping later IDs. |
| Old M04: Interaction, forms and lifecycle | Controlled fields, trimming, message timeout, effect dependencies/cleanup | New M02 lifecycle and new M03 forms | **Merge:** fold the essential parts into those two references; keep the message-dependent timeout as an optional worked comparison. Do not retain another full introductory forms lesson. |
| Old M05: Navigation and structure | Router layouts, stacks, dynamic IDs, back behavior and invalid routes | Only general screen terminology in new M02 | **Keep:** teach after the new opener with explicit Router dependencies/file layout and an offline screen-switch simulation. A navigation screen is not automatically an Android Activity. |

### Recommended sequence for review

New M00 introduction (quiz), M01 setup/refresher (coding), M02 lifecycle (quiz), M03 basic form/layout (coding), M04 reusable components/props plus a tightly scoped responsive-accessible screen (quiz), M05 navigation (coding). Old M04 is absorbed; old M02/M03 contribute only the follow-on material. M06 onward keep their IDs provisionally, pending the requested five-module authoring batches.

This creates **22 numbered lessons, M00–M21**, not 21. Do not hide that increase. M00 can be an opening/orientation meeting if the schedule allows; retaining exactly 21 requires a separately approved later merge. Assessment parity becomes even numbers = quiz and odd numbers = coding, with M20's 20-question/2-essay finals exception and M21's project brief preserved unless the instructor changes them. Existing M06–M19 assessments therefore need explicit conversion after approval; copying their old parity would break the new sequence.

## Offline delivery plan to validate before class

- Prepare Node, VS Code, a compatible native client and a starter with dependencies installed while online. Copy a clean starter by USB; keep student work separate. Web requires checking/installing its extra platform dependencies beforehand.
- Five-minute smoke test: check node -v; start the copied project with npx expo start --offline; open the chosen client; change one text label; exercise one input and one invalid case. Record the client/OS/SDK and result. Inspect M02 logs in DevTools and demonstrate hide/show separately from background/foreground.
- Phone over local Wi-Fi: no internet is needed for the bundle path, but the network must allow device-to-PC traffic and the native client must be compatible. Not certified until tested on that classroom network.
- Emulator: prepare its system image and Expo-compatible app in advance. Do not count first-time emulator downloads as offline work.
- iOS Simulator: requires an appropriate macOS/Xcode host; unavailable here.
- Web: a browser run can check form/state basics but cannot substitute for native AppState, keyboard or permission behavior.
- No runnable setup: use a 150–250 word explanation or a paper trace with the same 10-point 4/2/2/2 rubric, adapted to correct trace, edge case, reasoning and reproducibility. Final exact prompts belong to the approved batch.

## Official sources inspected

- [Expo project creation](https://docs.expo.dev/get-started/create-a-project/) — retrieved transition text conflicts with the submitted note; do not treat cached text as a tested installed version.
- [Expo CLI](https://docs.expo.dev/more/expo-cli/) — --offline, local networking and tunnel requirements.
- [Expo debugging tools](https://docs.expo.dev/debugging/tools/) — React Native DevTools Console.
- [React useEffect](https://react.dev/reference/react/useEffect) — effect timing, cleanup and development checks.
- [React Native AppState](https://reactnative.dev/docs/appstate) — native states and device-specific behavior.
- [React Native text input](https://reactnative.dev/docs/handling-text-input) — controlled input.
- [React Native Flexbox](https://reactnative.dev/docs/flexbox) — defaults and layout axes.

The version-only reviewed copy is ADET_M01_reviewed-version.md. Its version note was corrected explicitly; other proposed corrections remain in this report pending the requested review. No active module has been changed.

Next action after review: approve or revise the overlap decisions and total count, then author the first batch of five. The submitted prompt is the source of this approval stop; it is not an extra approval rule invented for the task.
