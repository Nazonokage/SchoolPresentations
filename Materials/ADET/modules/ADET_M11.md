# ADET M11 · Authentication, authorization and secure sessions

[Module index](README.md) · Midterm · 60–90 minutes · 10-item quiz

## A. Lesson Preview & Review

**Can a signed-in student read another student's record?** Recall M08: the server owns the records. Today we separate proving who you are from being allowed to see something.

**Learning targets:** tell authentication from authorization, explain what secure storage is for, show why a client-side check is not protection, and describe a server ownership check.

**Trace:** Session → Identity → Ownership → Allow or deny. Explain in your own words: login stores `ana`; Read denies access to Ben's record; Logout returns to Signed out.

## B. Detailed Main Lesson

### In plain words

Logging in answers "who are you?". Permission answers "may you open this record?". A student can have a valid session and still be refused someone else's record. This lesson uses a *local model*: it exercises the screen, but a real app must let the server decide.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| Authentication | Establishing identity (a session) | Thinking login means access to everything |
| Authorization | Checking the record owner against the verified identity | Hiding a button and calling it protected |
| Secure storage | `SecureStore` keeps small secrets on the device | Putting a session secret in plain preferences |
| Server check | The backend validates the session and queries by record ID **and** verified owner | Trusting an ID the client sends |
| Expiry and revocation | Server policy; storage alone cannot decide validity | Assuming a stored token is still valid |
| OAuth | A provider, redirect and `state` check; mobile public clients commonly use PKCE; a token need not be a JWT | Treating OAuth as login by itself |

```text
actor      record owner   result
(none)     ben            sign in first (401 unauthenticated)
ana        ben            denied (403 not authorized)
ben        ben            record opened
```

**Predict first:** press Read before logging in, then log in and press Read.

| Step | Message | Concept |
|---|---|---|
| Read (signed out) | Sign in first (not authenticated) | No identity |
| Login, Read | Denied: ben owns this record (not authorized) | Identity, wrong owner |
| Logout | Signed out | Local value removed |

**Misconception:** "a hidden button protects the record." A modified app can call the API directly; only a server-side ownership check on every request protects it. No home-made cryptography, no database passwords or private keys in client code.

### Common mistakes

- Mixing up "not signed in" and "signed in but not allowed".
- Trusting a record ID or owner name sent by the client.
- Storing a long-lived secret in plain storage.

## C. Analogy, Guided Program & Practice

**Analogy.** May school ID ka, pero hindi ibig sabihin na puwede mong buksan ang record ng kaklase. Ang guwardiya sa gate ang authentication; ang registrar sa bintana ang authorization.

**Use case:** a student portal where each student sees only their own grades.

**Install first (online):**

```powershell
npx expo install expo-secure-store
```

Check the package docs for any `app.json` setting. This package is expected to work in Expo Go, but that has not yet been tested on the course baseline.

**Run it.** Copy this lesson's complete `App.tsx` into your prepared project from M01 (replace the whole file). Run `npx tsc --noEmit`, then `npx expo start --offline` in the prepared lab or `npx expo start` while online. Metro transpiles; it does not type-check. Course versions are recorded in M01.

**Lab note.** Quiz modules do not need a delivery mode. Run this demo on the instructor's prepared device, or trace the three rows above on paper.

**App.tsx — complete checkpoint** · [Copyable file](../examples/M11/App.tsx)

```tsx
import { useState } from "react";
import { View, Text, Button } from "react-native";
import * as SecureStore from "expo-secure-store";

const SESSION_KEY = "demoActor";
const RECORD_OWNER = "ben"; // who owns the record in this model

type Action = "login" | "read" | "logout";

export default function App() {
  const [message, setMessage] = useState("Signed out");

  async function runAction(action: Action) {
    try {
      if (action === "login") await SecureStore.setItemAsync(SESSION_KEY, "ana");
      if (action === "logout") await SecureStore.deleteItemAsync(SESSION_KEY);
      const actor = await SecureStore.getItemAsync(SESSION_KEY);
      if (action === "read") {
        if (actor === null) setMessage("Sign in first (not authenticated)");
        else if (actor === RECORD_OWNER) setMessage("Record opened");
        else setMessage("Denied: " + RECORD_OWNER + " owns this record (not authorized)");
      } else {
        setMessage(actor ?? "Signed out");
      }
    } catch (error) {
      setMessage(String(error));
    }
  }

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Text>Local session model</Text>
      <Button title="login" onPress={() => runAction("login")} />
      <Button title="read" onPress={() => runAction("read")} />
      <Button title="logout" onPress={() => runAction("logout")} />
      <Text>{message}</Text>
    </View>
  );
}
```

**Breakdown.** `SESSION_KEY` holds the demo actor. `runAction` writes, deletes or reads it, then reads the stored actor. The Read branch distinguishes no actor, the owner, and another actor. This is a mock session; it contains no password, no server and no real identity check.

**Expected behavior.** Login displays `ana`. Read denies access to Ben's record. Logout displays Signed out.

**Ungraded practice.** Sketch the server check for two users, including an expired session and a record owned by someone else.

**Troubleshooting.** If hiding a button is the only protection, try the same request directly against the API in a controlled lab.

## D. Assessment, Wrap-Up & References

### 10-item quiz

Give a short answer for each item. The guided change above is ungraded.

1. What is authentication?
2. What is authorization?
3. What kind of data is SecureStore meant for?
4. Which actor does Login store in this model?
5. Signed in as that actor, can they read Ben's record? Which concept decides?
6. What does Logout remove?
7. Why can a modified app bypass a client-side guard?
8. Does encrypting a token prove it is still valid?
9. Which layer must check ownership on a real record request?
10. After a provider redirect, what needs checking?

**Answer key (instructor).**
1. Proving who the user is.
2. Deciding what that user may access.
3. Small secrets such as session material.
4. `ana`.
5. No; authorization (ownership).
6. The locally stored actor value.
7. The client is under the user's control; the server must enforce the rule.
8. No; expiry and revocation are server policy.
9. The backend, on every request.
10. The `state` value and the response, then validate tokens on the server; PKCE for mobile public clients.

**Wrap-up.** Explain the difference between "not signed in" and "not allowed" using the three rows of the table. Name the layer you would inspect first if one student could read another's record.

[SecureStore](https://docs.expo.dev/versions/latest/sdk/securestore/)

### Instructor notes

Pacing: 5 review, 15 explanation, 10 demo, 25 quiz, 5 wrap-up. Call the demo a mock session, never "secure login". Device behavior is not yet recorded on the course baseline.
