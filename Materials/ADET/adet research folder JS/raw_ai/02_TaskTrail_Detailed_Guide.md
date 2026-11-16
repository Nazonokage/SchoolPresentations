# 📱 Application Development and Emerging Technologies
## Including Event-Driven Programming — TypeScript · React Native · Expo

> **Course edition:** November 2026 · **Reference stack:** Expo SDK 58 (React Native 0.88, React, TypeScript strict) · **Fallback stack:** Expo SDK 57
> **Audience:** Students with some JavaScript / web-development background
> **Basis:** Rebuilt from the original ADET table of contents (Android/Java → Kotlin/Compose), re-targeted to TypeScript + React Native + Expo

---

## 0. How to Read This Course Guide

Every module follows the same template so you can scan it quickly:

| Block | Meaning |
|---|---|
| **In a nutshell** | The whole module in 2–3 sentences |
| **What are we creating** | The concrete thing students build in the lab |
| **Legacy ADET mapping** | Which original Android module this replaces, and how |
| **Runs in** | ✅ Expo Go · 🔧 needs a development build (see §3) |
| **Outcomes / Topics / Key code / Lab** | The teaching content |

Code samples are **teaching skeletons**: they show the shape of each API. Before class, run `npx expo install --fix` and check the docs page for your SDK version, because Expo package APIs move between SDKs (this course flags the places where that happened recently).

---

## 1. Course Description & Outcomes

This course teaches students to design, build, test, and ship cross-platform mobile apps in **TypeScript**, using **React Native** with **Expo**. It keeps the original ADET scope (UI, events, navigation, background work, device hardware, data, security, publishing) and adds **emerging technologies** (AI features, native UI via Expo UI, native modules, widgets, agent tooling).

By the end, students can:

1. Explain how React Native renders native UI and how Expo fits around it (Metro, Hermes, New Architecture, config plugins, EAS).
2. Write strictly-typed TypeScript for components, hooks, data models, and API contracts.
3. Build event-driven UIs with hooks, gestures, forms, and validated input.
4. Structure multi-screen apps with Expo Router (file-based, typed routes, deep links).
5. Integrate device features: notifications, background tasks, location/maps, camera, audio/video, sharing, SMS/mail handoff.
6. Fetch, cache, persist, and secure data (TanStack Query, SQLite, SecureStore, OAuth).
7. Connect to a TypeScript backend and an AI model without leaking secrets.
8. Test, profile, build, and distribute an app with EAS to Google Play and the App Store.

---

## 2. Version Policy (Decision & Reasoning)

**Decision: teach against SDK 58 concepts, keep every lab runnable on SDK 57.**

Why this is the right call as of November 2026:

- **SDK 58** (released Oct 15, 2026) is the current stable release: built for iOS 27, includes React Native 0.88. Expo's upgrade guide says the **Strict TypeScript API is now the default** (deep imports from `react-native/Libraries/*` become type errors; refs use instance types such as `ViewInstance` / `TextInputInstance`) and that **Expo Router's native tabs moved to `expo-router/native-tabs`**. A TypeScript course should teach the strict behavior from day one.
- **SDK 57** (June 30, 2026) was a deliberately small release (React Native 0.86, no breaking changes), so 57 → 58 differences for beginner-level code are limited and listed in "Version notes" below.
- **The weak point is Expo Go itself.** Expo describes Expo Go as a playground for learners, it supports **only one SDK at a time** on iPhones, and the store versions lag releases (App Store approval delays in 2026). Expo said the store Expo Go for SDK 58 would follow "within a few weeks" of the Oct 2026 release. **Instructor action before Week 1:** check what the store Expo Go supports *today* and let `create-expo-app` pick the matching SDK (it prompts for store-compatible vs latest).
- Expo Go now requires being **logged in to the same Expo account in both the terminal (Expo CLI) and the app** to load a project in dev mode.

**Version notes to flag in class**

| Topic | SDK 57 | SDK 58 |
|---|---|---|
| React Native | 0.86 | 0.88 |
| Type checking | Legacy + Strict opt-in | Strict TypeScript API default |
| Expo Router native tabs | `expo-router/unstable-native-tabs` | `expo-router/native-tabs` |
| Android release builds | R8 optional | R8 on by default (can opt out via `expo-build-properties`) |
| iOS | Xcode 26.x | Built for iOS 27 / scene life cycle |

> ⚠️ Treat all version tables as "verified at time of writing." Re-check Expo's changelog (`expo.dev/changelog`) at the start of each term.

---

## 3. Expo Go vs Development Build — Which Modules Need What

Expo Go is a prebuilt app: it can only run native code that shipped inside it. A **development build** is your own debug app with `expo-dev-client`. Plan the course so students stay in Expo Go as long as possible, then switch.

| Capability | Expo Go | Dev build needed |
|---|---|---|
| Components, layout, styling, Expo Router, Reanimated, gestures | ✅ | — |
| Forms, TanStack Query, fetch, SQLite, SecureStore, AsyncStorage | ✅ | — |
| Location (foreground), maps, camera, image picker, audio/video | ✅ | — |
| Local notifications (scheduled) | ✅ | — |
| **Remote push notifications** | ❌ (not supported since SDK 53) | 🔧 |
| **Background tasks (TaskManager / BackgroundTask)** | ❌ Android unavailable; no background execution on iOS | 🔧 (and a **physical iOS device**) |
| Custom native libraries, app icon/name/splash config, app/universal links | ❌ | 🔧 |
| Writing your own native module | ❌ | 🔧 |

**Recommended switch point:** Module 10 (notifications) onward introduces dev builds through EAS Build or `npx expo run:android`. Students without a Mac can still build iOS via EAS Build in the cloud (an Apple Developer account is required to run on a physical iPhone).

---

## 4. The Running Project — **TaskTrail**

Instead of 28 disconnected demos, students grow one app across the course:

**TaskTrail** — an offline-first task & place planner. Users create tasks, attach photos/voice notes/locations, get reminders, sync to a backend, sign in, and ask an AI assistant to summarize their week.

| Module range | TaskTrail grows by… |
|---|---|
| 0–6 | Static UI: task cards, themed screens, layout |
| 7–9 | Add/edit tasks (validated forms), tab + detail navigation, task list |
| 10–13 | Reminders, system-event handling, background sync |
| 14–17 | Share tasks, location pins & map, photo attachments, voice notes |
| 18–21 | API calls with caching, SQLite persistence, sign-in, TypeScript backend |
| 22–25 | Hardening, tests, performance, EAS builds and store release |
| 26–27 | AI assistant, native UI experiments, final capstone |

---

## 5. Suggested Schedule (18 Weeks — adjust to your calendar)

| Week | Modules | Milestone |
|---|---|---|
| 1 | 0, 1 | Environment working; first TypeScript exercises |
| 2 | 2, 3 | Typed components with state |
| 3 | 4, 5 | Core components + layout |
| 4 | 6, 7 (part 1) | Theming; events and gestures |
| 5 | 7 (part 2), 8 | Forms; Expo Router navigation |
| 6 | 9 | Lists and data display — **Quiz 1** |
| 7 | 10, 11 | Notifications; system events |
| 8 | **Midterm project checkpoint** | TaskTrail v1 (UI + nav + local state) |
| 9 | 12, 13 | Background work; scheduling |
| 10 | 14, 15 | Sharing; location/maps |
| 11 | 16, 17 | Camera; audio/video |
| 12 | 18, 19 | Networking; persistence — **Quiz 2** |
| 13 | 20, 21 | Auth; backend |
| 14 | 22, 23 | Security; performance |
| 15 | 24 | Testing |
| 16 | 25 | EAS build + release |
| 17 | 26 | Emerging tech |
| 18 | 27 | Capstone demos |

**Suggested grading:** Labs 30% · Quizzes 15% · Midterm checkpoint 15% · Capstone 30% · Participation/code review 10%.

---

# PHASE 0 — Foundations

## Module 0 — The Mobile Landscape & Your Toolchain

> **In a nutshell:** How a TypeScript file becomes a native app. You meet React Native (JS drives real native views), Expo (tooling + SDK on top), Metro (bundler), Hermes (JS engine), and the New Architecture, which is now the only architecture (the legacy one was dropped in SDK 55).

**What are we creating:** A "Hello TaskTrail" project running on a real phone *and* an emulator/simulator, with a verified TypeScript compile (`npx tsc --noEmit`) and lint (`npx expo lint`).

**Legacy ADET mapping:** Modules 1–2 (Android stack, Android Studio setup). Replaces Linux-kernel-to-ART diagrams with the RN pipeline: *TS → Metro → Hermes bytecode → JSI → native views*.

**Runs in:** ✅ Expo Go (with an Expo account logged in on both CLI and app)

**Outcomes**
- Explain the difference between React Native, Expo, Expo Go, and a development build.
- Create, run, and reload a project; read an error in the dev overlay and React Native DevTools.
- Describe the New Architecture at a high level (JSI, Fabric renderer, TurboModules).

**Topics**
1. Native vs cross-platform vs web trade-offs (including where Flutter/Kotlin still win).
2. Install: current Node LTS, an editor (VS Code), Android Studio emulator and/or Xcode simulator, Expo Go.
3. `npx create-expo-app@latest tasktrail`, project tree (`app/`, `assets/`, `app.json`, `tsconfig.json`).
4. Dev loop: Fast Refresh, `npx expo start`, QR code, LAN vs tunnel.
5. The Expo Go limits (§3) and when to move to a dev build.

**Key commands**
```bash
npx create-expo-app@latest tasktrail   # choose the SDK that matches store Expo Go if asked
cd tasktrail
npx expo start
npx expo-doctor@latest                  # checks for common project problems
npx expo install --fix                  # aligns package versions to your SDK
```

**Lab:** Run on device + emulator, change a `Text`, trigger and fix a deliberate TypeScript error, and screenshot the DevTools console.

---

## Module 1 — Modern JavaScript → TypeScript Fundamentals

> **In a nutshell:** A fast, practical TypeScript course for people who already know JS: types, interfaces, unions, narrowing, generics, `async/await`, and modules, always in the context of app data.

**What are we creating:** The **domain model** of TaskTrail (`Task`, `Priority`, `Place`) plus pure utility functions (sort, filter, group) with full types.

**Legacy ADET mapping:** Replaces the Kotlin/Java language refresher that sat implicitly under Modules 1–3.

**Runs in:** ✅ (plain TS; can also run with `npx tsx`)

**Outcomes**
- Model app data with `type`/`interface`, union types, and literal types.
- Narrow types safely and avoid `any`; use `unknown` at boundaries.
- Write generic helpers and typed async functions.

**Topics**
1. `strict` mode and what each flag catches.
2. Primitives, arrays, tuples, objects, `readonly`, `as const`.
3. Unions, discriminated unions, type guards, exhaustive `switch` with `never`.
4. Generics (`Array<T>`, `Promise<T>`, constraints), utility types (`Partial`, `Pick`, `Omit`, `Record`).
5. Modules (ES imports/exports), path aliases (`@/…`).
6. `async/await`, error handling, `Promise.all`.

**Key code**
```ts
export type Priority = 'low' | 'medium' | 'high';

export interface Task {
  id: string;
  title: string;
  done: boolean;
  priority: Priority;
  dueAt?: number;          // epoch ms
  place?: { lat: number; lng: number; label: string };
}

export function sortByPriority(tasks: readonly Task[]): Task[] {
  const rank: Record<Priority, number> = { high: 0, medium: 1, low: 2 };
  return [...tasks].sort((a, b) => rank[a.priority] - rank[b.priority]);
}

type Result<T> = { ok: true; value: T } | { ok: false; error: string };

export async function safe<T>(fn: () => Promise<T>): Promise<Result<T>> {
  try { return { ok: true, value: await fn() }; }
  catch (e) { return { ok: false, error: e instanceof Error ? e.message : 'Unknown error' }; }
}
```

**Lab:** Implement `groupByDay(tasks)`, `isOverdue(task, now)`, and a `Result<T>` consumer; every function must compile under `strict` with zero `any`.

---

## Module 2 — TypeScript for React & React Native

> **In a nutshell:** Typing components, props, children, events, hooks, and style objects, plus validating *runtime* data with Zod so types stay honest at API boundaries.

**What are we creating:** A typed `TaskCard` component API and a Zod schema that validates sample JSON into `Task`.

**Legacy ADET mapping:** Part of Module 3–4 (typed views). Replaces `findViewById` casts and XML attribute guessing with compile-time checking.

**Runs in:** ✅

**Outcomes**
- Type props with `type Props = {...}`; type event handlers and callbacks.
- Infer TypeScript types from Zod schemas with `z.infer`.
- Understand why SDK 58's Strict TypeScript API matters (no private deep imports; instance types for refs).

**Topics**
1. Function components, `ReactNode`, `ComponentProps<typeof View>`.
2. Typed `useState<T>`, `useReducer`, and discriminated-union actions.
3. Typed style: `StyleProp<ViewStyle>`, `StyleSheet.create`.
4. Zod schemas, `safeParse`, schema → type.
5. `tsc --noEmit` in CI; ESLint with `expo lint`.

**Key code**
```tsx
import { z } from 'zod';
import { StyleProp, ViewStyle, Pressable, Text } from 'react-native';

export const TaskSchema = z.object({
  id: z.string(),
  title: z.string().min(1),
  done: z.boolean(),
  priority: z.enum(['low', 'medium', 'high']),
  dueAt: z.number().optional(),
});
export type TaskDTO = z.infer<typeof TaskSchema>;

type TaskCardProps = {
  task: TaskDTO;
  onToggle: (id: string) => void;
  style?: StyleProp<ViewStyle>;
};

export function TaskCard({ task, onToggle, style }: TaskCardProps) {
  return (
    <Pressable onPress={() => onToggle(task.id)} style={style}>
      <Text>{task.done ? '✅' : '⬜'} {task.title}</Text>
    </Pressable>
  );
}
```

**Lab:** Validate a deliberately malformed JSON payload; show the Zod error list and why a TS type alone would not have caught it.

---

# PHASE 1 — The Modern UI

## Module 3 — Components, State & the "Lifecycle" (Activities → React)

> **In a nutshell:** Android's Activity lifecycle becomes React's render-and-effect model. State lives in hooks; side effects live in `useEffect` with cleanup; app foreground/background is observed with `AppState`.

**What are we creating:** A live **session timer** that pauses when the app goes to the background, and a counter-driven "tasks done today" widget.

**Legacy ADET mapping:** Module 3 (Activities & lifecycle). `onCreate/onResume/onPause` → mount/update/cleanup effects + `AppState`; Compose `remember`/`mutableStateOf` → `useState`/`useRef`/`useMemo`.

**Runs in:** ✅

**Outcomes**
- Predict when a component re-renders; avoid stale closures.
- Write effects with correct dependencies and cleanup.
- Distinguish *screen* lifecycle (Router focus) from *app* lifecycle (`AppState`).

**Topics**
1. Render cycle, state updates (batched, functional updates), derived state vs stored state.
2. `useEffect` timing, dependency arrays, cleanup, `useRef` for mutable values.
3. `useMemo`/`useCallback` (and when *not* to use them).
4. `AppState` (`active` / `background` / `inactive`).
5. Lifecycle comparison table (Android ↔ React).

**Key code**
```tsx
import { useEffect, useRef, useState } from 'react';
import { AppState, Text } from 'react-native';

export function SessionTimer() {
  const [seconds, setSeconds] = useState(0);
  const running = useRef(true);

  useEffect(() => {
    const sub = AppState.addEventListener('change', (s) => { running.current = s === 'active'; });
    const id = setInterval(() => { if (running.current) setSeconds((n) => n + 1); }, 1000);
    return () => { sub.remove(); clearInterval(id); };
  }, []);

  return <Text>Focused for {seconds}s</Text>;
}
```

**Lab:** Log every mount/update/unmount; reproduce a stale-closure bug and fix it; document the Android↔React lifecycle table in the README.

---

## Module 4 — Core Components (Views & Widgets → React Native Components)

> **In a nutshell:** The building blocks: `View`, `Text`, `Image` (prefer `expo-image`), `TextInput`, `Pressable`, `Switch`, `ScrollView`, `ActivityIndicator`, `Modal`, plus accessibility basics.

**What are we creating:** A polished **Task Detail screen** (title, notes input, priority switch, status chip, delete button) with accessibility labels.

**Legacy ADET mapping:** Module 4. `TextView→Text`, `EditText→TextInput`, `Button→Pressable`, `ImageView→Image`, `CheckBox/Switch→Switch`, `ProgressBar→ActivityIndicator`.

**Runs in:** ✅

**Outcomes**
- Pick the right core component and handle its props/events with types.
- Add accessibility (`accessibilityRole`, `accessibilityLabel`, minimum 44×44 touch targets).
- Know why `Text` must wrap all text in RN.

**Topics**
1. Core component catalog and typed props.
2. `Pressable` states (`pressed`) vs legacy touchables.
3. `TextInput`: keyboard types, `secureTextEntry`, `returnKeyType`, `onSubmitEditing`.
4. `expo-image` for caching and placeholders.
5. Accessibility and screen readers (TalkBack / VoiceOver).

**Key code**
```tsx
<Pressable
  accessibilityRole="button"
  accessibilityLabel="Delete task"
  onPress={onDelete}
  style={({ pressed }) => [styles.btn, pressed && styles.pressed]}
>
  <Text style={styles.btnText}>Delete</Text>
</Pressable>
```

**Lab:** Build the screen, then test it with TalkBack or VoiceOver and fix three accessibility issues you find.

---

## Module 5 — Layout (Flexbox, Safe Areas, Responsive UI)

> **In a nutshell:** RN uses Flexbox (column by default) instead of XML layouts. You learn `flex`, `gap`, alignment, absolute positioning, `useWindowDimensions`, safe-area insets, and orientation handling.

**What are we creating:** A responsive **Home screen skeleton** — header, summary row, list area, floating action button — that works on phones, tablets, and landscape.

**Legacy ADET mapping:** Module 5. `LinearLayout→View + flexDirection`, `ConstraintLayout→flex + absolute`, `FrameLayout→position:'absolute'`, Compose `Row/Column/Box→View` with direction.

**Runs in:** ✅

**Outcomes**
- Reason about main axis vs cross axis; use `flex`, `flexGrow`, `gap`.
- Respect safe areas with `react-native-safe-area-context`.
- Adapt to window size with `useWindowDimensions` (and breakpoints).

**Topics**
1. Flexbox model; `justifyContent`, `alignItems`, `flexWrap`.
2. Percent vs fixed sizes; `aspectRatio`.
3. Safe areas, edge-to-edge Android, keyboard avoidance.
4. Orientation and large screens (foldables/tablets; SDK 58 prepares for iPhone Duo).
5. Layout debugging with DevTools.

**Key code**
```tsx
import { useWindowDimensions, View } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';

export function Screen({ children }: { children: React.ReactNode }) {
  const { width } = useWindowDimensions();
  const insets = useSafeAreaInsets();
  const columns = width >= 700 ? 2 : 1;
  return (
    <View style={{ flex: 1, paddingTop: insets.top, paddingBottom: insets.bottom, paddingHorizontal: 16 }}>
      {children}
    </View>
  );
}
```

**Lab:** Recreate a given mockup three ways (phone portrait, landscape, tablet) and record screenshots.

---

## Module 6 — Styling, Theming & Assets (Resources → Tokens)

> **In a nutshell:** Centralize colors, spacing, and type into theme tokens; support light/dark mode; load fonts and images properly; and (optionally) adopt NativeWind (Tailwind-style) once you know `StyleSheet`.

**What are we creating:** A **design-token theme** (`theme.ts`), dark mode, custom font, app icon/splash assets, and a localized string table (English + Filipino).

**Legacy ADET mapping:** Module 8 (resources). `colors.xml/styles.xml → TS tokens`; `strings.xml → i18n objects/`expo-localization`; vector drawables → SVG or icon fonts; Material 3 dynamic theming → system color scheme + tokens.

**Runs in:** ✅ for styling/fonts/i18n; 🔧 for fully custom app icon/splash/name testing (Expo Go cannot apply most native config)

**Outcomes**
- Build a token-based theme and switch on `useColorScheme()`.
- Load custom fonts with `expo-font`; add app assets via `app.json`.
- Localize UI strings and format dates/numbers.

**Topics**
1. `StyleSheet.create` vs inline vs utility classes (NativeWind) — trade-offs.
2. Theme provider + typed tokens.
3. `expo-font`, `expo-image`, SVG, icon sets (`@expo/vector-icons`).
4. `expo-localization` and `Intl`.
5. App config: name, icon, splash, `scheme` (dev-build caveats).

**Key code**
```ts
// theme.ts
import { useColorScheme } from 'react-native';

const palette = {
  light: { bg: '#FFFFFF', card: '#F4F4F5', text: '#111827', primary: '#4F46E5' },
  dark:  { bg: '#0B0F19', card: '#161B27', text: '#F3F4F6', primary: '#818CF8' },
} as const;

export const spacing = { xs: 4, sm: 8, md: 16, lg: 24 } as const;

export function useTheme() {
  return palette[useColorScheme() === 'dark' ? 'dark' : 'light'];
}
```

**Lab:** Apply the theme to every existing screen, flip the system theme live, and add Filipino strings for the Home screen.

---

# PHASE 2 — Interaction & Navigation

## Module 7 — Event-Driven Programming (Events, Gestures, Forms, Animation)

> **In a nutshell:** Mobile apps are event loops: taps, long-presses, drags, keyboard, timers, and network responses all trigger handlers that update state, and state re-renders the UI. This module covers handlers as typed lambdas, **state hoisting**, gestures, validated forms, and animations that run off the JS thread.

**What are we creating:** The **Add/Edit Task form** (validated with React Hook Form + Zod) and a **swipe-to-complete** gesture with an animated check.

**Legacy ADET mapping:** Module 6 (event-driven programming). Anonymous inner classes / `OnClickListener` → arrow-function props; Kotlin lambdas → TS callbacks; Compose state hoisting → "lift state up".

**Runs in:** ✅

**Outcomes**
- Explain the event flow: native event → RN synthetic event → handler → state → render.
- Hoist state so children are stateless and testable.
- Build forms with schema validation and good error UX.
- Use Reanimated + Gesture Handler for 60 fps interactions.

**Topics**
1. Press events (`onPress`, `onLongPress`, `onPressIn/Out`), text events (`onChangeText`, `onBlur`, `onSubmitEditing`).
2. Event objects, debouncing and throttling.
3. State hoisting and controlled components.
4. Forms: `react-hook-form` + `zod` + `@hookform/resolvers`.
5. Keyboard handling (`KeyboardAvoidingView`, `Keyboard` events).
6. Gestures (`react-native-gesture-handler`) and animation (`react-native-reanimated`: shared values, `withSpring`, worklets).
7. Haptics (`expo-haptics`).

**Key code**
```tsx
import { useForm, Controller } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { TextInput, Text, Pressable, View } from 'react-native';

const schema = z.object({
  title: z.string().trim().min(1, 'Title is required').max(80),
  notes: z.string().max(500).optional(),
});
type FormValues = z.infer<typeof schema>;

export function TaskForm({ onSubmit }: { onSubmit: (v: FormValues) => void }) {
  const { control, handleSubmit, formState: { errors } } = useForm<FormValues>({
    resolver: zodResolver(schema),
    defaultValues: { title: '', notes: '' },
  });

  return (
    <View>
      <Controller
        control={control}
        name="title"
        render={({ field: { value, onChange, onBlur } }) => (
          <TextInput value={value} onChangeText={onChange} onBlur={onBlur} placeholder="Task title" />
        )}
      />
      {errors.title && <Text accessibilityLiveRegion="polite">{errors.title.message}</Text>}
      <Pressable onPress={handleSubmit(onSubmit)}><Text>Save</Text></Pressable>
    </View>
  );
}
```

**Version note:** In SDK 58's strict typing, refs to RN components use instance types (e.g., `TextInputInstance`). If you focus the next field programmatically, use the type your SDK's migration guide shows.

**Lab:** Build the form; add a swipe gesture with a spring animation; write the event-flow diagram for "tap Save" from touch to re-render.

---

## Module 8 — Navigation with Expo Router (Intents → Routes)

> **In a nutshell:** Screens are **files**. `app/(tabs)/index.tsx` is a route, `app/task/[id].tsx` is a dynamic route, `_layout.tsx` defines the navigator (Stack, Tabs). Links, params, modals, redirects, and **deep links** come built in.

**What are we creating:** TaskTrail's **navigation shell**: bottom tabs (Tasks, Map, Settings), a Task Detail stack screen with a typed `id` param, a modal "Add Task" screen, and a working deep link (`tasktrail://task/42`).

**Legacy ADET mapping:** Module 7 (Intents & navigation). Explicit Intent → `router.push`; Intent extras → route params; implicit Intent / App Links → deep links (`Linking`); Navigation Compose NavHost → file-based routes.

**Runs in:** ✅ (deep-link *scheme* testing is best in a dev build)

**Outcomes**
- Map a folder layout to URLs and navigators.
- Pass and read typed params; protect routes (auth redirect).
- Open external apps/URLs with `Linking`.

**Topics**
1. File-based routing: groups `(tabs)`, dynamic `[id]`, catch-all `[...rest]`, `+not-found`.
2. `<Stack>`, `<Tabs>`, modal presentation; header configuration.
3. `Link`, `router.push/replace/back`, `useLocalSearchParams`.
4. Typed routes (`experiments.typedRoutes` in app config).
5. Deep links and the `scheme` field in `app.json`.
6. Native tabs (`expo-router/native-tabs` in SDK 58; `unstable-native-tabs` in 57).
7. Auth gates (redirect from layout).

**Key structure & code**
```
app/
  _layout.tsx            // root <Stack>
  (tabs)/
    _layout.tsx          // <Tabs>
    index.tsx            // Tasks
    map.tsx
    settings.tsx
  task/[id].tsx          // detail
  add.tsx                // presented as modal
```
```tsx
// app/(tabs)/index.tsx
import { Link } from 'expo-router';
<Link href={{ pathname: '/task/[id]', params: { id: task.id } }}>{task.title}</Link>

// app/task/[id].tsx
import { useLocalSearchParams } from 'expo-router';
const { id } = useLocalSearchParams<{ id: string }>();
```

**Lab:** Build the shell, trigger `tasktrail://task/42` from the OS (via `npx uri-scheme open` or `adb`/`xcrun simctl openurl`), and handle "task not found" gracefully.

---

## Module 9 — Lists & Data Display (Adapters → FlatList)

> **In a nutshell:** Lists are the core of most apps. `FlatList` virtualizes rows so only visible items render. You pass typed arrays, a `renderItem`, and a stable `keyExtractor` — no adapters, no `HashMap`s.

**What are we creating:** The **Task List screen**: sections by day, pull-to-refresh, empty state, swipe actions, and search/filter.

**Legacy ADET mapping:** Module 20 (data lists). `SimpleAdapter` + `HashMap` → typed array + `renderItem`; `RecyclerView` → `FlatList` (or FlashList for heavy lists); `ListView` empty view → `ListEmptyComponent`.

**Runs in:** ✅

**Outcomes**
- Render large lists efficiently and type the item model.
- Implement refresh, pagination hooks, sections, headers/footers, separators.
- Diagnose list jank (inline functions, missing keys, heavy rows).

**Topics**
1. `FlatList` vs `SectionList` vs `ScrollView`.
2. `keyExtractor`, `getItemLayout`, `initialNumToRender`, `windowSize`.
3. Memoized row components (`React.memo`) and stable callbacks.
4. Pull-to-refresh (`refreshing`/`onRefresh`), infinite scroll (`onEndReached`).
5. Search with debounced input; empty/error/loading states.

**Key code**
```tsx
<FlatList
  data={filteredTasks}
  keyExtractor={(t) => t.id}
  renderItem={({ item }) => <TaskCard task={item} onToggle={toggle} />}
  ItemSeparatorComponent={() => <View style={{ height: 8 }} />}
  ListEmptyComponent={<Text>No tasks yet. Tap + to add one.</Text>}
  refreshing={isRefreshing}
  onRefresh={refetch}
/>
```

**Lab:** Generate 5,000 fake tasks, profile scrolling with and without `React.memo`, and write down the measured difference.

---

# PHASE 3 — System Events & Background Operations

## Module 10 — Alerts, Modals & Notifications

> **In a nutshell:** Ask the user for decisions (alerts/modals) and reach them outside the app (notifications). **Local** notifications work in Expo Go; **remote push** needs a development build and credentials.

**What are we creating:** A **task reminder**: choose a time, get permission, schedule a local notification, and tap it to open the right Task Detail screen. Stretch: register for an Expo push token (dev build).

**Legacy ADET mapping:** Module 10. Android 13 `POST_NOTIFICATIONS` runtime permission → `expo-notifications` permission request; `NotificationChannel` → `setNotificationChannelAsync`; `AlertDialog` → `Alert.alert` / state-driven `Modal`.

**Runs in:** ✅ local notifications · 🔧 remote push (not supported in Expo Go since SDK 53)

**Outcomes**
- Request notification permission at the right moment with context.
- Create Android channels; schedule, cancel, and handle taps.
- Explain the push pipeline (app → Expo push service → FCM/APNs → device).

**Topics**
1. `Alert.alert` vs custom `Modal` vs bottom sheets.
2. Permission UX patterns (pre-prompt → system prompt → settings fallback).
3. `expo-notifications`: handler, channels, scheduling, listeners, response handling.
4. Push tokens, credentials, tickets & receipts (dev build).
5. Notification data → deep link.

**Key code**
```ts
import * as Notifications from 'expo-notifications';

Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldPlaySound: false,
    shouldSetBadge: false,
    shouldShowBanner: true,
    shouldShowList: true,
  }),
});

export async function scheduleReminder(taskId: string, title: string, at: Date) {
  const { status } = await Notifications.requestPermissionsAsync();
  if (status !== 'granted') return null;

  await Notifications.setNotificationChannelAsync('reminders', {
    name: 'Reminders',
    importance: Notifications.AndroidImportance.HIGH,
  });

  return Notifications.scheduleNotificationAsync({
    content: { title: 'Task due', body: title, data: { taskId } },
    trigger: { type: Notifications.SchedulableTriggerInputTypes.DATE, date: at, channelId: 'reminders' },
  });
}
```

**Lab:** Schedule a reminder 30 seconds out; background the app; tap the notification; route to `/task/[id]`. Document what *didn't* work in Expo Go vs a dev build.

---

## Module 11 — App & System Events (Broadcast Receivers → Listeners)

> **In a nutshell:** There are no `BroadcastReceiver`s in RN. You subscribe to JS event sources (`AppState`, `NetInfo`, `Linking`, `Keyboard`, `Dimensions`/`Appearance`) and **always unsubscribe in effect cleanup**.

**What are we creating:** A **System Status bar** for TaskTrail that shows online/offline state, a "sync paused" banner when offline, and reacts to incoming deep links and theme changes.

**Legacy ADET mapping:** Module 11. Android 8+ implicit-broadcast limits and `DisposableEffect` registration → effect-with-cleanup listeners; `ACTION_BATTERY_LOW` → `expo-battery`; airplane/connectivity → `@react-native-community/netinfo`.

**Runs in:** ✅

**Outcomes**
- Build a reusable `useOnlineStatus()` hook.
- Explain why leaked subscriptions cause bugs and memory leaks.
- Choose the right API for each classic Android broadcast.

**Topics**
1. `AppState`, `Appearance`/`useColorScheme`, `Keyboard`.
2. `NetInfo` (connectivity type, reachability).
3. `Linking.addEventListener('url', …)` and `getInitialURL()`.
4. `expo-battery`, `expo-device`, `expo-network` (use what your SDK exposes).
5. Mapping table: Android broadcast → RN/Expo equivalent.

**Key code**
```ts
import { useEffect, useState } from 'react';
import NetInfo from '@react-native-community/netinfo';

export function useOnlineStatus() {
  const [online, setOnline] = useState<boolean | null>(null);
  useEffect(() => {
    const unsubscribe = NetInfo.addEventListener((s) => setOnline(s.isConnected ?? null));
    return unsubscribe;
  }, []);
  return online;
}
```

**Lab:** Toggle airplane mode on a device and show the banner; leave a listener un-cleaned on purpose, log duplicate events, then fix it.

---

## Module 12 — Background Work (Services & WorkManager → Background Tasks)

> **In a nutshell:** Mobile OSes aggressively limit background work. `expo-background-task` runs **deferrable** JS work (it uses WorkManager on Android and BGTaskScheduler on iOS) with no guarantee of exact timing. It is for syncing and prefetching, not for tickers or exact alarms.

**What are we creating:** A **background sync task** that uploads pending (offline-created) tasks and logs each run, plus an in-app "last sync" indicator.

**Legacy ADET mapping:** Module 12. Foreground-service types / long-running Services → generally *not available in managed Expo* (ongoing location tracking uses `expo-location` background mode); WorkManager → `expo-background-task` (it literally wraps it on Android).

**Runs in:** 🔧 **Development build required.** Per the Expo TaskManager docs, in Expo Go `TaskManager` is not available on Android and does not support background execution on iOS. Background tasks are also not available on iOS simulators — use a **physical iPhone**.

**Outcomes**
- Define tasks at module scope and register them correctly.
- Explain why timing is OS-controlled and how to test with the trigger helper.
- Design idempotent sync operations (safe to run twice).

**Topics**
1. Why background execution is restricted (battery, Doze, App Standby, iOS BGTaskScheduler).
2. `TaskManager.defineTask` (must run at **module scope**, not inside a component).
3. `BackgroundTask.registerTaskAsync`, status, unregister.
4. Single shared worker: multiple tasks all run through one worker; the minimum interval is determined by the last registered task.
5. Testing: `triggerTaskWorkerForTestingAsync`, `adb` job inspection.
6. Idempotency, retries, and conflict handling.

**Key code**
```ts
import * as TaskManager from 'expo-task-manager';
import * as BackgroundTask from 'expo-background-task';

const SYNC_TASK = 'tasktrail-sync';

TaskManager.defineTask(SYNC_TASK, async () => {
  try {
    await syncPendingTasks();                       // your idempotent function
    return BackgroundTask.BackgroundTaskResult.Success;
  } catch {
    return BackgroundTask.BackgroundTaskResult.Failed;
  }
});

export async function enableSync() {
  await BackgroundTask.registerTaskAsync(SYNC_TASK, { minimumInterval: 15 }); // minutes; verify in your SDK docs
}
```

**Lab:** Build a dev build, register the task, press a debug button that calls `triggerTaskWorkerForTestingAsync`, and show the log. Write one paragraph on why you can't promise users "syncs every 5 minutes."

---

## Module 13 — Scheduling (Alarms & Schedulers → Triggers & Policies)

> **In a nutshell:** Choose the right tool for *when* something happens: **notification triggers** for user-visible reminders at a time/interval, **background tasks** for deferrable work, **foreground timers** for in-app countdowns. RN does not expose exact-alarm APIs in managed Expo, so design for "approximately on time."

**What are we creating:** A **recurring reminder system** (daily/weekly) and a **decision chart** for "which scheduler for which job" in TaskTrail.

**Legacy ADET mapping:** Module 13. `AlarmManager` exact alarms and `SCHEDULE_EXACT_ALARM` → scheduled notifications (the OS owns delivery timing); `WorkManager` → background tasks; `Handler.postDelayed` → timers in effects.

**Runs in:** ✅ scheduled local notifications · 🔧 background tasks

**Outcomes**
- Compare timing guarantees across the three mechanisms.
- Schedule, list, and cancel notifications; avoid duplicate schedules.
- Handle device reboot/timezone expectations (test, don't assume).

**Topics**
1. Trigger types: date, time-interval, daily, weekly, calendar-style (as your SDK exposes).
2. Managing schedules: `getAllScheduledNotificationsAsync`, `cancelScheduledNotificationAsync`.
3. Doze and OEM battery savers (Philippine-market Android OEM quirks: aggressive app killing).
4. Foreground timers: `setInterval`, `requestAnimationFrame`, cleanup.
5. Idempotent scheduling keyed by `taskId`.

**Key code**
```ts
// cancel then re-schedule so editing a task never duplicates its reminder
await Notifications.cancelScheduledNotificationAsync(task.reminderId);
const reminderId = await scheduleReminder(task.id, task.title, newDate);
```

**Lab:** Build the "which scheduler?" decision table for 6 scenarios (e.g., "remind me at 7:30 sharp", "sync when on Wi-Fi", "pomodoro countdown") and justify each choice.