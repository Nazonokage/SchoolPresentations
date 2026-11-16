# ADET M04 · Interaction, forms and lifecycle

[Module index](README.md) · Prelim · 60–90 minutes · Individual coding activity

## A. Lesson Preview & Review

**Why does a form lose a message?** Turn input into validated state and clean up effects.

By the end, trace **Type → Trim → Validate → Feedback**, run the checkpoint, and explain this result in your own words: Whitespace gives Enter a title. A real title gives Saved followed by the title and then clears the message.

## B. Detailed Main Lesson

The input displays title, and onChangeText writes the next value to state. This two-way connection makes the input controlled. Trim catches text made entirely of spaces. The counter uses the current string length. A successful press here previews a save message in memory.

An effect starts a timer when the message changes. Its cleanup cancels the old timer before the next effect or when the screen unmounts. Repeating the identical message does not change state, so it will not restart this timer. For complex forms, React Hook Form can manage fields and Zod can check submitted data. The API still validates its own inputs.

### Work through the behavior

Trace a single keystroke. The native input reports the entire new string. The setter stores it, React renders again, and value puts the same string back into the control. If value is fixed to an empty string while the handler merely logs changes, the student can type but sees no lasting change. Ask the class to reproduce that defect on a copy, then restore the setter.

### Curriculum connections

- TextInput, press/submit events, keyboard dismissal and controlled values.
- Required fields, trimming, bounds and useful inline errors; prevent duplicate submission.
- useEffect dependencies and cleanup; timers, subscriptions, focus and AppState distinctions.
- Extract a custom hook only after duplicated behavior is visible.
- React Hook Form and Zod as a prepared extension; compare schema validation with static TypeScript types.

Use the working screen first. Use the remaining comparisons for discussion or the extra 30 minutes.

![Type → Trim → Validate → Feedback](../visuals/M04.svg)

*Figure 4.* Type → Trim → Validate → Feedback. Show the first stage on the concept slide and ask students to predict the last. On the demonstration slide, place the example beside its actual output. For projector sizing see the [visual guide](../visuals/README.md).

![Illustration of New task](../visuals/M04-screen.svg)

*Sample screen illustration.* Saved: Bring library card. Place beside the code, then replace with a student device capture after running the checkpoint.

## C. Analogy, Guided Program & Practice

Parang resibo ang confirmation. Ipakita lang kung may laman ang form.

**Run it.** Follow the [Expo setup](../examples/README.md). From the examples folder select this checkpoint:

```powershell
node select.mjs 04
cd mobile
npm start -- --clear
```

**App.tsx** · [Example file](../examples/M04/App.tsx)

```tsx
import { useEffect, useState } from "react";
import { View, Text, Button, TextInput } from "react-native";

export default function App() {
  const [title, set] = useState("");
  const [msg, say] = useState("");
  useEffect(() => {
    if (!msg) return;
    const timer = setTimeout(() => say(""), 4000);
    return () => clearTimeout(timer);
  }, [msg]);
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <TextInput
        accessibilityLabel="Task title"
        placeholder="Task title"
        value={title}
        onChangeText={set}
      />
      <Text>{title.length} characters</Text>
      <Button
        title="Save"
        onPress={() =>
          say(title.trim() ? "Saved: " + title.trim() : "Enter a title")
        }
      />
      <Text accessibilityLiveRegion="polite">{msg}</Text>
    </View>
  );
}
```

**Expected behavior.** Whitespace gives Enter a title. A real title gives Saved followed by the title and then clears the message.

**Independent change.** Keep the last saved title visible, support editing it, and reject titles over 80 characters without replacing it.

**Troubleshooting.** If a stale timer clears newer feedback, check the cleanup and effect dependencies.

## D. Assessment, Wrap-Up & References

### One individual coding activity

Keep the last saved title visible, support editing it, and reject titles over 80 characters without replacing it. Submit the modified source, exact run command, one successful result and one edge or failure result. Explain the line responsible for the difference.

| Evidence | Points |
|---|---:|
| Working core and independent change | 4 |
| Meaningful edge case and response | 2 |
| Explain data flow and your own change | 2 |
| Reproducible setup and readable source | 2 |

**Wrap-up.** Explain how the program moves from “Type” to “Feedback”. Name the layer you would inspect if the expected result disappeared.

[Technical reference](https://react.dev/reference/react/useEffect) · [Research notes and corrections](../adet%20research%20folder%20JS/TECHNICAL_REVIEW.md)
