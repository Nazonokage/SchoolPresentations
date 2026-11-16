# ADET M20 · Applied knowledge for the mini-capstone defense

[Module index](README.md) · Finals · Individual · 60–90 minutes · 20-item quiz + two essays

## A. Lesson Preview & Review

**Can you explain your design with evidence?** Recall M00 to M19. Today you practice defending decisions the way a panel will ask for them.

**Learning targets:** answer scenario questions in one or two sentences, trace one flow from tap to storage and back, and describe a failure with a test and evidence a panel could inspect.

**Trace:** requirement → design choice → observable result → failure check. Explain in your own words one decision aloud before writing.

## B. Defense warm-up

### In plain words

A good defense names the user's problem, the one decision you made, what the panel can see, and what happens when something fails. *Paano mo patutunayan na gumana?* Point to the screen, the record, the trace or the test that settles the question.

| Defense habit | Why it helps |
|---|---|
| Name the input and the expected result | The panel can check you |
| Name the layer (screen, API, storage, device) | Shows you can isolate a problem |
| Show one success and one failure | Shows you tested more than the happy path |
| Say what you would change and what must stay fixed | Shows you understand the contract |

**Practice:** state your tentative project, its one flow and one failure in 60 seconds, then answer the quiz.

## C. Applied quiz · 20 items

Spend about 20 minutes. Answer each scenario in one or two sentences. Each item is worth one point.

1. A task screen stores its input in a normal local variable. What should own the changing input?
2. Two cards should show independent counters. Where should each count live?
3. Filtering changes the row order. What key should identify the edited task?
4. A detail link opens on a fresh launch. What information should the route carry?
5. The phone calls `localhost` but the API runs on a PC. Which address should the phone use?
6. GET returns HTTP 404. Why might `fetch` still fulfill?
7. A JSON response lacks `title`. What check is missing?
8. A task list returns an empty array. What should the UI display?
9. A retry after an uncertain POST creates duplicates. Suggest a recovery.
10. Where should the MongoDB URI or SQL password be stored?
11. How can one mobile screen use either database track?
12. How would you prove a task survived beyond React state?
13. A cached count stays stale after saving. Which action updates it?
14. Which storage suits an unsent local draft?
15. A signed-in user changes the requested record ID. Which layer checks ownership?
16. Camera permission is denied. How can a report still be completed?
17. A reminder was scheduled. What additional evidence demonstrates delivery?
18. A feature needs a native library missing from Expo Go. Which build should you prepare?
19. At large font size a button label clips. Give a practical fix.
20. A validator accepts titles of 1 to 80 characters. Which pair of inputs tests the upper boundary?

**Answer key (instructor), with the lesson it comes from.**
1. State, such as `useState` (M02, M03).
2. In each card's own component state (M04).
3. The record's stable ID, not its row position (M06).
4. The stable record ID in the route (M05).
5. The PC's network address or a reachable host name; `localhost` is the phone itself (M07).
6. `fetch` rejects only on a network failure; check `response.ok` (M07).
7. Runtime validation of the response shape (M07, M19).
8. An empty state such as "No tasks yet", not an error (M07).
9. Reload before retrying; use a client-made operation ID so the server can ignore a repeat (M08, M09, M10).
10. In the server's environment, never in the app (M07, M08).
11. Both servers follow one API contract and return the same JSON; only the base URL differs (M08).
12. Restart the app and reload from the API, or open a second client (M08).
13. Invalidate the query key and refetch (M10).
14. Local key/value storage (M09).
15. The server/backend (M11).
16. A text-only path that does not need the photo (M12).
17. Seeing the notification on the device after backgrounding, or a recorded response when tapped (M13).
18. A development build (M12, M13, M17).
19. Let the text wrap, remove fixed heights, allow scrolling and test with larger fonts (M04).
20. 80 characters accepted and 81 characters rejected (M17).

## D. Defense essays · two responses

Allow about 15 minutes per essay. Write one or two focused paragraphs each, using your proposed project where possible.

1. Choose one campus problem and defend your mobile design. Trace a tap from the screen through validation and the API to a SQL row or MongoDB document, then back to the UI. Justify your chosen storage and name one decision you could change without changing the API contract.
2. Your demo phone loses its connection immediately after Save. Explain what the app knows, what the student sees, and how to recover without silently duplicating a record. Describe a reproducible test and the evidence you would show the panel.

**Essay rubric (5 points each).**

| Criterion | Points |
|---|---:|
| Correct trace or recovery steps in order, with the layer named | 2 |
| Justified choice and what could change without breaking the contract | 1 |
| A reproducible test and the evidence shown | 1 |
| Clear, specific writing tied to a real project | 1 |

Suggested score: quiz 20 points plus 5 per essay, 30 total. Keep both essays as rehearsal notes for [Module 21](ADET_M21.md). The summative and periodical have separate slots.

### Instructor notes

Pacing: 5 introduction, 20 quiz, 30 essays, 5 wrap-up. Accept any answer that names the idea in the key. Essay 2 should mention that the app cannot know whether the server saved the record, so it reloads or checks before retrying. Device behavior is not recorded for this module.
