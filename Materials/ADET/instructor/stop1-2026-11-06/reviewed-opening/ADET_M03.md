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

### Common mistakes

- Putting loose text outside a `Text` component.
- Forgetting `flex: 1` on the outer `View`, so the screen is not full height.
- Using `onPress={handleLogin()}` instead of `onPress={handleLogin}`.

## C. Analogy, Guided Program & Practice

**Analogy.** Parang form sa registrar: ang guard (validation) ay nagsusuri kung kumpleto ang papel bago ka papasukin. Kapag kulang, may paalala (message). Kapag kumpleto, binabati ka.

**Real-world use case.** A campus portal login: the screen checks for empty fields before it ever contacts a server.

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
- *Keyboard covers the fields:* acceptable for this lesson; keyboard handling comes later.
- *Typing does nothing:* check that `value` and `onChangeText` both use the same state.

## D. Assessment, Wrap-Up & References

### One individual coding activity

Add a **Show password** button that toggles whether the password is hidden (use state and `secureTextEntry={!show}`). Also show a different message when only the username is empty. Submit the modified source, the exact run command, one successful result and one edge or failure result. Explain the line responsible for the difference.

| Evidence | Points |
|---|---:|
| Working core and independent change | 4 |
| Meaningful edge case and response | 2 |
| Explain data flow and your own change | 2 |
| Reproducible setup and readable source | 2 |

**Wrap-up.** Explain how the program moves from "Type" to "Message". Name the layer you would inspect if the message never changed.

[React Native: View](https://reactnative.dev/docs/view) · [TextInput](https://reactnative.dev/docs/textinput) · [Layout with Flexbox](https://reactnative.dev/docs/flexbox)

### Instructor notes

- Overlap check: the Layout, assets and accessibility module extends this one with images and deeper accessibility. Keep this module to basic layout.
- Do not call this login "secure". Say plainly it only checks empty input.