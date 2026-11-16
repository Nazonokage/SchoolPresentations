/**
 * Integrative Programming & Technologies 1 — Course Introduction
 * Clean academic lecture style adapted from education templates.
 *
 * Palette: warm cream bg, deep navy accent, dark ink, muted labels
 * Layout: LAYOUT_WIDE (13.333" × 7.5")
 */

const pptxgen = require("pptxgenjs");

// ---------- design tokens ----------
const COLORS = {
  bg:        "F1ECDF",  // warm cream
  ink:       "1A1A1A",  // body / titles
  navy:      "1F3DA8",  // primary accent
  navyLight: "8FA4D9",  // soft navy
  muted:     "6B6B6B",  // small labels
  mutedSoft: "9A9A9A",
  divider:   "D9D2C2",
  sage:      "5B7A5B",  // supporting green
  white:     "FFFFFF",
  card:      "F8F5ED",
  voteA:     "1F3DA8",  // Express
  voteB:     "2E7D32",  // Flask
};

const FONT_BODY  = "Helvetica Neue";
const FONT_TITLE = "Helvetica Neue";

const W = 13.333;
const H = 7.5;

const pres = new pptxgen();
pres.layout  = "LAYOUT_WIDE";
pres.title   = "Integrative Programming & Technologies 1 — Course Introduction";
pres.author  = "IT Instructor";
pres.company = "Integrative Programming & Technologies 1";

// shared chrome
function addChrome(slide, { topLabel, page, section }) {
  slide.addText(topLabel, {
    x: 0.7, y: 0.45, w: 7, h: 0.3,
    fontFace: FONT_BODY, fontSize: 11, color: COLORS.muted,
    charSpacing: 3, margin: 0,
  });
  slide.addText(page, {
    x: 0.7, y: 7.05, w: 2.5, h: 0.25,
    fontFace: FONT_BODY, fontSize: 11, color: COLORS.muted,
    charSpacing: 2, margin: 0,
  });
  slide.addText(section, {
    x: W - 5.2, y: 7.05, w: 4.5, h: 0.25,
    fontFace: FONT_BODY, fontSize: 11, color: COLORS.muted,
    charSpacing: 3, align: "right", margin: 0,
  });
}

// ============================================================================
// SLIDE 1 — Title
// ============================================================================
{
  const s = pres.addSlide();
  s.background = { color: COLORS.bg };

  s.addText("INTEGRATIVE PROGRAMMING & TECHNOLOGIES 1", {
    x: 0.7, y: 0.5, w: 10, h: 0.35,
    fontFace: FONT_BODY, fontSize: 13, color: COLORS.ink,
    charSpacing: 3, margin: 0,
  });

  s.addText("Course Introduction  ·  First Meeting", {
    x: W - 5.5, y: 0.5, w: 4.8, h: 0.35,
    fontFace: FONT_BODY, fontSize: 13, color: COLORS.muted,
    align: "right", margin: 0,
  });

  s.addText(
    [
      { text: "Welcome to", options: { breakLine: true } },
      { text: "Integrative", options: { color: COLORS.navy, italic: true, breakLine: true } },
      { text: "Programming.", options: { breakLine: false } },
    ],
    {
      x: 0.7, y: 1.8, w: 12, h: 3.2,
      fontFace: FONT_TITLE, fontSize: 64, color: COLORS.ink,
      margin: 0, lineSpacingMultiple: 1.05,
    }
  );

  s.addText("Learning how systems talk to each other — and how we make them work as one.", {
    x: 0.7, y: 5.3, w: 10, h: 0.4,
    fontFace: FONT_BODY, fontSize: 18, color: COLORS.muted, margin: 0,
  });

  s.addShape(pres.shapes.OVAL, {
    x: W - 1.9, y: H - 1.9, w: 1.0, h: 1.0,
    fill: { color: COLORS.navy }, line: { type: "none" },
  });
}

// ============================================================================
// SLIDE 2 — What is this subject?
// ============================================================================
{
  const s = pres.addSlide();
  s.background = { color: COLORS.bg };
  addChrome(s, { topLabel: "01  ·  DEFINITION", page: "02 / 11", section: "WHAT IS THIS?" });

  s.addText(
    [
      { text: "What is ", options: { color: COLORS.ink } },
      { text: "Integrative Programming", options: { color: COLORS.navy, italic: true } },
      { text: "?", options: { color: COLORS.ink } },
    ],
    {
      x: 0.7, y: 1.1, w: 12, h: 0.7,
      fontFace: FONT_TITLE, fontSize: 32, margin: 0,
    }
  );

  // two cards
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 0.7, y: 2.1, w: 5.7, h: 3.8,
    fill: { color: COLORS.card }, rectRadius: 0.1,
    shadow: { type: "outer", color: "000000", blur: 8, offset: 2, opacity: 0.06 },
  });
  s.addText("OFFICIAL VIEW", {
    x: 1.0, y: 2.35, w: 5, h: 0.3,
    fontFace: FONT_BODY, fontSize: 12, color: COLORS.navy, charSpacing: 2, margin: 0,
  });
  s.addText("This course examines the various types of programming languages and their appropriate use. It addresses scripting languages, architectures, application programming interfaces (APIs), and programming practices that facilitate the management, integration, and security of the systems that support an organization.", {
    x: 1.0, y: 2.85, w: 5.1, h: 2.7,
    fontFace: FONT_BODY, fontSize: 15, color: COLORS.ink, margin: 0,
  });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 6.8, y: 2.1, w: 5.7, h: 3.8,
    fill: { color: COLORS.card }, rectRadius: 0.1,
    shadow: { type: "outer", color: "000000", blur: 8, offset: 2, opacity: 0.06 },
  });
  s.addText("INSTRUCTOR'S VIEW", {
    x: 7.1, y: 2.35, w: 5, h: 0.3,
    fontFace: FONT_BODY, fontSize: 12, color: COLORS.navy, charSpacing: 2, margin: 0,
  });
  s.addText("Think of it as the practical skill of adding features and making different systems work together — just like in Systems Integration & Architecture (SIA).\n\nYou will learn how to connect applications, exchange data, secure those connections, and build real integrated projects.", {
    x: 7.1, y: 2.85, w: 5.1, h: 2.7,
    fontFace: FONT_BODY, fontSize: 15, color: COLORS.ink, margin: 0,
  });
}

// ============================================================================
// SLIDE 3 — Why it matters (modern education)
// ============================================================================
{
  const s = pres.addSlide();
  s.background = { color: COLORS.bg };
  addChrome(s, { topLabel: "02  ·  RELEVANCE", page: "03 / 11", section: "WHY IT MATTERS" });

  s.addText(
    [
      { text: "Why this course ", options: { color: COLORS.ink } },
      { text: "matters", options: { color: COLORS.navy, italic: true } },
      { text: " today", options: { color: COLORS.ink } },
    ],
    {
      x: 0.7, y: 1.1, w: 12, h: 0.6,
      fontFace: FONT_TITLE, fontSize: 30, margin: 0,
    }
  );

  const points = [
    { num: "01", title: "Real systems are never alone", desc: "Modern applications talk to APIs, databases, payment gateways, AI services, and other apps every day." },
    { num: "02", title: "Integration is a core IT skill", desc: "Employers look for developers who can connect existing systems safely and cleanly — not just build isolated features." },
    { num: "03", title: "Project-based & outcome-focused", desc: "You will practice the same thinking used in industry: design, implement, test, and secure integrated solutions." },
    { num: "04", title: "Foundation for advanced topics", desc: "Prepares you for microservices, cloud integration, DevOps pipelines, and enterprise architecture work." },
  ];

  points.forEach((p, i) => {
    const y = 1.95 + i * 1.15;
    s.addText(p.num, {
      x: 0.7, y: y, w: 0.8, h: 0.4,
      fontFace: FONT_BODY, fontSize: 18, color: COLORS.navy, bold: true, margin: 0,
    });
    s.addText(p.title, {
      x: 1.7, y: y, w: 10.5, h: 0.35,
      fontFace: FONT_BODY, fontSize: 18, color: COLORS.ink, bold: true, margin: 0,
    });
    s.addText(p.desc, {
      x: 1.7, y: y + 0.35, w: 10.5, h: 0.5,
      fontFace: FONT_BODY, fontSize: 15, color: COLORS.muted, margin: 0,
    });
  });
}

// ============================================================================
// SLIDE 4 — What we will actually learn
// ============================================================================
{
  const s = pres.addSlide();
  s.background = { color: COLORS.bg };
  addChrome(s, { topLabel: "03  ·  SCOPE", page: "04 / 11", section: "WHAT WE LEARN" });

  s.addText("What we will actually learn", {
    x: 0.7, y: 1.05, w: 12, h: 0.5,
    fontFace: FONT_TITLE, fontSize: 28, color: COLORS.ink, margin: 0,
  });

  const topics = [
    { title: "Integration Concepts", items: "Architectures, challenges, patterns" },
    { title: "Data Exchange", items: "XML, JSON, schemas, mapping" },
    { title: "APIs & Web Services", items: "REST, middleware, SOA thinking" },
    { title: "Scripting & Coding", items: "Integrative coding, design patterns" },
    { title: "Security Practices", items: "Auth, tokens, secure communication" },
    { title: "Hands-on Projects", items: "Connect apps, databases, services" },
  ];

  topics.forEach((t, i) => {
    const col = i % 3;
    const row = Math.floor(i / 3);
    const x = 0.7 + col * 4.15;
    const y = 1.85 + row * 2.2;

    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: x, y: y, w: 3.9, h: 1.9,
      fill: { color: COLORS.card }, rectRadius: 0.1,
      shadow: { type: "outer", color: "000000", blur: 6, offset: 1.5, opacity: 0.05 },
    });
    s.addText(t.title, {
      x: x + 0.25, y: y + 0.35, w: 3.4, h: 0.45,
      fontFace: FONT_BODY, fontSize: 16, color: COLORS.navy, bold: true, margin: 0,
    });
    s.addText(t.items, {
      x: x + 0.25, y: y + 0.9, w: 3.4, h: 0.6,
      fontFace: FONT_BODY, fontSize: 14, color: COLORS.ink, margin: 0,
    });
  });
}

// ============================================================================
// SLIDE 5 — Link to SIA
// ============================================================================
{
  const s = pres.addSlide();
  s.background = { color: COLORS.bg };
  addChrome(s, { topLabel: "04  ·  CONNECTION", page: "05 / 11", section: "SIA RELATIONSHIP" });

  s.addText(
    [
      { text: "How this relates to ", options: { color: COLORS.ink } },
      { text: "Systems Integration\n& Architecture", options: { color: COLORS.navy, italic: true } },
    ],
    {
      x: 0.7, y: 1.1, w: 12, h: 1.3,
      fontFace: FONT_TITLE, fontSize: 28, margin: 0,
    }
  );

  const links = [
    { label: "SIA focuses on", text: "the big picture — architectures, SOA, middleware, testing, usability, and how systems fit together at the organizational level." },
    { label: "This course focuses on", text: "the practical programming side — writing the code, scripts, APIs, and data exchanges that make those architectures actually work." },
    { label: "Together they form", text: "a complete skill set: you understand why systems need to integrate (SIA) and you know how to build the connections (IPT)." },
  ];

  links.forEach((l, i) => {
    const y = 2.7 + i * 1.25;
    s.addText(l.label, {
      x: 0.7, y: y, w: 12, h: 0.3,
      fontFace: FONT_BODY, fontSize: 14, color: COLORS.navy, bold: true, margin: 0,
    });
    s.addText(l.text, {
      x: 0.7, y: y + 0.35, w: 12, h: 0.7,
      fontFace: FONT_BODY, fontSize: 16, color: COLORS.ink, margin: 0,
    });
  });
}

// ============================================================================
// SLIDE 6 — Learning outcomes
// ============================================================================
{
  const s = pres.addSlide();
  s.background = { color: COLORS.bg };
  addChrome(s, { topLabel: "05  ·  OUTCOMES", page: "06 / 11", section: "BY THE END" });

  s.addText("By the end of this course you will be able to", {
    x: 0.7, y: 1.1, w: 12, h: 0.5,
    fontFace: FONT_TITLE, fontSize: 26, color: COLORS.ink, margin: 0,
  });

  const outcomes = [
    "Explain integration concepts, architectures, and common challenges",
    "Use scripting and design patterns for integrative coding",
    "Work with modern data formats (JSON, XML) and mapping techniques",
    "Design and consume REST APIs and basic web services",
    "Apply basic security practices to integrated systems",
    "Build and test a simple end-to-end integrated application",
  ];

  outcomes.forEach((o, i) => {
    const y = 1.85 + i * 0.7;
    s.addShape(pres.shapes.OVAL, {
      x: 0.75, y: y + 0.08, w: 0.28, h: 0.28,
      fill: { color: COLORS.navy }, line: { type: "none" },
    });
    s.addText(o, {
      x: 1.3, y: y, w: 11.2, h: 0.5,
      fontFace: FONT_BODY, fontSize: 18, color: COLORS.ink, margin: 0,
    });
  });
}

// ============================================================================
// SLIDE 7 — Language vote intro
// ============================================================================
{
  const s = pres.addSlide();
  s.background = { color: COLORS.bg };
  addChrome(s, { topLabel: "06  ·  DECISION", page: "07 / 11", section: "LANGUAGE CHOICE" });

  s.addText(
    [
      { text: "Your first decision: ", options: { color: COLORS.ink } },
      { text: "which language?", options: { color: COLORS.navy, italic: true } },
    ],
    {
      x: 0.7, y: 1.15, w: 12, h: 0.6,
      fontFace: FONT_TITLE, fontSize: 28, margin: 0,
    }
  );

  s.addText("We will build real integrated features together. You get to vote for the primary backend framework we will use for the semester.", {
    x: 0.7, y: 1.9, w: 12, h: 0.6,
    fontFace: FONT_BODY, fontSize: 17, color: COLORS.muted, margin: 0,
  });

  // two big cards
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 0.7, y: 2.7, w: 5.7, h: 3.5,
    fill: { color: COLORS.card }, rectRadius: 0.12,
    shadow: { type: "outer", color: "000000", blur: 8, offset: 2, opacity: 0.06 },
  });
  s.addText("OPTION A", {
    x: 1.0, y: 2.95, w: 5, h: 0.3,
    fontFace: FONT_BODY, fontSize: 13, color: COLORS.voteA, charSpacing: 2, margin: 0,
  });
  s.addText("Express\n(Node.js)", {
    x: 1.0, y: 3.4, w: 5.1, h: 1.1,
    fontFace: FONT_TITLE, fontSize: 32, color: COLORS.ink, margin: 0,
  });
  s.addText("JavaScript / TypeScript ecosystem\nFast for APIs & real-time features\nHuge community & job market", {
    x: 1.0, y: 4.7, w: 5.1, h: 1.2,
    fontFace: FONT_BODY, fontSize: 15, color: COLORS.muted, margin: 0,
  });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 6.9, y: 2.7, w: 5.7, h: 3.5,
    fill: { color: COLORS.card }, rectRadius: 0.12,
    shadow: { type: "outer", color: "000000", blur: 8, offset: 2, opacity: 0.06 },
  });
  s.addText("OPTION B", {
    x: 7.2, y: 2.95, w: 5, h: 0.3,
    fontFace: FONT_BODY, fontSize: 13, color: COLORS.voteB, charSpacing: 2, margin: 0,
  });
  s.addText("Flask\n(Python)", {
    x: 7.2, y: 3.4, w: 5.1, h: 1.1,
    fontFace: FONT_TITLE, fontSize: 32, color: COLORS.ink, margin: 0,
  });
  s.addText("Clean & beginner-friendly\nExcellent for data & AI integration\nStrong academic & industry presence", {
    x: 7.2, y: 4.7, w: 5.1, h: 1.2,
    fontFace: FONT_BODY, fontSize: 15, color: COLORS.muted, margin: 0,
  });
}

// ============================================================================
// SLIDE 8 — Quick comparison
// ============================================================================
{
  const s = pres.addSlide();
  s.background = { color: COLORS.bg };
  addChrome(s, { topLabel: "07  ·  COMPARISON", page: "08 / 11", section: "EXPRESS vs FLASK" });

  s.addText("Quick side-by-side", {
    x: 0.7, y: 1.1, w: 12, h: 0.5,
    fontFace: FONT_TITLE, fontSize: 26, color: COLORS.ink, margin: 0,
  });

  // header row
  s.addText("Aspect", { x: 0.7, y: 1.85, w: 3.2, h: 0.4, fontFace: FONT_BODY, fontSize: 14, color: COLORS.muted, bold: true, margin: 0 });
  s.addText("Express (Node.js)", { x: 4.0, y: 1.85, w: 4.2, h: 0.4, fontFace: FONT_BODY, fontSize: 14, color: COLORS.voteA, bold: true, margin: 0 });
  s.addText("Flask (Python)", { x: 8.4, y: 1.85, w: 4.2, h: 0.4, fontFace: FONT_BODY, fontSize: 14, color: COLORS.voteB, bold: true, margin: 0 });

  // divider
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.7, y: 2.35, w: 12, h: 0.015,
    fill: { color: COLORS.divider }, line: { type: "none" },
  });

  const rows = [
    ["Language", "JavaScript / TypeScript", "Python"],
    ["Learning curve", "Familiar if you know JS", "Very gentle for beginners"],
    ["Best for", "APIs, real-time, full-stack JS", "Data-heavy, AI, clean backends"],
    ["Ecosystem", "npm — huge & fast-moving", "PyPI — mature & scientific"],
    ["Industry demand", "Very high (web & startups)", "High (data, enterprise, AI)"],
    ["Our focus", "Building integrated services", "Building integrated services"],
  ];

  rows.forEach((r, i) => {
    const y = 2.55 + i * 0.6;
    s.addText(r[0], { x: 0.7, y: y, w: 3.2, h: 0.45, fontFace: FONT_BODY, fontSize: 15, color: COLORS.ink, bold: true, margin: 0 });
    s.addText(r[1], { x: 4.0, y: y, w: 4.2, h: 0.45, fontFace: FONT_BODY, fontSize: 15, color: COLORS.ink, margin: 0 });
    s.addText(r[2], { x: 8.4, y: y, w: 4.2, h: 0.45, fontFace: FONT_BODY, fontSize: 15, color: COLORS.ink, margin: 0 });
  });
}

// ============================================================================
// SLIDE 9 — How we will run the class
// ============================================================================
{
  const s = pres.addSlide();
  s.background = { color: COLORS.bg };
  addChrome(s, { topLabel: "08  ·  APPROACH", page: "09 / 11", section: "HOW WE LEARN" });

  s.addText("How this class will run", {
    x: 0.7, y: 1.1, w: 12, h: 0.5,
    fontFace: FONT_TITLE, fontSize: 28, color: COLORS.ink, margin: 0,
  });

  const methods = [
    { title: "Short lectures", desc: "Clear concepts first — then we code." },
    { title: "Live coding & labs", desc: "Most sessions include hands-on practice." },
    { title: "Project-based", desc: "You will add real features to an integrated system over the term." },
    { title: "Peer learning", desc: "You vote, discuss, and help each other debug." },
    { title: "Modern tools", desc: "Git, Postman, modern editors, and real frameworks." },
    { title: "Outcome focus", desc: "Every module moves you closer to a working integrated project." },
  ];

  methods.forEach((m, i) => {
    const col = i % 3;
    const row = Math.floor(i / 3);
    const x = 0.7 + col * 4.15;
    const y = 1.9 + row * 2.2;

    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: x, y: y, w: 3.9, h: 1.9,
      fill: { color: COLORS.card }, rectRadius: 0.1,
    });
    s.addText((i + 1).toString().padStart(2, "0"), {
      x: x + 0.25, y: y + 0.3, w: 3.4, h: 0.35,
      fontFace: FONT_BODY, fontSize: 14, color: COLORS.navy, margin: 0,
    });
    s.addText(m.title, {
      x: x + 0.25, y: y + 0.7, w: 3.4, h: 0.4,
      fontFace: FONT_BODY, fontSize: 17, color: COLORS.ink, bold: true, margin: 0,
    });
    s.addText(m.desc, {
      x: x + 0.25, y: y + 1.2, w: 3.4, h: 0.5,
      fontFace: FONT_BODY, fontSize: 14, color: COLORS.muted, margin: 0,
    });
  });
}

// ============================================================================
// SLIDE 10 — Expectations
// ============================================================================
{
  const s = pres.addSlide();
  s.background = { color: COLORS.bg };
  addChrome(s, { topLabel: "09  ·  EXPECTATIONS", page: "10 / 11", section: "CLASSROOM CULTURE" });

  s.addText("What I expect from you", {
    x: 0.7, y: 1.15, w: 12, h: 0.5,
    fontFace: FONT_TITLE, fontSize: 28, color: COLORS.ink, margin: 0,
  });

  const expects = [
    { title: "Show up ready to build", text: "Bring a laptop when possible. Code is the best way to learn this subject." },
    { title: "Ask questions early", text: "Integration problems are normal. The sooner we surface them, the better." },
    { title: "Collaborate honestly", text: "Help classmates, share ideas, but submit your own work." },
    { title: "Think like an integrator", text: "Always ask: “How does this piece connect to the rest of the system?”" },
  ];

  expects.forEach((e, i) => {
    const y = 1.9 + i * 1.15;
    s.addText((i + 1).toString(), {
      x: 0.7, y: y, w: 0.6, h: 0.45,
      fontFace: FONT_BODY, fontSize: 22, color: COLORS.navy, bold: true, margin: 0,
    });
    s.addText(e.title, {
      x: 1.5, y: y, w: 11, h: 0.4,
      fontFace: FONT_BODY, fontSize: 18, color: COLORS.ink, bold: true, margin: 0,
    });
    s.addText(e.text, {
      x: 1.5, y: y + 0.4, w: 11, h: 0.5,
      fontFace: FONT_BODY, fontSize: 16, color: COLORS.muted, margin: 0,
    });
  });
}

// ============================================================================
// SLIDE 11 — Closing / Vote call
// ============================================================================
{
  const s = pres.addSlide();
  s.background = { color: COLORS.bg };

  s.addText("INTEGRATIVE PROGRAMMING & TECHNOLOGIES 1", {
    x: 0.7, y: 0.5, w: 12, h: 0.35,
    fontFace: FONT_BODY, fontSize: 13, color: COLORS.muted, charSpacing: 2, margin: 0,
  });

  s.addText(
    [
      { text: "Ready to ", options: { color: COLORS.ink } },
      { text: "vote", options: { color: COLORS.navy, italic: true } },
      { text: "?", options: { color: COLORS.ink } },
    ],
    {
      x: 0.7, y: 1.8, w: 12, h: 1.0,
      fontFace: FONT_TITLE, fontSize: 48, margin: 0,
    }
  );

  s.addText("Express or Flask — you decide the direction of our hands-on work this semester.", {
    x: 0.7, y: 3.0, w: 11, h: 0.5,
    fontFace: FONT_BODY, fontSize: 18, color: COLORS.muted, margin: 0,
  });

  // two vote buttons visual
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 0.7, y: 4.0, w: 5.5, h: 1.4,
    fill: { color: COLORS.voteA }, rectRadius: 0.1,
  });
  s.addText("VOTE  A\nExpress (Node.js)", {
    x: 0.7, y: 4.25, w: 5.5, h: 1.0,
    fontFace: FONT_BODY, fontSize: 20, color: COLORS.white, align: "center", bold: true, margin: 0,
  });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 7.1, y: 4.0, w: 5.5, h: 1.4,
    fill: { color: COLORS.voteB }, rectRadius: 0.1,
  });
  s.addText("VOTE  B\nFlask (Python)", {
    x: 7.1, y: 4.25, w: 5.5, h: 1.0,
    fontFace: FONT_BODY, fontSize: 20, color: COLORS.white, align: "center", bold: true, margin: 0,
  });

  s.addText("Questions? Let’s talk after the vote.", {
    x: 0.7, y: 5.8, w: 12, h: 0.4,
    fontFace: FONT_BODY, fontSize: 16, color: COLORS.ink, margin: 0,
  });

  s.addText("11 / 11", {
    x: 0.7, y: 7.05, w: 2, h: 0.25,
    fontFace: FONT_BODY, fontSize: 11, color: COLORS.muted, margin: 0,
  });
}

pres.writeFile({ fileName: "/home/workdir/artifacts/IPT1_Course_Introduction.pptx" })
  .then(() => console.log("Created: IPT1_Course_Introduction.pptx"))
  .catch(err => console.error(err));