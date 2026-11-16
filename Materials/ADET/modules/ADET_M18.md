# ADET M18 · Solo project integration

[Module index](README.md) · Pre-final · 60–90 minutes · Individual coding activity

## A. Lesson Preview & Review

**What can one student deliver end to end?** Recall M08 to M16: you met validation, persistence, failure paths and fallbacks one at a time. Today you combine a small set of them into one working flow.

**Learning targets:** choose one campus problem and one user action that solves it, name who owns each piece of state, integrate validation, persistence and failure handling, and write evidence another student can reproduce.

**Trace:** User action → Validate → Persist → Verify. Explain in your own words: a personal errand appears after creating and refreshing; a failed request shows feedback and the existing list stays usable.

## B. Detailed Main Lesson

### In plain words

One complete, working flow is worth more than many half-finished screens. Pick one problem, one action and one place the data lives. Then prove it: create a record, restart, refresh, and see it again. Prove the failure too: stop the server and show that the screen still makes sense.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| Acceptance criterion | One sentence that says when the feature is done, for example "a finished errand can be reopened" | Endless features, no finish line |
| State owner | The search field belongs to the screen, the stored task to the backend, the "Loading" text to the request | Two copies of the same data |
| Validate at the edge | The app checks input and the server checks again | Trusting only the client |
| Verify persistence | Create, restart, refresh, see it again | "It worked once" |
| Failure without loss | A failed request leaves the existing list on screen | A cleared list after an error |
| Reproducible notes | Setup commands, seed data and a short test checklist | "Works on my laptop" |

```text
user action -> validate (client) -> API validates -> store -> reload -> screen
                                          failure -> message, list unchanged
```

**Predict first:** you stop the practice server and press Refresh. Does the list on screen disappear?

| Step | Screen | Reason |
|---|---|---|
| Add "Photocopy ID" | Loaded 1 | Written and reloaded |
| Show unfinished | 1 row | Derived filter, data unchanged |
| Stop server, Refresh | Network error, list still shown | The `catch` does not clear `tasks` |
| Start server, Refresh | Loaded 1 | Source of truth restored |

A classmate should be able to reproduce your acceptance criterion using only your setup notes and sample data. Use Git commits, a README, seed data and a small test checklist. Optional native or emerging features come only after the core works.

**Misconception:** "more features means a better project." A single flow with a success case, an invalid input and a failure case is easier to defend than many untested screens.

### Common mistakes

- Starting several features and finishing none.
- Clearing the list when a request fails.
- Skipping the notes that let another student run the project.

## C. Analogy, Guided Program & Practice

**Analogy.** Mas madaling patunayan ang isang buong gumaganang flow kaysa maraming kalahating screen. Parang isang buong ulam na luto at natikman, kaysa limang ulam na hilaw.

**Use case:** a personal errands tracker that survives a restart.

**Install first.** None. The practice server needs no package or network.

**Run it.** Copy this lesson's complete `App.tsx` into your prepared project from M01 (replace the whole file). Run `npx tsc --noEmit`, then `npx expo start --offline` in the prepared lab or `npx expo start` while online. Metro transpiles; it does not type-check. Course versions are recorded in M01.

**Practice server.** With no setup, `request()` uses a small fake server that lives inside the app, so this lesson runs offline. The Stop/Start button rehearses a connection failure. To use a real API instead, start one from [the API examples](../examples/api/README.md), set `EXPO_PUBLIC_API_URL`, and restart Expo (the value is read when the app bundles). On a physical phone use the PC's network address, not `localhost`.

**App.tsx — integration checkpoint** · [Copyable file](../examples/M18/App.tsx)

```tsx
import { useState } from "react";
import { View, Text, Button, TextInput, FlatList } from "react-native";

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

export default function App() {
  const [onlyUnfinished, setOnlyUnfinished] = useState(false);
  const [tasks, setTasks] = useState<Task[]>([]);
  const [title, setTitle] = useState("");
  const [message, setMessage] = useState("");
  const [busy, setBusy] = useState(false);
  const [serverUp, setServerUp] = useState(true); // used by the practice server only

  async function callApi(method: "GET" | "POST" | "PATCH" | "DELETE", id = "") {
    setBusy(true);
    try {
      if (method !== "GET") {
        const response = await request("/tasks" + (id ? "/" + id : ""), {
          method,
          headers: { "Content-Type": "application/json" },
          body:
            method === "DELETE"
              ? undefined
              : JSON.stringify(method === "POST" ? { title } : { done: true }),
        });
        if (!response.ok) throw new Error("HTTP " + response.status);
        if (method === "POST") setTitle("");
      }
      const reload = await request("/tasks");
      if (!reload.ok) throw new Error("Reload failed");
      const list: unknown = await reload.json();
      if (
        !Array.isArray(list) ||
        !list.every(
          (row) =>
            typeof row?.id === "string" &&
            typeof row.title === "string" &&
            typeof row.done === "boolean",
        )
      ) {
        throw new Error("Invalid record");
      }
      setTasks(list);
      setMessage("Loaded " + list.length);
    } catch (error) {
      // A failed request leaves the existing list on screen
      setMessage(String(error));
    } finally {
      setBusy(false);
    }
  }

  function toggleServer() {
    setPracticeServerUp(!serverUp);
    setServerUp(!serverUp);
  }

  // Derived value: the screen filters; the backend still owns the records
  const visibleTasks = onlyUnfinished ? tasks.filter((task) => !task.done) : tasks;

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <TextInput value={title} onChangeText={setTitle} placeholder="Task title" />
      <Button disabled={busy} title="Add" onPress={() => callApi("POST")} />
      <Button disabled={busy} title="Refresh" onPress={() => callApi("GET")} />
      <Button title={serverUp ? "Stop practice server" : "Start practice server"} onPress={toggleServer} />
      <Text>{message}</Text>
      <Button
        title={onlyUnfinished ? "Show all" : "Show unfinished"}
        onPress={() => setOnlyUnfinished(!onlyUnfinished)}
      />
      <FlatList
        data={visibleTasks}
        keyExtractor={(task) => task.id}
        renderItem={({ item }) => (
          <View>
            <Text>
              {item.title} {item.done ? "✓" : ""}
            </Text>
            <Button disabled={busy} title="Finish" onPress={() => callApi("PATCH", item.id)} />
            <Button disabled={busy} title="Delete" onPress={() => callApi("DELETE", item.id)} />
          </View>
        )}
      />
    </View>
  );
}
```

**Breakdown.** This is the M08 CRUD screen plus a derived "unfinished" filter. `callApi` validates the reply before `setTasks`. The `catch` leaves `tasks` as it was. `visibleTasks` is computed, so the backend still owns the records.

**Expected behavior.** A personal errand appears after creating and refreshing. A failed request shows feedback and the existing screen remains usable.

**Ungraded practice.** Write one acceptance criterion for your own idea and say which state value each person or system owns.

**Troubleshooting.** If the screen works only until you restart the client, trace whether the POST actually reached the API and what the reload returned.

## D. Assessment, Wrap-Up & References

### One individual coding activity — 10 points

Implement **your own domain feature** on top of this checkpoint (for example a priority flag, a due text or a category). Submit a short diagram, the change, the run commands, a persistent result and failure evidence, and one acceptance criterion you tested.

| Evidence | Points |
|---|---:|
| Working core and your own feature | 4 |
| Meaningful edge case and failure evidence | 2 |
| Explain the data flow and your own change | 2 |
| Reproducible commands and readable source | 2 |

### Three equal-point delivery modes

**Mode 1 — Offline computer lab.** Before class, the lab PCs need Node 24.18.1, npm 11.16.0, VS Code and a separate copy of the prepared starter including `node_modules`. Use `START-LAB.cmd`; replace only the student's `App.tsx`. No installs in class. The practice server needs no network. Local type-checking passed for this lesson's code on the course baseline; a phone on local Wi-Fi with a compatible Expo Go, or a prepared emulator, still needs a successful [smoke test](../offline-lab/SMOKE-TEST.md). If no display route passes, use Mode 3, not an untested promise. `--tunnel` is an online fallback only.

**Mode 2 — Prepared personal laptop.** Follow the handout below, bring your laptop and do the activity in class. Submit source, `package.json`, the lockfile, a README with the commands and the actual activity date, success and failure evidence and a brief explanation. Recommended folder or repository: `ADET-M18-LASTNAME` (the instructor confirms the pattern). Do not upload `node_modules`, cache or secrets.

**Mode 3 — Written alternative (10 points).** Trace your chosen action through validate, API, storage and verify, with one failure. Give one acceptance criterion, the fields that identify a record, and the status codes you expect. Submit a step-by-step table plus a 150–250-word explanation. It earns the same maximum as the coding activity; no device screenshot is required.

| Written evidence | Points |
|---|---:|
| Correct complete trace and proposed change | 4 |
| Edge or failure case and justified correction | 2 |
| Explanation connecting code to visible behavior | 2 |
| Labeled inputs, ordered steps and readable evidence | 2 |

Guided copying and predictions are ungraded. Only the one selected assessment mode is graded.

**Wrap-up.** Explain, in order, how your action reaches storage and returns, and which state each part owns. Name the layer you would inspect first if the record vanished after a restart.

[React Native networking](https://reactnative.dev/docs/network)

### Instructor notes

Pacing: 5 review, 15 explanation, 10 guided code, 25 activity, 5 wrap-up. Keep the feature small. Accept the practice server for the in-class demo but ask students to say plainly that it resets when the app restarts; the persistence claim needs a real backend. Native features are optional and only after the core works. Device and network behavior are not yet recorded on the course baseline.

### Before next meeting — M18 preparation handout (put it on the last slide of the previous meeting)

For the upcoming **M18 coding meeting**, prepare **your own laptop**, then bring it. The instructor confirms the date and naming pattern.

```powershell
npx create-expo-app@latest ADET-M18-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M18-LASTNAME
npx tsc --noEmit
npx expo start
```

No extra packages are needed for the core activity. Use the distributed manifest and lockfile for exact versions. Open the app once before class and bring a screenshot or the exact error. Without home internet, prepare on campus Wi-Fi, mobile data or an agreed hotspot, or copy the [prepared starter and dependencies by USB](../offline-lab/README.md). Internet preparation is not graded.
