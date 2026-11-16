# ADET M19 · Finals rehearsal and repair

[Module index](README.md) · Finals · 60–90 minutes · 10-item quiz

## A. Lesson Preview & Review

**A form looks finished but accepts spaces.** Recall M17: tests catch defects at the edges. Today you reproduce a defect, find which layer it lives in, repair it and prove the repair.

**Learning targets:** reproduce a bug with the smallest failing input, decide whether it belongs to the screen, the API or the device, make one repair, and retest both the success and the failure path.

**Trace:** Reproduce → Isolate → Repair → Retest. Explain in your own words: three spaces give Rejected; a task with surrounding spaces gives Accepted.

## B. Detailed Main Lesson

### In plain words

Fixing a bug starts with making it happen on purpose. You find the smallest input that fails, work out which layer is wrong, change one thing and run the same input again. Writing the steps down is what makes the repair believable.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| Reproduce | The smallest failing input, written down | Guessing at a fix |
| Isolate | Is it the screen, the API or the device? | Changing three layers at once |
| Repair log | Three columns: input, expected, observed | Memory instead of evidence |
| Retest | Run the same inputs again, success and failure | "It seems fine now" |
| Type vs runtime | A compile-time type does not validate a network reply | Trusting TypeScript for outside data |
| Seed data | Use a known record, not a shared class database | Results nobody can repeat |

```text
reproduce -> isolate (screen? API? device?) -> one repair -> retest same inputs
```

**Predict first:** make a faulty copy by removing `.trim()`, so `checkTitle` uses `text ? ... : ...`. What does three spaces give?

| Input | Expected | Fixed version | Faulty copy (no trim) |
|---|---|---|---|
| (empty) | Rejected | Rejected | Rejected |
| three spaces | Rejected | Rejected | **Accepted** |
| `  Book  ` | Accepted | Accepted | Accepted |

Only the faulty copy disagrees, and only on spaces; that smallest failing input names the exact fix. For an API problem, record the status code and a sample body with personal details removed. Then say whether the repair belongs in the screen, the server or both. Restore the original behavior and repeat the same checks.

**Misconception:** "the compiler would have caught it." A type such as `string` accepts spaces and any text a server sends. Validation must run at runtime where the data enters.

### Common mistakes

- Changing several things before retesting.
- Passing a handler call (`onPress={go()}`) instead of a function, which runs it during rendering.
- Not recording the input that failed.

## C. Analogy, Guided Program & Practice

**Analogy.** Alamin muna kung paano ulitin ang bug bago galawin ang code. Parang doktor: itatanong muna kung kailan sumasakit bago magbigay ng gamot.

**Use case:** rehearsing the repair step of your solo project.

**Install first.** None.

**Run it.** Copy this lesson's complete `App.tsx` into your prepared project from M01 (replace the whole file). Run `npx tsc --noEmit`, then `npx expo start --offline` in the prepared lab or `npx expo start` while online. Metro transpiles; it does not type-check. Course versions are recorded in M01.

**Lab note.** Quiz modules do not need a delivery mode. Work on a separate copy for the faulty version.

**App.tsx — fixed baseline** · [Copyable file](../examples/M19/App.tsx)

```tsx
import { useState } from "react";
import { View, Text, Button, TextInput } from "react-native";

// The fixed version. The practice below removes trim() on a separate copy.
function checkTitle(text: string) {
  return text.trim() ? "Accepted" : "Rejected";
}

export default function App() {
  const [input, setInput] = useState("");
  const [message, setMessage] = useState("");

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <TextInput placeholder="Task" value={input} onChangeText={setInput} />
      {/* Pass a function, do not call it while rendering */}
      <Button title="Check" onPress={() => setMessage(checkTitle(input))} />
      <Text>{message}</Text>
    </View>
  );
}
```

**Breakdown.** `checkTitle` is the single rule. The button passes a function to `onPress`, which runs only when tapped. The message line shows the result.

**Expected behavior.** Spaces give Rejected. A task with surrounding spaces gives Accepted.

**Ungraded practice.** On a separate copy, remove `.trim()` and fill the repair log (input, expected, observed). Restore the baseline.

**Troubleshooting.** If tapping does nothing, verify the callback runs, then trace the value the condition reads.

## D. Assessment, Wrap-Up & References

### 10-item quiz

Give a short answer for each item. The guided change above is ungraded.

1. Where is a press handler registered?
2. What does `trim` remove?
3. Which boundary checks incoming JSON?
4. What does a blank string display?
5. What does a title with surrounding spaces and real text display?
6. What changes if `trim` is removed, for an input of spaces only?
7. Why does calling a handler during rendering cause trouble?
8. A valid save disappears after restarting. What do you inspect?
9. How do you demonstrate a personal repair?
10. What takes priority before the practical?

**Answer key (instructor).**
1. On the component's event prop, such as `onPress`.
2. Leading and trailing whitespace.
3. Runtime validation where data enters (client reply check and server); not TypeScript.
4. Rejected.
5. Accepted.
6. The spaces become truthy text, so it is Accepted, which is the bug.
7. It runs on every render and can trigger repeated updates.
8. The persistence layer: storage, API or database, not the label.
9. Same input before and after, plus an explanation of the changed line.
10. One core flow that works, with a success path and a failure path.

**Wrap-up.** Explain how you would take a reported bug from "Reproduce" to "Retest" on your own project. Name the layer you would inspect first if a valid save disappeared.

[Debugging](https://reactnative.dev/docs/debugging)

### Instructor notes

Pacing: 5 review, 15 explanation, 10 guided code, 25 quiz, 5 wrap-up. The summative and periodical exams are separate slots. Use known seed records, not a shared class database. Device behavior is not yet recorded on the course baseline.
