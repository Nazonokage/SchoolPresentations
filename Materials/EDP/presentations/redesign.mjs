import {highlight} from './highlight.mjs';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const dir=path.dirname(fileURLToPath(import.meta.url)),root=path.dirname(dir);
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const plain=s=>s.replace(/\[([^\]]+)\]\([^)]*\)/g,'$1').replace(/\*\*|`/g,'').trim();
const sec=(md,h)=>{const i=md.indexOf(h);if(i<0)return '';const rest=md.slice(i+h.length);const d=h.match(/^#+/)[0].length;const m=[...rest.matchAll(/^#+ .+$/gm)].find(x=>x[0].match(/^#+/)[0].length<=d);return rest.slice(0,m?.index??rest.length).trim();};
const assignments=JSON.parse(fs.readFileSync(path.join(dir,'assignments.json')));
const bank=JSON.parse(fs.readFileSync(path.join(dir,'mcq-bank.json'))),cases=JSON.parse(fs.readFileSync(path.join(dir,'output-quiz-cases.json')));
const css=fs.readFileSync(path.join(dir,'classroom.css'),'utf8');
const script=`(()=>{const slides=[...document.querySelectorAll('.slide')];let at=0,size=1;function show(i){at=Math.max(0,Math.min(slides.length-1,i));slides.forEach((s,j)=>{s.hidden=j!==at});document.querySelector('#count').textContent=(at+1)+' / '+slides.length;document.querySelector('#progress').style.width=((at+1)/slides.length*100)+'%';}document.addEventListener('keydown',e=>{if(e.ctrlKey||e.metaKey||e.target.matches('input,textarea,select'))return;const moves={ArrowRight:at+1,ArrowLeft:at-1,Home:0,End:slides.length-1};if(e.key in moves){e.preventDefault();show(moves[e.key])}if(['+','=','-','0'].includes(e.key)){size=e.key==='0'?1:Math.max(1,Math.min(1.6,size+(e.key==='-'?-.1:.1)));document.documentElement.style.setProperty('--scale',size)}if(e.key==='Escape')document.querySelectorAll('details[open]').forEach(d=>d.open=false)});document.addEventListener('contextmenu',e=>{e.preventDefault();show(at+1)});document.addEventListener('mousedown',e=>{if(e.button===3||e.button===4){e.preventDefault();e.stopImmediatePropagation();show(at+(e.button===4?1:-1))}},true);document.addEventListener('auxclick',e=>{if(e.button>2)e.preventDefault()},true);document.addEventListener('click',async e=>{const b=e.target.closest('[data-copy]');if(!b)return;const text=document.getElementById(b.dataset.copy).textContent;try{await navigator.clipboard.writeText(text);b.textContent='Copied'}catch{b.textContent='Select code and press Ctrl+C'}});let x;document.addEventListener('touchstart',e=>{x=e.touches.length===1?e.touches[0].clientX:null},{passive:true});document.addEventListener('touchend',e=>{if(x!==null&&Math.abs(e.changedTouches[0].clientX-x)>90)show(at+(e.changedTouches[0].clientX<x?1:-1));x=null},{passive:true});show(Number(location.hash.slice(1))||0)})();`;
const para=s=>s.split(/\n\s*\n/).filter(x=>x.trim()&&!x.startsWith('['));
const prose=s=>para(s).map(x=>`<p>${esc(plain(x))}</p>`).join('');
const routes={1:['Event occurs','Handler runs','State changes'],2:['Synchronous work','Promise reaction','Timer callback'],3:['User clicks','Listener runs','DOM updates'],4:['Producer emits','Listeners react','Cleanup'],5:['Input changes','Async operation','Latest result'],6:['Event name','Typed payload','Handler'],7:['Current state','Guard check','Next state'],8:['Search input','Debounce / switch','Result'],9:['Server sends','Client receives','Screen updates'],10:['Source','Backpressure','Destination'],11:['Arrange','Act','Assert'],12:['Producer','Channel','Consumer'],13:['Delivery','Process / retry','Acknowledge'],14:['Transaction','Outbox','Consumer'],15:['Event history','Pure reducer','Current state'],16:['Workflow step','Failure','Compensation'],17:['Validate','Process','Observe'],18:['User action','Feature logic','Evidence'],19:['Reproduce','Repair','Regression check'],21:['Package','Demonstrate','Defend']};
const records=[];
for(let n=1;n<=21;n++){
 const id=String(n).padStart(2,'0'),md=fs.readFileSync(path.join(root,'modules',`EDP_M${id}.md`),'utf8').replaceAll('\r','');
 const title=plain(md.match(/^# (.+)/)[1]).replace(/^EDP Module \d+[: ·]+/,'');const slides=[];
 const add=(type,title,body)=>slides.push({type,title,body});
 const diagram=path.join(root,'visuals',`m${n===21?'20':id}-guide.svg`);
 const visual=fs.existsSync(diagram)?`<img class="diagram" alt="Module ${id} event flow" src="data:image/svg+xml;base64,${fs.readFileSync(diagram).toString('base64')}">`:'';
 const targets=sec(md,'## A. Lesson Preview & Review').match(/\*\*Learning targets\*\*([\s\S]*?)(?=\*\*Before class)/)?.[1]||'';
 const goals=[...targets.matchAll(/^\d+\. (.+)$/gm)].map(m=>m[1]);
 add('EVENT-DRIVEN PROGRAMMING · '+id,title,`<div class="hero"><div><p class="intro">${esc(md.match(/\*\*In a nutshell:\*\* ([^\n]+)/)?.[1]||'Explain your design choices and support them with evidence.')}</p><ol class="targets">${goals.map(g=>`<li>${esc(g)}</li>`).join('')}</ol><p class="small">60–90 minutes · Predict, run, explain, modify</p></div><div class="hero-art"><span>{ }</span><p>Input<br>Event<br>Reaction</p></div></div>`);
 const main=sec(md,'## B. Main Lesson');const chunks=[...main.matchAll(/^### (.+)\n([\s\S]*?)(?=^### |$(?![\s\S]))/gm)];
 for(const m of chunks){
 const paragraphs=para(m[2]);const points=paragraphs.map(p=>plain(p).match(/^.*?[.!?](?:\s|$)/)?.[0]||plain(p));
 add('MAIN LESSON',plain(m[1]),`<div class="lesson"><div class="principles">${points.map((p,i)=>`<article><span class="step">${String(i+1).padStart(2,'0')}</span><p>${esc(p)}</p></article>`).join('')}</div><aside class="concept-visual"><h3>Locate this idea in the flow</h3><div class="vertical-flow">${(routes[n]||routes[1]).map((label,i)=>`<div><b>${i+1}</b>${esc(label)}</div>`).join('')}</div><details><summary>Detailed teaching notes</summary>${paragraphs.map(p=>`<p>${esc(plain(p))}</p>`).join('')}</details></aside></div>`);
 }
 if(visual)add('VISUAL WALKTHROUGH','Follow the event flow',`${visual}<p class="caption">Trace the arrows. Identify the input, handler, visible effect, and cleanup boundary.</p>`);
 const analogy=sec(md,'### Everyday connection');if(analogy)add('CONNECT THE IDEA','An everyday example',`<blockquote>${esc(plain(analogy))}</blockquote><div class="strip">${esc(plain(sec(md,'### Sa madaling salita')).split('[Quick')[0])}</div>`);
 const setup=sec(md,'### Run the complete example');const files=[...md.matchAll(/^### File: `([^`]+)`[\s\S]*?```[^\n]*\n([\s\S]*?)\n```/gm)];
 for(const [i,f] of files.entries()){
 const fpath=path.join(root,'examples',f[1]),code=fs.existsSync(fpath)?fs.readFileSync(fpath,'utf8').trimEnd():f[2];
 const commands=[...setup.matchAll(/```[^\n]*\n([\s\S]*?)```/g)].map(x=>x[1]).join('\n');
 add('GUIDED CODE · '+f[1],'Run the complete program',`<div class="code-layout"><div class="code-window"><header><span>${esc(f[1])} · complete file</span><button data-copy="code-${i}">Copy complete code</button></header><pre><code id="code-${i}">${highlight(code)}</code></pre></div><aside><h3>Run from EDP/examples</h3><pre class="command">${highlight(commands||'See the module setup instructions.')}</pre><p>Offline lab: copy the entire offline-lab folder, then open START-LAB.cmd.</p><p>Keep supporting files together. Node must already be installed.</p><h3>1. Predict</h3><p>Write the first output before running.</p><h3>2. Run</h3><p>Compare what you see with your prediction.</p><h3>3. Explain</h3><p>Point to the callback or branch responsible for the result.</p></aside></div>`);
 }
 if(files.length){
 const f=files[files.length-1],lines=f[2].split('\n');
 const relevant=lines.findIndex(l=>/addEventListener|\.on\(|async function|function |=>/.test(l));
 const start=Math.max(0,relevant);const excerpt=lines.slice(start,start+12).join('\n');
 const explanation=plain(sec(md,'### Expected behavior and explanation checkpoint')).split('Before editing')[0];
 add('CODE WALKTHROUGH · '+f[1],'Connect the code to its behavior',`<div class="code-layout"><div class="code-window"><header>Lines ${start+1}–${Math.min(start+12,lines.length)} · explanation excerpt</header><pre><code>${highlight(excerpt)}</code></pre></div><aside><h3>What this program demonstrates</h3><p>${esc(explanation)}</p><h3>Trace it aloud</h3><p>Identify the input value, the callback or branch that uses it, and the statement that exposes the result.</p><p>Copy the complete program from the preceding slide. This excerpt is for explanation.</p></aside></div>`);
 }
 const expected=sec(md,'### Expected behavior and explanation checkpoint');if(expected)add('TRACE AND EXPLAIN','What changes when it runs?',`<div class="result">${prose(expected)}</div><div class="trace"><div>1. Find the input</div><div>2. Follow the handler</div><div>3. Observe the result</div></div>`);
 const trouble=sec(md,'### Troubleshooting and common mistake');if(trouble)add('DEBUGGING','When the result is unexpected',`<div class="two"><article><h3>Common mistake</h3>${prose(para(trouble)[0]||'')}</article><article><h3>Check the setup</h3>${prose(para(trouble).slice(1).join('\n\n'))}</article></div>`);
 if(n<20){add('RECAP','Before the assessment',`<ol class="recap">${goals.map(g=>`<li>${esc(g)}</li>`).join('')}</ol><p class="strip">${esc(plain(sec(md,'### Your independent change')).split('**Checkpoint')[0].split('Checkpoint:')[0])}</p>`);}
 if(bank[n]){
 const qs=bank[n],outs=cases.filter(c=>c.module===n);
 for(let i=0;i<5;i+=4)add('ASSESSMENT · 5 MCQ + 5 OUTPUT','Multiple choice',`<div class="quiz-grid ${i===4?'single':''}">${qs.slice(i,i+4).map((q,j)=>`<article class="q"><div class="qno">QUESTION ${i+j+1}</div><h3>${esc(q.q)}</h3><div class="options">${q.options.map((o,k)=>`<div><b>${'ABCD'[k]}</b><span>${esc(o)}</span></div>`).join('')}</div></article>`).join('')}</div>`);
 for(let i=0;i<5;i+=4)add('ASSESSMENT · WRITE THE EXACT OUTPUT','Guess the output',`<div class="quiz-grid ${i===4?'single':''}">${outs.slice(i,i+4).map(q=>`<article class="q"><div class="qno">QUESTION ${q.item}</div><pre><code>${highlight(q.code)}</code></pre></article>`).join('')}</div>`);
 add('INSTRUCTOR ANSWERS · AFTER THE QUIZ','Multiple-choice answers',`<div class="answers">${qs.map((q,i)=>`<article><b>${i+1}. ${'ABCD'[q.answer]}</b><p>${esc(q.why)}</p></article>`).join('')}</div>`);
 add('INSTRUCTOR ANSWERS · AFTER THE QUIZ','Expected output',`<div class="answers">${outs.map(q=>`<article><b>${q.item}.</b><pre>${esc(q.answer)}</pre></article>`).join('')}</div>`);
 }else if(n<20){
 const dependencyLesson=[6,8].includes(n);
 const mode=dependencyLesson?'LAB IF PREPARED · ASSIGNMENT IF DOWNLOADS ARE NEEDED':'OFFLINE COMPUTER-LAB ACTIVITY';
 const setupNote=n===6?'Full type checking needs the TypeScript packages. If already installed, work in the lab. If missing, complete the type-checking task as an assignment: use the original examples folder, run npm ci, then npm run typecheck and node m06.ts. Running m06.ts alone does not type-check it.':n===8?'The supplied offline-lab folder already includes RxJS: copy the entire folder and run START-LAB.cmd, then select 8. No npm download is needed for that route. If using the original examples folder without installed packages, finish as an assignment: run npm ci, then npm run serve and open http://127.0.0.1:4173/m08.html.':'Use the prepared offline-lab folder on the lab PC. Open START-LAB.cmd and enter this module number. Node must already be installed. The supplied example needs no npm package download.';
 const task=assignments[n][0].match(/<p>([\s\S]*?)<\/p>/)?.[1]||'';
 add(mode,'Your independent coding task',`<div class="activity-card"><p>${task}</p><p>${esc(setupNote)}</p><p>Copy the complete starter, make the requested change, then show one success case and one failure or cleanup case. Explain the line that changes the behavior.</p></div>`);

 const combined=assignments[n][1];const split=combined.indexOf('<p><b>Repository:');
 if(split<0)throw Error('Missing submission boundary for '+n);
 const essay=combined.slice(0,split);
 add('TOPIC ESSAYS · INDIVIDUAL','Explain the principles in your own words',`<p class="essay-instruction">Answer both prompts. Write one focused paragraph for each: explain the principle, give a concrete example, and justify what should happen. Use your code when available; you can draft your reasoning while dependencies are being prepared.</p><div class="essay-prompts">${essay.replace(/<p>Write one focused paragraph[\s\S]*$/, '')}</div><p class="caption">Save as essays.md. Suggested scoring per response: accuracy 2, concrete example 1, reasoning 1, evidence or predicted result 1.</p>`);
 add('SUBMISSION INSTRUCTIONS','Name, upload, and submit',combined.slice(split).replace(/(edp-m\d+-[^<]+)(<\/code>)/, '$1-yyyy-mm-dd$2')+`<p class="caption">Replace yyyy-mm-dd with the activity or assignment date announced by your instructor. This is the task date, not an invented deadline. Due date and submission channel: as announced. Offline classwork may be saved locally first and uploaded when access is available.</p>`+`<div class="trace"><div>1. Run your saved files</div><div>2. Check the README</div><div>3. Submit the link</div></div>`);

 }else if(n===20){
 const qs=[...sec(md,'## C. Applied quiz · 20 items').matchAll(/^(\d+)\. (.+)$/gm)];for(let i=0;i<qs.length;i+=4)add('DEFENSE PREPARATION','Applied questions',`<div class="quiz-grid">${qs.slice(i,i+4).map(q=>`<article class="q"><div class="qno">QUESTION ${q[1]}</div><h3>${esc(q[2])}</h3></article>`).join('')}</div>`);
 add('DEFENSE PREPARATION','Two essays',prose(sec(md,'## D. Defense essays · two responses')));
 const answerDoc=fs.readFileSync(path.join(root,'instructor/ANSWER_KEY.md'),'utf8').replaceAll('\r','');
 const answerSection=answerDoc.split(/^## Module 20[^\n]*\n/m)[1]?.split(/^## Module /m)[0]||'';
 const items=[...answerSection.matchAll(/^(\d+)\. (.+)$/gm)].slice(0,20);
 for(let i=0;i<items.length;i+=4)add('INSTRUCTOR ANSWERS','Defense preparation key',`<div class="quiz-grid">${items.slice(i,i+4).map(q=>`<article class="q"><div class="qno">${q[1]}</div><p>${esc(plain(q[2]))}</p></article>`).join('')}</div>`);
 add('INSTRUCTOR GUIDE','Essay scoring',`<p>Each essay: accurate principles 2, concrete application 1, justified reasoning 1, observable verification 1.</p><p>Look for an event flow with success, rejection and cleanup evidence; then distinguish duplicate registration from message redelivery using a repeatable trace.</p>`);

 }else{
 const ideas=[...md.matchAll(/^\| (\d+\. [^|]+)\|([^|]+)\|([^|]+)\|$/gm)];for(let i=0;i<ideas.length;i+=4)add('SOLO MINI-CAPSTONE','Choose a project you can explain',`<div class="quiz-grid">${ideas.slice(i,i+4).map(x=>`<article class="q"><h3>${esc(x[1])}</h3><p>${esc(x[2])}</p><p class="caption">Show: ${esc(x[3])}</p></article>`).join('')}</div>`);
 add('SUBMISSION','Package your solo project',`<p>Repository: <code>edp-capstone-project-surname-firstname-section-yyyy-mm-dd</code></p><p>Include runnable source, README commands, a diagram, success and failure evidence, and your design explanation. Submit the repository URL and commit ID through your instructor’s channel.</p><p>Use the offline lab guide for setup and file requirements. Replace yyyy-mm-dd with the announced project date. Confirm your deadline with your instructor.</p>`);
 }
 add('WRAP-UP','Explain it. Then make it yours.',`<blockquote>“What happened, who reacted, and how do you know?”</blockquote><p>Keep your working version and explain one change in your own words.</p><details><summary>Lesson references and further reading</summary>${prose(sec(md,'### References and further reading'))}</details>`);
 if(slides.length>25)throw Error(`${id}: ${slides.length} slides`);
 const html=`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>EDP ${id} · ${esc(title)}</title><style>${css}</style></head><body><div id="progress"></div><main>${slides.map((s,i)=>`<section class="slide" ${i?'hidden':''}><div class="eyebrow">${esc(s.type)}</div><h1>${esc(s.title)}</h1><div class="body">${s.body}</div></section>`).join('\n')}</main><span id="count"></span><script>${script}</script></body></html>`;
 fs.writeFileSync(path.join(dir,`EDP_M${id}.html`),html);records.push({module:n,file:`EDP_M${id}.html`,slides:slides.length,title});
}
fs.writeFileSync(path.join(dir,'deck-manifest.json'),JSON.stringify(records,null,2));console.log(records.map(r=>`${r.module}:${r.slides}`).join(' '));
