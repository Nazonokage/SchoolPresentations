# ADET M09 · Local storage and offline behavior

[Module index](README.md) · Midterm · 60–90 minutes · 10-item quiz

## A. Lesson Preview & Review

**Where did my draft go after reopening?** Recall M08: records live on the server. Today we separate what the phone keeps from what the server owns.

**Learning targets:** tell state, local storage, a cache and server data apart; save and restore a small value with a storage key; handle a missing key; explain why offline editing needs more than a cache.

**Trace:** Type → Save key → Restart → Restore. Explain in your own words: save "Bring ID", close and reopen, tap Restore and the text returns; unsaved edits are replaced by the stored value.

## B. Detailed Main Lesson

### In plain words

React state disappears when the screen goes away. A value saved under a key on the phone survives closing the app. That saved draft is yours alone: the server does not have it, and neither does a classmate's phone.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| State | Lives with the component; gone when it unmounts | Expecting a draft to survive a restart |
| Key/value storage | `setItem(key, text)` writes; `getItem(key)` reads | Reading a key that was never written |
| Missing key | `getItem` returns `null`, so the sample falls back to `""` | `null` shown as text or crashing |
| Cache | A stored copy of server data for speed; the server still decides what is true | Treating a stale copy as the truth |
| SQLite | Local structured data you can query | Packing many records into one key |
| Offline edits | Need an operation ID, retry rules and a conflict policy | Claiming "offline sync" because a draft was saved |

```text
phone:  [ TextInput state ] --Save--> [ key "campus.draft" ]
                                      survives restart
        [ TextInput state ] <-Restore-- [ key "campus.draft" ]
server: owns the real records (not involved here)
```

**Predict first:** Save "Bring ID", type "Bring lunch" without saving, then tap Restore. What does the box show?

| Step | Box text | Stored value | Reason |
|---|---|---|---|
| Type "Bring ID", Save | Bring ID | Bring ID | Written under the key |
| Type "Bring lunch" | Bring lunch | Bring ID | Not saved |
| Restore | Bring ID | Bring ID | Stored value replaces the edit |
| Restore with no key | (empty) | none | `null` becomes `""` |

**Offline reasoning.** A pending edit sent to a server needs a client-made operation ID. If the server accepted it but the reply was lost, a retry without that ID creates a duplicate. Two devices editing the same record need a conflict policy, for example comparing a base revision or last-updated value. A cache alone provides none of this.

**Misconception:** "I saved a draft, so my app works offline." Saving locally is one piece; synchronizing without losing or duplicating data is a separate design. MMKV needs a compatible native build; secrets belong in secure storage (M11), not plain preferences.

### Common mistakes

- Forgetting to `await` the save before reading.
- Using different key strings in Save and Restore.
- Treating cached server data as editable truth.

## C. Analogy, Guided Program & Practice

**Analogy.** Ang draft sa phone ay parang notebook sa bag. Hindi pa ito naipapasa sa guro (server). Kapag nawala ang bag (ibang phone), wala rin ang notebook.

**Use case:** a student drafts a request on the bus with no signal and finishes it later.

**Install first (online):**

```powershell
npx expo install @react-native-async-storage/async-storage
```

This package is expected to work in Expo Go, but that has not yet been tested on the course baseline. Restart the server after installing.

**Run it.** Copy this lesson's complete `App.tsx` into your prepared project from M01 (replace the whole file). Run `npx tsc --noEmit`, then `npx expo start --offline` in the prepared lab or `npx expo start` while online. Metro transpiles; it does not type-check. Course versions are recorded in M01.

**Lab note.** Quiz modules do not need a delivery mode. If the lab starter lacks this package, run this demo from the instructor's prepared device, or trace it on paper.

**App.tsx — complete checkpoint** · [Copyable file](../examples/M09/App.tsx)

```tsx
import { useState } from "react";
import { View, Text, Button, TextInput } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";

const DRAFT_KEY = "campus.draft";

export default function App() {
  const [draft, setDraft] = useState("");
  const [message, setMessage] = useState("");

  async function saveDraft() {
    try {
      await AsyncStorage.setItem(DRAFT_KEY, draft);
      setMessage("Saved on device");
    } catch (error) {
      setMessage(String(error));
    }
  }

  async function restoreDraft() {
    try {
      // A missing key gives null, so we fall back to an empty string
      const saved = await AsyncStorage.getItem(DRAFT_KEY);
      setDraft(saved ?? "");
      setMessage(saved === null ? "Nothing saved yet" : "Restored");
    } catch (error) {
      setMessage(String(error));
    }
  }

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <TextInput placeholder="Draft" value={draft} onChangeText={setDraft} />
      <Button title="Save draft" onPress={saveDraft} />
      <Button title="Restore draft" onPress={restoreDraft} />
      <Text>{message}</Text>
    </View>
  );
}
```

**Breakdown.** `DRAFT_KEY` is the one key both buttons use. `saveDraft` writes the current text. `restoreDraft` reads the key and replaces the text; it reports "Nothing saved yet" if the key is missing. Errors go to the message line.

**Expected behavior.** Save "Bring ID", close and reopen, tap Restore, and the text returns. Unsaved edits are replaced by the stored value.

**Ungraded practice.** Predict what Restore shows on a second phone. Add a Clear saved draft button and explain how it differs from clearing the text box.

**Troubleshooting.** If Restore gives an old value, confirm the save finished and the key matches.

## D. Assessment, Wrap-Up & References

### 10-item quiz

Give a short answer for each item. The guided change above is ungraded.

1. Give one example of data that belongs in a local draft.
2. What is a cache?
3. When is SQLite a better fit than one key/value entry?
4. What does `getItem` return for a missing key, and how does the sample handle it?
5. After Save and a restart on the same installation, what remains?
6. After editing without saving, what does Restore do?
7. Why is the saved draft absent on another phone?
8. Why is a cached response not enough for offline edits?
9. Where should a session secret go instead of plain preference storage?
10. How can you detect a conflict between two devices editing one record?

**Answer key (instructor).**
1. Unsent text, such as a half-written request.
2. A stored copy of data for speed or offline reading; not the source of truth.
3. Structured records that need queries.
4. `null`; the sample shows "Nothing saved yet" and uses an empty string.
5. The value stored under the key.
6. It replaces the unsaved text with the stored value.
7. It is stored on that installation only.
8. Pending edits also need operation IDs, retry rules and a conflict policy.
9. Secure storage (M11).
10. Compare a base revision or last-updated value before applying the edit.

**Wrap-up.** Explain how text typed in the box ends up back in it after a restart, and what the server knows about it. Name the layer you would inspect if Restore returned an old value.

[AsyncStorage usage](https://react-native-async-storage.github.io/async-storage/docs/usage/)

### Instructor notes

Pacing: 5 review, 15 explanation, 10 demo, 25 quiz, 5 wrap-up. Demonstrate on one prepared device if the lab starter does not include the package. This is a draft demonstration, not an offline sync engine. Device behavior has not yet been recorded on the course baseline.
