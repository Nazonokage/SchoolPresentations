# EDP Module 20: Applied Knowledge and Mini-Capstone Defense Preparation

[Module index](README.md) | [Setup and commands](../examples/README.md)

**Period:** Finals · **Meeting:** 60–90 minutes · **Assessment:** 20-item applied quiz plus two defense essays (individual, 30 points)

## A. Lesson Preview & Review

Choose a tentative project. Then practice defending its decisions with a concrete input, the expected behavior and evidence a panel could inspect.

**In a nutshell:** Explain one event flow from requirement to evidence, including how it fails. No new code is introduced; this module checks that you can reason about what you have already built.

**Learning targets**

1. Answer applied scenarios about listeners, timers, async work, validation, state rules and reliability.
2. Defend one design choice with an observable result and a failure check.
3. Distinguish similar-looking faults, such as duplicate registration versus redelivery, using evidence.

**Before class:** M01–M19 summaries, the Quick Reference and your M18 project notes. No new code is introduced.

**60-minute route:** 5 minutes preview, 10 warm-up, 20 quiz, 25 essay writing (finish the second essay as preparation). For 90 minutes, write both essays in class (about 15 minutes each) and add 10 minutes of feedback.

**Scope:** Core: the 20-item quiz and the two essays, answered from your own project where possible. This module does not introduce new infrastructure. The quiz answer key is separate and instructor-only.

## B. Main Lesson

### Defense warm-up

Use this sequence: **requirement → design choice → observable result → failure check.** Explain one decision aloud before writing. *Paano mo patutunayan na gumana?* Point to the screen, record, event trace or test that would settle the question.

A worked example from the canteen board:

- **Requirement:** A collect command must only succeed when the order is ready.
- **Design choice:** A transition table; undefined entries are rejected (M07).
- **Observable result:** `Rejected: collect in waiting`, then `ready -> collected` after the order is prepared.
- **Failure check:** A second collect is rejected as well, and no new fact is recorded.

### What counts as evidence

A panel can inspect a console trace, a test that fails when the behavior is removed, an event list with payloads, or a diagram that matches the code. A claim such as “it works” or “it is secure” is not evidence until one of these shows it. When your project is a local model, say so plainly: honesty about limits is part of the answer.

## C. Applied Quiz · 20 items

Spend about 20 minutes. Answer each scenario in one or two sentences. Each item is worth one point.

1. A button responds before it is clicked. What registration mistake might explain it?
2. A timeout is followed by a synchronous log. Which runs first?
3. What happens to a pending timeout after clearTimeout receives its handle?
4. One order should trigger an invoice and kitchen update. How can they stay independent?
5. A Node listener takes a long time synchronously. What does that do to emit?
6. A setup function runs twice and each click now logs twice. What should you inspect?
7. A newly added list row has no direct handler. How can a parent handle its click?
8. Why handle submit on the form instead of only a button click?
9. An old search result arrives last. What check protects the display?
10. Which input pattern waits for a quiet interval before searching?
11. What is required in addition to TypeScript for incoming network messages?
12. A user tries to collect an order still being prepared. What should happen?
13. A reactive search screen closes. What releases its subscription?
14. Which taught transport suits one-way live campus announcements?
15. A slow destination cannot consume incoming chunks. What should the producer respect?
16. Two kitchen workers should divide jobs. Which model fits?
17. An acknowledgment is lost after a charge succeeds. What protects against a second charge?
18. Why record an outbox item with an order in the same transaction?
19. Why avoid sending email inside a replay reducer?
20. Which test demonstrates cleanup after a listener is removed?

## D. Defense Essays, Assessment & Wrap-Up

### Two essays

Allow about 15 minutes per essay. Write one or two focused paragraphs each, using your proposed project where possible.

1. Defend an event flow for your own campus project. Name its producer, payload, two possible reactions and state rule. Trace one accepted action and one rejected action. Explain which reaction runs synchronously and how you will prove that cleanup works.
2. A student reports that one action produced two notifications. Compare duplicate registration with redelivery after a lost acknowledgment. Explain how you would distinguish them using a trace, repair the relevant cause and demonstrate the repair with a repeatable test.

### Scoring

| Part | Points | Evidence |
| --- | ---: | --- |
| Applied quiz | 20 | One point per item (20 items) |
| Essay 1: your event flow | 5 | Producer, payload, two reactions and state rule named (2); accepted and rejected trace (1); synchronous versus later reaction identified and a cleanup proof named (1); specific to your own project (1) |
| Essay 2: two notifications | 5 | Duplicate registration and redelivery distinguished with evidence such as `listenerCount` versus a repeated event ID (2); repair matches the cause, for example removing the extra registration versus deduplicating by ID (1); repeatable test described (1); clear and concise (1) |
| Total | 30 | Quiz 20 plus 5 per essay |

The summative and periodical exams have separate slots; this module is not either of them.

### Wrap-up

You should now be able to explain one event flow, its failure behavior and the evidence that would convince a panel. Keep both essays as rehearsal notes for [Module 21](EDP_M21.md).

**Exit reflection (ungraded):** Which of your own design decisions was hardest to defend with evidence, and what trace or test would fix that?

**Next connection:** M21 is the solo mini-capstone announcement and readiness package. Bring your essays and your project folder.

### References and further reading

- [Official/reference documentation: nodejs.org](https://nodejs.org/api/events.html)
- [Official/reference documentation: developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/removeEventListener)

The prose is an original teaching text informed by the references. Read [validation notes](../instructor/VALIDATION.md) before distributing a new toolchain version.
