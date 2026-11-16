# ADET M03 · Building a screen: layout and a login form

[Module index](README.md) · Prelim · 60–90 minutes · Individual coding activity

## A. Lesson Preview & Review

**Can you build a clean login screen with React Native?** Place components on screen with Flexbox, read what the user types and show a message.

**Learning targets.**
1. Use `View`, `Text`, `TextInput` and `Button`.
2. Lay out a screen with Flexbox and `StyleSheet`.
3. Keep typed text in state with a controlled input.
4. Validate empty input and show a message.

By the end, trace **Type → State → Press → Message**, run the checkpoint, and explain in your own words: an empty field shows "Enter both username and password." and a filled form shows "Welcome, <name>!".

## B. Detailed Main Lesson

### In plain words

A screen is a stack of boxes. `View` is a box, `Text` shows words, `TextInput` lets the user type and `Button` lets them tap. Flexbox decides where the boxes sit. Whatever the user types is saved in state so your code can read it when they press the button.

### The building blocks

| Component | Purpose |
|---|---|
| `View` | A container that holds other components |
| `Text` | Shows raw text nodes; props such as `Button.title` and `TextInput.placeholder` accept strings |
| `TextInput` | A box to type in |
| `Button` | A tappable button with a `title` and an `onPress` function |

### Flexbox in three ideas

- A `View` stacks its children **top to bottom** by default (`flexDirection: "column"`).
- `justifyContent` places children along the main direction (center, space-between).
- `alignItems` places children across it (center, stretch).

```text
flex: 1 container (column)
+----------------------+
|   (justifyContent:   |
|     "center")        |
|   [ Login ]          |
|   [ Username    ]    |
|   [ Password    ]    |
|   [   LOG IN    ]    |
|   message text       |
+----------------------+
```

### Styles

`StyleSheet.create({ ... })` collects styles in one place. Use `padding` for space inside a box and `gap` for space between children.

### Controlled input

A **controlled input** gets its text from state and updates the state on every keystroke: `value={username}` and `onChangeText={setUsername}`. `secureTextEntry` obscures the displayed characters; it does not authenticate or encrypt a password.

### Accessibility

Add `accessibilityLabel` so screen readers can name each field.

### Trace a controlled field

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

### Common mistakes

- Putting loose text outside a `Text` component.
- Forgetting `flex: 1` on the outer `View`, so the screen is not full height.
- Using `onPress={handleLogin()}` instead of `onPress={handleLogin}`.

## C. Analogy, Guided Program & Practice

**Analogy.** Parang form sa registrar: ang guard (validation) ay nagsusuri kung kumpleto ang papel bago ka papasukin. Kapag kulang, may paalala (message). Kapag kumpleto, binabati ka.

**Real-world use case.** A campus portal login: the screen checks for empty fields before it ever contacts a server.

### Core dependency check

| Import / tool | Prepared source | Extra install / permission / plugin |
|---|---|---|
| react | Blank template; component state/effects where used | None |
| react-native | Blank template; native views and built-in APIs | None |
| TypeScript / Expo CLI | Prepared dev toolchain | None during offline class |

Core entry: index.ts → App.tsx. Compatible Expo Go can host these APIs; perform the actual native-client smoke test before class. This does not certify the phone/network route.

**Install first.** No extra packages.

**Fresh-project command (online preparation on your own laptop):**

```powershell
npx create-expo-app@latest ADET-M03-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M03-LASTNAME
npx tsc --noEmit
npx expo start
```

Metro transpiles; run `npx tsc --noEmit` separately after replacing App.tsx. In the prepared offline starter use `npx expo start --offline`. Bring that prepared laptop next meeting.

**Run it.** Use the project from M01, replace `App.tsx`, then `npx expo start`.

**App.tsx**

```tsx
import { useState } from "react";
import { View, Text, TextInput, Button, StyleSheet } from "react-native";

export default function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  function handleLogin() {
    // Reject empty username or password
    if (username.trim() === "" || password === "") {
      setMessage("Enter both username and password.");
      return;
    }
    setMessage("Welcome, " + username.trim() + "!");
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Login</Text>
      <TextInput
        style={styles.input}
        placeholder="Username"
        autoCapitalize="none"
        accessibilityLabel="Username"
        value={username}
        onChangeText={setUsername}
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        secureTextEntry
        accessibilityLabel="Password"
        value={password}
        onChangeText={setPassword}
      />
      <Button title="LOG IN" onPress={handleLogin} />
      <Text>{message}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: "center", padding: 24, gap: 12 },
  title: { fontSize: 28, fontWeight: "bold", textAlign: "center" },
  input: {
    borderWidth: 1,
    borderColor: "#888",
    borderRadius: 8,
    padding: 10,
    fontSize: 16,
  },
});
```

**Expected behavior.** Pressing LOG IN with an empty field shows "Enter both username and password." With both filled it shows "Welcome, <name>!". This demo checks only for empty input and does not authenticate. Real sign-in comes in a later module.

### Worked validation trace

The rule is exactly `username.trim() === "" || password === ""`. Only the username is trimmed. A spaces-only password passes this demonstration; do not silently alter real passwords.

| Username | Password | Result |
|---|---|---|
| empty | empty | Enter both username and password. |
| three spaces | secret | Enter both username and password. |
| Liora | empty | Enter both username and password. |
| Liora | three spaces | Welcome, Liora! (no authentication occurs) |
| Liora | secret | Welcome, Liora! (no authentication occurs) |

**Predict, then check:** Which condition rejects a spaces-only username? Why does the same not happen to a spaces-only password?

**Troubleshooting.**
- *Red error about text strings:* some text is outside a `Text` component.
- *Keyboard covers the fields:* dismiss it to inspect feedback; record this layout limitation. M04 introduces a scrollable screen. Do not claim this minimal form is production-ready.
- *Typing does nothing:* check that `value` and `onChangeText` both use the same state.

### Optional ungraded comparison — feedback that clears

Old M04's message-dependent timer now belongs here, connected to M02's effect cleanup. The complete [App.timeout.tsx](../examples/M03/App.timeout.tsx) uses only template packages. Copy it as App.tsx in a spare starter copy and run the same type-check/start commands. It adds useEffect to the React import and a four-second timeout that clears nonempty feedback.

**Predict first:** submit a different message after two seconds. Which timeout should clear the new message? The old effect cleans up its timeout, then the new effect schedules one for the changed message. At roughly four seconds after that change, feedback clears. Submitting the identical message does not change state, so it does not restart this timer. A delay is a minimum scheduling request, not an accurate clock. This is a UI cleanup comparison, not an event-driven architecture lesson.

| Moment | Message | Resource |
|---|---|---|
| Start | empty | No timeout |
| Submit valid pair | Welcome, Virel! | Schedule A |
| Submit an empty username before A fires | Enter both username and password. | Cancel A; schedule B |
| B callback eventually runs | empty | Feedback cleared; effect no longer schedules work |

For keyboard dismissal, React Native's Keyboard.dismiss() can be called in the press handler; it is a built-in API, not validation. Keep it separate from the rule determining the message. More elaborate form libraries do not remove the need for server validation; they are outside this small core checkpoint.

## D. Assessment, Wrap-Up & References

### One individual coding activity

Add a **Show password** button that toggles whether the password is hidden (use state and `secureTextEntry={!showPassword}`). Also show a different message when only the username is empty. Submit the modified source, the exact run command, one successful result and one edge or failure result. Explain the line responsible for the difference.

| Evidence | Points |
|---|---:|
| Working core and independent change | 4 |
| Meaningful edge case and response | 2 |
| Explain data flow and your own change | 2 |
| Reproducible setup and readable source | 2 |

### Three equal-point delivery modes

**Mode 1 — Offline computer lab.** Before class, PCs need Node 24.18.1, npm 11.16.0, VS Code and a separate copy of the prepared starter including node_modules. Use `START-LAB.cmd`; replace only the student's App.tsx. No new installs in class. Local type-checking and Android bundling passed; a reachable phone on local Wi-Fi with compatible Expo Go or a prepared emulator still needs a successful [smoke test](../offline-lab/SMOKE-TEST.md). If no native display route passes, use Mode 3, not an untested promise of offline phone access. `--tunnel` is an online fallback only.

**Mode 2 — Prepared personal laptop.** Follow the announcement below before class; bring your laptop and run the same activity during the next scheduled coding meeting. Submit source, package.json, lockfile, README with commands and the actual activity date, success/failure evidence and a brief explanation. Recommended repository: `ADET-M03-LASTNAME` (instructor confirms the pattern). Do not upload node_modules, cache or secrets.

**Mode 3 — Written alternative (10 points).** Trace empty fields, a spaces-only username, a spaces-only password and a normal pair. Explain an early return, design the show-password state change, and identify a controlled-input wiring failure. Submit a step-by-step table plus a 150–250-word explanation. This earns the same maximum as the coding activity; no device screenshot is required.

| Written evidence | Points |
|---|---:|
| Correct complete trace and proposed independent change | 4 |
| Edge/failure case and justified correction | 2 |
| Explanation connecting code to visible behavior | 2 |
| Labeled inputs, ordered steps and readable evidence | 2 |

Guided copying and predictions are ungraded. Only the one selected assessment mode is graded.

**Wrap-up.** Explain how the program moves from "Type" to "Message". Name the layer you would inspect if the message never changed.

[React Native: View](https://reactnative.dev/docs/view) · [TextInput](https://reactnative.dev/docs/textinput) · [Layout with Flexbox](https://reactnative.dev/docs/flexbox)

### Instructor notes

**60-minute pacing:** 5 review, 15 explanation, 10 guided program, 25 individual activity, 5 wrap-up. Use the additional 30 minutes for support and deeper traces, not another graded task.

- Do not call this login "secure". Say plainly it only checks empty input.

**Teaching evidence:** keys and grading guidance are in [the separate instructor key](../instructor/OPENER_ANSWER_KEY.md). Use the local flow diagram beside the matching code; no external image download is required. Record actual hardware outcomes rather than treating expected output as a measured device result.

**Instructor scheduling note:** reuse the following preparation block at the end of the meeting BEFORE this coding activity. It is included here as the activity's setup handout.

### Before next meeting — M03 preparation handout (send before this lesson)

For the upcoming **M03 coding meeting**, prepare **your own laptop**, then bring it and do the activity in class. The instructor confirms the date and naming pattern; `ADET-M03-LASTNAME` is the recommended folder/repository name.

```powershell
npx create-expo-app@latest ADET-M03-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M03-LASTNAME
npx tsc --noEmit
npx expo start
```

No extra packages are needed for this core activity. Use the distributed manifest and lockfile for exact versions. Open the app once before class; bring a screenshot or the exact error. Without home internet, prepare on campus Wi-Fi, mobile data or an agreed hotspot, or copy the [prepared starter and dependencies by USB](../offline-lab/README.md). Internet preparation is not the graded activity. Put this announcement on the **last presentation slide of the previous meeting**; the teacher supplies the real meeting date.

### Before next meeting — laptop preparation announcement

For the upcoming **M04 coding meeting**, prepare **your own laptop**, then bring it and do the activity in class. The instructor confirms the date and naming pattern; `ADET-M04-LASTNAME` is the recommended folder/repository name.

```powershell
npx create-expo-app@latest ADET-M04-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M04-LASTNAME
npx tsc --noEmit
npx expo start
```

No extra packages are needed for this core activity. Use the distributed manifest and lockfile for exact versions. Open the app once before class; bring a screenshot or the exact error. Without home internet, prepare on campus Wi-Fi, mobile data or an agreed hotspot, or copy the [prepared starter and dependencies by USB](../offline-lab/README.md). Internet preparation is not the graded activity. Put this announcement on the **last presentation slide of the previous meeting**; the teacher supplies the real meeting date.
