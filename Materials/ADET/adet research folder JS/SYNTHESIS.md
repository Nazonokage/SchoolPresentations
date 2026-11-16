# ADET combined topic bank and compilation basis

**3 November update:** [Current compiled contents](../ADET_compiled%20contents.md) now provides a working 20-module sequence and alternating assessments. MongoDB or MySQL/MariaDB through a custom API are the primary backend choices; BaaS remains comparison material. Earlier open module-count notes below are historical.

[Research home](README.md)

## Coverage to retain across the reports

| Topic family | Material to include in the future contents | Candidate practical result |
| --- | --- | --- |
| Foundation and toolchain | Short JS/TS refresher, Expo/RN roles, Metro/Hermes, native versus cross-platform, Go/build distinction, architecture overview | First working Expo campus screen |
| Components and lifecycle | Typed props/state, hooks, effects/cleanup, focus and AppState, custom hooks | Reusable task/office card and interactive counter |
| Layout, assets and inclusion | Core views, safe areas, Flexbox, responsive UI, themes, images/fonts/icons, accessibility/localization | Readable themed campus interface |
| Interaction and state | Press/input/keyboard events, gestures/animation, useState/reducer/Context and Zustand comparison | Editable task/order flow |
| Navigation and lists | Router stack/tab/dynamic routes, parameters/deep links, FlatList/SectionList/FlashList, refresh/pagination | List/detail screens with stable IDs |
| Data and forms | fetch/Axios, JSON checks, TanStack Query, form controls, React Hook Form/Zod, loading/error/empty states | Validated form and cached API view |
| Persistence and offline | AsyncStorage, SQLite, MMKV, optional Drizzle; cache versus durable state; sync/conflicts and optimistic changes | A checklist that survives restart |
| Identity and authorization | Mock versus real login, provider redirect, AuthSession, JWT/refresh-token concepts, SecureStore, backend policies | Session-flow demonstration and ownership checks |
| Backend options | Supabase/Firebase/custom Node/PHP, REST/GraphQL, API routes, server hosting and secrets | Small client/backend CRUD example |
| Notifications and system events | Alerts/modals, local/remote notifications, app/network/battery/orientation events, subscriptions and cleanup | Reminder demo and app-state indicator |
| Background work | TaskManager/BackgroundTask, scheduling versus exact alarms, constraints and force-quit behavior | Deferrable-work demonstration or scheduling decision table |
| Native handoff and system data | Share/Sharing/Linking, dialer/SMS/email, contacts/media-library, privacy | Share a task or select minimal sample data |
| Hardware and multimedia | Image picker/camera, audio/video, location/maps, foreground/background/geofencing and sensors | One permission-aware attachment or map feature |
| Quality and release | Tests, profiling, render/list optimization, security, privacy, EAS Build/Submit/Update, CI/CD, release notes | Tested release candidate and deployment plan |
| Monetization and emerging topics | RevenueCat/IAP/ads, AI via trusted backend, Expo UI/modules, widgets/App Intents, server features | Small experimental prototype or comparative design review |

## How to compile the later contents

Follow the EDP document style: each module has an **in-a-nutshell explanation**, **what we will discuss**, **what we will create**, detailed numbered subtopics, outcomes/evidence, prerequisites, and a practical-versus-demonstration label. Preserve the broad source coverage while choosing a manageable primary behavior for each meeting.

Keep a short Day 1 refresher rather than consuming the early term with a second introductory programming course. Introduce components and React state explicitly; the reports' React prerequisites are not proof our students already know them.

Teach useState and plain validated input before introducing multiple external state/form libraries. Use one default styling approach first, then compare NativeWind/Unistyles. Demonstrate the reason for TanStack Query after a small fetch example. Avoid requiring every alternative library in one student project.

TaskTrail is a useful running-project candidate. Supply independent complete checkpoints so a broken previous lab does not block later learning. Offer one or two extensions to each student rather than demanding auth, maps, push, voice, AI, offline sync and store publication together in a solo final project.

Use explicit runtime labels: Expo Go candidate, development-build/device requirement, server-hosted feature, or conceptual demonstration. Compatibility must be verified per API, SDK and platform before assigning a lab; the reports' blanket compatibility tables are not a tested baseline.

Keep EDP and ADET complementary: EDP explains event flow and asynchronous behavior in depth; ADET applies those concepts to usable mobile interfaces and data. Browser script-tag listeners are not React Native DOM APIs.

## Open items

- Final ADET module count and period allocation; previous 17-topic planning is historical and the new source bank contains more material.
- Actual SDK/React Native/React/TypeScript versions and Expo Go match.
- Device availability, dev-build setup and classroom network constraints.
- Current package APIs for Zustand, React Hook Form/Zod, NativeWind/Unistyles, RevenueCat, FlashList/Drizzle and platform-native extensions.
- Current app-store policies and provider-specific OAuth setup.
- Missing continuation of Report 2, if the user has more material.

These do not prevent collecting the topics now. They must be resolved or labeled before publishing executable lessons.
