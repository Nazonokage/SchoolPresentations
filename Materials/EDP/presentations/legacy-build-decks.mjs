import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const course = path.resolve(here, '..');
const modulesDir = path.join(course, 'modules');
const examplesDir = path.join(course, 'examples');
const visualDir = path.join(course, 'visuals');
import { assessmentSlides, breakdownSlides } from './teaching-sections.mjs';
const answerText = fs.readFileSync(path.join(course, 'instructor', 'ANSWER_KEY.md'), 'utf8');

const escapeHtml = value => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#39;').replaceAll('`', '&#96;').replaceAll('${', '&#36;{');
const plain = value => value
  .replace(/!\[([^\]]*)\]\([^)]*\)/g, '$1')
  .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
  .replace(/<img\b[^>]*alt="([^"]*)"[^>]*>/g, '$1')
  .replace(/`([^`]+)`/g, '$1')
  .replace(/\*\*(.*?)\*\*/g, '$1').replace(/\*(.*?)\*/g, '$1')
  .replace(/^\s*>\s?/gm, '').replace(/\|/g, ' · ')
  .replace(/^\s*[-*]\s+/gm, '• ').replace(/^\s*\d+\.\s+/gm, '• ')
  .trim();
const words = s => (s.match(/\S+/g) || []).length;
const section = (md, heading, nextHeading = null) => {
  const start = md.indexOf(heading);
  if (start < 0) return '';
  const from = start + heading.length;
  const tail = md.slice(from);
  const matches = [...tail.matchAll(/^#{1,4} .+$/gm)];
  const depth = heading.match(/^#+/)?.[0].length;
  const end = (depth ? matches.find(m => m[0].match(/^#+/)[0].length <= depth) : matches[0])?.index ?? tail.length;
  return tail.slice(0, end).trim();
};
const paragraphs = source => source.split(/\n\s*\n/).map(x => x.trim()).filter(x => x && !x.startsWith('|') && !/^```/.test(x) && !/^\[[^\]]+\]\(/.test(x));
function excerpt(source, limit = 95) {
  const out = [];
  for (const p of paragraphs(source)) {
    const cleaned = plain(p.replace(/^#+\s.*$/gm, '').replace(/^\*\*[^*]+\*\*\s*/gm, '').trim());
    if (!cleaned) continue;
    const remaining = limit - out.reduce((n, v) => n + words(v), 0);
    if (remaining <= 0) break;
    const w = cleaned.split(/\s+/);
    out.push(w.length > remaining ? `${w.slice(0, remaining).join(' ')}…` : cleaned);
  }
  return out.join('\n\n');
}
const splitList = source => source.split(/\n/).map(line => line.match(/^\s*(\d+)\.\s+(.+)$/)).filter(Boolean).map(m => ({ n: m[1], text: plain(m[2]) }));
function markdownBlocks(md, level) {
  const re = new RegExp(`^#{${level}}\\s+(.+)$`, 'gm');
  const matches = [...md.matchAll(re)];
  return matches.map((m, i) => ({ title: plain(m[1]), body: md.slice(m.index + m[0].length, matches[i + 1]?.index ?? md.length).trim() }));
}
function codeFiles(md) {
  const out = [];
  const re = /^### File: `([^`]+)`[\s\S]*?```[^\n]*\n([\s\S]*?)\n```/gm;
  for (const match of md.matchAll(re)) out.push({ name: match[1], code: match[2] });
  return out;
}
function getAnswer(moduleNo) {
  const chunks = answerText.split(/^## Module /m).slice(1);
  const chunk = chunks.find(value => value.startsWith(String(moduleNo).padStart(2, '0')));
  return chunk ? chunk.slice(chunk.indexOf('\n') + 1).trim() : '';
}
function quizAnswers(answer) {
  return answer.split(/\n/).map(line => line.match(/^\s*(\d+)\.\s+(.+)$/)).filter(Boolean).map(m => ({ n: m[1], text: plain(m[2].replace(/\*\*/g, '')) }));
}
function svgData(number) {
  const file = path.join(visualDir, `m${String(number).padStart(2, '0')}-guide.svg`);
  if (fs.existsSync(file)) return `data:image/svg+xml;base64,${Buffer.from(fs.readFileSync(file)).toString('base64')}`;
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 560" role="img"><title>Event-driven mini-capstone flow</title><rect width="1200" height="560" rx="40" fill="#10243b"/><g font-family="system-ui" font-size="34" fill="#f4f8fc" text-anchor="middle"><rect x="90" y="200" width="230" height="140" rx="24" fill="#155e75"/><text x="205" y="255">Student action</text><text x="205" y="300">producer</text><path d="M335 270h110" stroke="#f4b860" stroke-width="10"/><path d="m445 270-28-20v40z" fill="#f4b860"/><rect x="475" y="200" width="250" height="140" rx="24" fill="#334155"/><text x="600" y="255">Validated</text><text x="600" y="300">event payload</text><path d="M740 270h100" stroke="#f4b860" stroke-width="10"/><path d="m840 270-28-20v40z" fill="#f4b860"/><rect x="870" y="150" width="250" height="100" rx="20" fill="#166534"/><text x="995" y="212">UI reaction</text><rect x="870" y="290" width="250" height="100" rx="20" fill="#7f1d1d"/><text x="995" y="352">Test + cleanup</text><text x="600" y="480" fill="#cbd5e1">Design → demonstrate → explain the limit</text></g></svg>`;
  return `data:image/svg+xml;base64,${Buffer.from(svg).toString('base64')}`;
}
function highlight(code) {
  const escaped = escapeHtml(code);
  return escaped.replace(/(\/\/[^\n]*|\b(?:const|let|var|function|return|if|else|for|of|in|await|async|new|throw|try|catch|finally|class|extends|import|from|export|default|interface|type|true|false|null|undefined)\b|\b\d+(?:\.\d+)?\b|&quot;[^\n]*?&quot;|&#39;[^\n]*?&#39;)/g, token => {
    let kind = 'kw';
    if (/^\/\//.test(token)) kind = 'comment';
    else if (/^(?:\d)/.test(token)) kind = 'num';
    else if (/^(?:&quot;|&#39;)/.test(token)) kind = 'str';
    return `<span class="tok-${kind}">${token}</span>`;
  });
}
const json = value => JSON.stringify(value).replaceAll('</script', '<\\/script');

function buildDeck(moduleNo) {
  const file = `EDP_M${String(moduleNo).padStart(2, '0')}.md`;
  const md = fs.readFileSync(path.join(modulesDir, file), 'utf8');
  const title = plain(md.match(/^#\s+(.+)$/m)?.[1] || `EDP Module ${moduleNo}`);
  const nutshell = plain(md.match(/\*\*In a nutshell:\*\*\s*([^\n]+)/)?.[1] || 'Explore the module idea, run the example and explain the result.');
  const targetsRaw = section(md, '**Learning targets**');
  const targets = splitList(targetsRaw).map(x => x.text).slice(0, 4);
  const period = plain(md.match(/\*\*Period:\*\*\s*([^·\n]+)/)?.[1] || (moduleNo >= 20 ? 'Finals' : 'Course module'));
  const main = section(md, '## B. Main Lesson');
  const concepts = markdownBlocks(main, 3).filter(item => !/^\[[^\]]+\]\(/.test(item.title));
  const everyday = plain(section(md, '### Everyday connection'));
  const expected = plain(section(md, '### Expected behavior and explanation checkpoint'));
  const independent = plain(section(md, '### Your independent change'));
  const code = codeFiles(md);
  const assessmentBody = section(md, '## D. Assessment, Wrap-Up & References');
  const quiz = splitList(section(md, '### 10-item quiz'));
  const codingTask = section(md, '### One coding activity');
  const wrap = plain(section(md, '### Wrap-up'));
  const answers = quizAnswers(getAnswer(moduleNo));
  const allAnswers = moduleNo === 20 ? getAnswer(moduleNo) : '';
  const ideas = moduleNo === 21 ? [...md.matchAll(/^\|\s*(\d+)\.\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|$/gm)].map(m => [plain(m[1] + '. ' + m[2]), plain(m[3]), plain(m[4])]) : [];
  const slides = [];
  const push = (eyebrow, heading, inner, klass = '') => slides.push({ eyebrow, heading, inner, klass });

  push(`EDP · ${period} · MODULE ${String(moduleNo).padStart(2, '0')}`, title, `<div class="hero-grid"><div><p class="lead">${escapeHtml(nutshell)}</p><p>We will connect one real-world event to code you can run, inspect and change.</p><div class="pills"><span>Predict</span><span>Run</span><span>Explain</span><span>Modify</span></div></div><figure class="visual"><img src="${svgData(moduleNo)}" alt="Event-flow diagram for ${escapeHtml(title)}"><figcaption>Visual guide · follow the flow before reading the code</figcaption></figure></div><div class="target-row">${targets.map(t => `<div class="target">${escapeHtml(t)}</div>`).join('')}</div>`, 'title-slide');
  push('01 · START HERE', 'In a nutshell', `<div class="big-idea">${escapeHtml(nutshell)}</div><div class="callout"><strong>By the end</strong><ul>${targets.map(t => `<li>${escapeHtml(t)}</li>`).join('')}</ul></div><p class="taglish">Prediction muna. Then run it, explain what changed, and make one independent edit.</p>`);
  const visualData = svgData(moduleNo);
  push('02 · TRACE THE FLOW', moduleNo === 21 ? 'From idea to evidence' : 'A visual map of the topic', `<div class="visual-large"><img src="${visualData}" alt="Diagram showing the main flow for ${escapeHtml(title)}"><p class="caption">Use the arrows to narrate what happens first, what can fail, and how the program finishes or cleans up.</p></div>`);

  for (const [i, concept] of concepts.entries()) {
    const parts = paragraphs(concept.body).map(p => plain(p)).filter(Boolean);
    for (const [j, text] of parts.entries()) {
      push(`CORE IDEA ${i + 1} · ${j + 1}/${parts.length}`, concept.title,
        `<div class="concept-layout"><article class="concept-copy"><p>${escapeHtml(text)}</p></article><aside class="concept-note"><span class="badge">TRACE IT</span><p>Find where this principle appears in the program.</p><div class="flow-steps"><div>Input / event</div><div>Handler / decision</div><div>Observable result</div></div><p class="taglish">Ano ang mangyayari kung magbago ang input?</p></aside></div>`);
    }
  }
  const setup = section(md, '### Run the complete example');
  if (setup) push('LAB SETUP', 'How to run this lesson', `<div class="output">${escapeHtml(setup.replace(/```[^\n]*\n/g,'').replace(/```/g,''))}</div>`);

  if (code.length) {
    for (const [i, sample] of code.entries()) {
      const referenced = path.join(examplesDir, sample.name);
      let verifiedSource = sample.code;
      if (fs.existsSync(referenced)) verifiedSource = fs.readFileSync(referenced, 'utf8').replace(/\n$/, '');
      const codeId = `sample-${moduleNo}-${i}`;
      const lines = verifiedSource.split('\n').length;
      push(`CODE LAB · ${sample.name}`, `Copy, run, and explain`, `<div class="code-layout"><section class="code-card"><header><span>${escapeHtml(sample.name)} · complete source</span><button class="copy" data-copy="${codeId}" aria-label="Copy complete ${escapeHtml(sample.name)} program">Copy code</button></header><pre><code id="${codeId}" data-plain="${escapeHtml(verifiedSource)}">${highlight(verifiedSource)}</code></pre></section><aside class="run-card"><h3>Run it</h3><p>Use the exact command from the module's example setup. Keep required neighboring files in the same folder.</p><div class="stat">${lines} source lines</div><p>Copy captures the full program even when the code panel scrolls.</p><p class="taglish">Huwag hulaan ang output—predict, run, then explain.</p></aside></div>`, 'code-slide');
    }
  }

  if (expected) push('CODE LAB · EXPECTED RESULT', 'What should you observe?', `<div class="output">${escapeHtml(expected)}</div><div class="question-grid"><div><strong>Trace</strong><p>Which input or event began this path?</p></div><div><strong>State</strong><p>What changed, and what stayed the same?</p></div><div><strong>Failure</strong><p>What happens on rejected or invalid work?</p></div></div>`);
  if (everyday) push('CONNECT IT TO LIFE', 'An everyday analogy', `<div class="analogy"><div class="analogy-icon" aria-hidden="true">↗</div><blockquote>${escapeHtml(everyday)}</blockquote></div><p class="taglish">Gamitin ang analogy para ipaliwanag ang producer, listeners, payload, at response.</p>`);
  if (independent) push('YOUR TURN · GUIDED PRACTICE', 'Make one change of your own', `<div class="activity-card"><span class="badge">UN-GRADED PRACTICE</span><p>${escapeHtml(independent)}</p><ol><li>Predict the output before editing.</li><li>Make only the requested change.</li><li>Run it and compare the result.</li><li>Explain why the behavior changed.</li></ol></div>`);

  if (moduleNo === 21 && ideas.length) {
    push('SOLO MINI-CAPSTONE · OPTION 1/3', 'Project ideas 1–4', projectCards(ideas.slice(0, 4)));
    push('SOLO MINI-CAPSTONE · OPTION 2/3', 'Project ideas 5–8', projectCards(ideas.slice(4, 8)));
    push('SOLO MINI-CAPSTONE · OPTION 3/3', 'Project ideas 9–10', projectCards(ideas.slice(8, 10)));
  }

  const troubleshooting = plain(section(md, '### Troubleshooting and common mistake'));
  if (troubleshooting) push('DEBUGGING GUIDE', 'When the result is unexpected', `<div class="concept-copy"><p>${escapeHtml(troubleshooting)}</p></div>`);
  const simple = plain(section(md, '### Sa madaling salita'));
  if (simple) push('EXPLAIN IT IN YOUR WORDS', 'Sa madaling salita', `<div class="analogy"><blockquote>${escapeHtml(simple)}</blockquote></div>`);
  const refs = [...section(md, '### References and further reading').matchAll(/\[([^\]]+)\]\((https?:[^)]+)\)/g)];
  if(refs.length) push('FURTHER READING', 'Documentation for this lesson', `<ul>${refs.map(r=>`<li><a href="${escapeHtml(r[2])}" target="_blank" rel="noopener">${escapeHtml(r[2])}</a></li>`).join('')}</ul>`);
  push('RECAP · BEFORE THE ASSESSMENT', 'The idea to take with you', `<div class="recap-grid"><div><span>01</span><p>${escapeHtml(targets[0] || nutshell)}</p></div><div><span>02</span><p>${escapeHtml(targets[1] || 'Trace event input, payload, handler and result.')}</p></div><div><span>03</span><p>${escapeHtml(targets[2] || 'Test a failure and state the boundary honestly.')}</p></div></div><p class="taglish">Sa madaling salita: explain the flow in your own words, then show proof.</p>${wrap ? `<div class="small-note">${escapeHtml(wrap)}</div>` : ''}`);
  if (moduleNo === 20) {
    const q20 = splitList(section(md, '## C. Applied quiz · 20 items'));
    for (let i = 0; i < q20.length; i += 4) push(`APPLIED QUIZ · ITEMS ${q20[i].n}–${q20[Math.min(i + 3, q20.length - 1)].n}`, 'Defend the design choice', `<ol class="question-list">${q20.slice(i, i + 4).map(q => `<li><span>${q.n}.</span>${escapeHtml(q.text)}</li>`).join('')}</ol><p class="hint">Answer each in one or two sentences. Point to evidence you could show a panel.</p>`);
    const essayBlock = section(md, '## D. Defense essays · two responses');
    const essays = splitList(essayBlock);
    push('DEFENSE PREP · TWO ESSAYS', 'Explain your design and your evidence', `<ol class="question-list">${essays.map(q => `<li><span>${q.n}.</span>${escapeHtml(q.text)}</li>`).join('')}</ol><div class="callout"><strong>Suggested scoring</strong><p>Quiz: 20 points. Each essay: 5 points for principles, application, reasoning, and observable verification.</p></div>`);
  } else if (quiz.length) {
    for (let i = 0; i < quiz.length; i += 4) push(`CHECK YOUR UNDERSTANDING · ${i + 1}–${Math.min(i + 4, quiz.length)}`, 'Quick check', `<ol class="question-list">${quiz.slice(i, i + 4).map(q => `<li><span>${q.n}.</span>${escapeHtml(q.text)}</li>`).join('')}</ol><p class="hint">Answer first; explain your reasoning to a partner.</p>`);
  } else if (codingTask) {
    const rubric = codingTask.split('\n').filter(line => line.trim().startsWith('|')).map(line => line.trim()).filter((line, i) => i > 0 && !/^\|\s*[-: ]+\|/.test(line));
    const textPart = codingTask.split(/\n\s*\|/)[0];
    push('ASSESSMENT · ONE CODING ACTIVITY', 'Build, test, and explain', `<div class="activity-card"><p>${escapeHtml(excerpt(textPart, 90))}</p><div class="submit-box"><strong>Show your work</strong><p>Complete program · exact run command · one success case · one failure/edge case · explain your independent change.</p></div>${rubric.length ? `<div class="rubric">${rubric.map(row => `<p>${escapeHtml(plain(row.replace(/^\|\s*/, '').replace(/\s*\|\s*/g, ' · ').replace(/\|$/, '')))}</p>`).join('')}</div>` : ''}</div>`);
  } else {
    push('ASSESSMENT · MINI-CAPSTONE READINESS', 'Prepare a project you can defend', `<div class="activity-card"><p>Choose one project idea, identify its event flow, and prepare a small working demonstration with a testable success and failure case.</p><p>Use the supplied starter as a reference. Explain what you changed, what you tested, and what remains a limitation.</p></div>`);
  }



  if (moduleNo === 20) {
    const answerList = allAnswers.split('\n').map(line => line.match(/^\s*(\d+)\.\s+(.+)$/)).filter(Boolean).map(m => ({ n: m[1], text: plain(m[2].replace(/\*\*/g, '')) })).slice(0, 20);
    for (let i = 0; i < answerList.length; i += 4) push(`INSTRUCTOR ANSWER KEY · ${i + 1}–${Math.min(i + 4, answerList.length)}`, 'Applied quiz — suggested answers', `<ol class="answer-list">${answerList.slice(i, i + 4).map(a => `<li><span>${a.n}.</span>${escapeHtml(a.text)}</li>`).join('')}</ol>`);
    push('INSTRUCTOR GUIDE · ESSAY RUBRIC', 'Look for sound reasoning', `<div class="answer-list"><p>Each essay: 2 points for accurate principles, 1 for a concrete application, 1 for justified reasoning about a failure or alternative, and 1 for observable verification.</p><p>Essay 1 should name an event and payload, two reactions, a state rule, accepted/rejected paths, and cleanup evidence.</p><p>Essay 2 should distinguish duplicate handler registration from redelivery of one event ID, then propose a trace and repeatable regression test.</p></div>`);
  } else if (answers.length) {
    for (let i = 0; i < answers.length; i += 4) push(`INSTRUCTOR ANSWER KEY · ${i + 1}–${Math.min(i + 4, answers.length)}`, 'Suggested answers', `<ol class="answer-list">${answers.slice(i, i + 4).map(a => `<li><span>${a.n}.</span>${escapeHtml(a.text)}</li>`).join('')}</ol><p class="hint">Accept equivalent technically correct reasoning. Use this slide after students have attempted the questions.</p>`);
  } else {
    const teach = getAnswer(moduleNo);
    const expectedMatch = teach.match(/Expected starting trace:[\s\S]*?(?=\n\nRequired student change:|$)/);
    const changeMatch = teach.match(/Required student change:[\s\S]*?(?=\n\nAward using|$)/);
    push('INSTRUCTOR NOTES', 'Teaching check', `<div class="answer-list"><p>${escapeHtml(plain(expectedMatch?.[0] || 'Use the module answer key and verify student work from its behavior, not screenshots alone.'))}</p><p>${escapeHtml(plain(changeMatch?.[0] || 'Check that the independent change and explanation are present.'))}</p></div>`);
  }

  push('SALAMAT · KEEP BUILDING', 'Understand it. Change it. Defend it.', `<div class="closing"><div class="celebrate" aria-hidden="true">✓</div><p class="lead">${escapeHtml(moduleNo === 21 ? 'Start small. Make the event flow clear. Build something you can explain.' : 'Hindi lang code ang mahalaga—kaya mo bang ipaliwanag at baguhin ito?')}</p><p>Take one idea, test it, and keep asking: what happened, who reacted, and how do we know?</p></div>`);

  if (moduleNo <= 19) {
    const start = slides.findIndex(s => /APPLIED QUIZ|CHECK YOUR UNDERSTANDING|ASSESSMENT ·/.test(s.eyebrow));
    const end = slides.findIndex(s => s.eyebrow.startsWith('SALAMAT'));
    if(start >= 0) slides.splice(start,end-start,...assessmentSlides(moduleNo, quiz, answers, codingTask, code, getAnswer(moduleNo)));
  }
  const codeEnd = slides.findIndex(s=>s.eyebrow.includes('EXPECTED RESULT'));
  if(codeEnd >= 0) slides.splice(codeEnd,0,...breakdownSlides(moduleNo,code));
  compactSlides(slides);
  const safeSlides = slides.map(s => `<section class="slide ${s.klass || ''}" aria-label="${escapeHtml(s.eyebrow)}: ${escapeHtml(s.heading)}"><div class="slide-scroll"><div class="eyebrow">${escapeHtml(s.eyebrow)}</div><h2>${escapeHtml(s.heading)}</h2><div class="content">${s.inner}</div></div></section>`).join('\n');
  let html = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#0a1424"><title>${escapeHtml(title)} · EDP Presentation</title><style>
:root{color-scheme:dark;--bg:#081321;--panel:#102238;--panel2:#142b43;--ink:#f5f8fc;--muted:#cbd5e1;--teal:#2dd4bf;--amber:#f4b860;--rose:#fb7185;--text-scale:1;--body-size:clamp(1.25rem,1vw + 1rem,2rem);--detail-size:clamp(1rem,.45vw + .85rem,1.35rem);--title-size:clamp(1.8rem,2.5vw + 1rem,3.8rem);font-family:Inter,ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;font-size:16px}*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;background:var(--bg);color:var(--ink)}body{font-size:calc(var(--body-size)*var(--text-scale));line-height:1.48}.deck{height:100dvh;width:100vw;position:relative;background:radial-gradient(ellipse at 85% 0%,#143553 0,transparent 42%),linear-gradient(135deg,#081321,#0d1c2f 65%,#101a29)}.slide{position:absolute;inset:0;display:none;padding:clamp(1.1rem,3vw,3.4rem) clamp(1.2rem,5vw,5rem) 6.2rem;opacity:0;transform:translateX(24px);transition:opacity 350ms ease,transform 350ms ease}.slide.active{display:block;opacity:1;transform:translateX(0)}.slide.leaving{display:block;opacity:0;transform:translateX(var(--exit-x, -24px));pointer-events:none}.slide-scroll{height:100%;overflow:auto;overscroll-behavior:contain;scrollbar-color:#45627c transparent;padding:0 .3rem .7rem}.eyebrow{color:var(--teal);font-size:max(16px,calc(var(--detail-size)*var(--text-scale)));font-weight:800;letter-spacing:.1em;text-transform:uppercase;margin:0 0 .65rem}h2{font-size:calc(var(--title-size)*var(--text-scale));line-height:1.12;margin:0 0 1.2rem;max-width:30ch;letter-spacing:-.025em}h3{font-size:calc(1.35rem*var(--text-scale));margin:.2rem 0 .7rem}p,li,td,th,blockquote,figcaption{font-size:calc(1.12rem*var(--text-scale));line-height:1.48}p{margin:.55rem 0 1rem}.content{max-width:1500px;margin:0 auto}.lead{font-size:calc(clamp(1.45rem,1.5vw + 1rem,2.4rem)*var(--text-scale));line-height:1.35;font-weight:650}.title-slide h2{font-size:calc(clamp(2.4rem,4.2vw + 1rem,5rem)*var(--text-scale));max-width:24ch}.hero-grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(320px,.95fr);gap:clamp(1rem,3vw,3rem);align-items:center}.visual{margin:0;min-width:0;overflow:hidden;border:1px solid #35516b;border-radius:1.2rem;background:#10243b;padding:.7rem}.visual img,.visual-large img{display:block;width:100%;height:clamp(210px,34vh,380px);object-fit:contain}.visual figcaption,.caption{font-size:max(16px,calc(var(--detail-size)*var(--text-scale)));color:var(--muted);margin:.35rem .3rem}.target-row{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.8rem;margin-top:1.3rem}.target,.callout,.concept-note,.run-card,.activity-card,.submit-box{border:1px solid #35516b;background:linear-gradient(135deg,#142d46,#102238);border-radius:1rem;padding:1rem 1.2rem}.target{font-size:calc(1rem*var(--text-scale));color:#e6edf5}.big-idea{font-size:calc(clamp(1.8rem,3vw + 1rem,3.2rem)*var(--text-scale));font-weight:750;line-height:1.2;max-width:34ch;margin:1rem 0 2rem;color:#fff}.callout{max-width:900px}.callout ul{margin:.5rem 0;padding-left:1.5rem}.taglish{color:#b9d8e1;border-left:4px solid var(--amber);padding:.25rem 0 .25rem 1rem}.visual-large{max-width:1200px;margin:0 auto;background:#10243b;border:1px solid #35516b;border-radius:1rem;padding:1.2rem}.visual-large img{height:min(55vh,520px)}.concept-layout{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(260px,.7fr);gap:1.2rem;align-items:start}.concept-copy{font-size:calc(1.15rem*var(--text-scale));max-width:75ch}.concept-copy p{font-size:inherit}.concept-note{border-top:4px solid var(--amber)}.badge,.pills span{display:inline-flex;align-items:center;border:1px solid #41617c;border-radius:999px;padding:.3rem .8rem;color:var(--teal);font-size:max(16px,calc(var(--detail-size)*var(--text-scale)));font-weight:750}.code-layout{display:grid;grid-template-columns:minmax(0,1.45fr) minmax(250px,.65fr);gap:1rem;height:min(62vh,650px);min-height:340px}.code-card{display:flex;flex-direction:column;min-width:0;min-height:0;overflow:hidden;border:1px solid #3e5870;border-radius:1rem;background:#07101a}.code-card header{flex-shrink:0;display:flex;justify-content:space-between;align-items:center;gap:.7rem;padding:.7rem 1rem;background:#172c40;font-size:max(16px,calc(var(--detail-size)*var(--text-scale)));font-weight:700}.code-card pre{flex:1;min-height:0;overflow:auto;margin:0;padding:1rem;color:#e6edf5;tab-size:2;white-space:pre;font:calc(1rem*var(--text-scale))/1.5 ui-monospace,SFMono-Regular,Consolas,monospace}.code-card code,.code-card code span{font:inherit}.tok-kw{color:#7dd3fc}.tok-str{color:#86efac}.tok-num{color:#fcd34d}.tok-comment{color:#94a3b8}.copy,.nav button,.scale button{font:inherit;font-size:max(16px,calc(var(--detail-size)*var(--text-scale)));color:var(--ink);background:#1d3b56;border:1px solid #52718c;border-radius:.65rem;padding:.45rem .8rem;cursor:pointer}.copy:active{transform:translateY(1px);background:#0f766e}.run-card{overflow:auto}.stat{padding:.65rem 1rem;border-radius:.7rem;background:#193b4b;color:var(--teal);font-weight:800}.output{border-left:5px solid var(--teal);background:#0d2633;padding:1.3rem 1.6rem;border-radius:.8rem;white-space:pre-wrap;font:calc(1.12rem*var(--text-scale))/1.6 ui-monospace,Consolas,monospace}.question-grid,.recap-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem;margin-top:1.3rem}.question-grid>div,.recap-grid>div{padding:1rem;border-radius:.9rem;background:#142a40;border:1px solid #2b4964;min-width:0}.analogy{display:flex;gap:1.4rem;align-items:center;max-width:1100px;margin:8vh auto 2rem}.analogy-icon,.celebrate{display:grid;place-items:center;flex:0 0 5rem;height:5rem;border-radius:50%;background:#0f766e;color:white;font-size:2.5rem;font-weight:900}.analogy blockquote{margin:0;padding:1.5rem;border-left:5px solid var(--amber);background:#10243b;border-radius:.8rem;font-size:calc(1.5rem*var(--text-scale))}.activity-card{max-width:1120px;border-top:4px solid var(--amber)}.activity-card ol{padding-left:1.5rem}.submit-box{margin-top:1rem;background:#0b1c2a}.rubric{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.45rem 1rem;margin-top:1rem}.rubric p{margin:0;padding:.55rem;border-radius:.5rem;background:#0d1b2a;font-size:calc(1rem*var(--text-scale))}.question-list,.answer-list{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.8rem 1.4rem;list-style:none;margin:0;padding:0}.question-list li,.answer-list li{display:flex;gap:.75rem;align-items:flex-start;background:#11263c;border:1px solid #29465f;border-radius:.8rem;padding:.8rem 1rem;min-width:0}.question-list li span,.answer-list li span{color:var(--amber);font-weight:900;flex:0 0 auto}.hint,.small-note{color:var(--muted);font-size:calc(1rem*var(--text-scale));margin-top:1rem}.recap-grid span{font-size:calc(1.5rem*var(--text-scale));color:var(--teal);font-weight:900}.recap-grid p{margin:.5rem 0}.pills{display:flex;flex-wrap:wrap;gap:.5rem}.closing{max-width:1050px;margin:10vh auto;text-align:center}.celebrate{margin:0 auto 1.4rem;background:#166534}.closing .lead{margin:0 auto 1rem;max-width:28ch}.idea-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.8rem}.idea{padding:.9rem 1rem;border:1px solid #35516b;background:#102238;border-radius:.8rem;min-width:0}.idea h3{font-size:calc(1.15rem*var(--text-scale));color:var(--teal)}.idea p{font-size:calc(1rem*var(--text-scale));margin:.3rem 0}.idea .demo{border-top:1px solid #35516b;padding-top:.35rem;color:#f8d79d}.nav{position:absolute;bottom:0;left:0;right:0;display:flex;align-items:center;gap:.8rem;padding:.7rem clamp(1rem,4vw,3rem);background:rgba(4,12,21,.94);border-top:1px solid #2a4259;z-index:10}.nav button{min-width:48px}.nav .grow{flex:1}.counter{font-size:max(16px,calc(var(--detail-size)*var(--text-scale)));min-width:100px;text-align:center;color:#e1e8ef}.progress{position:absolute;top:0;left:0;height:5px;background:var(--teal);width:0;transition:width 200ms ease;z-index:12}.scale{display:flex;gap:.35rem;align-items:center}.scale output{font-size:16px;min-width:52px;text-align:center;color:#cbd5e1}.modal{position:absolute;inset:0;z-index:20;display:none;place-items:center;background:#020812d9;padding:2rem}.modal.open{display:grid}.modal-card{max-width:700px;padding:2rem;border:1px solid #51708a;border-radius:1rem;background:#102238}.modal-card p{margin:.4rem 0}.modal button{margin-top:1rem}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}.answer-list{grid-template-columns:repeat(2,minmax(0,1fr))}.answer-list p{margin:.2rem}.btn-ok{color:#7aefcc!important}.btn-copied{box-shadow:inset 0 2px 6px #02070d;background:#0f766e!important}@media(max-width:900px){.hero-grid,.concept-layout,.code-layout{grid-template-columns:1fr}.hero-grid{align-items:start}.visual img{height:clamp(180px,26vh,280px)}.code-layout{height:auto;min-height:0}.code-card{height:54vh}.run-card{max-height:22vh}.question-grid,.recap-grid{grid-template-columns:1fr}.target-row{grid-template-columns:1fr}.slide{padding-left:1rem;padding-right:1rem}.title-slide h2{font-size:calc(clamp(2rem,6vw,3.6rem)*var(--text-scale))}}@media(max-width:600px){.question-list,.idea-grid,.rubric{grid-template-columns:1fr}.nav{gap:.3rem;padding:.55rem}.nav button{padding:.35rem .55rem;min-width:42px}.counter{min-width:72px}.scale{gap:.2rem}.scale output{min-width:44px}.nav .grow{min-width:0}.slide{padding-bottom:6rem}.visual-large img{height:auto;max-height:45vh}.analogy{margin:2rem auto;align-items:flex-start}.analogy-icon{flex-basis:3.5rem;height:3.5rem;font-size:1.7rem}}@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
</style></head><body><main class="deck" aria-label="${escapeHtml(title)} slide deck"><div class="progress" id="progress"></div>${safeSlides}<nav class="nav" aria-label="Slide navigation"><button id="prev" aria-label="Previous slide">←</button><button id="next" aria-label="Next slide">→</button><span id="counter" class="counter" aria-live="polite"></span><span class="grow"></span><div class="scale" aria-label="Text size controls"><button id="smaller" aria-label="Decrease text size">A−</button><output id="scaleValue" aria-live="polite">100%</output><button id="larger" aria-label="Increase text size">A+</button><button id="resetScale" aria-label="Reset text size">Reset</button></div><button id="help" aria-label="Show keyboard shortcuts">?</button></nav><div id="helpModal" class="modal" role="dialog" aria-modal="true" aria-labelledby="helpTitle"><div class="modal-card"><h2 id="helpTitle">Presentation shortcuts</h2><p><b>→ / Right-click / Mouse4</b> — next slide</p><p><b>← / Mouse3</b> — previous slide</p><p><b>Home / End</b> — first or last slide</p><p><b>?</b> — show or close this guide · <b>Esc</b> — close</p><p>Swipe left or right on a touch screen. Use A− / A+ to adjust text size.</p><button id="closeHelp">Close</button></div></div></main><div class="sr-only" id="announce" aria-live="polite"></div><script>
(()=>{'use strict';const slides=[...document.querySelectorAll('.slide')];let index=0,scale=1,touchX=null;const counter=document.getElementById('counter'),progress=document.getElementById('progress'),announce=document.getElementById('announce'),modal=document.getElementById('helpModal');function show(next){next=Math.max(0,Math.min(slides.length-1,next));if(next===index&&slides[index].classList.contains('active'))return;const old=slides[index],direction=next>index?1:-1;old.classList.remove('active');old.classList.add('leaving');old.style.setProperty('--exit-x',direction>0?'-24px':'24px');window.setTimeout(()=>old.classList.remove('leaving'),360);index=next;slides[index].classList.add('active');slides[index].style.transform=direction>0?'translateX(24px)':'translateX(-24px)';requestAnimationFrame(()=>requestAnimationFrame(()=>slides[index].style.transform='translateX(0)'));counter.textContent=(index+1)+' / '+slides.length;progress.style.width=((index+1)/slides.length*100)+'%';announce.textContent='Slide '+(index+1)+' of '+slides.length+': '+slides[index].querySelector('h2').textContent;slides[index].querySelector('.slide-scroll').scrollTop=0}function focused(){const e=document.activeElement;return e&&(['INPUT','TEXTAREA','SELECT','BUTTON'].includes(e.tagName)||e.isContentEditable)}document.getElementById('prev').addEventListener('click',()=>show(index-1));document.getElementById('next').addEventListener('click',()=>show(index+1));function toggleHelp(open=!modal.classList.contains('open')){modal.classList.toggle('open',open);if(open)document.getElementById('closeHelp').focus();else document.getElementById('closeHelp').blur()}document.getElementById('help').addEventListener('click',()=>toggleHelp());document.getElementById('closeHelp').addEventListener('click',()=>toggleHelp(false));document.addEventListener('keydown',e=>{if(e.key==='Escape'&&modal.classList.contains('open')){toggleHelp(false);return}if(focused()||modal.classList.contains('open'))return;if(e.key==='ArrowRight'){e.preventDefault();show(index+1)}else if(e.key==='ArrowLeft'){e.preventDefault();show(index-1)}else if(e.key==='Home'){e.preventDefault();show(0)}else if(e.key==='End'){e.preventDefault();show(slides.length-1)}else if(e.key==='?'){e.preventDefault();toggleHelp()}});document.addEventListener('contextmenu',e=>{e.preventDefault();e.stopImmediatePropagation();show(index+1)},true);document.addEventListener('mousedown',e=>{if(e.button===3||e.button===4){e.preventDefault();e.stopImmediatePropagation();show(index+(e.button===4?1:-1))}},true);document.addEventListener('mouseup',e=>{if(e.button===3||e.button===4){e.preventDefault();e.stopImmediatePropagation()}},true);document.addEventListener('auxclick',e=>{if(e.button===3||e.button===4){e.preventDefault();e.stopImmediatePropagation()}},true);document.addEventListener('click',async e=>{const b=e.target.closest('[data-copy]');if(!b)return;const code=document.getElementById(b.dataset.copy);const raw=code?.getAttribute('data-plain')||code?.textContent||'';try{await navigator.clipboard.writeText(raw);b.textContent='Copied!';b.classList.add('btn-copied');window.setTimeout(()=>{b.textContent='Copy code';b.classList.remove('btn-copied')},1200)}catch{const area=document.createElement('textarea');area.value=raw;document.body.append(area);area.select();document.execCommand('copy');area.remove();b.textContent='Copied!';window.setTimeout(()=>b.textContent='Copy code',1200)}});function setScale(value){scale=Math.max(1,Math.min(1.6,Math.round(value*10)/10));document.documentElement.style.setProperty('--text-scale',scale);document.getElementById('scaleValue').value=Math.round(scale*100)+'%'}document.getElementById('smaller').addEventListener('click',()=>setScale(scale-.1));document.getElementById('larger').addEventListener('click',()=>setScale(scale+.1));document.getElementById('resetScale').addEventListener('click',()=>setScale(1));document.addEventListener('touchstart',e=>{touchX=e.changedTouches[0].clientX},{passive:true});document.addEventListener('touchend',e=>{if(touchX===null)return;const dx=e.changedTouches[0].clientX-touchX;if(Math.abs(dx)>70)show(index+(dx<0?1:-1));touchX=null},{passive:true});counter.textContent='1 / '+slides.length;progress.style.width=(100/slides.length)+'%';slides[0].classList.add('active');document.querySelectorAll('.copy').forEach(b=>b.dataset.label=b.textContent)})();
</script></body></html>`;
  html = html.replace('<div class="progress" id="progress"></div>', '<div class="progress" id="progress"></div><div id="counter" class="counter" aria-live="polite">1 / ' + slides.length + '</div>');
  html = html.replace(/<nav class="nav"[\s\S]*?<\/nav>/, '');
  html = html.replace('</style>', '.counter{position:absolute;top:.8rem;right:clamp(1rem,4vw,3rem);z-index:11;min-width:0;padding:.35rem .7rem;border:1px solid #35516b;border-radius:999px;background:#081321e8;color:#e1e8ef;text-align:center}\n.slide{padding-bottom:clamp(1rem,4vh,3rem)}\n</style>');
  html = html.replace("document.getElementById('prev').addEventListener('click',()=>show(index-1));document.getElementById('next').addEventListener('click',()=>show(index+1));", '');
  html = html.replace("document.getElementById('help').addEventListener('click',()=>toggleHelp());", '');
  html = html.replace("document.getElementById('smaller').addEventListener('click',()=>setScale(scale-.1));document.getElementById('larger').addEventListener('click',()=>setScale(scale+.1));document.getElementById('resetScale').addEventListener('click',()=>setScale(1));", '');
  html = html.replace("else if(e.key==='?'){e.preventDefault();toggleHelp()}", "else if(e.key==='?'){e.preventDefault();toggleHelp()}else if(e.key==='+'||e.key==='='){e.preventDefault();setScale(scale+.1)}else if(e.key==='-'){e.preventDefault();setScale(scale-.1)}else if(e.key==='0'){e.preventDefault();setScale(1)}");
  html = html.replace("document.getElementById('scaleValue').value=Math.round(scale*100)+'%'", "announce.textContent='Text size '+Math.round(scale*100)+'%'");
  html = html.replace('Use A− / A+ to adjust text size.', 'Use + / − / 0 to adjust text size.');
  html = html.replace('</style>', `
.quiz-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem;align-items:stretch}.quiz-cell{min-width:0;padding:1rem;border:1px solid #45627c;border-radius:.8rem;background:#0d1c2f}.quiz-cell h3{font-size:calc(1.25rem*var(--text-scale));line-height:1.35;color:#f8d79d}.quiz-cell p,.quiz-cell li{font-size:calc(1.05rem*var(--text-scale));line-height:1.4}.quiz-cell ol{margin:.5rem 0;padding-left:1.5rem}.quiz-cell pre{font-size:calc(1rem*var(--text-scale));line-height:1.45;padding:.7rem;tab-size:2;text-align:left;white-space:pre;overflow:auto}.quiz-cell .hint{display:none}.quiz-cell .code-card{max-height:none!important}.quiz-cell .output{font-size:calc(1rem*var(--text-scale));padding:.6rem}.code-card pre{text-align:left;tab-size:2;white-space:pre;font-size:calc(1.1rem*var(--text-scale));line-height:1.5}.paired-content{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1.5rem}.paired-content>article{min-width:0}.paired-content .concept-layout{display:block}.paired-content .concept-note{display:none}.paired-content p{font-size:calc(1.25rem*var(--text-scale))}.paired-content h3{color:#f8d79d}.paired-content .code-layout{display:block;height:auto}.paired-content .run-card{max-height:none}.paired-content .code-card{height:45vh}@media(max-width:760px){.quiz-grid,.paired-content{grid-template-columns:1fr}}
/* Reference-inspired classroom layout: blueprint grid, generous type, bounded panels. */
.deck{background:repeating-linear-gradient(0deg,#5ec8f208 0px,#5ec8f208 1px,transparent 1px,transparent 42px),repeating-linear-gradient(90deg,#5ec8f208 0px,#5ec8f208 1px,transparent 1px,transparent 42px),#0b131e}
.slide{padding-top:3.5rem}.slide-scroll{max-width:1480px;margin:auto}h2{max-width:38ch;font-size:calc(clamp(2rem,3.2vw,3.4rem)*var(--text-scale));padding-bottom:.7rem;border-bottom:2px solid #e8935a55}
p,li,td,th,blockquote,.concept-copy,.concept-copy p{font-size:calc(clamp(1.35rem,1.65vw,1.85rem)*var(--text-scale));line-height:1.6}
.concept-layout{grid-template-columns:minmax(0,1.4fr) minmax(280px,.7fr);gap:3rem}.concept-note{border-top-color:#e8935a}.concept-note p{font-size:calc(1.2rem*var(--text-scale))}
.flow-steps{display:grid;gap:.6rem}.flow-steps div{border-left:4px solid #5ec8f2;padding:.6rem 1rem;background:#081321;font-size:calc(1.1rem*var(--text-scale))}
a{color:#81d4fa;overflow-wrap:anywhere}.output{font-size:calc(1.25rem*var(--text-scale))}.question-list{gap:1rem}.question-list li{font-size:calc(1.25rem*var(--text-scale))}.visual-large{overflow:auto}.visual-large img{min-width:900px;height:auto;max-height:none}.title-slide h2{font-size:calc(clamp(2rem,3.4vw,3.8rem)*var(--text-scale))}.counter{top:auto;bottom:.6rem}.slide{padding-bottom:3.5rem}
@media(max-width:900px){.concept-layout{grid-template-columns:1fr}.question-list{grid-template-columns:1fr}}
@media print{html,body{height:auto;overflow:visible}.deck{height:auto}.slide,.slide.active{display:block;position:relative;opacity:1;transform:none;break-after:page;height:auto}.slide-scroll{overflow:visible}.counter,.progress,.modal,.copy{display:none}}
</style>`);
  return { html, title, count: slides.length };
}

function projectCards(ideas) {
  return `<div class="idea-grid">${ideas.map(([title, principle, demo]) => `<article class="idea"><h3>${escapeHtml(title)}</h3><p><b>Principle:</b> ${escapeHtml(principle)}</p><p class="demo"><b>Defense demo:</b> ${escapeHtml(demo)}</p></article>`).join('')}</div>`;
}

function compactSlides(slides) {
  // Consolidate quiz items without removing any questions or answers.
  for (const prefix of ['QUIZ ·', 'INSTRUCTOR ANSWER ·']) {
    const items = slides.filter(s=>s.eyebrow.startsWith(prefix));
    if(!items.length) continue;
    const first = slides.indexOf(items[0]);
    for(const item of items) slides.splice(slides.indexOf(item),1);
    const groups=[];
    for(let i=0;i<items.length;i+=4) groups.push({eyebrow:prefix+' ITEMS '+(i+1)+'–'+Math.min(i+4,items.length),heading:prefix.startsWith('QUIZ')?'Knowledge check':'Output and explanation',inner:'<div class="quiz-grid">'+items.slice(i,i+4).map((q,j)=>'<article class="quiz-cell"><h3>'+escapeHtml(q.eyebrow+' · '+q.heading)+'</h3>'+q.inner+'</article>').join('')+'</div>'});
    slides.splice(first,0,...groups);
  }
  // Show two code sections per breakdown page; full source remains in the code lab.
  for(let i=0;i<slides.length-1;i++){
    if(slides[i].eyebrow.startsWith('CODE BREAKDOWN') && slides[i+1].eyebrow.startsWith('CODE BREAKDOWN')){
      const pair=slides.splice(i,2);slides.splice(i,0,{eyebrow:'CODE WALKTHROUGH',heading:'Read the code in order',inner:'<div class="paired-content">'+pair.map(s=>'<article><h3>'+escapeHtml(s.eyebrow)+'</h3>'+s.inner+'</article>').join('')+'</div>'});
    }
  }
  while(slides.length>25){
    const i=slides.findIndex((s,k)=>s.eyebrow.startsWith('CORE IDEA')&&slides[k+1]?.eyebrow.startsWith('CORE IDEA'));
    if(i<0) break;
    const pair=slides.splice(i,2);slides.splice(i,0,{eyebrow:'CONCEPT CONNECTION',heading:pair[0].heading,inner:'<div class="paired-content">'+pair.map(s=>'<article><h3>'+escapeHtml(s.heading)+'</h3>'+s.inner+'</article>').join('')+'</div>'});
  }
  if(slides.length>25){
    const intro=slides.findIndex(s=>s.eyebrow==='01 · START HERE');
    if(intro>=0) slides.splice(intro,1); // The title already contains the same targets and nutshell.
  }
  if(slides.length>25){
    const ref=slides.findIndex(s=>s.eyebrow==='FURTHER READING');
    if(ref>=0){const item=slides.splice(ref,1)[0];slides[slides.length-1].inner+='<details><summary>Lesson references</summary>'+item.inner+'</details>';}
  }
  if(slides.length>25) throw new Error('Deck exceeds 25 slides: '+slides.length);
}

const records = [];
for (let n = 1; n <= 21; n++) {
  const out = buildDeck(n);
  const name = `EDP_M${String(n).padStart(2, '0')}.html`;
  fs.writeFileSync(path.join(here, name), out.html, 'utf8');
  records.push({ module: n, file: name, title: out.title, slides: out.count, bytes: Buffer.byteLength(out.html) });
}
fs.writeFileSync(path.join(here, 'deck-manifest.json'), `${JSON.stringify(records, null, 2)}\n`, 'utf8');
console.log(`Generated ${records.length} self-contained decks (${records.reduce((a, b) => a + b.slides, 0)} slides).`);
