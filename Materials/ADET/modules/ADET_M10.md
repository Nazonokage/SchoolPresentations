# ADET M10 · Server state and reliable mutations

[Module index](README.md) · Midterm · 60–90 minutes · Individual coding activity

## A. Lesson Preview & Review

**Why does the count stay stale after a successful save?** Recall M08: after a write the app reloaded the list by hand. Today a cache library does that bookkeeping, and we learn what it cannot do.

**Learning targets:** tell server state from UI state, name a query by its key, invalidate after a successful mutation, and show a failed save without repeating it automatically.

**Trace:** Cached count → POST → Invalidate → Refetch. Explain in your own words: the count rises after Add visit and a refetch; with the server stopped the screen shows a load or save failure.

## B. Detailed Main Lesson

### In plain words

Server data is a copy that can become old at any moment, because other phones can change the real records. A cache library (TanStack Query) keeps that copy, labels it with a key, and refetches when you say it is old. Button feedback is a different kind of state: it belongs to the screen.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| Query key | `["tasks"]` names one cached result | Different readers use different keys and never refresh |
| Mutation | A POST that changes the server | Treating it like a read |
| Invalidation | After success, mark the key old so active queries refetch | The count stays stale after a save |
| Pending state | `isPending` disables Add so a double tap does not send two POSTs | Duplicate records |
| Retry safety | Repeating a POST can create duplicates | Auto-retrying a write |
| Stale data | An old count can be shown if it is labeled and recoverable | Hiding the failure |

```text
useQuery(["tasks"]) --> count 3 (cached)
Add visit -> POST ok -> invalidateQueries(["tasks"]) -> refetch -> count 4
Add visit -> POST fails -> no invalidate -> show "Save failed"
```

**Predict first:** two phones read a count of 3. Phone B adds a record. What does phone A show, and when does it change?

| Moment | Phone A sees | Reason |
|---|---|---|
| Phone B saves | 3 | A's cache is old but unaware |
| A refetches or invalidates | 4 | Fresh read |
| Server stopped, A refetches | "Cannot load (last known count: 4)" | Query failed; old data kept and labeled |

Optimistic updates show a predicted change first and undo it on rejection. They are an extension. A cache alone does not give background or offline synchronization.

**Misconception:** "the cache keeps itself current." It only knows what you tell it: a refetch, an invalidation or a refetch trigger such as regaining focus.

### Common mistakes

- Invalidating before the POST succeeds.
- A different `queryKey` in the reader and in `invalidateQueries`.
- Turning on automatic retries for a POST.

## C. Analogy, Guided Program & Practice

**Analogy.** Na-save na sa server pero luma pa ang bilang? Parang lumang menu board sa kantina: tama ang kusina, luma ang karatula. I-refresh ang tamang karatula (query key).

**Use case:** a campus visit counter that several staff phones update.

**Install first (online):**

```powershell
npx expo install @tanstack/react-query
```

It is plain JavaScript, so it needs no `app.json` change. Install it while online, then restart the server. For the offline lab, the prepared starter must already contain it (see Mode 1).

**Run it.** Copy this lesson's complete `App.tsx` into your prepared project from M01 (replace the whole file). Run `npx tsc --noEmit`, then `npx expo start --offline` in the prepared lab or `npx expo start` while online. Metro transpiles; it does not type-check. Course versions are recorded in M01.

**Practice server.** With no setup, `request()` uses a small fake server that lives inside the app, so this lesson runs offline. The Stop/Start button rehearses a connection failure. To use a real API instead, start one from [the API examples](../examples/api/README.md), set `EXPO_PUBLIC_API_URL`, and restart Expo (the value is read when the app bundles). On a physical phone use the PC's network address, not `localhost`.

**App.tsx — complete checkpoint** · [Copyable file](../examples/M10/App.tsx)

```tsx
import { useState } from "react";
import { View, Text, Button } from "react-native";
import {
  QueryClient,
  QueryClientProvider,
  useMutation,
  useQuery,
  useQueryClient,
} from "@tanstack/react-query";

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

// retry: false so a failed load shows an error immediately in class
const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });

function TaskCount() {
  const cache = useQueryClient();
  const [serverUp, setServerUp] = useState(true); // used by the practice server only

  const count = useQuery({
    queryKey: ["tasks"],
    queryFn: async () => {
      const response = await request("/tasks");
      if (!response.ok) throw new Error("Load failed");
      const rows: unknown = await response.json();
      if (!Array.isArray(rows)) throw new Error("Expected a list");
      return rows.length;
    },
  });

  const addVisit = useMutation({
    mutationFn: async () => {
      const response = await request("/tasks", {
        method: "POST",
        body: JSON.stringify({ title: "Library visit" }),
      });
      if (!response.ok) throw new Error("Save failed");
    },
    // Only after a successful save: mark the cached count as old and fetch again
    onSuccess: () => cache.invalidateQueries({ queryKey: ["tasks"] }),
  });

  function toggleServer() {
    setPracticeServerUp(!serverUp);
    setServerUp(!serverUp);
  }

  const label = count.isPending
    ? "Loading"
    : count.isError
      ? "Cannot load" + (count.data !== undefined ? " (last known count: " + count.data + ")" : "")
      : "Server count: " + count.data;

  return (
    <View style={{ gap: 12 }}>
      <Text>{label}</Text>
      <Button disabled={addVisit.isPending} title="Add visit" onPress={() => addVisit.mutate()} />
      <Button title={serverUp ? "Stop practice server" : "Start practice server"} onPress={toggleServer} />
      {addVisit.isError && <Text>Save failed. Check the server before retrying.</Text>}
    </View>
  );
}

export default function App() {
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60 }}>
      <QueryClientProvider client={client}>
        <TaskCount />
      </QueryClientProvider>
    </View>
  );
}
```

**Breakdown.** `QueryClient` holds the cache; `retry: false` makes failures show at once in class. `useQuery` reads the count under `["tasks"]`. `useMutation` posts, and only `onSuccess` invalidates that key. `addVisit.isPending` disables the button while saving. The label keeps the last count visible when a later refetch fails.

**Expected behavior.** The count rises after Add visit and the refetch. With the practice server stopped, Add shows "Save failed" and the count itself does not change, because nothing asked for a new read. A failed refetch (the Retry button in the activity) shows "Cannot load" with the last known count.

**Ungraded practice.** Predict the screen after stopping the server and pressing Add. Restore the sample before assessment.

**Troubleshooting.** If data stays stale, compare the query key used by the reader and the invalidation.

## D. Assessment, Wrap-Up & References

### One individual coding activity — 10 points

Add a **Retry (refetch) button** that appears when loading failed, and show **recovery after the practice server is started again**. Do not repeat the POST automatically. Use `count.refetch()`.

| Evidence | Points |
|---|---:|
| Working core and independent change | 4 |
| Meaningful edge case (failed save or failed load) and response | 2 |
| Explain which key is invalidated and why | 2 |
| Reproducible commands and readable source | 2 |

### Three equal-point delivery modes

**Mode 1 — Offline computer lab.** Before class, the lab PCs need Node 24.18.1, npm 11.16.0, VS Code and a separate copy of the prepared starter including `node_modules`, plus `@tanstack/react-query` installed while online. Use `START-LAB.cmd`; replace only the student's `App.tsx`. No installs in class. The practice server needs no network. Local type-checking passed for this lesson's code on the course baseline; a phone on local Wi-Fi with a compatible Expo Go, or a prepared emulator, still needs a successful [smoke test](../offline-lab/SMOKE-TEST.md). If no display route passes, use Mode 3, not an untested promise. `--tunnel` is an online fallback only.

**Mode 2 — Prepared personal laptop.** Follow the handout below, bring your laptop and do the activity in class. Submit source, `package.json`, the lockfile, a README with the commands and the actual activity date, success and failure evidence and a brief explanation. Recommended folder or repository: `ADET-M10-LASTNAME` (the instructor confirms the pattern). Do not upload `node_modules`, cache or secrets.

**Mode 3 — Written alternative (10 points).** Trace phone A and phone B with a count of 3: B saves, A refetches, then the server stops and A refetches. Give the label each time, the key that is invalidated, and the line for the Retry button. Submit a step-by-step table plus a 150–250-word explanation. It earns the same maximum as the coding activity; no device screenshot is required.

| Written evidence | Points |
|---|---:|
| Correct complete trace and proposed change | 4 |
| Edge or failure case and justified correction | 2 |
| Explanation connecting code to visible behavior | 2 |
| Labeled inputs, ordered steps and readable evidence | 2 |

Guided copying and predictions are ungraded. Only the one selected assessment mode is graded.

**Wrap-up.** Explain why the count was stale before invalidation and what invalidation does. Name the layer you would inspect first if the count never changed after a successful save.

[TanStack Query for React Native](https://tanstack.com/query/latest/docs/framework/react/react-native)

### Instructor notes

Pacing: 5 review, 15 explanation, 10 guided code, 25 activity, 5 wrap-up. This is the only coding module that needs an extra package in Mode 1. Install `@tanstack/react-query` once while online and copy the starter, or use Mode 3. A model solution renders `<Button title="Retry" onPress={() => count.refetch()} />` when `count.isError`. Device behavior is not yet recorded on the course baseline.

### Before next meeting — M10 preparation handout (put it on the last slide of the previous meeting)

For the upcoming **M10 coding meeting**, prepare **your own laptop**, then bring it. The instructor confirms the date and naming pattern.

```powershell
npx create-expo-app@latest ADET-M10-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M10-LASTNAME
npx expo install @tanstack/react-query
npx tsc --noEmit
npx expo start
```

This lesson needs one extra package, installed above while online. Use the distributed manifest and lockfile for exact versions. Open the app once before class and bring a screenshot or the exact error. Without home internet, prepare on campus Wi-Fi, mobile data or an agreed hotspot, or copy the [prepared starter and dependencies by USB](../offline-lab/README.md). Internet preparation is not graded.
