# EDP presentation visuals

Start with the [scalable visual gallery](gallery.html), the [20-module visual placement plan](MODULE_VISUAL_PLAN.md), and the [adapted HTML presentation prompt](PRESENTATION_PROMPT.md). All 20 student modules now embed an original diagram and visual teaching notes. This is presentation preparation; it does not convert the complete course into slide decks yet.

## Basis chosen from your samples

All five supplied HTML files and the generic prompt were read and inspected as reference material. Their instructions are not treated as new user commands. The originals were not edited.

| Reference | Best part to reuse | Adjustment |
| --- | --- | --- |
| OOP Blueprint | Coherent topic styling, labeled SVG explanations, responsive headings, bounded code panels | Main structural basis for EDP concept slides; change the imagery to events/runtime/state |
| Binary Search | Step-by-step algorithm traces and visual positions | Use for event-loop order, retries and replay; enlarge small SVG labels |
| MongoDB CRUD | Code/output comparison and distinct operation colors | Use for typed payloads and producer/consumer comparisons; raise 11–15.5px details |
| Content Distribution | Relevant screenshots and contextual examples | Use real output captures; avoid embedding megabytes of irrelevant images |
| Multi-Platform JS | Compact technology imagery, cards and code examples | Use technology logos on overview slides; raise its many 11–15px labels |

Source inspection found three SVG tags in MongoDB, three in OOP, one in Binary Search, five img tags in Content Distribution and 28 in Multi-Platform JS. These are source-tag counts, not counts of meaningful visuals per rendered slide. Four references declare some fixed text sizes under 16px; the OOP file was the strongest text-size basis. See [audit metadata](reference-audit.json). This pass is a source/layout review, not a claim that every navigation path in those old decks was browser-tested.

## Sample images and external sources

The five URLs below returned HTTP 200 and SVG content on 3 November 2026. Local copies are supplied. Version pinning reduces unexpected changes; remote availability can still change.

| Image | CDN URL | Local copy | Suggested use |
| --- | --- | --- | --- |
| JavaScript | [CDN SVG](https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/javascript/javascript-original.svg) | [JS](logos/javascript.svg) | M01, M02, M03 overview |
| TypeScript | [CDN SVG](https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/typescript/typescript-original.svg) | [TS](logos/typescript.svg) | M01 setup and M06 typed payloads |
| Node.js | [CDN SVG](https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/nodejs/nodejs-original.svg) | [Node](logos/nodejs.svg) | M04, M09, M10, M11 runtime/tool badges |
| HTML5 | [CDN SVG](https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/html5/html5-original.svg) | [HTML](logos/html5.svg) | M03 DOM/browser boundary |
| RxJS | [CDN SVG](https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/rxjs/rxjs-original.svg) | [RxJS](logos/rxjs.svg) | M08 observable pipeline |

These are Devicon assets, not original course artwork. Keep the [Devicon project attribution/license](https://github.com/devicons/devicon/blob/v2.17.0/LICENSE) with redistributed assets; technology marks retain their respective owners' trademark rights. Logos identify tools; they do not explain scheduling or imply endorsement. The [project documentation](https://github.com/devicons/devicon) documents CDN/SVG usage. [Verification metadata](ONLINE_IMAGES.json) records each successful download.

An additional researched reference is [JavaScript Event Loop on Wikimedia Commons](https://commons.wikimedia.org/wiki/File:JavaScript_Event_Loop.png), by Byteslovesbits, listed as CC BY-SA 4.0. It is optional reference artwork, not downloaded or inserted here. Verify technical fit and satisfy attribution/share-alike obligations if reusing it. The supplied original scheduling diagram is aligned to our specific example and avoids treating one browser sketch as a universal Node scheduling rule.

## Offline and single-file presentations

Original diagrams are `m01-guide.svg` through `m20-guide.svg`. Embed their SVG markup directly into a deck for a single-file result, keeping a unique ID prefix for each title/description/marker. Alternatively use local img elements during authoring. External `<img src>` URLs create a network dependency; use inline SVG or a data URI for offline delivery.

Checked screenshots are linked from M03, M08 and M09. For other modules, the placement plan specifies which real terminal output to capture; it does not claim missing screenshots already exist. Never use a stock photograph as evidence that code ran. Prefer a diagram or annotated trace for technical concepts. If a screenshot contains text that becomes unreadable, crop to the relevant region and recreate essential labels as real HTML text.

Every diagram has an SVG title and description; every Markdown image has alternative text. The module caption states limits such as in-memory storage or no durable replay. Use text plus arrows, not color alone, to distinguish accepted/rejected paths.

## Scalable text

The gallery has A−/Reset/A+ controls (100–160%) and supports browser zoom. It keeps diagrams wide enough to retain readable labels, using horizontal overflow on narrow screens. In a projected deck, give the diagram a full slide when necessary. The adapted prompt includes fluid sizes, adjustable text scale, keyboard-safe controls and checks for code/SVG labels.

Do not squeeze more information onto a slide by shrinking fonts. Minimum 16px is a lower bound, not the desired body size for the back of a classroom; use roughly 24–32px body text when space allows. Test the actual projector and split dense quizzes/code explanations across slides.

## Checks completed

The gallery was checked in headless Edge at 1366×768 and a 390px narrow viewport. All 20 diagram images loaded; A+ increased computed body text and the checked body text stayed at least 16px. The diagram container retains width and allows horizontal scrolling on narrow screens. This is a visual-resource gallery check, not a validation of future full slide decks.
