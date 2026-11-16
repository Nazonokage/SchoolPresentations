# ADET M05 · Navigation and application structure

[Module index](README.md) · Prelim · 60–90 minutes · 10-item quiz

## A. Lesson Preview & Review

**Open the library from a link** Connect screens and separate temporary screen state from shared data.

By the end, trace **Home → Push ID → Read parameter → Office**, run the checkpoint, and explain this result in your own words: Visit library opens Library • Open 8 AM. An unknown office shows Office not found.

## B. Detailed Main Lesson

A route maps a file to a screen. Pressing Visit library pushes a destination onto the navigation stack. The file called [id].tsx reads the changing segment. A lookup converts that ID into display data. Passing an ID lets a cold launch reconstruct a screen even when the previous screen no longer exists.

A stack remembers the way back. Tabs represent peer areas such as Tasks and Settings. A layout supplies common navigation UI. Decide whether something belongs in a route, screen state or a shared store. Keep passwords and private tokens out of route parameters. A guard is useful navigation feedback while the API enforces access.

### Work through the behavior

On the board, draw a stack with Home at the bottom. Push an office once, press Back, and erase only the top box. A tab switch instead selects a peer section. Show how two different office IDs reuse one route file. Refresh that detail screen directly: if it depends on a prior click's global object, there is nothing to restore. Loading by ID or showing a missing-record message makes the screen understandable.

### Curriculum connections

- Expo Router file routes, layout files, stacks and tabs; navigate/back behavior.
- Dynamic route parameters and invalid/missing IDs; parse parameters before use.
- Screen state versus shared state; preview Context, reducer and Zustand trade-offs.
- Deep-link concepts and route guards; hiding a screen is not server authorization.
- Organize components, hooks and data services; retain complete independent lesson checkpoints.

Use the working screen first. Use the remaining comparisons for discussion or the extra 30 minutes.

![Home → Push ID → Read parameter → Office](../visuals/M05.svg)

*Figure 5.* Home → Push ID → Read parameter → Office. Show the first stage on the concept slide and ask students to predict the last. On the demonstration slide, place the example beside its actual output. For projector sizing see the [visual guide](../visuals/README.md).

![Illustration of Campus offices](../visuals/M05-screen.svg)

*Sample screen illustration.* Back. Place beside the code, then replace with a student device capture after running the checkpoint.

## C. Analogy, Guided Program & Practice

Parang room number ang ID. Kapag maling number, bigyan ang user ng malinaw na sagot.

**Run it.** Follow the [Expo setup](../examples/README.md). From the examples folder select this checkpoint:

```powershell
node select.mjs 05
cd mobile
npm start -- --clear
```

**[id].tsx** · [Example file](../examples/M05/%5Bid%5D.tsx)

```tsx
import { Text } from "react-native";
import { useLocalSearchParams } from "expo-router";
export default function Office() {
  const { id } = useLocalSearchParams();
  return (
    <Text style={{ padding: 30 }}>
      {id === "library" ? "Library • Open 8 AM" : "Office not found"}
    </Text>
  );
}
```

**App.tsx** · [Example file](../examples/M05/App.tsx)

```tsx
import { View, Button } from "react-native";
import { Stack, router } from "expo-router";
export default function App() {
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Stack.Screen options={{ title: "Campus offices" }} />
      <Button
        title="Visit library"
        onPress={() => router.push("/office/library")}
      />
    </View>
  );
}
```

**Expected behavior.** Visit library opens Library • Open 8 AM. An unknown office shows Office not found.

**Independent change.** Add clinic and link to it from the home screen. Try a made-up ID and use Back.

**Troubleshooting.** If navigation reports an unmatched route, verify the route files are inside the active app or src/app folder.

## D. Assessment, Wrap-Up & References

### 10-item quiz

Give a short answer for each item. The guided change above is ungraded.

1. What is a route parameter?
2. What does a stack preserve?
3. When are tabs useful?
4. Which path opens the library?
5. What does an unknown ID display?
6. What does Back do after pushing Library?
7. Why can a copied detail link fail with local-only selection state?
8. Why can a hidden route still expose data?
9. Where should a reusable ID be carried?
10. How should an invalid ID be handled?

**Wrap-up.** Explain how the program moves from “Home” to “Office”. Name the layer you would inspect if the expected result disappeared.

[Technical reference](https://docs.expo.dev/router/basics/core-concepts/) · [Research notes and corrections](../adet%20research%20folder%20JS/TECHNICAL_REVIEW.md)
