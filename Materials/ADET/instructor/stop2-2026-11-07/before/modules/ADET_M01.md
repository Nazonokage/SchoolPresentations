# ADET M01 · Expo ecosystem and Day-One refresher

[Module index](README.md) · Prelim · 60–90 minutes · 10-item quiz

## A. Lesson Preview & Review

**Can ₱50 buy two snacks?** Understand the mobile toolchain and refresh all essential syntax in one meeting.

By the end, trace **Budget 50 → Pay 25 → Pay 35 → Short 10**, run the checkpoint, and explain this result in your own words: Kulang: 10

## B. Detailed Main Lesson

A constant gives the price list a name. A variable holds the changing balance. Before the loop starts, left is 50. After the first price it is 25. After the second it is −10. The function returns that number to the caller. React evaluates the conditional expression and gives Text the shortage message. Students can calculate every step on paper before opening Expo.

Metro prepares the bundle on the development computer. Expo Go provides an already-built native host on the phone. A development build is your own host with the native libraries your app needs. TypeScript checks that a budget argument is numeric before the app runs. Hermes executes JavaScript on the device. Native components draw the resulting screen.

### Work through the behavior

Introduce yourself by showing one task from an ordinary school day. Ask students for their own example before showing syntax. On the board, draw two columns for price and balance. Ask one student to be the loop and another to decide which label appears. Change only the budget, predict the screen, then save the file and observe Fast Refresh. A stale phone screen and a wrong arithmetic result call for different investigations.

### Curriculum connections

- Opening demo and introductions: show the app students will gradually build; identify a useful campus problem.
- JavaScript refresher: let/const, values, operators, if/else, for/while, functions, parameters and returns; recognize arrays, objects and arrow callbacks.
- TypeScript introduction: simple annotations, inference and type checking versus runtime behavior; JSX as UI syntax.
- React Native, Expo, Metro and Hermes roles; native versus web UI; New Architecture/JSI as a brief conceptual overview.
- Prepared create-expo-app workspace, package scripts and device connection; Expo Go versus a development build; record tested versions during authoring.

Use the working screen first. Use the remaining comparisons for discussion or the extra 30 minutes.

![Budget 50 → Pay 25 → Pay 35 → Short 10](../visuals/M01.svg)

*Figure 1.* Budget 50 → Pay 25 → Pay 35 → Short 10. Show the first stage on the concept slide and ask students to predict the last. On the demonstration slide, place the example beside its actual output. For projector sizing see the [visual guide](../visuals/README.md).

![Illustration of Campus budget](../visuals/M01-screen.svg)

*Sample screen illustration.* Try changing the budget. Place beside the code, then replace with a student device capture after running the checkpoint.

<img src="../visuals/assets/react.svg" width="36" height="36" alt="react logo"> <img src="../visuals/assets/typescript.svg" width="36" height="36" alt="typescript logo">

## C. Analogy, Guided Program & Practice

Parang sobre ng baon: bawas bawat bili. Ano ang matitira pagkatapos ng pangalawa?

**Run it.** Follow the [Expo setup](../examples/README.md). From the examples folder select this checkpoint:

```powershell
node select.mjs 01
cd mobile
npm start -- --clear
```

**App.tsx** · [Example file](../examples/M01/App.tsx)

```tsx
import { View, Text } from "react-native";

export default function App() {
  const prices = [25, 35];
  function balance(budget: number) {
    let left = budget;
    for (const price of prices) left -= price;
    return left;
  }
  const left = balance(50);
  let message: string;
  if (left >= 0) {
    message = "Change: " + left;
  } else {
    message = "Kulang: " + Math.abs(left);
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Text>
        Baon: PHP 50.{" "}
        {message}
      </Text>
    </View>
  );
}
```

**Expected behavior.** Kulang: 10

**Independent change.** Try budgets 60 and 70. Explain why the exact-cost case takes the change branch.

**Troubleshooting.** If the QR opens but cannot load, check the phone and PC network and their Expo SDK compatibility. A red type error from passing a string has a different cause.

## D. Assessment, Wrap-Up & References

### 10-item quiz

Give a short answer for each item. The guided change above is ungraded.

1. Which tool serves the development bundle?
2. What does Expo Go open?
3. What does a function parameter receive?
4. What is the total of 25 and 35?
5. What does balance(50) return here?
6. Which branch displays for a budget of 70?
7. Why can copying the QR URL into a disconnected phone fail?
8. A string price joins digits. Why?
9. Which tool checks a numeric parameter before execution?
10. When does a project need a development build?

**Wrap-up.** Explain how the program moves from “Budget 50” to “Short 10”. Name the layer you would inspect if the expected result disappeared.

[Technical reference](https://docs.expo.dev/get-started/create-a-project/) · [Research notes and corrections](../adet%20research%20folder%20JS/TECHNICAL_REVIEW.md)
