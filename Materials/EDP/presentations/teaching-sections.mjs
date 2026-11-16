import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const slide=(eyebrow,heading,inner)=>({eyebrow,heading,inner});
const panel=(code)=>`<section class="code-card" style="height:auto;max-height:58vh"><pre><code>${esc(code)}</code></pre></section>`;
const themes=['order','task','click','order','search','message','state','search','announcement','chunk','test','job','delivery','record','event','booking','request','feature','repair'];
export const traces=[];
function outputQuestions(n){
 const topic=themes[n-1];
 const source=n<6 ? [
 [`let count = 0;\nfunction handle() { count += 1; }\nhandle();\nhandle();\nconsole.log(count);`,'2','Each call changes the same count once.'],
 [`console.log('start');\nsetTimeout(() => console.log('${topic}'), 0);\nconsole.log('end');`,`start\nend\n${topic}`,'The timer callback waits until the current synchronous work finishes.'],
 [`const pending = setTimeout(() => console.log('late'), 0);\nclearTimeout(pending);\nconsole.log('cancelled');`,'cancelled','Clearing the pending timer prevents its callback from running.'],
 [`Promise.resolve().then(() => console.log('promise'));\nconsole.log('sync');`,'sync\npromise','The promise reaction runs after the current synchronous code.'],
 [`async function run() {\n  try { await Promise.reject(new Error('offline')); }\n  catch (error) { console.log(error.message); }\n  finally { console.log('done'); }\n}\nrun();`,'offline\ndone','Rejection enters catch; finally runs afterward.']
 ] : [
 [`const listeners = new Set();\nconst handle = () => console.log('${topic}');\nlisteners.add(handle);\nlisteners.add(handle);\nfor (const fn of listeners) fn();`,topic,'A Set stores this same function reference once. This models a custom bus, not every event API.'],
 [`let state = 'pending';\nfunction complete() {\n  if (state !== 'pending') return;\n  state = 'done';\n  console.log(state);\n}\ncomplete();\ncomplete();`,'done','The state guard rejects the second transition.'],
 [`const seen = new Set();\nfor (const id of ['e1', 'e1', 'e2']) {\n  if (seen.has(id)) continue;\n  seen.add(id);\n  console.log(id);\n}`,'e1\ne2','The repeated event ID is ignored in this in-memory deduplication model.'],
 [`let latest = 2;\nfunction receive(version, value) {\n  if (version === latest) console.log(value);\n}\nreceive(2, 'new');\nreceive(1, 'old');`,'new','Only the response matching the latest version can update the display.'],
 [`const events = [2, -1, 3];\nconst total = events.reduce((sum, amount) => sum + amount, 0);\nconsole.log(total);\nconsole.log(events.length);`,'4\n3','The reducer derives state without changing the number of recorded events.']
 ];
 return source.map(([code,answer,why],i)=>{traces.push({module:n,item:i+6,code,answer});return {code,answer,why};});
}
export function assessmentSlides(n,quiz,answers,codingTask,code,teacher){
 const out=[];
 const topics={"2": ["async-flow", "Explain why await suspends one function without pausing the whole program. Trace the success and rejection paths.", "Explain how you would detect a blocking CPU loop and distinguish it from waiting for I/O."], "4": ["node-events", "Explain how one order triggers independent listeners and how registration order affects synchronous emit.", "Explain listener cleanup and error handling using one duplicate-registration or failed-handler example."], "6": ["typed-events", "Explain how your event map connects event names to payload types. Show an invalid payload example.", "Explain why TypeScript cannot validate untrusted network data at runtime and propose a runtime check."], "8": ["reactive-search", "Explain debounceTime and switchMap using a search where the earlier request finishes late.", "Explain catchError placement and subscription cleanup when the search screen closes."], "10": ["streams", "Explain backpressure using a fast source and slow destination in your stream.", "Explain when a worker helps CPU work and how you clean up after a stream or worker failure."], "12": ["messaging", "Compare distributing jobs among workers with broadcasting to subscribers in the local model.", "Explain which delivery guarantees your in-memory demonstration lacks and how you would demonstrate a lost message."], "14": ["outbox", "Explain why an outbox record and business change belong in one transaction.", "Explain schema validation and duplicate handling when a stored message is delivered again."], "16": ["saga", "Explain how commands, events and a read model serve different roles in your workflow.", "Trace a failed booking and its compensation. Explain why compensation differs from erasing history."], "18": ["integrated-project", "Trace one complete feature through its producer, payload, handler and state transition.", "Explain your failure and cleanup evidence, your independent changes and one remaining limitation."]};
 const assignment=topics[n];
 if(n%2===0){
 out.push(slide('ASSIGNMENT · INDIVIDUAL','Apply the lesson in your own program',`<div class="activity-card"><p>${esc(codingTask.split('**Submit')[0].replace(/\*\*/g,'').trim())}</p><p>Use the complete source shown earlier as your starter. Save the original first, then change one behavior.</p><p>Offline lab: copy the entire offline-lab folder and open START-LAB.cmd, then enter this module number. Node must already be installed. M08 includes local RxJS. Full TypeScript checking requires the prepared toolchain. If downloads are needed, complete setup as an assignment and document it; write the topic essays while waiting.</p></div>`));
 out.push(slide('ASSIGNMENT · ESSAYS AND SUBMISSION','Explain and submit your work',`<ol>${assignment.slice(1).map(q=>`<li>${esc(q)}</li>`).join('')}</ol><p>Write one focused paragraph per prompt in essays.md, citing your code and observed results. Suggested rubric per essay: accuracy 2, code reference 1, reasoning 1, evidence 1.</p><p><b>Repository:</b> <code>edp-m${String(n).padStart(2,'0')}-${assignment[0]}-surname-firstname-section</code></p><p>Upload source, required supporting files, README commands, essays.md and success/failure evidence. Submit the repo URL + commit ID. Keep passwords and node_modules out. See <a href="../offline-lab/README.md">offline lab and upload guide</a>.</p>`));
 out.push(slide('INSTRUCTOR · REVIEW AFTER SUBMISSION','Coding and essay assessment guide',`<p>${esc(teacher.replace(/```[\s\S]*?```/g,'').replace(/\*\*/g,'').slice(0,1800))}</p>`));
 return out;
 }
 const selected=quiz.slice(0,5);
 const key=[];
 for(let i=0;i<selected.length;i++){
 const correct=answers[i]?.text||'Explain the relevant event flow.';
 const distractors=answers.filter((_,j)=>j!==i).map(a=>a.text).filter(a=>a!==correct).slice(0,3);
 while(distractors.length<3)distractors.push(['All handlers run automatically before registration.','The runtime guarantees that no errors can occur.','Every callback creates a separate CPU thread.'][distractors.length]);
 const options=[...distractors];const position=(n+i)%4;options.splice(position,0,correct);
 out.push(slide(`QUIZ · MULTIPLE CHOICE ${i+1}/5`,selected[i].text,`<ol type="A">${options.map(o=>`<li>${esc(o)}</li>`).join('')}</ol><p class="hint">Choose one best answer. One point.</p>`));
 key.push(`${i+1}. ${'ABCD'[position]} — ${correct}`);
 }
 const outputs=outputQuestions(n);
 outputs.forEach((q,i)=>out.push(slide(`QUIZ · GUESS THE OUTPUT ${i+6}/10`,'Write the exact output in order',`${panel(q.code)}<p class="hint">Run as a standalone JavaScript program after answering. One point. This small model isolates a principle; explain its relationship to the lesson.</p>`)));
 out.push(slide('INSTRUCTOR ANSWERS · 1–5','Multiple-choice answers',`<ol>${key.map(k=>`<li>${esc(k)}</li>`).join('')}</ol>`));
 outputs.forEach((q,i)=>out.push(slide(`INSTRUCTOR ANSWER · ${i+6}`,'Output and explanation',`<div class="output">${esc(q.answer)}</div><p>${esc(q.why)}</p>`)));
 return out;
}
export function breakdownSlides(n,code){
 const out=[];
 for(const sample of code){
 const lines=sample.code.split('\n');
 const groups=[];for(let i=0;i<lines.length;i+=12)groups.push({start:i,lines:lines.slice(i,i+12)});
 for(const group of groups){
 const text=group.lines.join('\n');const notes=[];
 if(/import|require\(/.test(text))notes.push('Imports make dependencies available. Install packages named in the setup before running the complete file.');
 if(/addEventListener|\.on\(|\.subscribe\(/.test(text))notes.push('Registration connects a handler to a future event. Identify the event name and the function reference.');
 if(/await|Promise|setTimeout/.test(text))notes.push('Follow synchronous statements first, then the scheduled continuation. Waiting does not move CPU work to another thread.');
 if(/if\s*\(|throw|catch/.test(text))notes.push('The condition or error branch determines which path is accepted. Trace one valid input and one rejected input.');
 if(/remove|abort|clearTimeout|unsubscribe|\.off\(/i.test(text))notes.push('Cleanup releases pending work or registrations. Check what would happen if setup ran again.');
 if(/console\.log|textContent|write\(/.test(text))notes.push('These statements expose the result. Match each visible output to the statement that produces it.');
 if(!notes.length)notes.push('Identify the values this block creates or changes, then follow where the next block uses them.');
 out.push(slide(`CODE BREAKDOWN · ${sample.name} · LINES ${group.start+1}–${group.start+group.lines.length}`,'Follow this part of the program',`<div class="code-layout">${panel(text)}<aside class="run-card">${notes.map(note=>`<p>${esc(note)}</p>`).join('')}<p class="taglish">Ano ang input dito, at ano ang nagbago?</p><p>Excerpt for explanation. Copy the complete program from the code lab slide.</p></aside></div>`));
 }
 }
 return out;
}
process.on('exit',()=>fs.writeFileSync(path.join(here,'output-quiz-cases.json'),JSON.stringify(traces,null,2)));
