# Instructor answer keys

M00–M05: use [OPENER_ANSWER_KEY.md](OPENER_ANSWER_KEY.md). The following M06–M21 keys retain their existing assessments pending the later batches.

## M06 · Lists and shared client state

Look for this observed behavior: Type lib to see Library only. Mark it complete, clear the filter and observe Clinic is unchanged. Required independent work: Add a hide-completed switch and a reset action. Demonstrate an empty filtered list and restoration of all rows. Use the four criteria in the student sheet. An unchanged sample earns no independent-change credit.

## M07 · HTTP, APIs and asynchronous data

1. The server's response status
2. The async function's continuation
3. On the API server
4. Loading
5. No tasks yet
6. The HTTP error branch
7. It points to the phone
8. Its shape may differ
9. URL, network reachability and binding
10. To observe recoverable failure feedback

## M08 · Persistent CRUD through a database API

Look for this observed behavior: Add Library, mark it done, restart client, refresh and find its check mark. Delete it and refresh to see it disappear. Required independent work: Use one real backend. Add a reopen action for completed tasks and show a rejected blank title plus persistence after a server restart. Use the four criteria in the student sheet. An unchanged sample earns no independent-change credit.

## M09 · Local storage and offline behavior

1. Unsubmitted user input
2. A reusable copy of other data
3. Structured local records and queries
4. An empty draft
5. Restore retrieves the saved text
6. The previous saved value
7. Storage is device-local
8. Pending writes and reconciliation need a policy
9. In suitable secure storage
10. Compare server revision/version with the edit base

## M10 · Server state and reliable mutations

Look for this observed behavior: The count increases after Add visit and refetch. With the server stopped the screen shows load or save failure. Required independent work: Add pull-to-refresh or a Retry button and show recovery after restarting the API. Avoid automatically repeating POST. Use the four criteria in the student sheet. An unchanged sample earns no independent-change credit.

## M11 · Authentication, authorization and secure sessions

1. Establishing identity
2. Checking whether an operation is permitted
3. Device-local protected storage
4. ana
5. No
6. The demoActor entry
7. The client controls its own code
8. No, expiration and revocation still matter
9. The API using verified identity
10. That the response matches the initiated authorization flow

## M12 · Hardware, permissions and attachments

Look for this observed behavior: Allow capture to show a preview. Remove hides it. Deny access to see the fallback message. Required independent work: Add a text-only report path and a clear cancellation message. Use sample subjects for photos. Use the four criteria in the student sheet. An unchanged sample earns no independent-change credit.

## M13 · Notifications and background work

1. A device-scheduled user notification
2. A backend and push delivery service
3. The operating system
4. Ten seconds
5. Reminders disabled
6. A scheduling request succeeded
7. Foreground presentation has its own policy
8. OS and resource constraints
9. A usable in-app alternative
10. BackgroundTask with an appropriately registered task

## M14 · Linking, sharing and location

Look for this observed behavior: Share shows a chooser. Open map hands off a link to an Iloilo location. Return to see feedback. Required independent work: Share your selected campus place and add a visible address fallback if the handoff fails. Use the four criteria in the student sheet. An unchanged sample earns no independent-change credit.

## M15 · Audio, video and app performance

1. Media playback state and resources
2. To remove a streaming/network dependency
3. Return to the beginning
4. Starts the cue
5. playing
6. Suspend playback
7. Device volume, audio routing and interruptions
8. Debug instrumentation changes the workload
9. Measure the same realistic scenario before and after
10. Pair it with a visible label or transcript

## M16 · Backend alternatives and emerging technologies

Look for this observed behavior: With the supplied API online the message starts with Server. Stop it and the next press uses Offline. Required independent work: Change the server rule to select a tip for an empty list. Demonstrate your offline fallback and explain how the server selects its response and why private credentials stay on the server. Use the four criteria in the student sheet. An unchanged sample earns no independent-change credit.

## M17 · Testing, security and release planning

1. A check at an edge of accepted input
2. A build proposed for verification and release
3. Matching compatible native builds and updates
4. No
5. Yes
6. No
7. The installed binary lacks its native code
8. It is included in client code
9. Test a release build and review current platform requirements
10. When changing native code/configuration beyond the installed runtime

## M18 · Solo project integration

Look for this observed behavior: A personal errand appears after creating and refreshing. A failed request shows feedback and the existing screen remains usable. Required independent work: Implement your own domain feature on one chosen backend. Submit the diagram, change, run commands, persistent result and failure evidence. Use the four criteria in the student sheet. An unchanged sample earns no independent-change credit.

## M19 · Finals rehearsal and repair

1. In the component callback prop
2. Leading and trailing whitespace
3. Runtime validation at the consumer
4. Rejected
5. Accepted
6. They become accepted
7. It runs before the user acts
8. Which layer persisted it and whether the API committed
9. Show the failing input, change, and passing result
10. The required end-to-end flow and reproducible setup

## Module 20 · Applied knowledge for the mini-capstone defense

1. Component state bound to the input.
2. In each card instance, or keyed by card ID in their parent.
3. Its stable record ID.
4. A validated record ID that can be resolved independently.
5. A reachable PC address or hosted API URL.
6. HTTP error responses are responses. Check status or response.ok.
7. Runtime validation of the record shape.
8. An empty state distinct from loading and failure.
9. Refresh before retrying or use server-side idempotency.
10. In private backend configuration.
11. Both APIs implement the same HTTP and JSON contract.
12. Restart the server and client and fetch the same record again.
13. Invalidate or refetch the matching task query after success.
14. Device-local persistent key/value storage or SQLite.
15. The API verifies the actor and record owner on every protected request.
16. Offer a text-only path and preserve entered data.
17. Observe the notification on a supported device in the intended app state.
18. A compatible development build containing that library.
19. Allow wrapping or flexible height and verify with enlarged system text.
20. 80 should pass and 81 should fail.

**Essays, 5 points each.** Award 2 for accurate subject principles, 1 for a concrete application, 1 for justified reasoning about the failure or alternative, and 1 for observable verification. Accept equivalent well-supported designs.

Essay 1: expect a typed input, validated HTTP request, server-owned database access and a refreshed screen. Essay 2: a missing response leaves commit status uncertain. Look for refresh or stable operation identity before retry and a test that counts stored records.

## M21 · Final project readiness and presentation

Look for this observed behavior: Tapping each rehearsal item advances the count to 5/5. Tapping it again unchecks it. The count records your rehearsal, not automated proof. Required independent work: Submit your personal runnable project, a five-minute demo and a recorded clean-start check. Include one repaired or gracefully handled failure. Use the four criteria in the student sheet. An unchanged sample earns no independent-change credit.
