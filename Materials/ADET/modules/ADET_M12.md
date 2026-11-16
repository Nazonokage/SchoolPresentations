# ADET M12 · Hardware, permissions and attachments

[Module index](README.md) · Pre-final · 60–90 minutes · Individual coding activity

## A. Lesson Preview & Review

**Report a broken classroom chair with one photo.** Recall M07: a request can fail in different ways. A camera can too: denied, cancelled, or done.

**Learning targets:** ask for a permission at the moment it is needed, handle denied and cancelled as normal outcomes, treat a photo URI as a local reference, and keep a text-only path available.

**Trace:** User chooses → Permission → URI → Preview. Explain in your own words: allow shows an attachment, Remove clears it, deny shows a fallback message and the report can still continue.

## B. Detailed Main Lesson

### In plain words

A phone feature like the camera needs the user's permission. The student can say yes, say no, or open the camera and back out. Your app must work in all three cases. A successful photo gives you a local file path (a URI), not a web address.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| Permission at point of use | Ask when the student taps Take photo | A permission screen at launch with no context |
| Denied | The student said no; show a message and continue without a photo | A dead end |
| Cancelled | A normal choice; keep the screen as it was | Showing an error or clearing a good photo |
| URI | A reference to a file on this phone | Treating it as a link other devices can open |
| Upload | Needs size limits, server-side media checks and ownership rules | Trusting the file the client says it sent |
| Development build | Some native modules are not in Expo Go | Assuming every module runs in Expo Go |

```text
Take photo -> permission?
   denied ....... message, report continues (text only)
   granted -> camera
        cancelled .... screen unchanged
        photo ........ keep local URI -> preview
```

**Predict first:** attach a photo, then take another and cancel. Does the first photo stay?

| Step | Attached | Message | Reason |
|---|---|---|---|
| Practice: allow | chair-photo-1.jpg | Photo attached. | Photo branch |
| Practice: cancel | chair-photo-1.jpg | (unchanged) | Cancel keeps the old state |
| Practice: deny | chair-photo-1.jpg | Camera denied. Continue without a photo. | Denied branch |
| Remove | (none) | (unchanged) | Cleared on purpose |

**Misconception:** "a denied camera blocks the report." The report must remain possible without a photo. Contacts and sensors have their own permissions and should be optional too.

**Core and extension.** The core program uses a **practice camera** that returns the outcome you choose, so it needs no camera, dialog or package. The real `expo-image-picker` version follows as an extension; the three branches are identical.

### Common mistakes

- Asking for camera access before the student chooses the camera.
- Clearing the existing photo when the student cancels.
- Using a local URI as if it were a public link.

## C. Analogy, Guided Program & Practice

**Analogy.** Kapag ayaw magbigay ng camera access, puwede pa ring ituloy ang report. Parang pagsulat ng reklamo na walang larawan: mas mahina ang ebidensya, pero hindi ito ipinagbabawal.

**Use case:** a maintenance report where a photo helps but is not required.

**Install first.** None for the core program.

**Run it.** Copy this lesson's complete `App.tsx` into your prepared project from M01 (replace the whole file). Run `npx tsc --noEmit`, then `npx expo start --offline` in the prepared lab or `npx expo start` while online. Metro transpiles; it does not type-check. Course versions are recorded in M01.

**App.tsx — core checkpoint (practice camera)** · [Copyable file](../examples/M12/App.tsx)

```tsx
import { useState } from "react";
import { View, Text, Button } from "react-native";

type CameraOutcome = "photo" | "cancelled" | "denied";
type CameraResult = { status: CameraOutcome; name?: string };

// Practice camera: it returns the outcome you choose, so no camera, permission
// dialog or extra package is needed. The branches below match the real camera.
async function practiceCamera(outcome: CameraOutcome): Promise<CameraResult> {
  if (outcome === "photo") return { status: "photo", name: "chair-photo-1.jpg" };
  return { status: outcome };
}

export default function App() {
  const [photoName, setPhotoName] = useState("");
  const [message, setMessage] = useState("");

  async function takePhoto(outcome: CameraOutcome) {
    try {
      const result = await practiceCamera(outcome);
      if (result.status === "denied") {
        setMessage("Camera denied. Continue without a photo.");
        return;
      }
      // "cancelled" is a normal choice: leave the screen as it was
      if (result.status === "photo" && result.name) {
        setPhotoName(result.name);
        setMessage("Photo attached.");
      }
    } catch (error) {
      setMessage(String(error));
    }
  }

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Button title="Take photo (practice: allow)" onPress={() => takePhoto("photo")} />
      <Button title="Take photo (practice: cancel)" onPress={() => takePhoto("cancelled")} />
      <Button title="Take photo (practice: deny)" onPress={() => takePhoto("denied")} />
      {photoName !== "" && <Text>Attached: {photoName}</Text>}
      <Button title="Remove" onPress={() => setPhotoName("")} />
      <Text>{message}</Text>
    </View>
  );
}
```

**Breakdown.** `practiceCamera` stands in for the permission dialog and the camera. `takePhoto` has one branch per outcome: denied shows the fallback message, a photo stores its name, and cancelled changes nothing. Remove clears the attachment.

**Expected behavior.** Allow attaches a photo. Remove clears it. Deny shows the fallback message. Cancel changes nothing.

**Optional online extension: the real camera.**

```powershell
npx expo install expo-image-picker
```

Check the package docs for the camera permission text and any `app.json` setting. Test it on a physical device; an emulator without camera input can only test denial and cancellation. It has not yet been tested on the course baseline.

```tsx
import { useState } from "react";
import { View, Text, Button, Image } from "react-native";
import * as ImagePicker from "expo-image-picker";

export default function App() {
  const [uri, setUri] = useState("");
  const [message, setMessage] = useState("");

  async function takePhoto() {
    try {
      // Ask at the moment the student chooses the camera
      const permission = await ImagePicker.requestCameraPermissionsAsync();
      if (!permission.granted) {
        setMessage("Camera denied. Continue without a photo.");
        return;
      }
      const result = await ImagePicker.launchCameraAsync({ quality: 0.5 });
      if (!result.canceled) setUri(result.assets[0].uri);
    } catch (error) {
      setMessage(String(error));
    }
  }

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Button title="Take campus photo" onPress={takePhoto} />
      {uri !== "" && (
        <Image
          source={{ uri }}
          accessibilityLabel="Selected photo"
          style={{ width: 180, height: 180 }}
        />
      )}
      <Button title="Remove" onPress={() => setUri("")} />
      <Text>{message}</Text>
    </View>
  );
}
```

**Troubleshooting.** If the preview does not show, check the branch that stores the URI. Use sample subjects for photos, not other people.

## D. Assessment, Wrap-Up & References

### One individual coding activity — 10 points

Add a **cancellation message** ("No photo taken") and a **text-only report path**: a text box for the problem description and a Submit button that works with or without a photo and shows a summary line. Demonstrate all three camera outcomes.

| Evidence | Points |
|---|---:|
| Working core and independent change | 4 |
| Meaningful edge case (deny then submit text only) and response | 2 |
| Explain the branches and your change | 2 |
| Reproducible commands and readable source | 2 |

### Three equal-point delivery modes

**Mode 1 — Offline computer lab.** Before class, the lab PCs need Node 24.18.1, npm 11.16.0, VS Code and a separate copy of the prepared starter including `node_modules`. Use `START-LAB.cmd`; replace only the student's `App.tsx`. No installs in class. Local type-checking passed for this lesson's code on the course baseline; a phone on local Wi-Fi with a compatible Expo Go, or a prepared emulator, still needs a successful [smoke test](../offline-lab/SMOKE-TEST.md). If no display route passes, use Mode 3, not an untested promise. `--tunnel` is an online fallback only.

**Mode 2 — Prepared personal laptop.** Follow the handout below, bring your laptop and do the activity in class. Submit source, `package.json`, the lockfile, a README with the commands and the actual activity date, success and failure evidence and a brief explanation. Recommended folder or repository: `ADET-M12-LASTNAME` (the instructor confirms the pattern). Do not upload `node_modules`, cache or secrets.

**Mode 3 — Written alternative (10 points).** Trace allow, cancel, deny, Remove and a text-only Submit. Give `photoName` and the message after each, and write the cancellation message and the text-only submit rule. Submit a step-by-step table plus a 150–250-word explanation. It earns the same maximum as the coding activity; no device screenshot is required.

| Written evidence | Points |
|---|---:|
| Correct complete trace and proposed change | 4 |
| Edge or failure case and justified correction | 2 |
| Explanation connecting code to visible behavior | 2 |
| Labeled inputs, ordered steps and readable evidence | 2 |

Guided copying and predictions are ungraded. Only the one selected assessment mode is graded.

**Wrap-up.** Explain what the app does in each of the three outcomes and why a URI is not a shareable link. Name the layer you would inspect first if a granted camera showed no preview.

[ImagePicker](https://docs.expo.dev/versions/latest/sdk/imagepicker/)

### Instructor notes

Pacing: 5 review, 15 explanation, 10 guided code, 25 activity, 5 wrap-up. The practice camera makes the lab fully offline; rehearse the real camera on one physical device only. A model solution adds a `description` state, a `TextInput`, and a Submit button that sets a message like `"Report: " + description + (photoName ? " + photo" : " (no photo)")`. Device and permission behavior are not yet recorded on the course baseline.

### Before next meeting — M12 preparation handout (put it on the last slide of the previous meeting)

For the upcoming **M12 coding meeting**, prepare **your own laptop**, then bring it. The instructor confirms the date and naming pattern.

```powershell
npx create-expo-app@latest ADET-M12-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M12-LASTNAME
npx tsc --noEmit
npx expo start
```

No extra packages are needed for the core activity. Use the distributed manifest and lockfile for exact versions. Open the app once before class and bring a screenshot or the exact error. Without home internet, prepare on campus Wi-Fi, mobile data or an agreed hotspot, or copy the [prepared starter and dependencies by USB](../offline-lab/README.md). Internet preparation is not graded.
