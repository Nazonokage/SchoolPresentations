# ADET M21 · Mini-capstone announcement and solo project readiness

[Module index](README.md) · Finals · 60–90 minutes · Individual project

## Announcement

Build and defend **one individual project**. Continue the personal feature you began in M18. Choose one idea below or propose a comparable campus problem, and use your M20 essays to explain your decisions. The instructor confirms the submission date.

| Solo project idea | How to apply the principle | Defense demonstration |
|---|---|---|
| 1. Library seat requests | Server-side validation (M08). Send the seat ID to the API and enforce one reservation per seat and time slot in the database. | Request the same slot from two clients. Refresh both and show that only one reservation exists. |
| 2. Campus maintenance reports | Permission-aware design (M12). Make the description required and the photo optional. Keep typed text when camera access is denied. | Deny camera permission halfway through a report, submit it and retrieve the description. |
| 3. Study planner | Local drafts and server state (M09, M10). Save an unfinished task on the device. After a successful POST, clear the draft and refresh the server list. | Close the app mid-draft, restore it, then submit and show the updated count. |
| 4. Campus office directory | File-based routing (M05, M06). Give each office a stable ID and use that ID in its detail route, even when the directory is filtered. | Open a detail link directly, then try a made-up ID and show the recovery screen. |
| 5. Barangay supply checklist | Immutable list updates (M02, M06, M08). Mark a supply as packed by its record ID and persist that change through the API. | Filter the list, pack one item, then clear the filter and reload. Check that only the intended item changed. |
| 6. Study-break reminder | Notification lifecycle (M13). Keep the schedule ID so editing a reminder cancels the old schedule before creating the new one. | Schedule two different times for the same reminder. Show that only the revised reminder remains pending. |
| 7. Campus meetup card | Native handoff (M14). Build a share message from the selected venue and keep a readable address on screen for students who dismiss the chooser. | Open the share sheet, cancel it, then show that the selected venue and address are still available. |
| 8. Language practice flashcards | Media state and accessibility (M03, M15). Pair a bundled pronunciation clip with its transcript. Drive the playback label from player status. | Play and pause one card, then mute the phone and demonstrate how the transcript preserves the lesson. |
| 9. Club expense notebook | Input validation (M04, M08, M17). Check each amount in both the form and the API before saving the expense in integer centavos. | Submit a valid expense, then send a negative amount directly to the API. Reload and verify that the total stayed correct. |
| 10. Student equipment loans | Authorization (M11). Have the API derive the borrower from a verified session and check ownership before extending a loan. | Use two test accounts. Change the loan ID in the second account's request and show that the server refuses the extension. |

**Bring to the defense:** runnable source, setup instructions, a diagram, one successful case, one deliberate failure and evidence of your own change. Walk the panel through one design choice and one limitation. Use the readiness exercise below to rehearse.

## A. Lesson Preview & Review

**Could another student run your project from the submitted folder?** Recall M18: one complete flow beats many half-finished ones. Today you package and rehearse it.

**Learning targets:** run your project from a clean start, show a success case and a failure case, explain one of your own design choices, and hand the project over so someone else can run it.

**Trace:** Clean start → Demo → Failure case → Handoff. Explain in your own words: tapping each rehearsal item moves the count to 5/5; tapping again unchecks it; the count records your rehearsal, not automated proof.

## B. Detailed Main Lesson

### In plain words

A project is finished when someone else can run it and see it work, including when it fails. Rehearse with the real folder you will submit, not with the copy on your laptop's desktop. Tick a step only after you have shown evidence for it.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| Clean start | Follow your own README on another prepared machine | Commands that only work on your laptop |
| Persistent save | A fresh client can fetch what you saved | A demo that works until it restarts |
| Failure case | Name the input and the observed response | A demo with no failure shown |
| Handoff package | Client, API, schema or seed steps, an example config **without secrets**, commands, references, known limits | Missing files and leaked keys |
| Personal contribution | One design choice and one change you can make live | "I only copied the sample" |
| Honest limits | Name what your project does not do | Overclaiming |

```text
clean start -> demo (1 min name, 2 min working path) -> failure (1 min) -> trace your change (1 min)
tick each item only after showing evidence
```

**Predict first:** you tick "Valid save and reload" but the data disappears after a restart. Is the project ready?

| Rehearsal step | Evidence a panel can inspect |
|---|---|
| Clean launch | Started from the submitted README |
| Valid save and reload | Same record visible from a second client or after restart |
| Invalid input rejected | The input and the response |
| Failure and recovery | Server stopped, screen still usable |
| Explain personal change | The line you changed and why |

**Misconception:** "the checklist proves my project works." It records your rehearsal. Only the evidence you show does that. Use invented student information, never real data.

### Common mistakes

- A project that depends on a local absolute path.
- Including secrets or `node_modules` in the submission.
- Ticking the checklist without evidence.

## C. Analogy, Guided Program & Practice

**Analogy.** Kapag kailangan pang hulaan ng kaklase ang command, idagdag iyon sa README. Parang resipe: kung kailangan pang tawagan ang nagluto, kulang ang pagkakasulat.

**Use case:** the final five-minute rehearsal of your solo project.

**Install first.** None for the checklist.

**Run it.** Copy this lesson's complete `App.tsx` into your prepared project from M01 (replace the whole file). Run `npx tsc --noEmit`, then `npx expo start --offline` in the prepared lab or `npx expo start` while online. Metro transpiles; it does not type-check. Course versions are recorded in M01.

**App.tsx — rehearsal checklist** · [Copyable file](../examples/M21/App.tsx)

```tsx
import { useState } from "react";
import { View, Text, Button } from "react-native";

const steps = [
  "Clean launch",
  "Valid save and reload",
  "Invalid input rejected",
  "Failure and recovery",
  "Explain personal change",
];

export default function App() {
  const [completed, setCompleted] = useState<string[]>([]);

  function toggleStep(step: string) {
    setCompleted((current) =>
      current.includes(step) ? current.filter((item) => item !== step) : [...current, step],
    );
  }

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      {steps.map((step) => (
        <Button
          key={step}
          title={(completed.includes(step) ? "✓ " : "○ ") + step}
          onPress={() => toggleStep(step)}
        />
      ))}
      <Text>
        Rehearsed {completed.length}/{steps.length}
      </Text>
    </View>
  );
}
```

**Breakdown.** `steps` lists the five things to show. `toggleStep` adds a step to `completed` or removes it. The screen shows `completed.length` out of `steps.length`.

**Expected behavior.** Tapping each item advances the count to 5/5. Tapping an item again unchecks it. The count records your rehearsal, not automated proof.

**Ungraded practice.** Run the five-minute demo from a copy of your submitted folder, with a classmate following only your README.

**Troubleshooting.** A project that depends on a local absolute path may work only on its author's machine. Rehearse with the submitted folder.

## D. Assessment, Wrap-Up & References

### Individual activity — readiness rehearsal (10 points)

Submit your personal runnable project, a five-minute demo and a recorded clean-start check. Include one repaired or gracefully handled failure. Your instructor gives the rubric for the actual solo mini-capstone separately.

| Evidence | Points |
|---|---:|
| Working core and your own change | 4 |
| Failure case and recovery shown | 2 |
| Explain data flow and your own change | 2 |
| Reproducible setup and readable source | 2 |

**Delivery.** Mode 1: rehearse in the offline lab with the practice-server or sample-data version of your project. Mode 2: rehearse on your own prepared laptop. A student with no runnable route should talk to the instructor **before** the date; the written alternatives in earlier modules were designed for single concepts, not a whole project, so any substitute for the capstone is an instructor decision.

**Wrap-up.** Explain how your project moves from a clean start to a handoff another student can run. Name the layer you would inspect first if a classmate could not start it.

[Expo build introduction](https://docs.expo.dev/build/introduction/)

### Instructor notes

Pacing: 5 announcement, 15 explanation, 10 guided checklist, 25 rehearsal, 5 wrap-up. Confirm the date, rubric and any lab setup for the real defense. Decide in advance what a student with no runnable device may submit. Device behavior is not yet recorded on the course baseline.
