from pathlib import Path
import re, shutil, json

base = Path(__file__).resolve().parents[2]
backup = base / 'instructor/stop2-2026-11-07/before'
backup.mkdir(parents=True, exist_ok=True)
def save(relative, text):
    path = base / relative
    if path.exists():
        original = backup / relative
        if not original.exists():
            original.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, original)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + '\n', encoding='utf-8')

setup = '''**Install first.** Core imports come from `react` and `react-native`, already in the prepared blank TypeScript template. No additional package, permission or config plugin is required. Use SDK 58 / TypeScript 6.0.3 and the distributed lockfile. Compatible Expo Go is sufficient for these core APIs, but actual phone/network testing remains pending.

**Fresh project (online preparation only):**

```powershell
npx create-expo-app@latest ADET-M{number}-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M{number}-LASTNAME
```

**Run it.** Copy this lesson's complete `App.tsx` into your own prepared project. Run `npx tsc --noEmit`, then `npx expo start --offline` for the prepared lab, or `npx expo start` during online preparation. Metro transpiles; it does not type-check. The local bundle has been checked separately from actual device operation. Use the [five-minute smoke test](../offline-lab/SMOKE-TEST.md) before class. No web-preview packages are assumed.
'''

def announcement(number):
    return f'''### Before next meeting — laptop preparation announcement

For the upcoming **M{number} coding meeting**, prepare **your own laptop**, then bring it and do the activity in class. The instructor confirms the date and naming pattern; `ADET-M{number}-LASTNAME` is the recommended folder/repository name.

```powershell
npx create-expo-app@latest ADET-M{number}-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M{number}-LASTNAME
npx tsc --noEmit
npx expo start
```

No extra packages are needed for this core activity. Use the distributed manifest and lockfile for exact versions. Open the app once before class; bring a screenshot or the exact error. Without home internet, prepare on campus Wi-Fi, mobile data or an agreed hotspot, or copy the [prepared starter and dependencies by USB](../offline-lab/README.md). Internet preparation is not the graded activity. Put this announcement on the **last presentation slide of the previous meeting**; the teacher supplies the real meeting date.
'''

def modes(number, prompt):
    return f'''### Three equal-point delivery modes

**Mode 1 — Offline computer lab.** Before class, PCs need Node 24.18.1, npm 11.16.0, VS Code and a separate copy of the prepared starter including node_modules. Use `START-LAB.cmd`; replace only the student's App.tsx. No new installs in class. Local type-checking and Android bundling passed; a reachable phone on local Wi-Fi with compatible Expo Go or a prepared emulator still needs a successful [smoke test](../offline-lab/SMOKE-TEST.md). If no native display route passes, use Mode 3, not an untested promise of offline phone access. `--tunnel` is an online fallback only.

**Mode 2 — Prepared personal laptop.** Follow the announcement below before class; bring your laptop and run the same activity during the next scheduled coding meeting. Submit source, package.json, lockfile, README with commands and the actual activity date, success/failure evidence and a brief explanation. Recommended repository: `ADET-M{number}-LASTNAME` (instructor confirms the pattern). Do not upload node_modules, cache or secrets.

**Mode 3 — Written alternative (10 points).** {prompt} Submit a step-by-step table plus a 150–250-word explanation. This earns the same maximum as the coding activity; no device screenshot is required.

| Written evidence | Points |
|---|---:|
| Correct complete trace and proposed independent change | 4 |
| Edge/failure case and justified correction | 2 |
| Explanation connecting code to visible behavior | 2 |
| Labeled inputs, ordered steps and readable evidence | 2 |

Guided copying and predictions are ungraded. Only the one selected assessment mode is graded.
'''

docs = {}
for number in range(4):
    docs[number] = (base / f'instructor/stop1-2026-11-06/reviewed-opening/ADET_M{number:02}.md').read_text(encoding='utf-8')
    docs[number] = re.sub(r'\*\*Answer key \(instructor\)\.\*\*[^\n]*\n', '', docs[number])

docs[0] = docs[0].replace('Hermes is the JavaScript engine, not an AI tool.', 'Hermes is the JavaScript engine.')
docs[0] = docs[0].replace('gamit ang iisang plano.', 'gamit ang magkaparehong pangunahing plano, pero inaangkop ang ilang bahagi sa bawat lote.')
docs[0] = docs[0].replace('### Common mistakes', '''### Worked decision trace

**Predict first:** If a campus queue app shows tickets correctly but loses them after closing, is drawing a nicer icon enough?

1. Requirement: students need to keep their ticket number after reopening.
2. Design: show the current ticket and its status.
3. Build: implement the screen and a suitable saved-data mechanism.
4. Test: close and reopen; compare with the required behavior.
5. Result: losing the ticket fails the requirement, even if the screen looks attractive.
6. Maintain: repair the data behavior and retest before another release.

**Misconception:** sharing source guarantees identical behavior on every device. Shared code reduces duplication; each platform still needs testing. An SDK supplies development tools; Expo Go is a development host, not the finished store release. Skipping those distinctions leads to testing the wrong artifact.

### Common mistakes''')

docs[1] = docs[1].replace('change one line and add one package.', 'change a calculation and explain its result.')
docs[1] = docs[1].replace('4. Add a package safely.', '4. Trace variables, conditions, loops and a function using a baon calculation.')
docs[1] = docs[1].replace('**Fast Refresh** updates the phone without a restart.', '**Fast Refresh** usually updates the development screen; some edits trigger a remount or reload.')
docs[1] = docs[1].replace('the phone updates without a restart.', 'Fast Refresh normally updates the development screen.')
docs[1] = docs[1].replace('const name = "Ana"', 'const name = "Virel"')
start = docs[1].index('### Packages this course uses')
end = docs[1].index('### Common mistakes', start)
docs[1] = docs[1][:start] + '''### Read the baon program before typing

| Concept | What / why | How this example works | What goes wrong |
|---|---|---|---|
| `const` / `let` | Name values; use let when reassignment is needed | prices stays assigned to one array; remaining changes | Reassigning a const is invalid; const does not freeze an array |
| Function | Reuse a calculation with an input and result | calculateBalance receives budget and returns remaining | Forgetting return gives undefined instead of a balance |
| Loop | Apply a step to each item | Subtract each price once | Subtracting the total again double-counts spending |
| Condition | Select one result | balance >= 0 chooses Change; otherwise Kulang | Using > would classify a zero balance incorrectly |
| Type annotation | Check a value's expected type separately | budget: number rejects a string during tsc checking | Metro may still transpile code containing type errors |

**Misconception:** TypeScript validates every real-world input at runtime. Its types help check source code; actual external data still needs validation.

''' + docs[1][end:]
docs[1] = docs[1].replace('2. Add a second `Text` line with today\'s date using `new Date().toDateString()`.', '2. Change the budget to 80 and add a third price of 15. Show the resulting balance and explain each subtraction. Also test a budget equal to total spending.')
docs[1] = docs[1].replace('**Expected behavior.** The phone shows "Hello, ADET!".', '**Expected behavior.** The phone shows "Hello, ADET!" and "Kulang: PHP 10".')

docs[2] = docs[2].replace('const name = "Ana"', 'const name = "Virel"')
docs[2] = docs[2].replace('`(n) => n + 1`', '`(current) => current + 1`')
docs[2] = docs[2].replace('// A component that counts seconds while it is on screen', '// Count delivered interval callbacks, not precise elapsed time.')
docs[2] = docs[2].replace('// Add one second every 1000 ms', '// Request a callback roughly every 1000 ms; the OS can delay it.')
docs[2] = docs[2].replace('When you leave the screen, the timer must stop.', 'When this screen component is actually removed, its timer must be cleaned up.')
docs[2] = docs[2].replace('B. After the component first appears', 'B. After its initial commit (with possible development checks)')
docs[2] = docs[2].replace('**Independent change.** Add a "Pause" button inside `Timer` that stops counting without hiding it. Explain the difference between hiding and pausing.', '**Independent ungraded change.** Change the button labels to "Remove timer" and "Mount timer" so they describe the conditional removal precisely. Predict the counter after removing and adding it again. Optional extension: implement pause with separate state; changing AppState text alone does not pause it.')
docs[2] = docs[2].replace('### Common mistakes', '''### Why state and effects are separate

State is remembered data for a mounted component. A setter requests a new render so the displayed value can change; changing an ordinary local variable does not request that render. An effect connects to something outside rendering, such as a timer or system subscription. Its cleanup releases that resource. Starting an interval directly in the component body creates another interval on each render.

**Predict first:** The displayed count is 3. Remove Timer, then mount it again. Will it show 3 or 0?

| Step | React tree | Timer state / resource |
|---|---|---|
| Initial commit | Timer present | 0; interval installed |
| Three delivered ticks | Same Timer | 3; updater uses previous state |
| visible becomes false | Timer removed | Cleanup clears interval; local state discarded |
| visible becomes true | New Timer instance | 0; new interval installed |

The expected new value is 0. Merely hiding pixels or changing navigation focus need not remove the component. A dependency list controls when an effect resynchronizes; changed dependencies run old cleanup before new setup. Development Strict Mode may also probe setup/cleanup. This does not mean the OS promises a final cleanup when it terminates the process.

### Common mistakes''')

docs[3] = docs[3].replace('secureTextEntry={!show}', 'secureTextEntry={!showPassword}')
docs[3] = docs[3].replace('### Common mistakes', '''### Trace a controlled field

**Predict first:** If value is username but onChangeText only logs text, will the state remember what you typed?

The input reports the new string → setUsername stores that string → React renders → value supplies the stored string to TextInput. Logging alone omits the state update. A press callback reads the state and sets the feedback message; passing the function lets React call it later, while calling it during render runs it too early.

| Concept | Purpose and mechanism | Failure to investigate |
|---|---|---|
| Flexbox axes | column is the default; justifyContent follows the main axis, alignItems crosses it | Changing to row changes what each alignment means |
| StyleSheet | Names reusable style objects | A typo in a style property is not a new layout feature |
| Controlled input | value and setter keep visible text and data connected | Updating a different field's setter displays the wrong data |
| Validation and early return | Reject an invalid combination before the success message | Without return, the success message can replace the error |
| Accessible label | Gives an input an understandable name | A placeholder disappears while typing; it is not a persistent visible label |

**Misconception:** obscuring password characters signs a person in securely. This screen only demonstrates local validation, never checks a real account, and must use invented credentials.

### Common mistakes''')
docs[3] = docs[3].replace('*Keyboard covers the fields:* acceptable for this lesson; keyboard handling comes later.', '*Keyboard covers the fields:* dismiss it to inspect feedback; record this layout limitation. M04 introduces a scrollable screen. Do not claim this minimal form is production-ready.')

code4 = '''import { useState } from "react";
import { View, Text, Button, ScrollView, StyleSheet, useWindowDimensions } from "react-native";

type OfficeCardProps = { title: string; hours: string; capacity: number };

function OfficeCard({ title, hours, capacity }: OfficeCardProps) {
  const [visitors, setVisitors] = useState(0); // Each card owns separate state.
  const isFull = visitors >= capacity;
  return (
    <View style={styles.card}>
      <Text accessibilityRole="header" style={styles.heading}>{title}</Text>
      <Text style={styles.body}>{hours}</Text>
      <Text style={styles.body}>Visitors: {visitors} / {capacity}</Text>
      <Text style={styles.body}>{isFull ? "Full — please wait" : "Space available"}</Text>
      <Button title={`Join ${title}`} accessibilityLabel={`Join ${title} queue`}
        disabled={isFull}
        onPress={() => setVisitors((current) => Math.min(current + 1, capacity))} />
      <Button title={`Reset ${title}`} onPress={() => setVisitors(0)} />
    </View>
  );
}

export default function App() {
  const { width, fontScale } = useWindowDimensions();
  // Larger text gets a column even on a wider window.
  const useColumns = width >= 700 && fontScale <= 1.3;
  return (
    <ScrollView contentContainerStyle={styles.page}>
      <Text accessibilityRole="header" style={styles.heading}>Campus offices</Text>
      <Text style={styles.body}>Choose a queue. Full queues show a written reason.</Text>
      <View style={[styles.cards, { flexDirection: useColumns ? "row" : "column" }]}>
        <OfficeCard title="Library" hours="Open 8 AM" capacity={2} />
        <OfficeCard title="Clinic" hours="Open 9 AM" capacity={3} />
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  page: { flexGrow: 1, padding: 24, paddingTop: 60, paddingBottom: 48, gap: 16, backgroundColor: "#f1f5f9" },
  cards: { gap: 16 },
  card: { flex: 1, padding: 16, gap: 12, backgroundColor: "#ffffff", borderWidth: 1, borderColor: "#475569", borderRadius: 12 },
  heading: { color: "#0f172a", fontSize: 24, fontWeight: "bold" },
  body: { color: "#0f172a", fontSize: 18 },
});'''
code5 = '''import { useState } from "react";
import { View, Text, Button } from "react-native";

export default function App() {
  // A teaching model of a stack; this is NOT Expo Router.
  const [routes, setRoutes] = useState<string[]>(["home"]);
  const currentRoute = routes[routes.length - 1];
  const officeName = currentRoute === "library" ? "Library — Open 8 AM" : "Office not found";
  function pushOffice(id: string) {
    setRoutes((currentRoutes) => [...currentRoutes, id]);
  }
  function goBack() {
    // Keep the home route when there is no previous screen.
    setRoutes((currentRoutes) => currentRoutes.length > 1 ? currentRoutes.slice(0, -1) : currentRoutes);
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 16 }}>
      <Text>Navigation paper-model companion</Text>
      <Text>Stack: {routes.join(" → ")}</Text>
      {currentRoute === "home" ? (
        <View style={{ gap: 12 }}>
          <Button title="Visit library" onPress={() => pushOffice("library")} />
          <Button title="Try unknown office" onPress={() => pushOffice("unknown")} />
        </View>
      ) : <Text>{officeName}</Text>}
      <Button title="Back" disabled={routes.length === 1} onPress={goBack} />
    </View>
  );
}'''

docs[4] = '''# ADET M04 · Reusable components, props and one accessible screen

[Module index](README.md) · Prelim · 60–90 minutes · Individual coding activity

## A. Lesson Preview & Review

**If two office cards look alike, must we write the same screen twice?** Recall M03: state stores input; layout arranges it. Today we reuse one component with different data.

**Learning targets:** distinguish props from state, define a typed component contract, trace independent component instances, and adapt one screen to window size and larger text.

**Trace:** Parent supplies props → each card renders → a press changes that card's state → width/font scale selects the layout.

## B. Detailed Main Lesson

### In plain words

A reusable component is a small screen-building function used more than once. Props are its incoming settings. State is the changing information it remembers. Two OfficeCard instances share a function definition but do not automatically share their visitor counts.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| Typed props | OfficeCardProps requires title, hours and numeric capacity | Passing a string capacity fails the separate TypeScript check |
| Read-only inputs | A parent chooses each card's configuration | Mutating a prop is not a supported way to update parent state |
| Local state | Each mounted card remembers its own visitors | Expecting Library presses to update Clinic gives the wrong model |
| Functional updater | Calculates the next count from the previous count | Reading an old value in repeated updates can lose changes |
| Responsive layout | useWindowDimensions updates width and fontScale; our rule selects row or column | A fixed row can squeeze long labels and larger text |
| Accessible feedback | Text names status; labeled buttons describe actions | Color alone excludes users who cannot distinguish it |

```text
App
 ├─ Library props (capacity 2) → OfficeCard state: visitors 0
 └─ Clinic props  (capacity 3) → OfficeCard state: visitors 0
window width / fontScale → row or column for BOTH cards
```

**Predict first:** Press Join Library twice. What happens to Clinic? What happens on a third Library press?

| Step | Library | Clinic | Reason |
|---|---:|---:|---|
| Initial | 0 | 0 | Two independent instances |
| First Library press | 1 | 0 | Only its setter runs |
| Second Library press | 2 | 0 | At capacity; button disabled, Full text visible |
| Third attempted press | 2 | 0 | Disabled action; Math.min also bounds the update |
| Reset Library | 0 | 0 | Library's own state resets |

At width 390, fontScale 1: column. At width 800, fontScale 1: row. At width 800, fontScale 1.5: column. This is our explicit design rule, not a React Native default. Text scales naturally and cards have no fixed height; scrolling allows extra content. A screen-reader label helps, but actual TalkBack/VoiceOver and larger-text tests are still necessary.

**Misconception:** declaring a TypeScript type validates database values at runtime. It checks our source; later API modules must also validate incoming data.

### Common mistakes

- Copying whole card implementations instead of passing different props.
- Using one shared count accidentally when each card needs independent state.
- Preventing font scaling to make a cramped layout appear to fit.

## C. Analogy, Guided Program & Practice

**Analogy.** Parang dalawang queue counter na pareho ang disenyo: props ang pangalan at limit, state ang kasalukuyang bilang. Kapag may pumila sa Library, hindi nadaragdagan ang Clinic.

**Use case:** one campus screen shows two offices with their own queue limits. This is an in-memory demonstration, not a real shared queue service.

SETUP

**App.tsx — complete checkpoint** · [Copyable file](../examples/M04/App.tsx)

```tsx
CODE
```

**Breakdown.** The type describes the three incoming settings. OfficeCard owns visitors. isFull derives from the count; it is not a second stored value. App chooses row/column and supplies two different sets of props. StyleSheet names the repeated styles. ScrollView handles a screen taller than the window.

**Expected behavior:** Library fills at 2; Clinic remains independent and fills at 3. Reset affects only its own card. A smaller window or larger font changes the chosen arrangement. Device-specific behavior is a test expectation, not recorded hardware evidence.

**Ungraded practice:** predict the layout at width 699, then 700. Change Library hours and explain why a prop is appropriate. Restore the sample before assessment.

**Troubleshooting:** if both counts move, check where state lives; if text clips, remove fixed heights and test scrolling; if a prop error appears, compare its name/type with OfficeCardProps. A phone locked to portrait may not rotate; use a prepared resizable emulator or the paper width trace instead.

## D. Assessment, Wrap-Up & References

### One individual coding activity — 10 points

Add a Registrar card with capacity 4 using the same component. Add a Leave button inside OfficeCard that decreases only that card's count and never goes below zero. Give it a meaningful accessible label. Show one normal join/leave trace and an attempted leave at zero. Test a narrow layout and enlarged text where a native display is available; otherwise use the written alternative.

| Evidence | Points |
|---|---:|
| Reused card and working independent Leave change | 4 |
| Zero/capacity edge case and result | 2 |
| Explain props, state and layout rule | 2 |
| Reproducible commands and readable evidence | 2 |

MODES

**Wrap-up:** Explain why there is one OfficeCard function but three separate counts. Identify one accessibility issue that labels alone cannot solve.

[Props](https://react.dev/learn/passing-props-to-a-component) · [Window dimensions](https://reactnative.dev/docs/usewindowdimensions) · [Accessibility](https://reactnative.dev/docs/accessibility)

### Instructor notes

Use 5 minutes for review, 15 for explanation/trace, 10 for guided code, 25 for the assessment and 5 for wrap-up. The extra 30 minutes allow device and accessibility tests. Show the tree diagram before the code; place the width trace beside the layout explanation. M03 and M04 are intentionally both coding. No API, image CDN or new native package is required. Run the offline smoke test before students arrive; hardware and screen-reader results remain pending. Do not describe this teaching screen as certified accessible.
'''.replace('SETUP', setup.format(number='04')).replace('CODE', code4).replace('MODES', modes('04', 'Trace Library, Clinic and Registrar through two joins, one leave, and a leave at zero. Write the bounded decrement expression and justify the width/font-scale rule.'))

docs[5] = '''# ADET M05 · Navigation and application structure

[Module index](README.md) · Prelim · 60–90 minutes · 10-item quiz

## A. Lesson Preview & Review

**How can a Library button open the right screen and still let us go back?** M04 reused components; this lesson connects whole screens.

**Learning targets:** map files to routes, trace push/back, distinguish a stack from tabs, handle an invalid ID, and explain why a route guard is not authorization.

**Trace:** Home → push Library ID → read parameter → find office or show missing → Back.

## B. Detailed Main Lesson

### In plain words

Navigation decides which screen is shown and how the user returns. Expo Router connects paths to files. The offline core uses a tiny stack model to make the idea visible; that model is not Expo Router and does not provide deep links, native navigation or route persistence.

| Term | Why / how | Failure to watch |
|---|---|---|
| Route | A named destination such as /office/library | A path without a matching file cannot open its screen |
| Dynamic segment | [id].tsx reuses one screen for different office IDs | Unknown IDs must not silently become a valid office |
| Layout | _layout.tsx supplies a shared navigator | A route component alone does not configure the whole app |
| Stack | Push adds a destination; Back removes the top | Resetting to Home is different from returning to a previous screen |
| Tabs | Select peer sections such as Home and Settings | A tab switch need not destroy its previous screen |
| Deep link | An external URL opens a destination | Requiring an earlier click's object breaks a cold launch |
| Route guard | Redirects users to an appropriate screen | Hiding a screen does not secure data; the server authorizes requests |

```text
app/_layout.tsx            shared Stack
app/index.tsx             /
app/office/[id].tsx        /office/library or /office/unknown

Stack trace: [Home] → [Home, Library] → Back → [Home]
```

**Predict first:** A cold link supplies unknown as the ID. Should the screen show the Library anyway?

1. Read the ID as untrusted input, not proof that a record exists.
2. Normalize a possible array parameter to one string.
3. Look up the known ID. For unknown, display Office not found.
4. Offer Home when there is no previous route; Back only works when history exists.

**Misconception:** putting a full password/token in a route is convenient storage. URLs can be exposed in logs and shared links. Pass nonsecret identifiers; request protected data through an authorized API. A later shared-state lesson handles data used by multiple screens.

### Common mistakes

- Copying a Router route into App.tsx while leaving the blank entry unchanged.
- Using both app/ and src/app/ without knowing which tree is active.
- Assuming losing navigation focus always unmounts a screen.

## C. Analogy, Guided Program & Practice

**Analogy.** Parang room number ang route ID: isang direksiyon, hindi ang buong opisina. Ang history ay listahan ng dinaanan; kapag maling kuwarto ang number, malinaw na sabihin na hindi ito nahanap.

**Use case:** a campus directory opens office details by ID.

SETUP

### Core offline model — App.tsx

This complete program uses only template packages. Follow the printed stack, or run it on a prepared native client. [Copyable source](../examples/M05/App.tsx).

```tsx
CODE
```

**Breakdown:** routes is an array of destinations; spreading it appends an ID without changing the original array. slice removes its last entry. The conditional renders Home or a detail message. The guard preserves at least Home. This illustrates history; it intentionally does not imitate every Router behavior.

**Expected:** Visit library shows Library — Open 8 AM; Back restores Home. Try unknown office shows Office not found. Back is disabled at Home.

### Optional online extension — real Expo Router

Use a separate fresh `ADET-M05-LASTNAME` project created by the SDK-pinned command above. Do not alter the prepared offline starter. Install before class:

```powershell
npx expo install expo-router react-native-safe-area-context react-native-screens expo-linking expo-constants expo-status-bar
```

| Dependency | Role |
|---|---|
| expo-router | File routes and navigation API |
| react-native-safe-area-context | Native safe-area support |
| react-native-screens | Native screen primitives |
| expo-linking | URL/link integration |
| expo-constants | Expo runtime information used by the Router setup |
| expo-status-bar | Compatible status-bar package (also in the blank starter) |

Copy the **complete files** and follow [Router extension README](../examples/M05/router-extension/README.md). It explicitly changes package.json main to `expo-router/entry`, adds the expo-router plugin and scheme in app.json, and uses this one route tree:

```text
ADET-M05-LASTNAME/
  package.json         main: expo-router/entry
  app.json             plugins: expo-router; scheme: adetlab
  tsconfig.json        strict TypeScript; includes app/**/*.tsx
  app/
    _layout.tsx
    index.tsx
    office/[id].tsx
```

App.tsx is not the entry in this separate extension. Basic in-app Router navigation can use compatible Expo Go; no device permission is requested. Testing a custom installed scheme requires a development build that includes that native configuration. Expo Go's URL is not your app's permanent custom scheme. Real external link handling is revisited in M14. No browser packages or internet deployment are assumed.

**Ungraded modification:** add clinic with its own hours and a link. Predict the unknown case before running it. See the extension's file-by-file comments and parameter lookup trace.

**Troubleshooting:** unmatched route → inspect file name and active route tree; old App.tsx still shown → inspect main; unknown ID crashes → validate lookup and render a fallback; no Back history → offer Home. After a configuration change restart with `npx expo start --clear` while online; use the prepared offline flag only once dependencies are present.

## D. Assessment, Wrap-Up & References

### 10-item quiz — 1 point each

1. A route is: A. A destination path B. A password C. A database D. A font.
2. Which file supplies the shared navigator? A. package-lock.json B. app/_layout.tsx C. README.md D. assets/icon.png.
3. Which filename accepts changing office IDs? A. office.txt B. [id].tsx C. icon.png D. app.json.
4. A tab usually represents: A. A peer section B. A timer C. A password D. A compiler error.
5. A route guard replaces server authorization: A. Always B. Never; it controls navigation feedback C. Only offline D. Only on iOS.
6. Trace [Home], push Library, then Back. What remains?
7. The ID is unknown. What should the example display?
8. A screen loses focus. Must its component unmount? Explain briefly.
9. Can the template-only stack model open an external deep link? Explain.
10. A screen opens directly with no history. What safe navigation option does the example provide?

**Wrap-up:** Explain the difference between a component's state, the route's ID and the navigator's history. Identify where a parameter becomes a lookup result.

[Router installation](https://docs.expo.dev/router/installation/) · [Router notation](https://docs.expo.dev/router/basics/notation/) · [Navigation](https://docs.expo.dev/router/basics/navigation/)

### Instructor notes

Keep the quiz as the only graded evidence. Use 5 minutes review, 20 explanation/model trace, 15 demonstration, 15 quiz and 5 wrap-up. The real Router setup is optional prepared extension work for the additional 30 minutes, not an in-class download requirement. Show the route-tree diagram beside the matching files; keep the full setup in a handout. Device deep linking remains untested. Preserve core App.tsx and the extension's separate route tree; no selector should silently convert one into the other.
'''.replace('SETUP',setup.format(number='05')).replace('CODE',code5)

for number in [1,3]:
    prompt = ('Trace budgets 50, 60 and 80 with prices 25 and 35; then add price 15. Identify the loop, condition, function input/return and a type-error correction.' if number == 1 else 'Trace empty fields, a spaces-only username, a spaces-only password and a normal pair. Explain an early return, design the show-password state change, and identify a controlled-input wiring failure.')
    docs[number] = docs[number].replace('**Wrap-up.**', modes(f'{number:02}',prompt)+'\n**Wrap-up.**')

for number, text in docs.items():
    # Remove obsolete overlap instructions from references, retaining pedagogical notes.
    text = re.sub(r'^- Overlap check:.*\n', '', text, flags=re.M)
    text += '\n**Teaching evidence:** keys and grading guidance are in the separate instructor folder. Use the local flow diagram beside the matching code; no external image download is required. Record actual hardware outcomes rather than treating expected output as a measured device result.\n'
    if number in [0,1,2,3,4]:
        upcoming = {0:'01',1:'01',2:'03',3:'03',4:'04'}[number]
        # Coding modules carry their own reusable preparation block; preceding lessons announce the next activity.
        if number in [1,3,4]:
            text += '\n**Instructor scheduling note:** reuse the following preparation block at the end of the meeting BEFORE this coding activity. It is included here as the activity\'s setup handout.\n'
        text += '\n'+announcement(upcoming)
    if number == 3:
        text += '\n'+announcement('04')
    save(f'modules/ADET_M{number:02}.md',text)
    if number:
        code = re.search(r'```tsx\n(.*?)\n```',text,re.S).group(1)
        save(f'examples/M{number:02}/App.tsx',code)
        save(f'examples/M{number:02}/README.md',f'''# M{number:02} checkpoint

Use the [lesson](../../modules/ADET_M{number:02}.md). Copy App.tsx into your own [prepared blank starter](../../offline-lab/README.md). The core entry is index.ts → App.tsx; no extra packages. Run `npx tsc --noEmit`, then `npx expo start --offline` on the prepared environment. Native device/network verification is still required. Do not use instructor audit projects as a student starter.
''')
    else:
        save('examples/M00/README.md','''# M00 — paper activity only

No App.tsx, installation or coding is required. Use the [M00 lesson](../../modules/ADET_M00.md). Submit a six-step app-development plan, a platform choice with reasons and a role diagram. Predict what fails when a requirement is not tested. The separate quiz is graded; this discussion is ungraded.
''')

print('Authored M00–M05 and synchronized core examples; originals retained in stop2/before.')
