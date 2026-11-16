# ADET M07 · HTTP, APIs and asynchronous data

[Module index](README.md) · Midterm · 60–90 minutes · 10-item quiz

## A. Lesson Preview & Review

**The phone can reach a server and still get bad data.** Recall M06: lists are derived from stored records. Today the records arrive from a server, which can fail in several different ways.

**Learning targets:** read an HTTP status code, load JSON safely with `fetch`, validate the shape of a response, and show different messages for loading, error, empty and success.

**Trace:** Tap Load → HTTP → Check JSON → List or error. Explain in your own words: a fresh server gives "No tasks yet"; after adding a record its title appears; stopping the server gives an error message.

## B. Detailed Main Lesson

### In plain words

An API is a server that answers requests with data. Your app sends a request, waits, and then must decide what the answer means. The request can fail before reaching the server, the server can answer "not found", or it can answer correctly with an empty list. Those are three different situations and need three different messages.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| Status code | A number in every reply: 2xx worked, 4xx the request was wrong, 5xx the server failed | Treating every reply as success |
| `fetch` rejects only on network failure | A 404 still fulfills the promise; `response.ok` is how you notice | Parsing an error page as JSON |
| Validate the shape | Valid JSON can still be an object, not an array, or lack `title` | `rows.map` crashes on a bad reply |
| Empty is not an error | `[]` is a successful reply that deserves its own text | "Error" shown for a brand-new list |
| `localhost` | On a phone it means the phone itself | Timeouts on a physical device |

```text
Load tapped -> "Loading…" -> request
   no connection ............ catch -> error text
   reply, status not ok ..... throw HTTP 404 -> error text
   reply ok, bad shape ...... throw Invalid list
   reply ok, [] ............. "No tasks yet"
   reply ok, rows ........... titles shown
```

**Predict first:** the practice server starts empty. What does Load show? Then press Add sample task and Load again. Then Stop practice server and Load.

| Action | Message | Why |
|---|---|---|
| Load (empty) | No tasks yet | Success with `[]` |
| Add sample task, Load | Library visit | Success with one record |
| Stop server, Load | Error: Network request failed | The request never got a reply |

**Misconception:** "a 404 means the network is down." The server answered, so changing Wi-Fi will not help; the route or URL is wrong.

**Overlapping loads.** If two Load taps overlap and the older reply arrives last, it overwrites the newer one. Tag requests, cancel old ones, or disable the button while loading. Axios can wrap HTTP calls, but the reply still needs the same checks.

### Common mistakes

- Reading `response.json()` before checking `response.ok`.
- Using `localhost` from a physical phone.
- Showing the same message for an empty list and a failed request.

## C. Analogy, Guided Program & Practice

**Analogy.** Kapag walang laman ang listahan, iba iyon sa walang koneksiyon. Parang pagtawag sa tindahan: walang sumasagot (network), "wala po kami niyan" (404), o "meron, pero ubos na" (empty list).

**Use case:** a campus announcements screen that must stay readable on a weak connection.

**Install first.** None. The practice server needs no package or network.

**Run it.** Copy this lesson's complete `App.tsx` into your prepared project from M01 (replace the whole file). Run `npx tsc --noEmit`, then `npx expo start --offline` in the prepared lab or `npx expo start` while online. Metro transpiles; it does not type-check. Course versions are recorded in M01.

**Practice server.** With no setup, `request()` uses a small fake server that lives inside the app, so this lesson runs offline. The Stop/Start button rehearses a connection failure. To use a real API instead, start one from [the API examples](../examples/api/README.md), set `EXPO_PUBLIC_API_URL`, and restart Expo (the value is read when the app bundles). On a physical phone use the PC's network address, not `localhost`.

**App.tsx — complete checkpoint** · [Copyable file](../examples/M07/App.tsx)

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
  const [message, setMessage] = useState("Tap Load");
  const [serverUp, setServerUp] = useState(true); // used by the practice server only

  async function load() {
    setMessage("Loading…");
    try {
      const response = await request("/tasks");
      // fetch only fails on a network problem, so check the status ourselves
      if (!response.ok) throw new Error("HTTP " + response.status);
      const rows: unknown = await response.json();
      if (!Array.isArray(rows) || !rows.every((row) => typeof row?.title === "string")) {
        throw new Error("Invalid list");
      }
      setMessage(rows.map((row) => row.title).join(", ") || "No tasks yet");
    } catch (error) {
      setMessage(String(error));
    }
  }

  async function addSample() {
    try {
      const response = await request("/tasks", {
        method: "POST",
        body: JSON.stringify({ title: "Library visit" }),
      });
      setMessage(response.ok ? "Added. Tap Load again." : "HTTP " + response.status);
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
      <Button title="Load campus tasks" onPress={load} />
      <Button title="Add sample task" onPress={addSample} />
      <Button title={serverUp ? "Stop practice server" : "Start practice server"} onPress={toggleServer} />
      <Text>{message}</Text>
    </View>
  );
}
```

**Breakdown.** `request()` is the only place that knows whether the server is real or practice. `load` sets "Loading…" first, checks `response.ok`, validates the array, and handles empty. The `catch` handles the network failure. Practice server code sits below the imports; read `load` first.

**Expected behavior.** A fresh server gives No tasks yet. After adding a record, its title appears. Stopping the practice server produces an error message.

**Ungraded practice.** Add a Retry button. Change the validation so an object reply is rejected with its own message. Restore the sample before the quiz.

**Troubleshooting.** If a real phone times out but the PC works, check the server binding, port, network isolation and `http` versus `https` policy. Open the URL in the phone's browser first.

## D. Assessment, Wrap-Up & References

### 10-item quiz

Give a short answer for each item. The guided change above is ungraded.

1. What does HTTP status 404 tell the client?
2. Does `fetch` reject when the server replies 404? Why or why not?
3. What does this screen show between tapping Load and the reply arriving?
4. A reply is valid JSON `{"title":"x"}` (an object). Why does the list check reject it?
5. The server returns `[]`. What does the screen show, and is it an error?
6. Why does `localhost` often fail from a physical phone?
7. No request appears in the server log. What do you check first?
8. Where should database credentials live?
9. Why repeat the check with the server stopped?
10. Two Load taps overlap and the older reply arrives last. What goes wrong, and how can you avoid it?

**Answer key (instructor).**
1. The server was reached but could not find that resource.
2. No. Only a network failure rejects; check `response.ok`.
3. "Loading…".
4. It is not an array.
5. "No tasks yet"; a successful empty result, not an error.
6. On a phone, `localhost` means the phone itself; use the PC's network address.
7. Reachability: host, port, same network, firewall, binding. Try the phone's browser.
8. On the server only, never in the app or in an `EXPO_PUBLIC_` variable.
9. To see the catch path, which differs from empty and from 404.
10. The old reply overwrites the new one; cancel or tag requests, or disable the button while loading.

**Wrap-up.** Explain how a tap becomes a list or an error, naming the three ways a request can go wrong. Name the layer you would inspect first if nothing reached the server.

[React Native networking](https://reactnative.dev/docs/network)

### Instructor notes

Pacing: 5 review, 15 explanation, 10 guided code, 25 quiz and discussion, 5 wrap-up. Run the practice-server demo first; a real API is optional. Check the real-API route on the actual classroom network before class; do not promise it works. Hardware and network results are not yet recorded on the course baseline.
