# EDP Module 20 · Applied knowledge for the mini-capstone defense

[Course index](README.md) · Finals · Individual · 60–90 minutes

## A. Prepare

Choose a tentative project. Practice defending decisions using a concrete input, the expected behavior and evidence a panel could inspect.

## B. Defense warm-up

Use this sequence: requirement → design choice → observable result → failure check. Explain one decision aloud before writing. *Paano mo patutunayan na gumana?* Point to the screen, record, event trace or test that would settle the question.

## C. Applied quiz · 20 items

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

## D. Defense essays · two responses

Allow about 15 minutes per essay. Write one or two focused paragraphs each, using your proposed project where possible.

1. Defend an event flow for your own campus project. Name its producer, payload, two possible reactions and state rule. Trace one accepted action and one rejected action. Explain which reaction runs synchronously and how you will prove that cleanup works.
2. A student reports that one action produced two notifications. Compare duplicate registration with redelivery after a lost acknowledgment. Explain how you would distinguish them using a trace, repair the relevant cause and demonstrate the repair with a repeatable test.

Suggested score: quiz 20 points plus 5 per essay, 30 total. Keep both essays as rehearsal notes for [Module 21](EDP_M21.md). The summative and periodical have separate slots.
