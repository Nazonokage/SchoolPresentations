# ADET M02 · Components, props and state

[Module index](README.md) · Prelim · 60–90 minutes · Individual coding activity

## A. Lesson Preview & Review

**Two offices, two counters** Build a screen from reusable pieces and understand why state updates change it.

By the end, trace **Name prop → Card → Press → New count**, run the checkpoint, and explain this result in your own words: Library 2, Clinic 0 after two library presses

## B. Detailed Main Lesson

A component is a function that describes part of a screen. Each Card receives a name from its parent through props. React keeps visits for each mounted card. A press invokes the callback and schedules an update. The functional updater receives the previous count, so two quick taps can each add one. React renders the new label from the updated value.

Count is local because the library and clinic track separate visits. If a parent needs a total, move the counts to that parent and pass a callback down. Rendering an Image also requires a source and usable dimensions. Changing props or state gives React the information needed to redraw.

### Work through the behavior

Point at the two Card elements in the parent. They call the same component definition with different names. Predict the result of moving useState above the component and passing one counter into both cards. A parent holding one number would make both displays follow that number. To keep a shared total and individual counts, store a map keyed by office and derive the total from it.

### Curriculum connections

- View, Text, Image, Pressable and TextInput; imports, exports and component composition.
- Typed props, interfaces, optional properties and children; distinguish props from local state.
- useState, event callbacks and functional updates; immutable array/object updates.
- Conditional rendering, map and stable keys; component rendering versus direct DOM mutation.
- Read a compiler/runtime error and isolate a component; browser addEventListener is not the native component event API.

Use the working screen first. Use the remaining comparisons for discussion or the extra 30 minutes.

![Name prop → Card → Press → New count](../visuals/M02.svg)

*Figure 2.* Name prop → Card → Press → New count. Show the first stage on the concept slide and ask students to predict the last. On the demonstration slide, place the example beside its actual output. For projector sizing see the [visual guide](../visuals/README.md).

![Illustration of Campus offices](../visuals/M02-screen.svg)

*Sample screen illustration.* Visit. Place beside the code, then replace with a student device capture after running the checkpoint.

<img src="../visuals/assets/react.svg" width="36" height="36" alt="react logo">

## C. Analogy, Guided Program & Practice

Bawat opisina may sariling tally. Pindutin ang Library nang dalawang beses. Ilan ang dapat makita sa Clinic?

**Run it.** Follow the [Expo setup](../examples/README.md). From the examples folder select this checkpoint:

```powershell
node select.mjs 02
cd mobile
npm start -- --clear
```

**App.tsx** · [Example file](../examples/M02/App.tsx)

```tsx
import { useState } from "react";
import { View, Text, Button } from "react-native";
type Props = { name: string };
function Card({ name }: Props) {
  const [visits, set] = useState(0);
  return (
    <View>
      <Text>
        {name}: {visits} visits
      </Text>
      <Button title="Visit" onPress={() => set((n) => n + 1)} />
    </View>
  );
}
export default function App() {
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Card name="Library" />
      <Card name="Clinic" />
    </View>
  );
}
```

**Expected behavior.** Library 2, Clinic 0 after two library presses

**Independent change.** Add a capacity prop and a reset button. Stop adding at capacity and show a visible reason.

**Troubleshooting.** If the count jumps during initial render, check for onPress={handler()} instead of a callback.

## D. Assessment, Wrap-Up & References

### One individual coding activity

Add a capacity prop and a reset button. Stop adding at capacity and show a visible reason. Submit the modified source, exact run command, one successful result and one edge or failure result. Explain the line responsible for the difference.

| Evidence | Points |
|---|---:|
| Working core and independent change | 4 |
| Meaningful edge case and response | 2 |
| Explain data flow and your own change | 2 |
| Reproducible setup and readable source | 2 |

**Wrap-up.** Explain how the program moves from “Name prop” to “New count”. Name the layer you would inspect if the expected result disappeared.

[Technical reference](https://reactnative.dev/docs/intro-react) · [Research notes and corrections](../adet%20research%20folder%20JS/TECHNICAL_REVIEW.md)
