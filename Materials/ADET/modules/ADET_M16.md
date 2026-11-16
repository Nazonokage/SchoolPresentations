# ADET M16 · Backend alternatives and emerging technologies

[Module index](README.md) · Pre-final · 60–90 minutes · Individual coding activity

## A. Lesson Preview & Review

**Offer a useful study suggestion during an outage.** Recall M07 and M08: the screen must survive a failed request. Today the failure has a planned fallback, and we compare architectures.

**Learning targets:** call an endpoint and validate one field, give a fallback that works with no server, explain where a private key belongs, and compare a custom API with a managed backend.

**Trace:** Request → Server rule → Validate tip → Fallback. Explain in your own words: with the server on the message starts with "Server:"; stop it and the next press shows the "Offline:" message.

## B. Detailed Main Lesson

### In plain words

The phone asks a campus server for a tip. The server picks one using a rule you can read. If the server cannot be reached, the app uses its own simple rule. The two prefixes ("Server:" and "Offline:") tell the student which one answered.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| Server rule | Plain, explicit logic on the server chooses the tip | A "magic" answer nobody can explain |
| Validate | Check the status and that `tip` is a string | Showing `undefined` |
| Fallback | A deterministic tip works with no network | A blank screen during an outage |
| Private keys | A provider key lives in the server's environment, never in the app | A key inside `EXPO_PUBLIC_` is public |
| Managed backend | Supabase or Firebase give auth and data services; policies and ownership rules are still yours | Assuming a service secures itself |
| Server runtime | An Expo API route or cloud function still needs a deployed server for real phones | Expecting it to run inside the app |

```text
tap -> request /suggest
   ok + string tip .... "Server: <tip>"
   any failure ........ "Offline: review your first unfinished task."
```

**Predict first:** press the button with the server on, then stop it and press again. What changes?

| Server | Message | Source |
|---|---|---|
| On | Server: Review your first unfinished task. | Practice or real server rule |
| Off | Offline: review your first unfinished task. | App's own rule |
| Reply with no `tip` | Offline… | Validation failed, so fallback |

Compare REST and GraphQL, and real-time updates, by requirement. Widgets, App Intents, Expo modules and experimental features are a short research discussion, not installs. Test your change with one known input and one failure.

**Misconception:** "a provider outage and an empty answer are the same." A failed request and an empty but valid reply need different messages. The mobile app calls your campus API; that API can limit requests, remove personal data and choose a fallback before calling any provider.

### Common mistakes

- Putting a private key in the app.
- Skipping the shape check on the reply.
- Using one message for "empty" and "failed".

## C. Analogy, Guided Program & Practice

**Analogy.** May maibibigay pa ring study tip kahit walang signal. Parang pagtanong sa guro: kung wala siya, may sarili kang checklist.

**Use case:** study suggestions that never leave the student with nothing.

**Install first.** None.

**Run it.** Copy this lesson's complete `App.tsx` into your prepared project from M01 (replace the whole file). Run `npx tsc --noEmit`, then `npx expo start --offline` in the prepared lab or `npx expo start` while online. Metro transpiles; it does not type-check. Course versions are recorded in M01.

**Practice server.** With no setup, `request()` uses a small fake server that lives inside the app, so this lesson runs offline. The Stop/Start button rehearses a connection failure. To use a real API instead, start one from [the API examples](../examples/api/README.md), set `EXPO_PUBLIC_API_URL`, and restart Expo (the value is read when the app bundles). On a physical phone use the PC's network address, not `localhost`.

**App.tsx — complete checkpoint** · [Copyable file](../examples/M16/App.tsx)

```tsx
import { useState } from "react";
import { View, Text, Button } from "react-native";

// ---- Practice server: runs inside the app, so no network is needed. ----
// If EXPO_PUBLIC_API_URL is set, request() calls the real API instead.
const API_URL = process.env.EXPO_PUBLIC_API_URL;

type ApiResponse = { ok: boolean; status: number; json: () => Promise<unknown> };
type Task = { id: string; title: string; done: boolean };
type RequestOptions = { method?: string; body?: string; headers?: Record<string, string> };

let practiceTasks: Task[] = [];
let practiceNextId = 1;
let practiceServerUp = true;

// Flip the practice server off to rehearse a connection failure.
function setPracticeServerUp(isUp: boolean) {
  practiceServerUp = isUp;
}

async function request(path: string, options: RequestOptions = {}): Promise<ApiResponse> {
  if (API_URL) return fetch(API_URL + path, options);
  if (!practiceServerUp) throw new Error("Network request failed");
  const method = options.method ?? "GET";
  const reply = (status: number, body?: unknown): ApiResponse => ({
    ok: status >= 200 && status < 300,
    status,
    json: async () => body,
  });
  if (path === "/suggest") return reply(200, { tip: "Review your first unfinished task." });
  if (path === "/tasks" && method === "GET") return reply(200, practiceTasks);
  if (path === "/tasks" && method === "POST") {
    const title = String(JSON.parse(options.body ?? "{}").title ?? "").trim();
    if (title === "") return reply(422, { error: "title is required" });
    const task: Task = { id: String(practiceNextId++), title, done: false };
    practiceTasks = [...practiceTasks, task];
    return reply(201, task);
  }
  const id = path.split("/")[2];
  const found = practiceTasks.find((task) => task.id === id);
  if (!found) return reply(404, { error: "not found" });
  if (method === "PATCH") {
    const changes = JSON.parse(options.body ?? "{}");
    practiceTasks = practiceTasks.map((task) => (task.id === id ? { ...task, ...changes } : task));
    return reply(200, { ...found, ...changes });
  }
  if (method === "DELETE") {
    practiceTasks = practiceTasks.filter((task) => task.id !== id);
    return reply(204);
  }
  return reply(405, { error: "method not allowed" });
}

const OFFLINE_TIP = "Offline: review your first unfinished task.";

export default function App() {
  const [message, setMessage] = useState("");
  const [serverUp, setServerUp] = useState(true); // used by the practice server only

  async function getSuggestion() {
    try {
      const response = await request("/suggest");
      if (!response.ok) throw new Error("HTTP " + response.status);
      const value = (await response.json()) as { tip?: unknown } | null;
      // Validate the field before showing it
      if (typeof value?.tip !== "string") throw new Error("Bad tip");
      setMessage("Server: " + value.tip);
    } catch {
      // Any failure uses a rule that works with no network
      setMessage(OFFLINE_TIP);
    }
  }

  async function addSampleTask() {
    try {
      const response = await request("/tasks", {
        method: "POST",
        body: JSON.stringify({ title: "Library visit" }),
      });
      setMessage(response.ok ? "Added a sample task." : "HTTP " + response.status);
    } catch (error) {
      setMessage(String(error));
    }
  }

  function toggleServer() {
    setPracticeServerUp(!serverUp);
    setServerUp(!serverUp);
  }

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Button title="Get a study suggestion" onPress={getSuggestion} />
      <Button title="Add sample task" onPress={addSampleTask} />
      <Button title={serverUp ? "Stop practice server" : "Start practice server"} onPress={toggleServer} />
      <Text>{message}</Text>
    </View>
  );
}
```

**Breakdown.** `request("/suggest")` returns the practice server's rule (or the real API's). `getSuggestion` checks the status and the `tip` field. Any failure sets the offline message. The server rule is the line `path === "/suggest"` inside the practice server.

**Expected behavior.** With the practice server on, the message starts with "Server:". Stop it and the next press uses "Offline:". Add sample task puts a record on the practice server, which the activity needs.

**Ungraded practice.** Predict what happens if the server returns `{"tip": 5}`. Restore the sample before assessment.

**Troubleshooting.** If the app always shows Offline with a real API, open `/suggest` in the phone's browser and check the JSON field name.

## D. Assessment, Wrap-Up & References

### One individual coding activity — 10 points

Change the **server rule** so that, when the task list is empty, the tip is different (for example "Add one small task first."). In the practice server, read `practiceTasks.length`. Show the tip for an empty list, the tip for a non-empty list, and your offline fallback. Explain why a private provider key would stay on the server.

| Evidence | Points |
|---|---:|
| Working core and independent change | 4 |
| Meaningful edge case (empty list and outage) and response | 2 |
| Explain the rule and the key boundary | 2 |
| Reproducible commands and readable source | 2 |

### Three equal-point delivery modes

**Mode 1 — Offline computer lab.** Before class, the lab PCs need Node 24.18.1, npm 11.16.0, VS Code and a separate copy of the prepared starter including `node_modules`. Use `START-LAB.cmd`; replace only the student's `App.tsx`. No installs in class. The practice server needs no network. Local type-checking passed for this lesson's code on the course baseline; a phone on local Wi-Fi with a compatible Expo Go, or a prepared emulator, still needs a successful [smoke test](../offline-lab/SMOKE-TEST.md). If no display route passes, use Mode 3, not an untested promise. `--tunnel` is an online fallback only.

**Mode 2 — Prepared personal laptop.** Follow the handout below, bring your laptop and do the activity in class. Submit source, `package.json`, the lockfile, a README with the commands and the actual activity date, success and failure evidence and a brief explanation. Recommended folder or repository: `ADET-M16-LASTNAME` (the instructor confirms the pattern). Do not upload `node_modules`, cache or secrets.

**Mode 3 — Written alternative (10 points).** Trace the button with the server on and an empty list, on with one task, off, and a reply missing `tip`. Give the message and its source each time, write the changed rule, and explain where the provider key lives. Submit a step-by-step table plus a 150–250-word explanation. It earns the same maximum as the coding activity; no device screenshot is required.

| Written evidence | Points |
|---|---:|
| Correct complete trace and proposed change | 4 |
| Edge or failure case and justified correction | 2 |
| Explanation connecting code to visible behavior | 2 |
| Labeled inputs, ordered steps and readable evidence | 2 |

Guided copying and predictions are ungraded. Only the one selected assessment mode is graded.

**Wrap-up.** Explain how a request becomes "Server" or "Offline", and where a secret key would live. Name the layer you would inspect first if the fallback always showed.

[Expo API routes](https://docs.expo.dev/router/web/api-routes/)

### Instructor notes

Pacing: 5 review, 15 explanation, 10 guided code, 25 activity, 5 wrap-up. A model solution changes the practice rule to `practiceTasks.length === 0 ? "Add one small task first." : "Review your first unfinished task."`. Use the Add sample task button to move the practice server from an empty list to a non-empty one. Managed backends, GraphQL and experimental features stay as comparison only. Device and network behavior are not yet recorded on the course baseline.

### Before next meeting — M16 preparation handout (put it on the last slide of the previous meeting)

For the upcoming **M16 coding meeting**, prepare **your own laptop**, then bring it. The instructor confirms the date and naming pattern.

```powershell
npx create-expo-app@latest ADET-M16-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M16-LASTNAME
npx tsc --noEmit
npx expo start
```

No extra packages are needed for the core activity. Use the distributed manifest and lockfile for exact versions. Open the app once before class and bring a screenshot or the exact error. Without home internet, prepare on campus Wi-Fi, mobile data or an agreed hotspot, or copy the [prepared starter and dependencies by USB](../offline-lab/README.md). Internet preparation is not graded.
