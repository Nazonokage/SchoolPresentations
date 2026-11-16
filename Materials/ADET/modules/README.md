# ADET — 22 lessons, M00–M21

**Migration status.** M00–M05 were rewritten in the approved opener style. **M06–M21 were rewritten in a second pass** to the same style: plain-words intro, concept table, predict-then-trace, misconception, common mistakes, commented code with conventional names, "Install first", instructor notes and answer keys. Lesson text and example code are generated from the same files, and every example type-checks. Nothing here has been run on a phone yet; see the verification notes below.

[Prepared starter](../offline-lab/README.md) · [Examples](../examples/README.md) · [Teaching guide](../instructor/TEACHING_GUIDE.md)

Periods are flexible planning groups, not promised class dates. Reserve separate summative and periodical exam meetings. M03 and M04 are intentionally both coding. M20 is 20 questions plus two essays; M21 is the solo mini-capstone. If finals has only two teaching meetings, schedule M19 earlier and preserve M20 and M21. Course versions (Expo SDK 58, React Native, TypeScript, Node, npm) are recorded in [M01](ADET_M01.md).

| Period | Lesson | Classroom evidence |
|---|---|---|
| Prelim | [M00 · What is app development?](ADET_M00.md) | 10-item quiz |
| Prelim | [M01 · React Native platform, tools and first app](ADET_M01.md) | Individual coding activity |
| Prelim | [M02 · Screens, components and lifecycle](ADET_M02.md) | 10-item quiz |
| Prelim | [M03 · Layout and a login form](ADET_M03.md) | Individual coding activity |
| Prelim | [M04 · Reusable components and accessible screen](ADET_M04.md) | Individual coding activity |
| Prelim | [M05 · Navigation and application structure](ADET_M05.md) | 10-item quiz |
| Midterm | [M06 · Lists and shared client state](ADET_M06.md) | Individual coding activity |
| Midterm | [M07 · HTTP, APIs and asynchronous data](ADET_M07.md) | 10-item quiz |
| Midterm | [M08 · Persistent CRUD through a database API](ADET_M08.md) | Individual coding activity |
| Midterm | [M09 · Local storage and offline behavior](ADET_M09.md) | 10-item quiz |
| Midterm | [M10 · Server state and reliable mutations](ADET_M10.md) | Individual coding activity |
| Midterm | [M11 · Authentication, authorization and secure sessions](ADET_M11.md) | 10-item quiz |
| Pre-final | [M12 · Hardware, permissions and attachments](ADET_M12.md) | Individual coding activity |
| Pre-final | [M13 · Notifications and background work](ADET_M13.md) | 10-item quiz |
| Pre-final | [M14 · Linking, sharing and location](ADET_M14.md) | Individual coding activity |
| Pre-final | [M15 · Audio, video and app performance](ADET_M15.md) | 10-item quiz |
| Pre-final | [M16 · Backend alternatives and emerging technologies](ADET_M16.md) | Individual coding activity |
| Pre-final | [M17 · Testing, security and release planning](ADET_M17.md) | 10-item quiz |
| Pre-final | [M18 · Solo project integration](ADET_M18.md) | Individual coding activity |
| Finals | [M19 · Finals rehearsal and repair](ADET_M19.md) | 10-item quiz |
| Finals | [M20 · Applied knowledge for the mini-capstone defense](ADET_M20.md) | 20-item quiz + two essays |
| Finals | [M21 · Mini-capstone announcement and solo project readiness](ADET_M21.md) | Solo mini-capstone |

## Packages and offline status

Quiz modules do not need a delivery mode. Coding modules offer three equal-point modes (offline lab, prepared laptop, written alternative).

| Module | Extra package | Install command (online) | Offline lab route |
|---|---|---|---|
| M06, M14, M17, M19, M21 | none | none | Runs in the prepared starter |
| M07, M08, M16, M18 | none | none | Built-in practice server; optional real API through `EXPO_PUBLIC_API_URL` |
| M09 | `@react-native-async-storage/async-storage` | `npx expo install @react-native-async-storage/async-storage` | Quiz module; instructor demo or paper trace |
| M10 | `@tanstack/react-query` | `npx expo install @tanstack/react-query` | **Must be pre-installed in the lab starter**, otherwise Mode 3 |
| M11 | `expo-secure-store` | `npx expo install expo-secure-store` | Quiz module; instructor demo or paper trace |
| M12 | none for the core; optional `expo-image-picker` | `npx expo install expo-image-picker` | Core uses a practice camera; real camera is an online extension on a device |
| M13 | `expo-notifications` | `npx expo install expo-notifications` | Quiz module; remote push needs a development build |
| M15 | `expo-audio` | `npx expo install expo-audio` | Quiz module; needs `tone.wav` beside `App.tsx` |

## Verification notes

**Checked:** every `App.tsx` in M06–M21 (and the optional M12 picker file) passes `tsc` in strict mode against Expo SDK 58, React Native 0.88.1, React 19.3.0 and TypeScript 6.0.3; the practice server was tested in Node (empty list, 422 on a blank title, 404, 204, server-down error, suggest rule).

**Not yet checked:** any code on a physical phone or emulator; the Expo Go behavior of each extra package on this baseline; notification delivery, camera, audio and sharing behavior; a real API (`examples/api`) with these screens; the offline phone route on the lab network; M05 (written elsewhere) against this pass.
