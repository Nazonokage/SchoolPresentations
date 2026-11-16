# EDP visual guide and presentation image list

Prepared 3 November 2026. These are suggested slide placements, not fixed page numbers: split long material according to readable text size. Each module now includes its own diagram and teaching notes.

## Module 01: Callback and delayed order

- [Local sample diagram](m01-guide.svg): Register callback → Continue main code → Timer eligible → Run callback.
- Teaching caption: A timer schedules work; it does not pause subsequent statements.
- Output image: capture the actual M01 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 02: Scheduling trace

- [Local sample diagram](m02-guide.svg): Sync A, B → Promise C → Timer D → Async result.
- Teaching caption: This is the supplied example trace, not a universal ordering diagram for every Node context.
- Output image: capture the actual M02 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 03: DOM event path

- [Local sample diagram](m03-guide.svg): HTML button → Register listener → User clicks → Update text.
- Teaching caption: Show the real button screenshot beside this diagram; registration happens before the click.
- Output image: [checked browser capture](../instructor/m03-checked.png).
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 04: One event, several listeners

- [Local sample diagram](m04-guide.svg): Order created → Invoice listener → Kitchen listener → Dispose listeners.
- Teaching caption: Invoice and kitchen both react; the arrows here show reading order, not an async queue.
- Output image: capture the actual M04 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 05: Latest request wins

- [Local sample diagram](m05-guide.svg): Request 1 starts → Request 2 starts → Result 2 shown → Result 1 ignored.
- Teaching caption: An old response must not overwrite a newer request; cancellation alone is not the correctness check.
- Output image: capture the actual M05 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 06: Typed event boundary

- [Local sample diagram](m06-guide.svg): Unknown JSON → Runtime guard → Typed payload → Typed handler.
- Teaching caption: TypeScript checks source; the runtime guard checks external data.
- Output image: capture the actual M06 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 07: Order state machine

- [Local sample diagram](m07-guide.svg): Waiting → Preparing → Ready → Collected.
- Teaching caption: Only allowed transitions succeed. A direct waiting-to-collected command is rejected.
- Output image: capture the actual M07 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 08: Reactive search pipeline

- [Local sample diagram](m08-guide.svg): Input values → Debounce → Switch latest → Render result.
- Teaching caption: The browser example uses simulated results. Unsubscription tears down the stream.
- Output image: [checked browser capture](../instructor/m08-checked.png).
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 09: Live announcement flow

- [Local sample diagram](m09-guide.svg): Node server → SSE connection → EventSource → Announcement UI.
- Teaching caption: The stream is server-to-client; the sample has no durable replay.
- Output image: [checked browser capture](../instructor/m09-checked.png).
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 10: Stream pipeline

- [Local sample diagram](m10-guide.svg): Readable source → Transform → Slow writable → Completion.
- Teaching caption: Backpressure communicates capacity upstream; highWaterMark is not a universal hard memory cap.
- Output image: capture the actual M10 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 11: Behavior test cycle

- [Local sample diagram](m11-guide.svg): Arrange instance → Perform action → Assert result → Clean up.
- Teaching caption: A useful test checks rejected actions and cleanup as well as success.
- Output image: capture the actual M11 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 12: Messaging model comparison

- [Local sample diagram](m12-guide.svg): Producer → Queue or topic → Consumers → Replay position.
- Teaching caption: Use separate slides for competing consumers, broadcast and retained logs; do not imply identical guarantees.
- Output image: capture the actual M12 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 13: Reliable consumer

- [Local sample diagram](m13-guide.svg): Receive ID → Check duplicate → Apply effect → Ack or retry.
- Teaching caption: Real deduplication and the business change need an atomic durable boundary; this model is in memory.
- Output image: capture the actual M13 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 14: Outbox publication

- [Local sample diagram](m14-guide.svg): Domain write → Outbox record → Relay publishes → Inbox dedupes.
- Teaching caption: Domain write and outbox insert belong in one local transaction. Delivery can still duplicate.
- Output image: capture the actual M14 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 15: Replay and projection

- [Local sample diagram](m15-guide.svg): Accepted history → Pure reducer → Rebuilt state → Read projection.
- Teaching caption: Replay computes state; it must not blindly repeat emails or payments.
- Output image: capture the actual M15 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 16: Saga recovery

- [Local sample diagram](m16-guide.svg): Reserve → Attempt payment → Failure detected → Release reserve.
- Teaching caption: Compensation is a new action and can itself fail; it is not always a perfect rollback.
- Output image: capture the actual M16 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 17: Observe and authorize

- [Local sample diagram](m17-guide.svg): Validate shape → Check actor → Handle or reject → Log and metrics.
- Teaching caption: Correlation helps trace work; it does not authenticate the actor.
- Output image: capture the actual M17 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 18: Solo project vertical slice

- [Local sample diagram](m18-guide.svg): Input → Validate command → Change and emit → Test result.
- Teaching caption: One complete personal feature is the core; label optional network/database boundaries honestly.
- Output image: capture the actual M18 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 19: Repair rehearsal

- [Local sample diagram](m19-guide.svg): Observe symptom → Trace handler → Repair cause → Regression check.
- Teaching caption: Introduce one fault at a time and explain the mechanism before adding more complexity.
- Output image: capture the actual M19 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

## Module 20: Submission readiness

- [Local sample diagram](m20-guide.svg): Clean setup → Main flow → Failure demo → Explain and package.
- Teaching caption: Include reproducible commands, references and known limitations; keep credentials out of the archive.
- Output image: capture the actual M20 terminal result; no screenshot is claimed supplied.
- Place the visual on concept/code-trace slides; keep assessment answers in instructor mode.

