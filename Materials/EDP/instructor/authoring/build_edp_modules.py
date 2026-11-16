from pathlib import Path
import re
from edp_lesson_text import LESSONS as first
from edp_lesson_text_advanced import LESSONS as second
from edp_assessments import QUIZZES

root=Path('Application Development and Emerging Technologies (Inluding event Driven programming)/EDP')
modules=root/'modules'; teacher=root/'instructor'; examples=root/'examples'
modules.mkdir(exist_ok=True); teacher.mkdir(exist_ok=True)
lessons=first|second
taglish=[
'Ang callback ay function na ipinapasa para tawagin kapag kailangan. Sa setTimeout, naka-schedule ito; tuloy pa rin ang kasunod na code.',
'Habang naghihintay ang isang async operation, puwedeng umusad ang ibang gawain. Pero ang mabigat na synchronous loop ay nakaharang pa rin sa thread.',
'Piliin ang element, ikabit ang listener, saka hintayin ang click. Ang handler ang nagsasabi kung ano ang magbabago sa page.',
'Isang order event, maraming puwedeng reaction. Alisin ang listener kapag tapos na ang may-ari nito para walang dobleng response.',
'Hindi dahil huling dumating ang response ay iyon na ang pinakabagong request. Tingnan ang request ID bago ipakita ang result.',
'Tinutulungan tayo ng types habang nagsusulat. Pero ang data galing sa labas ay kailangan pa ring suriin habang tumatakbo ang program.',
'Hindi lahat ng action ay puwede sa lahat ng state. Kung hindi pa ready ang order, hindi pa dapat tanggapin ang collect.',
'Isipin ang input bilang sunod-sunod na values. Ang operators ang naglilinaw kung alin ang gagamitin, kailan, at hanggang kailan.',
'May tunay na network connection dito. Kapag reconnect, hindi ibig sabihin na naibalik na rin ang lahat ng nawalang messages.',
'Kung mas mabilis ang producer kaysa consumer, kailangan ng kontrol sa daloy. Hindi solusyon ang walang katapusang pag-ipon sa memory.',
'Hindi sapat ang walang error sa screen. Mag-assert ng inaasahang result at patunayang tumitigil ang listener pagkatapos ng cleanup.',
'Magkaiba ang paghahati ng trabaho at pagpapadala ng parehong balita sa maraming departamento. Piliin ang model ayon sa kailangan.',
'Puwedeng maulit ang delivery. Dapat hindi umulit ang singil o ibang business effect dahil lang naulit ang message.',
'Sabay itala ang business change at balak na mag-publish sa isang transaction. Hiwalay pa rin ang delivery kaya posible pa rin ang duplicate.',
'Ang replay ay pagbubuo ulit ng state mula sa history. Hindi ito pahintulot na ulitin ang email, bayad, o ibang external action.',
'Kapag pumalya ang susunod na hakbang, may recovery action. Hindi laging kayang ibalik nang eksakto ang lahat sa dati.',
'Sundan ang ebidensiya: aling event, aling workflow, anong result? Huwag isama ang password o token para lang mas maraming log.',
'Unahin ang isang buong gumaganang flow. Mas madaling ipaliwanag at i-test ang maliit pero malinaw na project.',
'Balikan ang alam na: predict, run, hanapin ang sanhi, ayusin, at i-test ulit. Hindi ito oras para magdagdag ng bagong framework.',
'Dapat kayang patakbuhin ng ibang tao ang project gamit ang instructions mo. Sabihin nang malinaw ang nagawa at ang limitasyon.'
]
contents=(root/'EDP_compiled contents.md').read_text(encoding='utf-8')
titles=dict((int(n),t) for n,t in re.findall(r'^## Module (\d+): (.+)$',contents,re.M))
mainfiles={i:[f'm{i:02}.mjs'] for i in range(1,21)}
mainfiles.update({1:['m01.mjs','m01-types.ts'],3:['m03-first.html','m03.html'],6:['m06.ts'],8:['m08.mjs','m08.html'],9:['server.mjs','m09.html'],10:['m10.mjs','m10-worker.mjs','worker.mjs'],11:['m11.test.mjs'],18:['project.mjs','m18.mjs','project.test.mjs'],20:['project.mjs','m20.mjs','project.test.mjs']})
assessment_key='# EDP instructor answer key and scoring guidance\n\nPrepared 3 November 2026. Distribute student module files separately from this instructor folder. Each odd-module quiz has exactly 10 items, one point each. Accept equivalent technically correct wording; give item-level feedback. Items 1–3 check concepts, 4–6 traces, 7–8 diagnosis, 9–10 application. Module 1 is diagnostic; actual grade weighting follows institutional policy.\n\n'
index='# EDP — Complete teaching modules\n\nTwenty authored Markdown lessons based on the compiled contents. Read [setup](../examples/README.md) first and consult the [validation report](../instructor/VALIDATION.md) for what was actually tested. These are classroom materials, not production deployments.\n\n| Module | Lesson | Period | Assessment |\n| --- | --- | --- | --- |\n'
coverage='# EDP compiled-contents coverage map\n\nEvery compiled subsection is mapped to its lesson below. Main-lesson prose explains the concepts; the runnable core implements a smaller subset. Advanced comparisons are reference/discussion, not an additional required installation or graded exercise.\n\n'
for i in range(1,21):
 d=lessons[i]; period='Prelim' if i<=5 else 'Midterm' if i<=11 else 'Pre-final' if i<=18 else 'Finals'
 assess='10-item quiz' if i%2 else 'Coding activity'
 index+=f'| {i:02} | [Module {i}: {titles[i]}](EDP_M{i:02}.md) | {period} | {assess} |\n'
 source_section=re.search(rf'^## Module {i}:.*?(?=^## Module {i+1}:|^## Source|\Z)',contents,re.M|re.S).group(0)
 topics=re.findall(r'^### (.+)$',source_section,re.M)
 coverage+=f'## M{i:02}: {titles[i]}\n\n[Lesson](../modules/EDP_M{i:02}.md)\n\n'+''.join(f'- {t}\n' for t in topics)+'\n'
 page=f'# EDP Module {i:02}: {titles[i]}\n\n[Module index](README.md) | [Setup and commands](../examples/README.md)\n\n**Period:** {period} · **Meeting:** 60–90 minutes · **Assessment:** {assess}\n\n'
 page+='## A. Lesson Preview & Review\n\n'+d['hook']+'\n\n**In a nutshell:** '+d['targets'][0]+' We will run a small example, explain its behavior and change one part ourselves.\n\n**Learning targets**\n\n'+''.join(f'{j}. {t}\n' for j,t in enumerate(d['targets'],1))
 prereq='Prior programming exposure; prepared Node/editor setup. All basic syntax is refreshed today.' if i==1 else 'Earlier core lessons or their supplied runnable checkpoints. No database or broker installation is required for this lesson.'
 page+='\n**Before class:** '+prereq+' Read the example filenames below and keep a clean copy before editing.\n\n'
 if i%2:
  page+='**60-minute route:** 5 minutes preview, 25 explanation/demo, 15 guided code, 10 quiz, 5 feedback. For 90 minutes, add 15 minutes practice and 15 discussion/debugging.\n\n'
 else:
  page+='**60-minute route:** 5 minutes preview, 15 explanation/demo, 30 coding, 10 review. For 90 minutes, add 15 guided exploration and 15 debugging/feedback.\n\n'
 page+='**Scope:** Prioritize the runnable core and learning targets. The later comparisons are reference reading or teacher demonstrations; do not attempt every extension in one meeting. Finals modules introduce no new infrastructure.\n\n## B. Main Lesson\n\n'+d['lesson']
 page+='\n## C. Analogy, Guided Program & Practice\n\n### Everyday connection\n\n'+d['analogy']+'\n\n### Run the complete example\n\nRun commands from the `EDP/examples` folder. Install the pinned dependencies once with `npm ci`; most `.mjs` examples otherwise use only Node built-ins. See the setup guide for the verified runtime.\n\n'
 if i==3: cmd='npm run serve'; extra='Start with http://127.0.0.1:4173/m03-first.html: a complete minimal button-and-script page. After that works, open http://127.0.0.1:4173/m03.html for the form/list/cleanup extension. Stop the server with Ctrl+C.'
 elif i==8: cmd='node m08.mjs\nnpm run serve'; extra='The console program shows a fixed input sequence. Then open http://127.0.0.1:4173/m08.html to type into a real search box. The browser loads the pinned local RxJS bundle; no CDN is required. Search results are simulated, not fetched from a real campus database. Stop the server with Ctrl+C.'
 elif i==9: cmd='npm run serve'; extra='Open http://127.0.0.1:4173/m09.html. Keep the terminal running. Stop/restart it to observe connection status; press Disconnect to close the stream. Do not start a second server on the same port.'
 elif i==6: cmd='npm run typecheck\nnode m06.ts'; extra='The verified Node 24 runtime executes this erasable TypeScript syntax; typecheck is still required. Node execution alone does not validate types.'
 elif i==11: cmd='node --test m11.test.mjs'; extra='A successful run reports three passing tests. Output timing values can differ.'
 elif i==1: cmd='node m01.mjs\nnpm run typecheck\nnode m01-types.ts'; extra='The first command needs no third-party library. Use the TypeScript companion only after the basic program is understood; its output is A1: PHP 60.'
 elif i in [18,20]: cmd=f'node m{i:02}.mjs\nnode --test project.test.mjs'; extra='Keep project.mjs beside the entry file. This starter is an in-memory model; it does not persist records across restarts.'
 else: cmd=f'node m{i:02}.mjs'; extra='Wait for completion and read the entire output. For Module 10 the worker files are optional; run node m10-worker.mjs separately.' if i==10 else 'Wait for completion and compare behavior with the expected trace before editing.'
 page+=f'```powershell\n{cmd}\n```\n\n{extra}\n\n'
 for name in mainfiles[i]:
  lang='html' if name.endswith('.html') else 'typescript' if name.endswith('.ts') else 'javascript'
  code=(examples/name).read_text(encoding='utf-8')
  page+=f'### File: `{name}`\n\n[Open runnable file](../examples/{name})\n\n```{lang}\n{code}```\n\n'
 page+='### Expected behavior and explanation checkpoint\n\n'+d['trace']+'\n\nBefore editing, identify the producer/input, callback or consumer, state/output, and cleanup boundary in the code. Trace one value through the program. Explain which line changes the outcome rather than only reading the console aloud.\n\n### Your independent change\n\n'+d['change']+'\n\n**Checkpoint:** Predict → run → explain → modify. *Hindi sapat na gumana dahil kinopya; dapat kaya mong sabihin kung bakit at baguhin ang isang behavior.*\n\n### Troubleshooting and common mistake\n\n'+d['pitfall']+'\n\nIf a command fails before any lesson output, check the working folder, filename, Node version and installed packages first. Distinguish setup errors from a deliberately rejected input or handled runtime failure.\n\n'
 page+='### Sa madaling salita\n\n'+taglish[i-1]+'\n\n[Quick reference and glossary](QUICK_REFERENCE.md)\n\n'
 page+='## D. Assessment, Wrap-Up & References\n\n'
 if i%2:
  page+='### 10-item quiz\n\nOne point per item. Answer after the explanation and guided practice. Give short answers; no extra graded coding submission today. The instructor keeps the answer key separately.\n\n'
  for j,(q,a) in enumerate(QUIZZES[i],1): page+=f'{j}. {q}\n'
  assessment_key+=f'## Module {i:02}\n\n'+''.join(f'{j}. **{a}**\n' for j,(q,a) in enumerate(QUIZZES[i],1))+'\n'
 else:
  page+='### One coding activity\n\n**Task:** '+d['change']+'\n\n**Submit one folder or archive containing:**\n\n1. Your complete modified program and any files needed to run it.\n2. A short README with the exact command and expected result.\n3. Evidence of one successful case and one rejected/failing case, plus a brief explanation of your independent change.\n\n| Criterion | Points | Evidence |\n| --- | ---: | --- |\n| Required behavior | 4 | Core works (2); requested independent change works (2) |\n| Error/edge behavior | 2 | Failure is detected (1); response preserves intended state or reports a clear limit (1) |\n| Understanding | 2 | Explain event/data flow (1); explain your own change (1) |\n| Reproducibility/readability | 2 | Commands/files are complete (1); names and small structure are understandable (1) |\n| Total | 10 | One activity, no separate quiz |\n\n'
  assessment_key+=f'## Module {i:02} — coding observation guide\n\nExpected starting trace: {d["trace"]}\n\nRequired student change: {d["change"]}\n\nAward using the module rubric. Require a live explanation or a brief code walkthrough; screenshots alone do not prove the independent change. Do not penalize equivalent correct implementations. Teacher reference code is a starting point, not the completed student task.\n\n'
 page+='### Wrap-up\n\n'+d['targets'][0]+' '+d['targets'][-1]+'\n\n**Exit reflection (ungraded):** What event or operation started the flow, what state changed, and what happens if that flow cannot complete? Name one assumption the sample deliberately makes.\n\n**Next connection:** '+('The next module builds on this core. Keep your working checkpoint; an independent starter is supplied if you need to restart.' if i<20 else 'Use the instructor’s separately issued final-practical instructions. This preparation activity does not replace the actual exam.')+'\n\n### References and further reading\n\n'
 for url in d['sources']: page+=f'- [Official/reference documentation: {url.split("/")[2]}]({url})\n'
 page+='\nThe prose and classroom code are original teaching examples informed by the references. Source reports are research inputs, not authority for unverified claims. Read [validation notes](../instructor/VALIDATION.md) before distributing a new toolchain version.\n'
 (modules/f'EDP_M{i:02}.md').write_text(page,encoding='utf-8')
(modules/'README.md').write_text(index+'\nOdd modules use quizzes; even modules use coding activities. Guided practice remains ungraded. Summative and periodical exams need their own dates and assessment papers. [Instructor guide](../instructor/TEACHING_GUIDE.md) · [Coverage map](../instructor/COVERAGE_MAP.md)\n',encoding='utf-8')
(teacher/'ANSWER_KEY.md').write_text(assessment_key,encoding='utf-8')
(teacher/'COVERAGE_MAP.md').write_text(coverage,encoding='utf-8')
(examples/'.gitignore').write_text('node_modules/\n',encoding='utf-8')
(examples/'README.md').write_text('''# EDP runnable example pack

## One-time setup

Use an editor, a modern desktop browser and Node.js. The execution host used for this pack is Node **24.18.1**; this is a tested baseline, not a claim about the newest release. The TypeScript examples use Node's supported erasable syntax and are checked separately with TypeScript **5.9.3** and Node typings **24.10.0**. RxJS is **7.8.2**. Exact dependencies are recorded in package-lock.json.

Open a terminal in this `examples` folder, then run:

```powershell
node --version
npm ci
npm run typecheck
npm test
```

Internet is needed to install dependencies initially. An instructor can prepare machines before class. Once installed, the examples use no remote data service. Do not commit or distribute node_modules as source; use the package manifest and lockfile. Keep every example filename unchanged when following a module.

## Entry points

- M01: `node m01.mjs`; optional typed companion `node m01-types.ts` after type checking.
- M02/M04/M05/M07/M08/M10/M12–M20: `node mNN.mjs` with the two-digit module number.
- M03, M08 and M09: `npm run serve`, then open http://127.0.0.1:4173/m03-first.html (first click), /m03.html (form/list), /m08.html (reactive search) or /m09.html (SSE). Keep the terminal open; stop with Ctrl+C. Do not run two copies on the same port.
- M06: `npm run typecheck`, then `node m06.ts`.
- M10 extension: `node m10-worker.mjs`; worker.mjs must remain beside it.
- M11: `node --test m11.test.mjs`.
- M18/M20 project checks: `node --test project.test.mjs`; both depend on project.mjs.

The server binds to loopback only. It is a local teaching server with no authentication, replay storage or public deployment configuration. The SSE counter restarts per connection. Browser examples are plain JavaScript; do not paste TypeScript annotations into their script blocks.

## Troubleshooting

`ERR_MODULE_NOT_FOUND`: run npm ci in this folder and check filenames. `EADDRINUSE`: stop the previous lesson server, or coordinate a deliberate port change in both instructions and server. TypeScript syntax failures: verify the supported Node version; do not confuse execution with tsc checking. An error expected by a test is not an unsuccessful test when the assertion catches it. Look for the final pass/fail result.

Examples from M12 onward are intentionally small local models. They do not establish durable delivery, database transactions, authentication, broker availability or production readiness. The lesson describes what is missing.
''',encoding='utf-8')
(teacher/'TEACHING_GUIDE.md').write_text('''# EDP instructor teaching guide

Prepared 3 November 2026. Use [module index](../modules/README.md), [answer key](ANSWER_KEY.md), [coverage map](COVERAGE_MAP.md) and [validation report](VALIDATION.md) together.

## Structure and pacing

Each lesson follows the existing course's A. Preview, B. Main Lesson, C. Analogy/Program, D. Assessment/Wrap-Up structure. M01–05 are Prelim, M06–11 Midterm, M12–18 Pre-final, M19–20 Finals preparation. These are prepared chapters, not guaranteed dates. Retain separate summative-before-periodical slots; exclude Saturdays. Use the existing calendar/capacity analysis before assigning dates.

M01 refreshes variables, conditions, loops and functions together and introduces setTimeout/clearTimeout. Give the prepared workspace before class; do not spend the whole meeting installing. Its quiz is diagnostic. M03 must begin with the hello button and script block before showing the full form/list extension. Pause after selection, registration, click and text update so students can identify each step.

Odd lessons have one 10-item quiz; even lessons have one coding submission. Do not add graded drills on top. The first three quiz items check concepts, next three traces, next two debugging and last two decisions. Answer keys are instructor material. Use local grading policy for weightings; the proposed coding rubric is 10 points.

## Depth and shortening

Core: the smallest runnable behavior and its failure/cleanup rule. Guided extension: modify the same program. Reference: compare architectures or tools without installing them. Twenty modules can exceed available teaching slots; combine selected related core material and remove optional activities instead of accelerating through two full lessons. If one meeting combines modules, assign one primary assessment and explicitly reschedule or omit the other.

M01–02: prioritise callbacks and observable scheduling. M03: first button, then form. M04–05: emitter and latest-result correctness. M06–08: typed payloads, state rules, one reactive pipeline. M09–11: one transport, one stream and meaningful tests. M12–17: the local model plus a failure diagram; do not demand production brokers, databases, telemetry stacks or cloud accounts. M18: one personal feature. M19–20: repair, explanation and reproducible packaging only.

## Demonstrating understanding

Ask students to predict, run, point to the responsible handler and change one behavior. When they cannot explain it, return to the last working checkpoint and remove one abstraction. Use natural Taglish to clarify the mechanism, not to replace the technical vocabulary. Students who need longer syntax revision can use M01 as catch-up reading without turning every Prelim module into basic programming.

Require one personal modification for coding assessments. The teacher's reference programs are complete runnable baselines, not final answers to all student tasks. Check equivalent solutions against behavior and explanation. Offer an accessible text/console route where a complex interface is not the learning objective.

## Project and exam boundaries

The solo project requires a coherent event flow, validation, a state rule, failure handling, cleanup, tests and setup notes. A small local application is acceptable when limitations are declared. Optional SQL/Mongo persistence must be behind a server API and tested separately; no database install is required by these EDP core examples. The architecture survey is not a requirement to deploy every pattern.

M18's checkpoint, M20's readiness submission, the summative and final practical are distinct assessment events. Avoid awarding multiple marks for the same unchanged artifact. Write the actual exam papers separately according to institutional policy; this pack contains lesson quizzes and activity rubrics, not a claimed official exam.

## Maintenance

Read VALIDATION before claiming an environment is tested. Recheck dependencies when upgrading; repeat type checks and the behavior/browser suite after code changes. Browser UI and host networking differ from console tests. Keep simulations labeled, retain source provenance, and do not use copied AI reports as proof of correctness.
''',encoding='utf-8')
readme=root/'README.md'
s=readme.read_text(encoding='utf-8')
s=s.replace('Current focus: researched content planning before lesson authoring.', 'Current focus: 20 authored EDP lessons with runnable examples, quizzes, coding activities and instructor notes. See validation for the tested scope.\n\n- [Start here: module index](modules/README.md)\n- [Runnable examples and setup](examples/README.md)\n- [Instructor guide](instructor/TEACHING_GUIDE.md)\n- [Validation report](instructor/VALIDATION.md)')
s=s.replace('Full teaching text and tested runnable code remain to be authored.', 'Full teaching lessons and runnable examples are now available; scheduling and actual summative/periodical exam papers remain separate.')
readme.write_text(s,encoding='utf-8')
print('Created 20 lessons, index, instructor key, coverage map and teaching/setup guides.')
