# ADET M05 · Navigation and application structure

[Module index](README.md) · Prelim · 60–90 minutes · 10-item quiz

## A. Lesson Preview & Review

**How can a Library button open the right screen and still let us go back?** M04 reused components; this lesson connects whole screens.

**Learning targets:** map files to routes, trace push/back, distinguish a stack from tabs, handle an invalid ID, and explain why a route guard is not authorization.

**Trace:** Home → push Library ID → read parameter → find office or show missing → Back.

## B. Detailed Main Lesson

### In plain words

Navigation decides which screen is shown and how the user returns. Expo Router connects paths to files. The offline core uses a tiny stack model to make the idea visible; that model is not Expo Router and does not provide deep links, native navigation or route persistence.

| Term | Why / how | Failure to watch |
|---|---|---|
| Route | A named destination such as /office/library | A path without a matching file cannot open its screen |
| Dynamic segment | [id].tsx reuses one screen for different office IDs | Unknown IDs must not silently become a valid office |
| Layout | _layout.tsx supplies a shared navigator | A route component alone does not configure the whole app |
| Stack | Push adds a destination; Back removes the top | Resetting to Home is different from returning to a previous screen |
| Tabs | Select peer sections such as Home and Settings | A tab switch need not destroy its previous screen |
| Deep link | An external URL opens a destination | Requiring an earlier click's object breaks a cold launch |
| Route guard | Redirects users to an appropriate screen | Hiding a screen does not secure data; the server authorizes requests |

```text
app/_layout.tsx            shared Stack
app/index.tsx             /
app/office/[id].tsx        /office/library or /office/unknown

Stack trace: [Home] → [Home, Library] → Back → [Home]
```

**Predict first:** A cold link supplies unknown as the ID. Should the screen show the Library anyway?

1. Read the ID as untrusted input, not proof that a record exists.
2. Normalize a possible array parameter to one string.
3. Look up the known ID. For unknown, display Office not found.
4. Offer Home when there is no previous route; Back only works when history exists.

**Misconception:** putting a full password/token in a route is convenient storage. URLs can be exposed in logs and shared links. Pass nonsecret identifiers; request protected data through an authorized API. A later shared-state lesson handles data used by multiple screens.

### Common mistakes

- Copying a Router route into App.tsx while leaving the blank entry unchanged.
- Using both app/ and src/app/ without knowing which tree is active.
- Assuming losing navigation focus always unmounts a screen.

## C. Analogy, Guided Program & Practice

**Analogy.** Parang room number ang route ID: isang direksiyon, hindi ang buong opisina. Ang history ay listahan ng dinaanan; kapag maling kuwarto ang number, malinaw na sabihin na hindi ito nahanap.

**Use case:** a campus directory opens office details by ID.

**Install first.** Core imports come from `react` and `react-native`, already in the prepared blank TypeScript template. No additional package, permission or config plugin is required. Use SDK 58 / TypeScript 6.0.3 and the distributed lockfile. Compatible Expo Go is sufficient for these core APIs, but actual phone/network testing remains pending.

**Fresh project (online preparation only):**

```powershell
npx create-expo-app@latest ADET-M05-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M05-LASTNAME
```

**Run it.** Copy this lesson's complete `App.tsx` into your own prepared project. Run `npx tsc --noEmit`, then `npx expo start --offline` for the prepared lab, or `npx expo start` during online preparation. Metro transpiles; it does not type-check. The local bundle has been checked separately from actual device operation. Use the [five-minute smoke test](../offline-lab/SMOKE-TEST.md) before class. No web-preview packages are assumed.


### Core offline model — App.tsx

This complete program uses only template packages. Follow the printed stack, or run it on a prepared native client. [Copyable source](../examples/M05/App.tsx).

```tsx
import { useState } from "react";
import { View, Text, Button } from "react-native";

export default function App() {
  // A teaching model of a stack; this is NOT Expo Router.
  const [routes, setRoutes] = useState<string[]>(["home"]);
  const currentRoute = routes[routes.length - 1];
  const officeName = currentRoute === "library" ? "Library — Open 8 AM" : "Office not found";
  function pushOffice(id: string) {
    setRoutes((currentRoutes) => [...currentRoutes, id]);
  }
  function goBack() {
    // Keep the home route when there is no previous screen.
    setRoutes((currentRoutes) => currentRoutes.length > 1 ? currentRoutes.slice(0, -1) : currentRoutes);
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 16 }}>
      <Text>Navigation paper-model companion</Text>
      <Text>Stack: {routes.join(" → ")}</Text>
      {currentRoute === "home" ? (
        <View style={{ gap: 12 }}>
          <Button title="Visit library" onPress={() => pushOffice("library")} />
          <Button title="Try unknown office" onPress={() => pushOffice("unknown")} />
        </View>
      ) : <Text>{officeName}</Text>}
      <Button title="Back" disabled={routes.length === 1} onPress={goBack} />
    </View>
  );
}
```

**Breakdown:** routes is an array of destinations; spreading it appends an ID without changing the original array. slice removes its last entry. The conditional renders Home or a detail message. The guard preserves at least Home. This illustrates history; it intentionally does not imitate every Router behavior.

**Expected:** Visit library shows Library — Open 8 AM; Back restores Home. Try unknown office shows Office not found. Back is disabled at Home.

### Optional online extension — real Expo Router

Use a separate fresh `ADET-M05-LASTNAME` project created by the SDK-pinned command above. Do not alter the prepared offline starter. Install before class:

```powershell
npx expo install expo-router react-native-safe-area-context react-native-screens expo-linking expo-constants expo-status-bar
```

| Dependency | Role |
|---|---|
| expo-router | File routes and navigation API |
| react-native-safe-area-context | Native safe-area support |
| react-native-screens | Native screen primitives |
| expo-linking | URL/link integration |
| expo-constants | Expo runtime information used by the Router setup |
| expo-status-bar | Compatible status-bar package (also in the blank starter) |

Copy the **complete files** and follow [Router extension README](../examples/M05/router-extension/README.md). It explicitly changes package.json main to `expo-router/entry`, adds the expo-router plugin and scheme in app.json, and uses this one route tree:

```text
ADET-M05-LASTNAME/
  package.json         main: expo-router/entry
  app.json             plugins: expo-router; scheme: adetlab
  tsconfig.json        strict TypeScript; includes app/**/*.tsx
  app/
    _layout.tsx
    index.tsx
    office/[id].tsx
```

App.tsx is not the entry in this separate extension. Basic in-app Router navigation can use compatible Expo Go; no device permission is requested. Testing a custom installed scheme requires a development build that includes that native configuration. Expo Go's URL is not your app's permanent custom scheme. Real external link handling is revisited in M14. No browser packages or internet deployment are assumed.

**Ungraded modification:** add clinic with its own hours and a link. Predict the unknown case before running it. See the extension's file-by-file comments and parameter lookup trace.

**Troubleshooting:** unmatched route → inspect file name and active route tree; old App.tsx still shown → inspect main; unknown ID crashes → validate lookup and render a fallback; no Back history → offer Home. After a configuration change restart with `npx expo start --clear` while online; use the prepared offline flag only once dependencies are present.

## D. Assessment, Wrap-Up & References

### 10-item quiz — 1 point each

1. A route is: A. A destination path B. A password C. A database D. A font.
2. Which file supplies the shared navigator? A. package-lock.json B. app/_layout.tsx C. README.md D. assets/icon.png.
3. Which filename accepts changing office IDs? A. office.txt B. [id].tsx C. icon.png D. app.json.
4. A tab usually represents: A. A peer section B. A timer C. A password D. A compiler error.
5. A route guard replaces server authorization: A. Always B. Never; it controls navigation feedback C. Only offline D. Only on iOS.
6. Trace [Home], push Library, then Back. What remains?
7. The ID is unknown. What should the example display?
8. A screen loses focus. Must its component unmount? Explain briefly.
9. Can the template-only stack model open an external deep link? Explain.
10. A screen opens directly with no history. What safe navigation option does the example provide?

**Wrap-up:** Explain the difference between a component's state, the route's ID and the navigator's history. Identify where a parameter becomes a lookup result.

[Router installation](https://docs.expo.dev/router/installation/) · [Router notation](https://docs.expo.dev/router/basics/notation/) · [Navigation](https://docs.expo.dev/router/basics/navigation/)

### Instructor notes

Keep the quiz as the only graded evidence. Use 5 minutes review, 20 explanation/model trace, 15 demonstration, 15 quiz and 5 wrap-up. The real Router setup is optional prepared extension work for the additional 30 minutes, not an in-class download requirement. Show the route-tree diagram beside the matching files; keep the full setup in a handout. Device deep linking remains untested. Preserve core App.tsx and the extension's separate route tree; no selector should silently convert one into the other.


**Teaching evidence:** keys and grading guidance are in [the separate instructor key](../instructor/OPENER_ANSWER_KEY.md). Use the local flow diagram beside the matching code; no external image download is required. Record actual hardware outcomes rather than treating expected output as a measured device result.
