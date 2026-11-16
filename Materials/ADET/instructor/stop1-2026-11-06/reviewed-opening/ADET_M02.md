# ADET M02 · Screens, components and the app lifecycle

[Module index](README.md) · Prelim · 60–90 minutes · 10-item quiz

## A. Lesson Preview & Review

**What happens to your screen when the user leaves and comes back?** Understand screens, components and what React Native calls the lifecycle.

**Learning targets.**
1. Explain what a screen and a component are.
2. Match Android's app building blocks to their React Native counterparts.
3. Trace mount, update and unmount with `useEffect`.
4. Detect when the app goes to the background and explain what happens to state.

By the end, trace **Mount → Update → Unmount**, run the checkpoint, and explain in your own words: the timer starts when the component appears, stops when the conditional render removes it, and starts again from 0 when a new Timer is mounted.

## B. Detailed Main Lesson

### In plain words

A **screen** is what the user sees at one moment. In React Native you build each screen from small reusable pieces called **components**. A component mounts when React adds it to the tree, can render again when data changes, and unmounts when React removes it. A component can be visually hidden or lose navigation focus while remaining mounted. When a component is removed, the data it kept in memory is gone.

### Screen, component and app

- **Component:** a function that describes part of the screen, such as `Text`, `Button` or your own `Timer`.
- **Screen:** a component that fills the whole screen for one task, such as a login screen.
- **App:** all your screens and logic together, starting at `App.tsx`.

### Android's building blocks and React Native

Android apps are made of four kinds of building blocks. React Native has loose counterparts. They are not one-to-one.

| Android term | What it does | React Native counterpart (loosely) |
|---|---|---|
| Activity | One screen the user interacts with | A screen component |
| Service | Background work with no UI | Background tasks (covered later) |
| Content Provider | Shares app data | Shared data through state, storage or an API (covered later) |
| Broadcast Receiver | Reacts to system announcements | Event listeners such as `AppState` |

### The component lifecycle

| Phase | When it happens | How you react |
|---|---|---|
| Mount | React adds the component to the tree | `useEffect` with an empty list `[]` |
| Update | Its state or props change | The function runs again and redraws |
| Unmount | React removes the component from the tree | The cleanup function you return from `useEffect` |

```text
Render ──> commit / mount ──> effect setup
   |
   v
Update (state changes) ──> render again
   |
   v
Unmount ──> cleanup runs ──> state is gone
```

`useEffect` setup runs after React commits the component. Do not treat it as an exact after-paint clock. With changed dependencies React cleans up the old effect before the next setup. In development, Strict Mode may perform an extra setup/cleanup cycle. The function you `return` from it is the **cleanup**. React runs it when the component is removed. Always clean up timers and listeners.

### The app lifecycle

React Native's `AppState` tells you whether the whole app is `active`, `inactive` (iOS) or `background`. An Android activity has callbacks like `onCreate` and `onStop`. The ideas map loosely.

| Android callback | Rough React Native equivalent |
|---|---|
| `onCreate` | First render and mount effect |
| `onStart` / `onResume` | `AppState` becomes `active` |
| `onPause` / `onStop` | `AppState` becomes `inactive` or `background` |
| `onDestroy` | No guaranteed JavaScript callback when the OS terminates the process |

**State and memory.** State held with `useState` lives in memory. It is lost when the component unmounts or when the system closes the app. Saving data so it survives is covered in a later module.

### JavaScript you need today

| Idea | Example |
|---|---|
| Constant and variable | `const name = "Ana"` and `let count = 0` |
| Arrow function | `(n) => n + 1` |
| Array and object | `[1, 2]` and `{ id: 1 }` |
| Curly braces in JSX | `<Text>{count}</Text>` |

### Common mistakes

- Starting a timer in `useEffect` and forgetting to clear it.
- Expecting local state to survive conditional removal; visual hiding or navigation blur alone does not necessarily remove it.
- Writing `onPress={handler()}` instead of `onPress={handler}`, which runs it during rendering.

## C. Analogy, Guided Program & Practice

**Analogy.** Parang entablado sa teatro: itinatayo ang set (mount), nagtatanghal ang mga artista habang may nagbabago sa eksena (update), at binabaklas ang set pagkatapos (unmount). Kapag binaklas na, wala na ang mga props sa entablado, kaya mawawala rin ang state.

**Real-world use case.** A food delivery app tracks your rider with a timer on the order screen. When you leave the screen, the timer must stop. A real app may choose to pause refreshing in the background. This sample observes AppState only; it does not implement background pausing. Intervals may be delayed or suspended and are not an accurate elapsed-time clock.

**Install first.** No extra packages.

**Fresh-project command (online preparation on your own laptop):**

```powershell
npx create-expo-app@latest ADET-M02-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M02-LASTNAME
npx tsc --noEmit
npx expo start
```

Metro transpiles; run `npx tsc --noEmit` separately after replacing App.tsx. In the prepared offline starter use `npx expo start --offline`. Bring that prepared laptop next meeting.

**Run it.** Use the project from M01, replace `App.tsx`, then `npx expo start`. Open React Native DevTools (press `j` in the Expo terminal with a compatible native app connected), then its Console. Terminal forwarding varies by runtime. This instruction is based on official documentation; a real-device log-location check remains pending.

**App.tsx**

```tsx
import { useEffect, useState } from "react";
import { AppState, View, Text, Button } from "react-native";

// A component that counts seconds while it is on screen
function Timer() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    console.log("Timer mounted");
    // Add one second every 1000 ms
    const intervalId = setInterval(() => setSeconds((current) => current + 1), 1000);
    // Cleanup: runs when Timer is removed
    return () => {
      clearInterval(intervalId);
      console.log("Timer unmounted");
    };
  }, []);

  return <Text>Seconds: {seconds}</Text>;
}

export default function App() {
  const [visible, setVisible] = useState(true);
  const [appState, setAppState] = useState(AppState.currentState);

  useEffect(() => {
    // Listen for the whole app going active or to the background
    const subscription = AppState.addEventListener("change", (nextAppState) => {
      setAppState(nextAppState);
      console.log("App state:", nextAppState);
    });
    return () => subscription.remove();
  }, []);

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Text>App state: {appState}</Text>
      {visible && <Timer />}
      <Button
        title={visible ? "Hide timer" : "Show timer"}
        onPress={() => setVisible((currentVisible) => !currentVisible)}
      />
    </View>
  );
}
```

**Expected behavior.** The seconds count up. Press "Hide timer" and the DevTools Console records "Timer unmounted". Press "Show timer" and the count restarts at 0. Switch to another app and back and the "App state" text changes.

**Independent change.** Add a "Pause" button inside `Timer` that stops counting without hiding it. Explain the difference between hiding and pausing.

**Troubleshooting.**
- *Count speeds up after several show/hide presses:* the cleanup is missing or wrong.
- *Nothing prints:* check the React Native DevTools Console and its connection to the app; do not assume Metro forwards logs.
- *Button text never changes:* check the `visible` state and the `onPress` callback.

## D. Assessment, Wrap-Up & References

### 10-item quiz

**Multiple choice**

1. What is a screen?
   A. What the user sees for one task · B. A database · C. A package manager · D. A cable
2. When does `useEffect(() => {...}, [])` run its main body?
   A. Never · B. After the component first appears · C. Only on errors · D. Before Node starts
3. What is the function returned from `useEffect` called?
   A. Cleanup · B. Reducer · C. Router · D. Manifest
4. Which `AppState` value means the app is in the background?
   A. `active` · B. `background` · C. `loading` · D. `paused-forever`
5. Which Android building block is a loose match for a screen?
   A. Activity · B. Service · C. Content Provider · D. APK

**Identification**

6. What happens to `useState` values when a component unmounts?
7. Which React Native API reports whether the app is active or in the background?
8. Which debugging tool’s Console should you use to inspect this native app’s JavaScript logs?
9. Why should you clear a timer in the cleanup function?
10. Name the three phases of a component's lifecycle.

**Answer key (instructor).** 1 A · 2 B · 3 A · 4 B · 5 A · 6 They are lost. · 7 `AppState` · 8 React Native DevTools Console; terminal forwarding is environment-dependent. · 9 Otherwise the timer keeps running after the component is gone, wasting resources and causing bugs. · 10 Mount, update, unmount.

**Wrap-up.** Explain how the timer moves from "Mount" to "Unmount", and say what is lost at the end. Name the layer you would inspect if the timer kept counting after hiding.

[React Native: state](https://reactnative.dev/docs/state) · [React Native: AppState](https://reactnative.dev/docs/appstate)

### Instructor notes

- Callback names from Android appear for comparison only. The mapping is approximate; say so.
- Overlap check: props and deeper state work are taught in the Components, props and state module. Keep this module to lifecycle.
- Test the sample on a physical device once. `AppState` values differ slightly between Android and iOS.