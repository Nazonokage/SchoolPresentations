**Complete Course: Application Development and Emerging Technologies**  
**Focus: Modern Cross-Platform Mobile Apps with TypeScript, React Native & Expo**

This course modernizes the original Android (Java/Kotlin + XML/Compose) curriculum into the current industry standard: **TypeScript + React Native + Expo (managed workflow + Expo Go for rapid development, EAS for production)**.  

It keeps the same phase structure so it maps cleanly to your existing materials, but every topic is rewritten for declarative React, file-based routing (Expo Router), strong TypeScript, modern Expo SDK modules, and 2025–2026 best practices (New Architecture is default, Expo Router is the primary navigation solution, TanStack Query for data, Zustand/Context for state, etc.).

---

### Course Goals
- Build production-ready iOS + Android apps from a single TypeScript codebase.
- Master Expo’s managed workflow, Expo Router, and the major Expo SDK modules.
- Apply modern patterns: type-safe navigation, state management, networking, offline-first, permissions, background work, and deployment via EAS.
- Produce a portfolio of real apps (notes/todo, social feed, maps + location, media player, full-stack CRUD with auth).

**Prerequisites**: Basic JavaScript/TypeScript and React (hooks, components, props, state). No prior mobile experience required.

**Tech Stack (2026 standard)**:
- TypeScript (strict)
- React Native + Expo (latest SDK, currently 58 era)
- Expo Router (file-based, typed routes)
- TanStack Query (server state)
- Zustand or Context + useReducer (client state)
- React Hook Form + Zod (forms)
- NativeWind / StyleSheet (styling)
- Expo modules: notifications, location, camera, media, secure-store, background-task, etc.
- EAS Build + Submit + Update

---

### Phase 1: Foundations & The Modern UI

**Module 1–2: Introduction to the React Native + Expo Platform**
- What is React Native vs native vs hybrid. Why Expo dominates in 2026.
- Android/iOS architecture overview from a JS/TS perspective (bridge → New Architecture / JSI / Fabric / TurboModules).
- Setting up the environment: Node, Expo CLI, Expo Go, Android Studio / Xcode (or Expo Device Hub), TypeScript strict mode.
- Creating a project with `npx create-expo-app@latest` (TypeScript template).
- Project structure, `app.json` / `app.config.ts`, Expo SDK modules, development builds vs Expo Go.
- Modern update: New Architecture is always on; Expo Go for rapid iteration, development builds when native modules require it.

**Module 3: Components, Screens & Lifecycle**
- Functional components, hooks (`useState`, `useEffect`, `useMemo`, `useCallback`, custom hooks).
- Screen lifecycle in React Native / Expo (focus/blur via Expo Router or React Navigation events, AppState).
- State management fundamentals (`useState` + `useReducer`).
- Modern update: Declarative UI + React lifecycle instead of Activity lifecycle methods. Type-safe props and state with TypeScript.

**Module 4: Core Views & Widgets**
- Core components: `View`, `Text`, `Image`, `Pressable`, `TextInput`, `ScrollView`, `SafeAreaView`, `ActivityIndicator`, etc.
- Mapping legacy concepts: TextView → Text, Button → Pressable, etc.
- Styling: StyleSheet, Flexbox (default column), Platform-specific styles, responsive design, dark/light theming.
- Modern update: Prefer functional components + TypeScript interfaces for props. Introduce NativeWind (Tailwind for RN) as optional modern styling approach.

**Module 5: Layouts (Arranging the UI)**
- Flexbox deep dive (flexDirection, justifyContent, alignItems, gap, etc.).
- `Row` / `Column` patterns with View, absolute positioning, dimensions.
- Lists: FlatList / FlashList / SectionList for performance.
- Modern update: No nested LinearLayout/ConstraintLayout boilerplate. Compose-like declarative layout with Flexbox + Expo Router layouts.

**Module 8: Resources & Assets**
- Images (local + remote with expo-image), fonts (expo-font, variable fonts), icons, colors, strings (i18n with expo-localization).
- Asset management, SVG support, theming (light/dark with system preference).
- Modern update: Vector assets preferred, Material Design / platform-native feel, dynamic theming.

---

### Phase 2: Interaction & Navigation

**Module 6: Event-Driven Programming**
- Handling presses, long-presses, gestures (Gesture Handler + Reanimated).
- Keyboard handling, text input events, form state.
- Modern update: Lambda-style event handlers (`onPress={() => ...}`), state hoisting, controlled components. Type-safe event handlers.

**Module 7: Navigation (Expo Router)**
- File-based routing (the modern standard).
- Stacks, Tabs, Drawers, nested navigators, route groups `(group)`, dynamic routes `[id]`, modals.
- Typed routes, deep linking, URL params, `useRouter`, `useLocalSearchParams`, `Link`.
- Passing data, protected routes, authentication flows.
- Modern update: Expo Router replaces explicit Intents + React Navigation config in most cases. Full TypeScript inference for routes and params. Automatic deep linking.

**Module 20: Data Lists & Performance**
- FlatList / FlashList best practices (keyExtractor, getItemLayout, windowSize, etc.).
- Infinite scroll, pull-to-refresh, optimistic updates.
- Strongly-typed data with TypeScript interfaces / Zod schemas.
- Modern update: No Adapters or HashMaps. Typed data + virtualized lists + TanStack Query for remote data.

---

### Phase 3: Background Operations & System Events

**Module 10: Notifications & Dialogs**
- Local & push notifications with `expo-notifications`.
- Permissions (Android 13+ POST_NOTIFICATIONS, iOS), channels, categories, interactive buttons.
- In-app dialogs / modals (Alert, custom modal screens with Expo Router presentation).
- Modern update: Unified Expo API. Note: full remote push requires a development build (not Expo Go on recent SDKs). Background handling with task manager.

**Module 11: System Events & Broadcast-style Behavior**
- AppState, NetInfo, DeviceEventEmitter patterns.
- Listening for system changes (connectivity, battery, orientation) safely.
- Modern update: React hooks + Expo modules instead of BroadcastReceivers. Use `useEffect` + cleanup (or `DisposableEffect`-style patterns).

**Module 12: Background Tasks & Work-like Scheduling**
- `expo-task-manager` + `expo-background-task` (WorkManager on Android, BGTaskScheduler on iOS).
- Deferrable work, background fetch/sync, surviving app kill/reboot.
- Constraints (battery, network, charging).
- Modern update: Preferred over old background services for most use cases. Clear distinction between deferrable tasks and foreground services.

**Module 13: Scheduling & Alarms**
- Local notification scheduling, exact vs inexact, recurring tasks.
- Background location / geofencing when needed.
- Modern update: Platform limits and battery-friendly approaches. Prefer WorkManager-style APIs via Expo.

---

### Phase 4: Device Hardware & External Integrations

**Module 14: Messaging, Sharing & System Intents**
- Sharing content via native Sharesheet (`expo-sharing` / Share API).
- Opening phone, SMS, email, maps, browser with Linking / Intent-like APIs.
- Modern update: Secure, permission-light hand-off to system apps. No heavy third-party SDKs for basic sharing.

**Module 15: Social & Auth Integrations**
- Native share sheet + deep links / App Links / Universal Links.
- Authentication: Expo AuthSession, Firebase Auth, Supabase, Clerk, or custom OAuth 2.0 / JWT.
- Modern update: Prefer system sharesheet and secure OAuth flows over legacy social SDKs.

**Module 16: Location-Based Services**
- `expo-location` (foreground + background), permissions, geofencing.
- Maps with `react-native-maps` or Expo-compatible map libraries + markers, routes.
- Modern update: Type-safe location objects, proper permission UX, battery-aware tracking.

**Module 19: Multimedia**
- Camera & ImagePicker (`expo-camera`, `expo-image-picker`).
- Audio / Video with `expo-av` or Media3-style players, expo-video.
- Media library access, recording, playback controls.
- Modern update: Modern Expo media modules + Reanimated for smooth UI.

---

### Phase 5: Data, Networking & APIs

**Module 18: Networking & Parsing**
- Fetch / Axios / Expo’s networking.
- TanStack Query (React Query) for caching, retries, pagination, mutations, optimistic updates.
- JSON handling, TypeScript types / Zod validation.
- Modern update: Replace raw HttpURLConnection-style code with typed, cached, offline-capable data layer.

**Module 21: Local Data & Content Providers-style Sharing**
- AsyncStorage / MMKV / expo-sqlite / expo-secure-store.
- Offline-first patterns, sync strategies.
- Sharing data between apps (limited; prefer files, share sheet, or backend).
- Modern update: Strong typing + secure storage. Room-like patterns via SQLite + TypeScript.

**Module 22: APIs, Authentication & Third-Party Services**
- REST / GraphQL consumption, API versioning, error handling.
- Auth flows (JWT, refresh tokens, protected routes in Expo Router).
- Firebase / Supabase / custom backend integration.
- Modern update: Secure token storage, type-safe API clients, OAuth 2.0 best practices.

**Module 23: Full-Stack Integration (Backend)**
- Connecting to Node / PHP / any backend (or Supabase/Firebase).
- Secure practices (prepared statements / parameterized queries on backend, HTTPS, proper CORS).
- Client-side: typed Retrofit-style clients with TanStack Query + Zod.
- Modern update: Emphasis on end-to-end type safety and security.

---

### Phase 6: Security, Optimization & Deployment

**Module 24: Permissions, Performance & Security**
- Runtime permissions UX, privacy manifests.
- Performance: list virtualization, memoization, Reanimated, New Architecture benefits, profiling.
- Security: secure storage, certificate pinning considerations, data encryption, preventing leaks.
- Accessibility, internationalization.
- Modern update: Coroutines → async/await + TanStack Query; Jetpack Security → expo-secure-store + best practices.

**Module 25: Publishing, Monetization & Emerging Topics**
- EAS Build (development, preview, production), EAS Submit, App Store / Play Console.
- Over-the-Air updates (EAS Update).
- App bundles / AAB, signing, testing tracks.
- Monetization: in-app purchases, subscriptions (RevenueCat or native), ads.
- Emerging: App Intents / Siri / Apple Intelligence exposure, home screen widgets, foldables, AI-assisted features, server components / data loaders in Expo Router.
- Modern update: Mandatory modern formats, cloud builds, continuous delivery with Expo.

---

### Suggested Learning Path & Projects
1. **Weeks 1–4**: Foundations → simple multi-screen app with Expo Router + TypeScript.
2. **Weeks 5–8**: Navigation + state + lists → notes/todo or habit tracker with local persistence.
3. **Weeks 9–12**: Networking + auth + notifications → social feed or booking app.
4. **Weeks 13–16**: Device features (camera, location, media) + background tasks.
5. **Weeks 17–20**: Full-stack app + performance + deployment to stores.

**Capstone ideas**:
- Full-stack food ordering / expense tracker / community app with auth, maps, push, offline support, and EAS deployment.

**Extra Modern Topics to Weave In**
- Strict TypeScript everywhere (typed routes, API responses, forms).
- Offline-first + optimistic UI.
- Accessibility & internationalization.
- Testing (Jest + React Native Testing Library).
- CI/CD with EAS + GitHub Actions.
- Emerging: Expo Modules 2.0, App Intents, widgets, server-side features in Expo Router.

This outline is ready to expand into full lesson plans, code labs, quizzes, and projects. Want me to expand any specific module into detailed lessons + code examples, create a syllabus document, or generate starter project templates next? Just say the word.