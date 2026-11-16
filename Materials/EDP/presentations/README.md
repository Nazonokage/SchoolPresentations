# EDP classroom presentations

Open EDP_M01.html through EDP_M21.html in a browser. These 21 standalone decks now contain 15–20 slides each, below the 25-slide maximum. Styles, scripts and guide diagrams are embedded.

## Reference and lesson design

Primary references are the instructor's OOP_M8_Part1_Methods_Arrays.html, DSA M12 Searching_Part2.html, module13_multiplatform_JS.html and module10_content_distribution.html. The redesign uses their restrained dark theme, copper/cyan hierarchy, code/explanation columns and short A–D choice tiles. Original subject files were not modified.

Main lessons use one concept per slide, short projected explanations, a module-specific flow and expandable detailed teaching notes. The module Markdown remains the full learning guide. Complete source panels preserve indentation and provide Copy; explanation excerpts are explicitly labeled. Long source panels scroll rather than shrinking text.

Odd modules 1–19 have five rewritten MCQs plus five output questions. MCQs and output questions occupy separate slides, grouped four at a time, with the fifth centered. Answers follow the assessment. Even modules have coding assignments, topic essays and repository instructions. M20 preserves 20 applied questions and two essays with instructor guidance; M21 retains ten project ideas and submission requirements.

## Navigation

Arrow keys, Home/End, right-click, mouse side buttons, or touch swipe. Use + / - / 0 for text size. No navigation toolbar. Browser zoom is supported. Smaller screens stack columns and allow scrolling.

## Authoring

Run `node build-decks.mjs` from this folder. This delegates to redesign.mjs. classroom.css is the shared style source, mcq-bank.json the revised questions and keys, assignments.json the preserved assignment content, and output-quiz-cases.json the output exercises. The old rendering code is retained in legacy-build-decks.mjs for reference only; do not use it to regenerate the current decks.

## Review

All 21 decks were opened in headless Edge at 1440×900. Navigation across every slide produced no JavaScript errors or slide-level horizontal overflow. Representative title, concept, full-code and MCQ screenshots were inspected and revised. Evidence is in review/browser-checks.json and review/*.png. This does not certify every screen size, enlarged-text state or classroom projector. Expanded notes and long source intentionally scroll.

Use ../offline-lab/README.md for computer-lab preparation and submission guidance. Node must be installed before offline class. Instructor answers are in the presentation; remove answer slides before distributing a quiz-only student copy.

## Topic essays and syntax colour

Each regular coding module now has a dedicated topic-essay slide and a separate repository/submission slide. Essay prompts emphasize principles, examples and reasoning; students can draft them before dependencies are ready. M20 retains its own defense-essay page.

Complete programs, walkthrough excerpts and output-quiz code now use embedded syntax highlighting. Indentation and whitespace are retained, and copied source excludes styling. Full programs are labeled complete file; walkthroughs remain labeled explanation excerpt. Predict / Run / Explain prompts appear beside the full code.

Edge checks confirmed 30 complete source blocks have exactly the same text as their example files (apart from browser newline normalization), nine regular essay pages are separate from repository instructions, and no script errors occurred. The essay and syntax-coloured code screenshots were visually inspected. Evidence: review/essay-code-checks.json, review/essays.png and review/syntax-code.png. All decks remain below 25 slides.
