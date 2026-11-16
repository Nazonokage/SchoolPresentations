# ADET technical review of supplied research

[Research home](README.md) | [Source checks](SOURCE_CHECKS.md)

## Corrections supported by inspected documentation

1. **BackgroundFetch is deprecated.** Use the documented BackgroundTask path for new deferrable-work teaching, with TaskManager where appropriate. It wraps platform scheduling rather than abolishing WorkManager/BGTaskScheduler. It does not promise exact periodic execution. [BackgroundFetch](https://docs.expo.dev/versions/latest/sdk/background-fetch/), [BackgroundTask](https://docs.expo.dev/versions/latest/sdk/background-task/).
2. **App termination matters.** OS constraints and user termination affect background tasks. Do not promise continuous execution after the app is closed, force-killed, or rebooted across all devices. Distinguish minimized, system-terminated, user-terminated and restarted states using the selected platform's documentation. [BackgroundTask](https://docs.expo.dev/versions/latest/sdk/background-task/).
3. **Update the media choices.** expo-av is deprecated. Use expo-audio for new audio examples and check expo-video for video. A new library does not remove platform audio/interruption configuration requirements. [AV legacy page](https://docs.expo.dev/versions/latest/sdk/av/), [Audio](https://docs.expo.dev/versions/latest/sdk/audio/).
4. **Expo APIs do not bypass permission requirements.** The notification documentation specifically states remote push is unavailable in Expo Go on Android from SDK 53 and requires a development build; local notifications remain available there. Keep this scoped statement rather than extending it unverified to every platform. [Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/).
5. **OTA compatibility is bounded.** Updates must match the installed native runtime; native-code changes require a compatible new build. Do not promise every fix reaches all users instantly. [Runtime versions](https://docs.expo.dev/eas-update/runtime-versions/).
6. **Client environment variables are visible.** EXPO_PUBLIC values are embedded in the application. A .env file, obfuscation or build-time key injection does not make a private client credential secret. [Environment variables](https://docs.expo.dev/guides/environment-variables/).
7. **MMKV is not a no-setup Expo Go assumption.** The maintainer's installation includes native dependencies and Expo prebuild. Choose and test its version/native-build route, and keep an accessible persistence baseline. Do not inherit benchmark claims as a guarantee for the classroom app. [MMKV](https://github.com/mrousavy/react-native-mmkv).
8. **Cached queries are not guaranteed background synchronization.** TanStack Query's React Native integrations include network/focus handling. Specify when work executes and how offline persistence/conflicts are handled; query caching alone is not a complete offline sync engine. [TanStack React Native guide](https://tanstack.com/query/latest/docs/framework/react/react-native).
9. **Server routes need a server runtime.** API files in an Expo project do not make a distributed mobile binary a private always-on backend. Document deployment and the URL used by the client. [Expo API routes](https://docs.expo.dev/router/web/api-routes/).
10. **Supabase requires authorization policies.** Sign-in and a hidden screen do not enforce row ownership. Teach database/RLS policy design and protect privileged server credentials. [Supabase RLS](https://supabase.com/docs/guides/database/postgres/row-level-security).
11. **Distinguish sharing APIs.** React Native Share supports text sharing; Expo Sharing is relevant for sharing files. Linking opens supported destinations rather than silently sending messages. [Share](https://reactnative.dev/docs/share), [Sharing](https://docs.expo.dev/versions/latest/sdk/sharing/).

## Claims to correct or verify before teaching

- TypeScript interfaces and props do not eliminate runtime bugs or validate fetched JSON. Runtime guards/schemas and error paths remain necessary.
- Do not call a selected framework the universal 2026 industry standard or claim a universal industry migration from Redux to Zustand. Explain the choice and trade-offs.
- Zustand, memoization and styling libraries do not automatically prevent all unnecessary renders or guarantee lag-free interfaces. Measure before optimizing.
- Expo Router and Next.js share file-routing ideas but are not conceptually identical in every routing, navigation or server behavior. OS handoffs and intents are not simply replaced by in-app routes.
- New Architecture/JSI can permit synchronous interactions; do not generalize that all native calls are synchronous. Pin the architecture explanation to tested RN/Expo versions.
- Report 2's precise SDK release dates, RN versions, iOS versions, native-tab imports and universal Expo-account login requirement remain unverified here. Do not adopt that compatibility table as established fact.
- OAuth access tokens are not necessarily JWTs; provider-specific flows and redirects need verification. A mock session is not real authorization. SecureStore helps storage, not every aspect of authentication security.
- Supabase/Firebase and PHP/MySQL are architectural choices. Custom backends remain valid; free hosting such as the pasted InfinityFree suggestion must be verified before assigning it.
- OS contact/media APIs are capability-specific interfaces, not one-for-one replacements for all Android ContentProvider behavior.
- Hermes defaults, Flipper availability, obfuscation/R8/ProGuard, native map keys and performance tools are version/platform-sensitive. No Acer or other specific laptop brand is a requirement.
- App-store testing periods, fees, bundle requirements and monetization policies require current official platform documentation. The supplied 14-day statement is not adopted as a universal rule.
- RevenueCat, widgets, native UI, AI tools and experimental server components need separate implementation references. A rule-based fallback is not an AI model; live model access needs a trusted server boundary.

Imported skeletons have not been executed. The review identifies specific concerns; it is not a complete code audit or production certification.
