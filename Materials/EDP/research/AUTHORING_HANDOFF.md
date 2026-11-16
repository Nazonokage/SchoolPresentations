> **Current EDP plan:** [compiled contents: 20 modules](../compiled%20contents.md), split 5 / 6 / 7 / 2 with flexible grouping. This supersedes the earlier 17-module allocation below.

# Handoff for EDP lesson authoring

Prepared 2 November 2026 for the user's intended next session on 3 November 2026. This file is a continuation aid, not a scheduled automation.

## Read first

1. [Synthesis](SYNTHESIS.md) and [technical review](TECHNICAL_REVIEW.md).
2. [Current agreed pacing](../../Modern_2026_Course_Pack/AGREED_PACING.md).
3. [Verified references](VERIFIED_SOURCES.md).
4. Raw reports only for examples or additional topic leads.

## Resolve the 17-unit sequence before writing

Keep M01–04 for the explicit refresher, M05–09 for language bridge and foundational browser interaction, M10–15 for selected async/reliability concepts and integration, M16–17 for Finals preparation. This is a sequencing envelope, not a finalized title list. Prioritize prerequisites over covering every advanced topic in the reports. Revisit the earlier EDP 23-topic inventory only as a topic bank.

M01 should be interesting: brief introductions, a campus-app demonstration, then a tiny editable program. Never expect the opening demonstration's advanced code to be understood immediately. Make the setup environment available without consuming the entire class with installation.

## Required lesson contents

Use the familiar lesson structure: preview/targets, full explanation, Taglish analogy, guided runnable program, expected output, code trace, independent modification, troubleshooting, instructor notes, and direct source links. A 60-minute core can extend to 90 minutes through practice. Each unit needs one clear primary behavior.

Label every file as browser JavaScript, browser TypeScript requiring a build step, or Node code. Explain arrays/objects and TypeScript before using them heavily. Keep the HTML/CSS shell complete and minimal. Retain separate summative/periodical assessments and a small individual final project.

## Verification during authoring

- Record actual Node/TypeScript/package versions and commands; preserve the dependency lockfile if dependencies are needed.
- Execute console examples and verify their output in the named module format.
- Type-check TypeScript; runtime execution alone is insufficient.
- Exercise browser input, keyboard operation, invalid input, repeated setup/cleanup, and expected failure/recovery.
- Check pending timer/listener cleanup and pre-aborted signals where used.
- Keep snippet references and incomplete pseudocode out of “copy and run” starters.
- Do not describe mocks as real network systems or claim all event-driven programs need brokers.

Full module text and runnable code remain for the next authoring session. ADET authoring is outside the present EDP-only focus.
