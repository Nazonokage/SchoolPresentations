# ADET M04 · Reusable components, props and one accessible screen

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

### Optional design comparison — assets and theme

An asset is a bundled file such as the starter's assets/icon.png. If you add Image from react-native, a local source such as `require("./assets/icon.png")` can work without an image server; the path is relative to App.tsx. Give it width/height and an accessibilityLabel when it conveys information. Decorative images should not create distracting duplicate announcements. No remote CDN is needed.

useColorScheme from react-native reports the preferred theme. A dark-theme extension chooses both foreground and background together, then checks contrast; changing only the background can hide text. Neither a theme hook nor a label automatically makes the whole screen accessible. These are optional ungraded design comparisons after the responsive core, not extra graded tasks.

### Common mistakes

- Copying whole card implementations instead of passing different props.
- Using one shared count accidentally when each card needs independent state.
- Preventing font scaling to make a cramped layout appear to fit.

## C. Analogy, Guided Program & Practice

**Analogy.** Parang dalawang queue counter na pareho ang disenyo: props ang pangalan at limit, state ang kasalukuyang bilang. Kapag may pumila sa Library, hindi nadaragdagan ang Clinic.

**Use case:** one campus screen shows two offices with their own queue limits. This is an in-memory demonstration, not a real shared queue service.

**Install first.** Core imports come from `react` and `react-native`, already in the prepared blank TypeScript template. No additional package, permission or config plugin is required. Use SDK 58 / TypeScript 6.0.3 and the distributed lockfile. Compatible Expo Go is sufficient for these core APIs, but actual phone/network testing remains pending.

**Fresh project (online preparation only):**

```powershell
npx create-expo-app@latest ADET-M04-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M04-LASTNAME
```

**Run it.** Copy this lesson's complete `App.tsx` into your own prepared project. Run `npx tsc --noEmit`, then `npx expo start --offline` for the prepared lab, or `npx expo start` during online preparation. Metro transpiles; it does not type-check. The local bundle has been checked separately from actual device operation. Use the [five-minute smoke test](../offline-lab/SMOKE-TEST.md) before class. No web-preview packages are assumed.


**App.tsx — complete checkpoint** · [Copyable file](../examples/M04/App.tsx)

```tsx
import { useState } from "react";
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
});
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

### Three equal-point delivery modes

**Mode 1 — Offline computer lab.** Before class, PCs need Node 24.18.1, npm 11.16.0, VS Code and a separate copy of the prepared starter including node_modules. Use `START-LAB.cmd`; replace only the student's App.tsx. No new installs in class. Local type-checking and Android bundling passed; a reachable phone on local Wi-Fi with compatible Expo Go or a prepared emulator still needs a successful [smoke test](../offline-lab/SMOKE-TEST.md). If no native display route passes, use Mode 3, not an untested promise of offline phone access. `--tunnel` is an online fallback only.

**Mode 2 — Prepared personal laptop.** Follow the announcement below before class; bring your laptop and run the same activity during the next scheduled coding meeting. Submit source, package.json, lockfile, README with commands and the actual activity date, success/failure evidence and a brief explanation. Recommended repository: `ADET-M04-LASTNAME` (instructor confirms the pattern). Do not upload node_modules, cache or secrets.

**Mode 3 — Written alternative (10 points).** Trace Library, Clinic and Registrar through two joins, one leave, and a leave at zero. Write the bounded decrement expression and justify the width/font-scale rule. Submit a step-by-step table plus a 150–250-word explanation. This earns the same maximum as the coding activity; no device screenshot is required.

| Written evidence | Points |
|---|---:|
| Correct complete trace and proposed independent change | 4 |
| Edge/failure case and justified correction | 2 |
| Explanation connecting code to visible behavior | 2 |
| Labeled inputs, ordered steps and readable evidence | 2 |

Guided copying and predictions are ungraded. Only the one selected assessment mode is graded.


**Wrap-up:** Explain why there is one OfficeCard function but three separate counts. Identify one accessibility issue that labels alone cannot solve.

[Props](https://react.dev/learn/passing-props-to-a-component) · [Window dimensions](https://reactnative.dev/docs/usewindowdimensions) · [Accessibility](https://reactnative.dev/docs/accessibility)

### Instructor notes

Use 5 minutes for review, 15 for explanation/trace, 10 for guided code, 25 for the assessment and 5 for wrap-up. The extra 30 minutes allow device and accessibility tests. Show the tree diagram before the code; place the width trace beside the layout explanation. M03 and M04 are intentionally both coding. No API, image CDN or new native package is required. Run the offline smoke test before students arrive; hardware and screen-reader results remain pending. Do not describe this teaching screen as certified accessible.


**Teaching evidence:** keys and grading guidance are in [the separate instructor key](../instructor/OPENER_ANSWER_KEY.md). Use the local flow diagram beside the matching code; no external image download is required. Record actual hardware outcomes rather than treating expected output as a measured device result.

**Instructor scheduling note:** reuse the following preparation block at the end of the meeting BEFORE this coding activity. It is included here as the activity's setup handout.

### Before next meeting — M04 preparation handout (send before this lesson)

For the upcoming **M04 coding meeting**, prepare **your own laptop**, then bring it and do the activity in class. The instructor confirms the date and naming pattern; `ADET-M04-LASTNAME` is the recommended folder/repository name.

```powershell
npx create-expo-app@latest ADET-M04-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M04-LASTNAME
npx tsc --noEmit
npx expo start
```

No extra packages are needed for this core activity. Use the distributed manifest and lockfile for exact versions. Open the app once before class; bring a screenshot or the exact error. Without home internet, prepare on campus Wi-Fi, mobile data or an agreed hotspot, or copy the [prepared starter and dependencies by USB](../offline-lab/README.md). Internet preparation is not the graded activity. Put this announcement on the **last presentation slide of the previous meeting**; the teacher supplies the real meeting date.
