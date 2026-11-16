# ADET M08 · Persistent CRUD through a database API

[Module index](README.md) · Midterm · 60–90 minutes · Individual coding activity

## A. Lesson Preview & Review

**Can two phones see the same task?** Recall M07: a response must be checked before it is shown. Today the app creates, reads, updates and deletes records that live on a server.

**Learning targets:** map Create, Read, Update, Delete to POST, GET, PATCH, DELETE; reload from the server after every write; tell invalid input (422) from a missing record (404); explain why credentials stay on the server.

**Trace:** Phone → Task API → Row or document → Refresh. Explain in your own words: add Library, finish it, refresh and find its check mark; delete it and refresh to see it disappear.

## B. Detailed Main Lesson

### In plain words

The phone never touches the database. It sends a small message (a method and some JSON) to an API. The API checks the message, changes the stored record and answers. After a change, the app asks the server for the list again, so the screen shows what is really stored.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| CRUD methods | POST creates, GET reads, PATCH changes part of a record, DELETE removes it | Using the wrong method gets 404 or 405 |
| Reload after write | The server is the source of truth; the screen replaces local state with the fresh list | The screen shows a record that was never saved |
| String IDs | The server turns a SQL row ID or a Mongo `_id` into a string for JSON | The client breaks when an ID type changes |
| 422 vs 404 | 422: the request was invalid (blank title). 404: the record does not exist | Offering "refresh" for bad input |
| Server-side safety | Prepared queries and allowed fields keep user input out of the query itself; credentials never ship in the app | A password inside `EXPO_PUBLIC_` is public |

```text
Add -> POST {title} -> server validates -> stores -> 201
        -> GET list -> validate -> replace tasks -> "Loaded n"
Finish -> PATCH {done:true} -> GET list
Delete -> DELETE (204, no body) -> GET list
```

**Predict first:** press Add with an empty title. What message appears, and does the list change?

| Step | Message | Tasks | Reason |
|---|---|---|---|
| Add "Library" | Loaded 1 | Library | POST then reload |
| Finish | Loaded 1 | Library ✓ | PATCH then reload |
| Add with blank title | Error: HTTP 422 | unchanged | Server rejected input |
| Delete | Loaded 0 | empty | 204, then reload |

**Two storage tracks, one contract.** In SQL a task is a row (`title`, `done` columns, `id` primary key). In MongoDB it is a document with an `_id`. Both servers answer with the same JSON, so this screen works with either. Authorization, indexes and transactions are next-step issues; you implement one track and compare the other.

**Misconception:** "after a successful POST I can just add the record locally." If the reload then fails, you cannot know what was stored. Refresh before retrying a create, or you may duplicate it.

### Common mistakes

- Parsing a 204 response body (there is none).
- Retrying a failed POST without checking what the server stored.
- Putting database credentials in the app.

## C. Analogy, Guided Program & Practice

**Analogy.** Iisang order slip ang sinusunod ng dalawang kusina: parehong API contract kahit magkaiba ang database. Ang slip ang JSON, ang kusina ang server, at ang kusinero ang nagtatago ng resipe (credentials).

**Use case:** a shared task list that two students can open on different phones.

**Install first.** None. The practice server lives inside the app.

**Run it.** Copy this lesson's complete `App.tsx` into your prepared project from M01 (replace the whole file). Run `npx tsc --noEmit`, then `npx expo start --offline` in the prepared lab or `npx expo start` while online. Metro transpiles; it does not type-check. Course versions are recorded in M01.

**Practice server.** With no setup, `request()` uses a small fake server that lives inside the app, so this lesson runs offline. The Stop/Start button rehearses a connection failure. To use a real API instead, start one from [the API examples](../examples/api/README.md), set `EXPO_PUBLIC_API_URL`, and restart Expo (the value is read when the app bundles). On a physical phone use the PC's network address, not `localhost`.

**App.tsx — complete checkpoint** · [Copyable file](../examples/M08/App.tsx)

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
      // Always reload: the server is the source of truth
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
      setMessage(String(error));
    } finally {
      setBusy(false);
    }
  }

  function toggleServer() {
    setPracticeServerUp(!serverUp);
    setServerUp(!serverUp);
  }

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <TextInput value={title} onChangeText={setTitle} placeholder="Task title" />
      <Button disabled={busy} title="Add" onPress={() => callApi("POST")} />
      <Button disabled={busy} title="Refresh" onPress={() => callApi("GET")} />
      <Button title={serverUp ? "Stop practice server" : "Start practice server"} onPress={toggleServer} />
      <Text>{message}</Text>
      <FlatList
        data={tasks}
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

**Breakdown.** `callApi` sends the write (unless the method is GET), checks `response.ok`, then always reloads and validates each record before `setTasks`. `busy` disables the buttons while a request is running. The practice server mirrors the real status codes.

**Expected behavior.** Add Library, finish it, press Refresh and see its check mark. Delete it and refresh to see it disappear. A blank title shows `HTTP 422`. Stop the practice server and every action shows a network error, with the old list still on screen.

**Ungraded practice.** Predict the message for finishing a task that was already deleted on the other client. Restore the sample before assessment.

**Troubleshooting.** If saving seems to work but nothing appears, check which base URL the GET uses. If a real API is set, check `EXPO_PUBLIC_API_URL`, restart Expo, and use a network address the phone can reach.

## D. Assessment, Wrap-Up & References

### One individual coding activity — 10 points

Add a **Reopen** action for finished tasks (PATCH `{done: false}`), show a **rejected blank title**, and show that the data **persists after the server is stopped and started** (for the practice server, note what that proves and what it does not). Use the practice server, or one real backend if your lab has one.

| Evidence | Points |
|---|---:|
| Working core and independent change | 4 |
| Meaningful edge case (blank title or missing record) and response | 2 |
| Explain the data flow and your own change | 2 |
| Reproducible commands and readable source | 2 |

### Three equal-point delivery modes

**Mode 1 — Offline computer lab.** Before class, the lab PCs need Node 24.18.1, npm 11.16.0, VS Code and a separate copy of the prepared starter including `node_modules`. Use `START-LAB.cmd`; replace only the student's `App.tsx`. No installs in class. The practice server needs no network. Local type-checking passed for this lesson's code on the course baseline; a phone on local Wi-Fi with a compatible Expo Go, or a prepared emulator, still needs a successful [smoke test](../offline-lab/SMOKE-TEST.md). If no display route passes, use Mode 3, not an untested promise. `--tunnel` is an online fallback only.

**Mode 2 — Prepared personal laptop.** Follow the handout below, bring your laptop and do the activity in class. Submit source, `package.json`, the lockfile, a README with the commands and the actual activity date, success and failure evidence and a brief explanation. Recommended folder or repository: `ADET-M08-LASTNAME` (the instructor confirms the pattern). Do not upload `node_modules`, cache or secrets.

**Mode 3 — Written alternative (10 points).** Trace Add Library, Finish, Add with a blank title, Delete, and a PATCH to a missing ID. Give the status code and the list after each step, and write the line for Reopen with its body. Submit a step-by-step table plus a 150–250-word explanation. It earns the same maximum as the coding activity; no device screenshot is required.

| Written evidence | Points |
|---|---:|
| Correct complete trace and proposed change | 4 |
| Edge or failure case and justified correction | 2 |
| Explanation connecting code to visible behavior | 2 |
| Labeled inputs, ordered steps and readable evidence | 2 |

Guided copying and predictions are ungraded. Only the one selected assessment mode is graded.

**Wrap-up.** Explain how a tap on Add reaches storage and comes back to the screen, and why the app reloads after a write. Name the layer you would inspect first if a saved record did not appear.

[FastAPI SQL databases](https://fastapi.tiangolo.com/tutorial/sql-databases/) · [React Native networking](https://reactnative.dev/docs/network)

### Instructor notes

Pacing: 5 review, 15 explanation, 10 guided code, 25 activity, 5 wrap-up. The practice server is in memory, so a restart of the *app* clears it; real persistence needs a real API. Say so plainly and do not count the practice server as database evidence. Start one real API only if you have tested it; see its README. A model Reopen action is `callApi("PATCH", id)` with a body of `{ done: false }`, so the function needs a second argument or a separate helper. Phone and network behavior are not yet recorded on the course baseline.

### Before next meeting — M08 preparation handout (put it on the last slide of the previous meeting)

For the upcoming **M08 coding meeting**, prepare **your own laptop**, then bring it. The instructor confirms the date and naming pattern.

```powershell
npx create-expo-app@latest ADET-M08-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M08-LASTNAME
npx tsc --noEmit
npx expo start
```

No extra packages are needed for the core activity. Use the distributed manifest and lockfile for exact versions. Open the app once before class and bring a screenshot or the exact error. Without home internet, prepare on campus Wi-Fi, mobile data or an agreed hotspot, or copy the [prepared starter and dependencies by USB](../offline-lab/README.md). Internet preparation is not graded.
