# EDP HTML presentation prompt — visuals and scalable text

Use this as the conversion prompt with one EDP module attached. It adapts the supplied generic prompt and selected reference patterns. The module remains the content authority; instructor answers are supplied separately when a teacher deck is requested.

---

Create one self-contained HTML presentation from the attached EDP module. Follow its A–D teaching sequence, preserve correct behavior, and keep natural short Taglish explanations. Theme it as an event-flow workshop: dark navy, high-contrast white, teal for accepted flow, amber for waiting and rose for errors; also use text labels/shapes so color is not the only cue.

Use the OOP Blueprint's coherent diagrams and readable structure as the primary design basis. Use Binary Search's step traces for scheduling/replay, MongoDB's code/output pairing, and Multi-Platform JS's compact tool imagery only when relevant. Choose a visual to explain a specific concept rather than adding generic technology pictures to every slide.

## Content and visuals

- Begin with the problem, learning targets and an inviting working example.
- Use the module's visual-guide diagram, caption and real checked output captures where supplied. Consult MODULE_VISUAL_PLAN.md for suggested placement. The placement list is flexible, not a required fixed page count.
- Most concept slides need a useful visual anchor: annotated code, timeline, diagram, table, real output or small interactive state. Do not require a decorative photo on every slide.
- Show a producer/listener/payload diagram, a happy path and a failure/cleanup path when relevant. Clearly label local simulation, real network connection and persistent system boundaries.
- Show JS/TS/Node/HTML/RxJS logos only on relevant title/overview/tool slides. Use the verified visual registry. Never invent URLs. Prefer the saved local SVGs embedded inline for offline delivery.
- Every image needs useful alt text. Inline SVGs need role="img", a unique title/description ID and accessible labels. Prefix IDs when embedding multiple diagrams.
- Use capped image height and object-fit:contain for diagrams/screenshots; cover is suitable only for photos whose cropping preserves meaning. Do not let natural image size set card height.
- Retain a complete runnable checkpoint. Long files may be split across explanation slides, but provide the full copyable program in a clearly labeled panel or appendix. Label fragments as fragments. Do not claim a partial snippet runs alone.
- After the core content, show the analogy, recap and the module's actual assessment. Odd modules: exactly the supplied 10-item quiz. Even modules: the supplied coding task/rubric. Do not invent extra graded activities.
- Student mode contains questions without answers. Include instructor answers only when requested, in a hidden teacher section or separate teacher output. Avoid exposing quiz answers while teaching the question slide.
- Closing text can be original encouragement. Do not invent attributed quotations.

## Fluid and adjustable text

All text must be at least 16 CSS pixels at default supported settings, including captions, badges, counters, buttons, table cells, code tokens and SVG labels. Prefer 24–32px body text for classroom projection. Use rem-based fluid typography and a user-controlled scale; body inheritance alone is insufficient if descendants hard-code px sizes.

Example starting CSS (adapt selectors to actual markup):

```css
:root {
  --text-scale: 1;
  --body-size: clamp(1.25rem, 1vw + 1rem, 2rem);
  --detail-size: clamp(1rem, .45vw + .85rem, 1.35rem);
  --title-size: clamp(1.75rem, 2.5vw + 1rem, 3.75rem);
}
body { font: calc(var(--body-size) * var(--text-scale))/1.55 system-ui; }
h1, h2 { font-size: calc(var(--title-size) * var(--text-scale)); line-height: 1.15; }
button, input, select, textarea { font: inherit; }
small, .caption, .badge, .counter, .code-label {
  font-size: max(16px, calc(var(--detail-size) * var(--text-scale)));
}
pre, code, pre span, svg text {
  font-size: max(16px, calc(var(--detail-size) * var(--text-scale)));
}
.grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem; }
.grid > * { min-width: 0; min-height: 0; }
.visual { overflow: auto; }
.visual svg { display: block; width: 100%; min-width: 960px; height: auto; }
@media (max-width: 800px) { .grid { grid-template-columns: 1fr; } }
@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

An SVG viewBox scales text visually: a computed 16px SVG font can still appear smaller after the SVG is shrunk. Check its actual rendered size. Prefer a full-slide diagram or reflowed HTML labels to forced tiny diagrams. The min-width above fits the supplied 1200-unit diagrams; adapt based on label size and scrolling requirements.

Do not show a fixed on-screen navigation or text-size toolbar. Keep only a discreet slide counter and thin progress bar. Support keyboard navigation, right-click/side-button navigation and touch swipe; use `+`, `−` and `0` keyboard shortcuts to change text size from 100% to 160% and reset. Show the shortcut guide with `?`. Support normal browser zoom and do not disable pinch zoom. Larger text must reflow or scroll inside appropriate panels; never scale the whole slide down with transform:scale to make overflow disappear.

## Navigation, layout and code

Support arrows, Home/End, a help overlay, slide count and progress without a fixed on-screen control bar. Right-click advances; side buttons follow the documented mapping and prevent browser history navigation. Ignore navigation shortcuts when focus is in an input, textarea, select, editable area or open modal. Keep selection and Copy buttons usable. Respect reduced-motion preferences.

Keep code and explanation panels bounded with min-height:0 and overflow:auto. On small screens stack the panels. Allow only necessary scrolling; reserve space for the navigation controls. Keep copied source plain and complete. Use one-pass highlighting, escape HTML safely, and ensure displayed HTML examples cannot close the containing script accidentally. Prefer static HTML/template elements rather than fragile nested JavaScript template literals when embedding complex lesson code.

## Acceptance checks

Test 1366×768 and 1920×1080, plus a narrow viewport. At default and 160% text scale, confirm readable text, accessible navigation, no clipped content, usable code panels, readable diagram labels and no JS console errors. Check actual computed font sizes and visual SVG scaling, not only declarations. Verify Copy output against the runnable module files. Verify all image loads; show a useful textual fallback if a remote image fails. Keep source attribution with redistributed third-party assets.
