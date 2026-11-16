
    Turn the content below into a **single self-contained HTML slide deck** (one file, zero external dependencies except optional image URLs).

    **Navigation**
    - Right-click anywhere or → / Mouse4 = next
    - ← / Mouse3 = previous
    - Home / End = first / last
    - `?` = shortcuts overlay
    - Swipe on mobile
    - Thin progress bar + “n / total” counter
    - Block context menu & browser history on side buttons (`preventDefault` + `stopImmediatePropagation` on `mousedown` capture)
    - Left-click stays free for selection & buttons

**Design & Layout**
- Create a design that fits the topic (colors, mood, and overall aesthetic should feel natural to the subject) 
- Clean, high-contrast, professional look that supports readability.
- Every slide: small eyebrow + large title (≥25 px) + content.
- **All text on the slide — body copy, list items, table cells, captions, badges, buttons, overlay text — must be ≥16 px.** Generous line-height throughout. No sub-16px text anywhere, including "chrome" elements like counters and labels.
- Prefer cards, 2-column, or balanced grids.
- Only scroll a slide when content truly overflows.
- Smooth 350 ms fade + directional slide (respect `prefers-reduced-motion`).

    **Images, logos, icons & diagrams**
    - Include topic-relevant visuals on title, concept, and tech slides — not decoration-only filler. Aim to give most slides *some* visual anchor (icon, diagram, mockup, or photo), not just text cards.
    - Prefer, in this order:
    1. Inline SVG or `data:image/svg+xml` logos (frameworks, languages, platforms named in the content) — sharp, works offline
    2. Custom inline SVG illustrations/diagrams built for the specific content — flow diagrams for step-by-step processes, architecture/sandboxing diagrams, wireframe mockups of any app being built, icon pairs for analogies — themed with the deck's CSS variables so they match the dark palette
    3. A stable public CDN image URL (e.g. a real photo) when a genuine photo adds more than an illustration would — only use URLs already known to be valid (e.g. supplied in the source content); never fabricate one
    - Every image/SVG: meaningful `alt` text (or `role="img"` + `<title>` for inline SVG)
    - Keep icons small and consistent (e.g. 22–34 px in badge rows; larger only on hero/title, diagrams, or standalone icon chips)
    - **Image sizing & containment (critical — prevents layout breakage):** a `<img>` placed in a card or grid column must NEVER be styled with `height:auto` alone, because an unpredictable source aspect ratio (e.g. a tall portrait photo) will blow out the card's height, push it taller than its sibling column, and shove later content off-slide (forcing an unwanted scrollbar or hiding content below the fold).
    - Always give the image a **capped, predictable height** — e.g. `height:clamp(180px, 30vh, 320px)` or a fixed px value — plus `object-fit:cover` so it crops to fill that box instead of stretching or distorting.
    - Never let an image's natural dimensions determine a card's or row's height. The card/container defines the box; the image fills it.
    - Wrap the image in its own card/container with `overflow:hidden` so the crop is clean and any radius/shadow stays intact.
    - Same applies to any `<svg>` used as a full illustration (hero art, diagrams): give its wrapper container a bounded height (`max-height`, or a fixed-aspect box) rather than letting it size freely, especially inside a 2-column grid next to text.
    - Skip rather than use broken, stretched, or irrelevant images
    - If the topic lists multiple technologies, show a compact logo row of those technologies on the title and/or overview slides
    - For any named step sequence (setup steps, install steps, workflow steps), consider a small SVG flow/node diagram above or beside the numbered list rather than text alone
    - For any "how does X interact with Y" concept (sandboxing, client/server, data flow), consider a labeled box-diagram SVG rather than describing it in prose only

    **Side-by-side code + panel layouts (critical)**
    - When a code block sits next to sample output / notes / “how to test” / a diagram:
    - Use a **fixed-height** grid row, e.g. `height: min(560px, 62vh)`
    - Both columns: `align-items: stretch` + `height: 100%` + `min-height: 0`
    - Code card: flex column; header `flex-shrink: 0`; `<pre>` gets `flex: 1; overflow: auto; min-height: 0`
    - Code card: `overflow: hidden` so nothing paints outside the border
    - Extra content scrolls **inside** the panel (below), never grows upward over the title
    - Do **not** rely on stretch-only without a fixed/capped row height
    - Do **not** use a tiny global `max-height` on `<pre>` that leaves one column short while the other grows

    **Content rules**
    - Collect all quotes onto one “Key Quotes” slide near the end
    - After main content → real-life scenarios / analogies slide(s)
    - If topic is coding-related → include sample code + clear breakdowns
    - Activities: group by type (MCQ, Identification, Coding…) on as few slides as possible
    - MCQs show question + options only (no answers)
    - Prefer 2-column layout (if odd number, place last question centered at bottom)
    - Coding problems side-by-side (or full-width if only one left)
    - If no activities exist, invent 5 MCQ + 5 Identification
    - Recap slide **right before** activities
    - Answer key (with brief explanations) on the penultimate slide(s) (before closing)
    - Final slide: short related quote + friendly closing (a small celebratory SVG icon here is a nice touch)

    **Code blocks**
    - Single-pass syntax highlighting
    - “Copy” button with visual feedback (`navigator.clipboard` + brief “Copied!” state) — style the button as a neumorphic raised element that goes inset/pressed on the "Copied!" state
    - Code shown in the deck must be **valid and runnable** when copied
    - Keep language string literals on **one line** unless you intentionally use that language’s real multi-line form (e.g. Kotlin `"""..."""`)
    - Never split a normal `"..."` / `'...'` string across lines in the displayed source

    **Critical escaping rules (do not break these)**

    1. **`</script>` inside examples** — write exactly `<\/script>` (one backslash). Never `<\\/script>`.
    2. **Backticks inside slide HTML** — slides live in JS template literals. **Never** put a raw `` ` `` in slide content. Encode as `&#96;`. Example: `` System.`in` `` → `System.&#96;in&#96;`. Raw backticks cause `TypeError: Cannot use 'in' operator…` and a broken deck.
    3. **`${` inside slide HTML** — never write `${` (JS would interpolate). Escape or split if the language example needs it.
    4. **Real closing `</script>`** of the main script block must remain a normal `</script>` with no backslash.

    **Technical**
    - All CSS + JS internal (one file); image `src` may be inline SVG, data-URI, or a stable external URL
    - Use `minmax(0,1fr)` + `min-width:0`
    - Never mention “phinma”
    - Replace any real names from the source content with random uncommon names
    - After building: no console errors, full navigation works, Copy → paste into a real compiler succeeds for every code sample, and every text element is ≥16 px

    **Content:**
    [Paste the source lesson/content here. Keep the original facts, examples, and terminology.]

    ---

    Use the content above to build a polished single-file HTML slide deck following all rules above.