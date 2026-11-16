# ADET M14 · Linking, sharing and location

[Module index](README.md) · Pre-final · 60–90 minutes · Individual coding activity

## A. Lesson Preview & Review

**Invite classmates without reading their contacts.** Recall M12: the student stays in control of device features. Today your app hands work to other apps and the student chooses where it goes.

**Learning targets:** use the share sheet and a map link, handle cancel and failure, explain why "returned to the app" does not prove delivery, and decide when location is truly needed.

**Trace:** Place → User choice → System app → Return. Explain in your own words: Share shows a chooser; Open map hands a link to an Iloilo location; coming back shows feedback.

## B. Detailed Main Lesson

### In plain words

Sharing and linking let your app start something in another app: a message, a map. The student picks the recipient. When they come back, your app only knows that the hand-off finished or failed, not whether a friend got the message.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| Share sheet | `Share.share` opens the system chooser with your prepared text | Building your own recipient picker |
| Linking | `Linking.openURL` hands a URL to an installed handler | Assuming every URL can be opened |
| Return | Control comes back whether or not anything was sent | Claiming "message delivered" |
| Fixed place | A public venue and map link are enough to meet | Asking for GPS you do not need |
| Foreground location | Request on demand, handle denied and approximate results, keep a static fallback | Tracking a student's trail |
| Background location | Needs separate consent and a real requirement | Adding it "just in case" |

```text
tap Share -> system chooser -> student picks app (or cancels) -> back in app
tap Map   -> external app opens the link                    -> back in app
```

**Predict first:** the student opens the share sheet and cancels. Does the screen say "Returned to app"?

| Action | Message | What it proves |
|---|---|---|
| Share, then cancel | Returned to app | Only that the sheet closed |
| Open map, no handler | An error message | The link could not open |
| Share, send | Returned to app | Still not proof of delivery |

**Misconception:** "if the app returns, the message was sent." Validate destinations, never build a URL from unchecked user text, and let the student take the final step for SMS, email and dialer links.

### Common mistakes

- Treating a successful return as delivery.
- Building a destination from unvalidated user text.
- Requesting location when a place name would do.

## C. Analogy, Guided Program & Practice

**Analogy.** Ibigay ang meeting place; ang student ang pipili kung kanino ipapadala. Parang pag-abot ng papel sa kaklase: ikaw ang nagbigay, hindi mo kontrolado kung ipapasa niya.

**Use case:** inviting classmates to a study spot.

**Install first.** None. `Share` and `Linking` come with React Native.

**Run it.** Copy this lesson's complete `App.tsx` into your prepared project from M01 (replace the whole file). Run `npx tsc --noEmit`, then `npx expo start --offline` in the prepared lab or `npx expo start` while online. Metro transpiles; it does not type-check. Course versions are recorded in M01.

**App.tsx — complete checkpoint** · [Copyable file](../examples/M14/App.tsx)

```tsx
import { useState } from "react";
import { View, Text, Button, Share, Linking } from "react-native";

const MAP_URL = "https://www.openstreetmap.org/?mlat=10.72&mlon=122.56";

export default function App() {
  const [message, setMessage] = useState("");

  async function handoff(kind: "share" | "map") {
    try {
      if (kind === "map") await Linking.openURL(MAP_URL);
      else await Share.share({ message: "Meet at the library at 3 PM" });
      // Returning to the app does not prove a message was delivered
      setMessage("Returned to app");
    } catch (error) {
      setMessage(String(error));
    }
  }

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Button title="Share study meetup" onPress={() => handoff("share")} />
      <Button title="Open Iloilo map" onPress={() => handoff("map")} />
      <Text>{message}</Text>
    </View>
  );
}
```

**Breakdown.** `MAP_URL` is fixed. `handoff` opens the map link or the share sheet, then reports "Returned to app". Any thrown error goes to the message line. Nothing here requests location.

**Expected behavior.** Share shows a chooser. Open map hands off a link to an Iloilo location. Return shows the feedback message. Opening a web link needs a handler and may need internet on the phone.

**Ungraded practice.** Predict what `Share.share` does when the student cancels. Restore the sample before assessment.

**Troubleshooting.** If a URL cannot open, check its scheme and the installed handler. Avoid destinations built from unvalidated user text.

## D. Assessment, Wrap-Up & References

### One individual coding activity — 10 points

Share **your selected campus place** and add a **visible address fallback** on the screen that stays readable if the hand-off fails or is cancelled. Show one normal result and one cancel or failure.

| Evidence | Points |
|---|---:|
| Working core and independent change | 4 |
| Meaningful edge case (cancel or failure) and response | 2 |
| Explain data flow and your own change | 2 |
| Reproducible commands and readable source | 2 |

### Three equal-point delivery modes

**Mode 1 — Offline computer lab.** Before class, the lab PCs need Node 24.18.1, npm 11.16.0, VS Code and a separate copy of the prepared starter including `node_modules`. Use `START-LAB.cmd`; replace only the student's `App.tsx`. No installs in class. Local type-checking passed for this lesson's code on the course baseline; a phone on local Wi-Fi with a compatible Expo Go, or a prepared emulator, still needs a successful [smoke test](../offline-lab/SMOKE-TEST.md). If no display route passes, use Mode 3, not an untested promise. `--tunnel` is an online fallback only.

**Mode 2 — Prepared personal laptop.** Follow the handout below, bring your laptop and do the activity in class. Submit source, `package.json`, the lockfile, a README with the commands and the actual activity date, success and failure evidence and a brief explanation. Recommended folder or repository: `ADET-M14-LASTNAME` (the instructor confirms the pattern). Do not upload `node_modules`, cache or secrets.

**Mode 3 — Written alternative (10 points).** Trace Share-then-cancel, Share-then-send and Map with no handler. State what the app knows each time, write the address-fallback line, and explain why "Returned to app" is not delivery. Submit a step-by-step table plus a 150–250-word explanation. It earns the same maximum as the coding activity; no device screenshot is required.

| Written evidence | Points |
|---|---:|
| Correct complete trace and proposed change | 4 |
| Edge or failure case and justified correction | 2 |
| Explanation connecting code to visible behavior | 2 |
| Labeled inputs, ordered steps and readable evidence | 2 |

Guided copying and predictions are ungraded. Only the one selected assessment mode is graded.

**Wrap-up.** Explain what the app does and does not know after the student returns. Name the layer you would inspect first if the map did not open.

[Share](https://reactnative.dev/docs/share) · [Linking](https://reactnative.dev/docs/linking)

### Instructor notes

Pacing: 5 review, 15 explanation, 10 guided code, 25 activity, 5 wrap-up. The share sheet works offline; the map page needs internet and a handler. A model solution keeps `const PLACE = "Library, Iloilo"` in state and displays it under the buttons, catching the error from `Share.share`. Location and maps are discussion only. Device behavior is not yet recorded on the course baseline.

### Before next meeting — M14 preparation handout (put it on the last slide of the previous meeting)

For the upcoming **M14 coding meeting**, prepare **your own laptop**, then bring it. The instructor confirms the date and naming pattern.

```powershell
npx create-expo-app@latest ADET-M14-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M14-LASTNAME
npx tsc --noEmit
npx expo start
```

No extra packages are needed for the core activity. Use the distributed manifest and lockfile for exact versions. Open the app once before class and bring a screenshot or the exact error. Without home internet, prepare on campus Wi-Fi, mobile data or an agreed hotspot, or copy the [prepared starter and dependencies by USB](../offline-lab/README.md). Internet preparation is not graded.
