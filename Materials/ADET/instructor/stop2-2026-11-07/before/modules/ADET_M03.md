# ADET M03 · Layout, assets and accessibility

[Module index](README.md) · Prelim · 60–90 minutes · 10-item quiz

## A. Lesson Preview & Review

**Will both offices fit on this phone?** Make mobile screens readable and usable on different devices.

By the end, trace **Width → Direction → Palette → Readable cards**, run the checkpoint, and explain this result in your own words: Two labeled office cards stack on a narrow window and sit beside each other above 540 units.

## B. Detailed Main Lesson

The window hook reports available width. The example uses that width to choose a column on narrow displays and a row on wider ones. Padding gives the text space inside each card. Gap separates siblings. The label stays text, so a screen reader can announce the office name without interpreting an icon.

The palette switches foreground and background together. Test a long translated title, dark mode and enlarged system text. Safe areas protect content near cutouts. A scrolling container helps long content, but a horizontal row can still overflow. StyleSheet groups styles for reuse. NativeWind and Unistyles are alternative authoring systems once the underlying Flexbox decisions are clear.

### Work through the behavior

Sketch two boxes across a narrow phone. If both have large fixed widths, the second can leave the screen. Flexbox chooses how children share the main axis. Try flex:1 on the wide-screen cards to distribute the available width. Set a descriptive accessibilityLabel only when the visible text does not already describe the control. Check the order a screen reader will visit the labels.

### Curriculum connections

- StyleSheet and Flexbox: direction, alignment, spacing and sizing.
- Safe areas, scrolling, keyboard overlap and small screens; test large text.
- Local/remote images, fonts and icons; loading and missing-asset behavior.
- Color contrast, accessible labels, touch targets and light/dark appearance; short localization examples.
- NativeWind and Unistyles as comparisons after plain styling; choose one baseline, not three required styling stacks.

Use the working screen first. Use the remaining comparisons for discussion or the extra 30 minutes.

![Width → Direction → Palette → Readable cards](../visuals/M03.svg)

*Figure 3.* Width → Direction → Palette → Readable cards. Show the first stage on the concept slide and ask students to predict the last. On the demonstration slide, place the example beside its actual output. For projector sizing see the [visual guide](../visuals/README.md).

![Illustration of Campus dashboard](../visuals/M03-screen.svg)

*Sample screen illustration.* Try a wider window. Place beside the code, then replace with a student device capture after running the checkpoint.

## C. Analogy, Guided Program & Practice

Kung mahaba ang pangalan, bigyan ng espasyo ang salita. Try an office name twice as long.

**Run it.** Follow the [Expo setup](../examples/README.md). From the examples folder select this checkpoint:

```powershell
node select.mjs 03
cd mobile
npm start -- --clear
```

**App.tsx** · [Example file](../examples/M03/App.tsx)

```tsx
import { View, Text } from "react-native";
import { useColorScheme, useWindowDimensions } from "react-native";
export default function App() {
  const dark = useColorScheme() === "dark";
  const { width } = useWindowDimensions();
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <View style={{ flexDirection: width > 540 ? "row" : "column", gap: 12 }}>
        {["Registrar", "Library"].map((name) => (
          <View
            key={name}
            style={{
              padding: 20,
              backgroundColor: dark ? "#163043" : "#e3f3fc",
            }}
          >
            <Text
              accessibilityRole="header"
              style={{ color: dark ? "white" : "#102030", fontSize: 22 }}
            >
              {name}
            </Text>
          </View>
        ))}
      </View>
    </View>
  );
}
```

**Expected behavior.** Two labeled office cards stack on a narrow window and sit beside each other above 540 units.

**Independent change.** Add hours in a second line. Compare a narrow screen at large text size with a wide screen.

**Troubleshooting.** If a card clips, remove fixed height first and let the text wrap. Check contrast in both themes.

## D. Assessment, Wrap-Up & References

### 10-item quiz

Give a short answer for each item. The guided change above is ungraded.

1. Which property selects the main axis?
2. Why give a control an accessible name?
3. What does useColorScheme report?
4. Which layout appears at width 400?
5. Which layout appears at width 700?
6. What happens when the color scheme changes?
7. A label disappears in dark mode. What should you inspect?
8. A long title clips at large text size. What should change?
9. How would you test responsive behavior?
10. Why retain visible text along with color?

**Wrap-up.** Explain how the program moves from “Width” to “Readable cards”. Name the layer you would inspect if the expected result disappeared.

[Technical reference](https://reactnative.dev/docs/flexbox) · [Research notes and corrections](../adet%20research%20folder%20JS/TECHNICAL_REVIEW.md)
