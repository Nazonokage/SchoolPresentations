# ADET M06 · Lists and shared client state

[Module index](README.md) · Midterm · 60–90 minutes · Individual coding activity

## A. Lesson Preview & Review

**If a list is filtered, which task did the student just tap?** Recall M04: props give a component its settings and state is what it remembers. Today a whole collection of records is kept predictable.

**Learning targets:** keep one list of records, derive the visible rows from a search text, identify a record by a stable ID, and update exactly one record without touching the others.

**Trace:** Task array → Filter → Stable ID → Toggle. Explain in your own words: type `lib` to see Library only, mark it complete, clear the filter and see that Clinic is unchanged.

## B. Detailed Main Lesson

### In plain words

A list on screen is just an array of records. You store the records once. The rows you see are computed from them, for example "only the tasks that contain the search text". Each record carries its own ID, so when the list shrinks or reorders, React and your code still know which record you meant.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| Single source of truth | `tasks` is stored once; `visibleTasks` is computed from it on every render | Storing a second filtered copy lets the two copies disagree |
| Stable key / ID | `keyExtractor` gives each row a key from the record's `id` | Using the row position as identity edits the wrong task after filtering |
| Immutable update | `map` returns a new array and replaces only the matching record | Mutating the old array can leave the screen unchanged |
| Empty state | `ListEmptyComponent` shows text when the filter matches nothing | A blank screen looks like a crash |
| Props vs shared state | Props are enough for a parent and its rows; a reducer, Context or a store is needed only when many screens edit the same records | Adding a store early adds code without solving a problem |

```text
tasks (all records, stored once)
   |  filter by query
   v
visibleTasks --> FlatList rows (key = task.id)
   ^
   | toggle id=2 -> map -> new tasks array (only id 2 changed)
```

**Predict first:** type `lib`, press the Library button, then clear the filter. What does Clinic show?

| Step | tasks | Rows visible | Reason |
|---|---|---|---|
| Start | Library, Clinic | 2 | Query is empty |
| Type `lib` | unchanged | 1 (Library) | Filter derives rows; no data changes |
| Press Library | Library done, Clinic open | 1 | `map` replaced id 1 only |
| Clear filter | unchanged | 2 | Clinic was never touched |

**Misconception:** "the row index is the ID." After filtering, Library is index 0 but still `id` 1. Updating by index would change whatever row is first, not the record the student meant.

**Compare, do not install:** a reducer centralizes update rules so they are easy to test; Context shares data between screens; Zustand is one external store. Pagination, virtualization and FlashList matter only after you have measured a slow list. Offer an accessible button next to any swipe action.

### Common mistakes

- Using the array index (or the title) as the key or as the update target.
- Storing `visibleTasks` in state and forgetting to update it when `tasks` changes.
- Editing an item in place instead of returning a new array.

## C. Analogy, Guided Program & Practice

**Analogy.** Hanapin ang record gamit ang ID, hindi ang puwesto sa pila. Ang pila (listahan) ay puwedeng umikli o magpalit ng ayos, pero ang taong may numero 2 ay si numero 2 pa rin. Ang `id` ang numero, ang `map` ang tagatawag na iisa lang ang tinatawag.

**Use case:** a student keeps a small to-do list of campus errands and searches it while the list grows. This is in-memory only; saving it comes in later modules.

**Install first.** None. `react` and `react-native` come with the prepared blank TypeScript project.

**Run it.** Copy this lesson's complete `App.tsx` into your prepared project from M01 (replace the whole file). Run `npx tsc --noEmit`, then `npx expo start --offline` in the prepared lab or `npx expo start` while online. Metro transpiles; it does not type-check. Course versions are recorded in M01.

**App.tsx — complete checkpoint** · [Copyable file](../examples/M06/App.tsx)

```tsx
import { useState } from "react";
import { View, Text, Button, TextInput, FlatList } from "react-native";

type Task = { id: number; title: string; done: boolean };

export default function App() {
  const [tasks, setTasks] = useState<Task[]>([
    { id: 1, title: "Library", done: false },
    { id: 2, title: "Clinic", done: false },
  ]);
  const [query, setQuery] = useState("");
  const [draft, setDraft] = useState("");
  const [editingId, setEditingId] = useState<number | null>(null);

  // Derived value: computed from tasks and query, never stored separately
  const visibleTasks = tasks.filter((task) =>
    task.title.toLowerCase().includes(query.toLowerCase()),
  );

  function saveDraft() {
    const title = draft.trim();
    if (title === "") return;
    if (editingId === null) {
      // New record: its ID comes from the data, not from the screen position
      const nextId = Math.max(0, ...tasks.map((task) => task.id)) + 1;
      setTasks((current) => [...current, { id: nextId, title, done: false }]);
    } else {
      setTasks((current) =>
        current.map((task) => (task.id === editingId ? { ...task, title } : task)),
      );
    }
    setEditingId(null);
    setDraft("");
  }

  function toggleDone(id: number) {
    // map copies the array and replaces only the matching record
    setTasks((current) =>
      current.map((task) => (task.id === id ? { ...task, done: !task.done } : task)),
    );
  }

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <TextInput placeholder="Filter campus tasks" value={query} onChangeText={setQuery} />
      <TextInput
        accessibilityLabel="Task title"
        placeholder="New or edited title"
        value={draft}
        onChangeText={setDraft}
      />
      <Button
        title={editingId === null ? "Add task" : "Save edit"}
        disabled={draft.trim() === ""}
        onPress={saveDraft}
      />
      <Text>
        Showing {visibleTasks.length} of {tasks.length}
      </Text>
      <FlatList
        data={visibleTasks}
        keyExtractor={(task) => String(task.id)}
        ListEmptyComponent={<Text>No matches</Text>}
        renderItem={({ item }) => (
          <View>
            <Button
              title={item.title + (item.done ? " ✓" : "")}
              onPress={() => toggleDone(item.id)}
            />
            <Button
              title={"Edit " + item.title}
              onPress={() => {
                setEditingId(item.id);
                setDraft(item.title);
              }}
            />
          </View>
        )}
      />
    </View>
  );
}
```

**Breakdown.** `tasks` is the only list. `visibleTasks` is derived and never stored. `toggleDone` and `saveDraft` return new arrays with `map` or spread. `keyExtractor` uses `String(task.id)`. The edit button copies a record's title into the draft and remembers its ID in `editingId`.

**Expected behavior.** Type `lib` to see Library only. Mark it complete, clear the filter and observe Clinic is unchanged. Add a task, then edit it by pressing its Edit button.

**Ungraded practice.** Predict which rows show for `c`, then for `zzz`. Why does "No matches" appear? Restore the sample before assessment.

**Troubleshooting.** If the wrong row changes after filtering, compare the ID used for the update with the one displayed. If rows flicker or duplicate, check that every key is unique.

## D. Assessment, Wrap-Up & References

### One individual coding activity — 10 points

Add a **hide-completed switch** and a **reset action** (back to the starting two tasks). Show an empty filtered list and the restoration of all rows. Keep the derived-value rule: do not store the filtered list. Use React Native's `Switch`, or a `Button` that toggles a boolean.

| Evidence | Points |
|---|---:|
| Working core and independent change | 4 |
| Meaningful edge case (empty filtered list) and response | 2 |
| Explain data flow and your own change | 2 |
| Reproducible commands and readable source | 2 |

### Three equal-point delivery modes

**Mode 1 — Offline computer lab.** Before class, the lab PCs need Node 24.18.1, npm 11.16.0, VS Code and a separate copy of the prepared starter including `node_modules`. Use `START-LAB.cmd`; replace only the student's `App.tsx`. No installs in class. Local type-checking passed for this lesson's code on the course baseline; a phone on local Wi-Fi with a compatible Expo Go, or a prepared emulator, still needs a successful [smoke test](../offline-lab/SMOKE-TEST.md). If no display route passes, use Mode 3, not an untested promise. `--tunnel` is an online fallback only.

**Mode 2 — Prepared personal laptop.** Follow the handout below, bring your laptop and do the activity in class. Submit source, `package.json`, the lockfile, a README with the commands and the actual activity date, success and failure evidence and a brief explanation. Recommended folder or repository: `ADET-M06-LASTNAME` (the instructor confirms the pattern). Do not upload `node_modules`, cache or secrets.

**Mode 3 — Written alternative (10 points).** Trace three tasks (Library, Clinic, Registrar) through: type `lib`, toggle Library, hide completed, reset. Write `tasks` and `visibleTasks` after each step, name the line that stores the hide flag, and justify why the filtered list is not stored. Submit a step-by-step table plus a 150–250-word explanation. It earns the same maximum as the coding activity; no device screenshot is required.

| Written evidence | Points |
|---|---:|
| Correct complete trace and proposed change | 4 |
| Edge or failure case and justified correction | 2 |
| Explanation connecting code to visible behavior | 2 |
| Labeled inputs, ordered steps and readable evidence | 2 |

Guided copying and predictions are ungraded. Only the one selected assessment mode is graded.

**Wrap-up.** Explain why `visibleTasks` is not stored in state, and what would break if the key were the array index. Name the part of the code you would inspect first if the wrong row toggled.

[FlatList](https://reactnative.dev/docs/flatlist) · [Rendering lists](https://react.dev/learn/rendering-lists)

### Instructor notes

Use 5 minutes for review, 15 for explanation and trace, 10 for guided code, 25 for the activity and 5 for wrap-up. The extra 30 minutes can compare a reducer on the board; do not add a package. Reducer, Context and Zustand stay as discussion. A model solution adds `const [hideDone, setHideDone] = useState(false)` and filters `tasks` with `!(hideDone && task.done)` inside `visibleTasks`; reset calls `setTasks` with the two starting records. Device behavior has not yet been recorded on the course baseline.

### Before next meeting — M06 preparation handout (put it on the last slide of the previous meeting)

For the upcoming **M06 coding meeting**, prepare **your own laptop**, then bring it. The instructor confirms the date and naming pattern.

```powershell
npx create-expo-app@latest ADET-M06-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M06-LASTNAME
npx tsc --noEmit
npx expo start
```

No extra packages are needed for the core activity. Use the distributed manifest and lockfile for exact versions. Open the app once before class and bring a screenshot or the exact error. Without home internet, prepare on campus Wi-Fi, mobile data or an agreed hotspot, or copy the [prepared starter and dependencies by USB](../offline-lab/README.md). Internet preparation is not graded.
