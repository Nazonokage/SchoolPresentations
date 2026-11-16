from update_opener import base, save
import re, json

save('examples/M05/router-extension/app/_layout.tsx', '''import { Stack } from "expo-router";

export default function RootLayout() {
  return <Stack />; // Each route renders inside this navigator.
}''')
save('examples/M05/router-extension/app/index.tsx', '''import { View, Button } from "react-native";
import { Stack, router } from "expo-router";

export default function HomeScreen() {
  return (
    <View style={{ flex: 1, padding: 24, gap: 16 }}>
      <Stack.Screen options={{ title: "Campus offices" }} />
      <Button title="Visit library" onPress={() => router.push("/office/library")} />
      <Button title="Try unknown office" onPress={() => router.push("/office/unknown")} />
    </View>
  );
}''')
save('examples/M05/router-extension/app/office/[id].tsx', '''import { View, Text, Button } from "react-native";
import { Stack, router, useLocalSearchParams } from "expo-router";

const offices: Record<string, { title: string; hours: string }> = {
  library: { title: "Library", hours: "Open 8 AM" },
};

export default function OfficeScreen() {
  const parameters = useLocalSearchParams<{ id?: string | string[] }>();
  // Normalize, then check existence. Types alone do not validate an incoming URL.
  const officeId = Array.isArray(parameters.id) ? parameters.id[0] : parameters.id;
  const office = officeId && Object.hasOwn(offices, officeId) ? offices[officeId] : undefined;
  return (
    <View style={{ flex: 1, padding: 24, gap: 16 }}>
      <Stack.Screen options={{ title: office?.title ?? "Missing office" }} />
      <Text>{office ? `${office.title} — ${office.hours}` : "Office not found"}</Text>
      <Button title={router.canGoBack() ? "Back" : "Home"}
        onPress={() => router.canGoBack() ? router.back() : router.replace("/")} />
    </View>
  );
}''')
save('examples/M05/router-extension/README.md', '''# M05 optional Router extension — separate project

This is the real Router version. The sibling App.tsx is a template-only navigation simulation. Never place this app/ directory inside the core offline starter; use a separate student project.

## Install first (online, before class)

```powershell
npx create-expo-app@latest ADET-M05-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M05-LASTNAME
npx expo install expo-router react-native-safe-area-context react-native-screens expo-linking expo-constants expo-status-bar
```

Use the SDK 58 course baseline and TypeScript 6.0.3. The install command selects SDK-compatible native packages; save this separate project's lockfile. All six dependencies are intentional: Router, safe area, screens, linking, Expo constants, and status bar. No new package is required by the offline simulation.

## Configure and copy

1. Copy the complete app/ folder beside package.json. Use app/ only, not a competing src/app/ tree.
2. Change only the main field in package.json to `"main": "expo-router/entry"`. Keep dependencies and scripts.
3. Merge these fields into the existing expo object in app.json; preserve its existing name, slug, icons and other settings:

```json
{
  "scheme": "adetlab",
  "plugins": ["expo-router"]
}
```

If a plugins array already exists, append expo-router once. No permission prompt is needed for in-app navigation. The custom scheme takes effect in a native build containing that configuration; Expo Go does not become an installed adetlab app. Typed-route generation is optional and is not enabled in this beginner checkpoint.

4. Use this complete tsconfig.json to include all route files:

```json
{
  "extends": "expo/tsconfig.base",
  "compilerOptions": { "strict": true },
  "include": ["**/*.ts", "**/*.tsx", ".expo/types/**/*.ts", "expo-env.d.ts"]
}
```

5. Keep the template's Expo Babel defaults; no custom Babel file is needed here. App.tsx and index.ts are no longer the entry, so leave them unused or omit them from this separate project.
6. Run `npx tsc --noEmit`, then `npx expo start --clear`. In-app navigation supports compatible Expo Go. Custom installed URL-scheme tests need a prepared development build; no such device test has been completed.

## Files and trace

- app/_layout.tsx supplies Stack.
- app/index.tsx supplies Home and two push actions.
- app/office/[id].tsx reads and checks the ID before rendering the record.

Predict before running: library → known record → Library — Open 8 AM. unknown → no own record → Office not found. Back returns to Home when history exists. On a direct entry with no history, Home replaces the destination. Checking Object.hasOwn also prevents inherited object properties such as constructor from being mistaken for records.

Add clinic to offices and a push button on Home as ungraded practice. Test known, unknown and no-history cases. Expo Go external links and a standalone custom scheme have different URL forms; do not infer native linking success from a bundle test.

## Troubleshooting

Old screen: inspect main. Unmatched route: inspect app/office/[id].tsx exactly. Missing package: complete online setup before class. Native mismatch: inspect the installed client's SDK instead of changing the lab starter blindly.

[Official manual installation](https://docs.expo.dev/router/installation/). Refer to the [stop-2 validation record](../../../instructor/stop2-2026-11-07/VALIDATION.md) for measured results.
''')

# Retain old route source for history only, outside the active example tree.
old_route = base / 'examples/M05/[id].tsx'
if old_route.exists():
    save('examples/M05/[id].tsx', '// Historical import location; use router-extension/app/office/[id].tsx in the separate Router project.\nexport { default } from "./router-extension/app/office/[id]";')

keys = '''# M00–M05 instructor keys and coding criteria

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
'''
save('instructor/OPENER_ANSWER_KEY.md',keys)

index = (base / 'modules/README.md').read_text(encoding='utf-8')
rows = [line for line in index.splitlines() if line.startswith('|') and re.search(r'\[M(?:0[6-9]|1\d|2[01]) ',line)]
newrows = [
'| Prelim | [M00 · What is app development?](ADET_M00.md) | 10-item quiz |',
'| Prelim | [M01 · React Native platform, tools and first app](ADET_M01.md) | Individual coding activity |',
'| Prelim | [M02 · Screens, components and lifecycle](ADET_M02.md) | 10-item quiz |',
'| Prelim | [M03 · Layout and a login form](ADET_M03.md) | Individual coding activity |',
'| Prelim | [M04 · Reusable components and accessible screen](ADET_M04.md) | Individual coding activity |',
'| Prelim | [M05 · Navigation and application structure](ADET_M05.md) | 10-item quiz |']
save('modules/README.md', '''# ADET — 22 lessons, M00–M21

M00–M05 are rewritten in the approved opener style. M06–M21 retain their existing topics and assessments and await the next authoring batches after stop-2 review. This is an explicit migration status, not a claim that all lessons are updated.

[Prepared starter](../offline-lab/README.md) · [Examples](../examples/README.md) · [Teaching guide](../instructor/TEACHING_GUIDE.md)

Periods are flexible planning groups, not promised class dates. Reserve separate summative and periodical exam meetings. M03 and M04 are intentionally both coding. M20 remains 20 questions plus two essays; M21 remains the solo mini-capstone. If finals has only two teaching meetings, schedule M19 earlier and preserve M20/M21.

| Period | Lesson | Classroom evidence |
|---|---|---|
'''+'\n'.join(newrows+rows))

root = (base/'README.md').read_text(encoding='utf-8')
start = root.index('## Teaching scope:')
save('README.md', '''# Application Development and Emerging Technologies

**22 lessons, M00–M21.** The approved opener M00–M05 is updated. M06–M21 remain pending the stop-2 review and subsequent batches; their topics and assessment types are preserved.

[All 22 lessons and evidence types](modules/README.md) · [Offline starter](offline-lab/README.md) · [Examples](examples/README.md) · [Instructor guide](instructor/TEACHING_GUIDE.md) · [Opener change log](instructor/stop2-2026-11-07/CHANGELOG.md)

'''+ '\n'.join(['| Lesson | Evidence |','|---|---|']+[f'| M{n:02} | '+('20-item quiz + two essays' if n==20 else 'Solo mini-capstone' if n==21 else 'Individual coding activity' if n in [1,3,4,6,8,10,12,14,16,18] else '10-item quiz')+' |' for n in range(22)])+'''

Use flexible period allocation for two 60–90-minute meetings weekly; reserve summative and periodical slots separately. No timetable dates are assumed. M20 and M21 are the final preparation/solo-project sequence. Current package baseline is SDK 58 and TypeScript 6.0.3; a prepared lockfile is provided. Physical-device/network validation remains outstanding.

Backend choices remain MongoDB through a Node API or MySQL/MariaDB through FastAPI using XAMPP/WampServer for the database. Core offline examples use template packages; later API/package lessons will gain mock-data alternatives during their batches.

[Research hub](adet%20research%20folder%20JS/README.md) · [Historical compiled contents](ADET_compiled%20contents.md). Imported reports and older outlines are research history; the module index above controls the approved count and assessment types.

'''+root[start:])

save('examples/README.md', '''# ADET runnable examples

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
''')

selector = '''// Instructor-only convenience. This replaces mobile/App.tsx; save student work first.
import { copyFile, writeFile } from "node:fs/promises";
const id = process.argv[2]?.padStart(2, "0");
if (!id || !Array.from({ length: 20 }, (_, index) => String(index + 1).padStart(2, "0")).includes(id)) {
  throw Error("Use node select.mjs 01 through 20; M00/M21 are not executable checkpoints.");
}
const file = (relative) => new URL(relative, import.meta.url);
await copyFile(file(`M${id}/App.tsx`), file("mobile/App.tsx"));
if (id === "15") await copyFile(file("M15/tone.wav"), file("mobile/tone.wav"));
await writeFile(file("mobile/index.js"), 'import { registerRootComponent } from "expo"; import App from "./App"; registerRootComponent(App);\\n');
console.log(`Selected M${id} as App.tsx. Real M05 Router uses its separate extension. From mobile run npm start -- --clear.`);
'''
save('examples/select.mjs',selector)

guide = (base/'instructor/TEACHING_GUIDE.md').read_text(encoding='utf-8')
guide = guide.replace('Alternating assessments apply through M19.', 'Use the explicit evidence table in modules/README.md; M03 and M04 are both coding.')
guide = guide.replace('M01 begins with introductions and its quiz is diagnostic.', 'M00 introduces app development with a quiz; M01 is the first coding meeting.')
guide = guide.replace('Twenty prepared chapters', 'Twenty-two prepared lessons')
guide = guide.replace('1–5 |', '00–05 |')
guide = guide.replace("run M04's validated form and demonstrate M05's route using that form's destination", 'combine M03 form review with M04 component reuse and use M05 as a prepared navigation demonstration')
guide = guide.replace('For M20 require a clean launch, seed/configuration notes and a five-minute explanation.', 'M20 remains a 20-item quiz plus two essays; M21 carries the solo mini-capstone readiness requirements.')
save('instructor/TEACHING_GUIDE.md',guide+'''

## Approved opener delivery — November 7, 2026

Use [OPENER_ANSWER_KEY.md](OPENER_ANSWER_KEY.md) for M00–M05. It supersedes old opening keys. M06–M21 keys remain in ANSWER_KEY.md until those batches are rewritten. Every coding module offers one graded activity in three equal-point modes; never grade all three. Copying the sample is guided practice.

Before class: verify Node/npm, student folder copies, installed dependencies, compatible native client, and the [five-minute smoke test](../offline-lab/SMOKE-TEST.md). The measured checks establish local compilation/bundling only. If no real display route works, use the written trace with its equivalent rubric. No new native package is needed in the opener core.

At the end of the preceding meeting, announce the next coding activity's laptop setup. Reuse its Before next meeting block on the LAST slide, with the actual date supplied by the teacher. M00 announces M01; M02 announces M03; M03 also announces M04. Students prepare their OWN laptop before class and bring it to do the activity. A module also carries its own reusable preparation block for the teacher to send earlier. M05's quiz needs no coding delivery modes.

The separate Router extension is optional online preparation. Core examples all use App.tsx. Do not run the old authoring generators over the rewritten lessons. The current opener generation sources are update_opener.py and opener_support.py; manual refinements and validation results must be preserved.
''')
oldkeys = (base/'instructor/ANSWER_KEY.md').read_text(encoding='utf-8')
later = oldkeys.index('## M06 ')
save('instructor/ANSWER_KEY.md', '# Instructor answer keys\n\nM00–M05: use [OPENER_ANSWER_KEY.md](OPENER_ANSWER_KEY.md). The following M06–M21 keys retain their existing assessments pending the later batches.\n\n'+oldkeys[later:])
print('Updated Router extension, keys, indexes, selector and teaching guidance.')
