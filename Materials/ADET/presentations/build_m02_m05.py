from pathlib import Path
from html import escape as e
import re, json, shutil

here=Path(__file__).resolve().parent
root=here.parent
reference=(here/'ADET_M01_slides.html').read_text(encoding='utf-8')
css=re.search(r'<style>(.*?)</style>',reference,re.S)[1]
scroll='''
/* ADET themed scrollbars: slides, code and note panels. */
*{scrollbar-width:thin;scrollbar-color:#9670cd #100c1b}
::-webkit-scrollbar{width:12px;height:12px}
::-webkit-scrollbar-track{background:#100c1b;border-radius:12px}
::-webkit-scrollbar-thumb{background:linear-gradient(180deg,#b375e1,#7050ad);border:3px solid #100c1b;border-radius:12px;min-height:40px}
::-webkit-scrollbar-thumb:hover{background:#cf9bf4}
::-webkit-scrollbar-thumb:active{background:#e9b9ff}
::-webkit-scrollbar-corner{background:#100c1b}
.s,.code pre,.snippet pre,.scroll-panel{scrollbar-gutter:stable;overscroll-behavior:contain}
@media(forced-colors:active){*{scrollbar-color:auto}}
'''
extras='''
:root{--scale:1}
html,body{font-size:calc(clamp(18px,1.45vw,22px)*var(--scale))}
h1{font-size:calc(clamp(34px,4.6vw,54px)*var(--scale))}
h2{font-size:calc(clamp(28px,3.1vw,40px)*var(--scale))}
h3{font-size:calc(22px*var(--scale))}
.eb,#ctr,.code header,.cp,.snippet header{font-size:calc(16px*var(--scale))}
code,.k,.code pre,.snippet pre,pre.tree{font-size:calc(clamp(16px,1.15vw,19px)*var(--scale))}
.code pre,.snippet pre{tab-size:2;white-space:pre;line-height:1.6}
.snippet{background:#07050d;border:1px solid var(--ln);border-radius:14px;overflow:hidden;min-width:0}
.snippet header{padding:8px 14px;background:var(--card2);color:var(--mu)}
.snippet pre{margin:0;padding:16px;overflow:auto;max-height:48vh;font-family:Consolas,monospace}
.scroll-panel{overflow:auto}.row{height:min(550px,63vh)}
.q2 .c:last-child:nth-child(odd){grid-column:auto;justify-self:stretch;width:auto}
.q2 .c{padding:18px 22px}.q2 h3{color:var(--tx)}.opt{margin-top:.4em;line-height:1.6}
a{color:#d8b4fe;text-underline-offset:4px}a:hover{color:#f5d0fe}
.caption{font-size:calc(16px*var(--scale));color:var(--mu);margin-top:12px}
.tag{display:inline-block;padding:5px 12px;border:1px solid var(--ln);border-radius:9px;margin:8px 8px 0 0;font-size:calc(16px*var(--scale));color:#c4b5fd}
.big{font-size:calc(26px*var(--scale));font-weight:700}
.s:focus{outline:none}.s{scroll-padding:30px}.s a:focus-visible,.cp:focus-visible{outline:3px solid var(--wn);outline-offset:4px}
.hero svg{max-height:clamp(240px,45vh,380px)}
@media(max-width:800px){.s{padding:34px 24px 60px}.row{height:auto}.code pre{max-height:56vh}.q2{grid-template-columns:minmax(0,1fr)}.hero{min-height:0}.hero svg{max-height:260px}}
@media print{html,body{height:auto;overflow:visible;background:white;color:black}#frame,#bar,#ctr,#help,.cp{display:none!important}.s{position:relative;opacity:1;visibility:visible;transform:none;break-after:page;overflow:visible;padding:25px}.s[aria-hidden=true]{display:block}.code pre,.row,.row>*{height:auto;max-height:none;overflow:visible}.c,.code,.snippet{break-inside:avoid}.s{print-color-adjust:exact;-webkit-print-color-adjust:exact}}
'''

def card(title,body,cls=''):
    return f'<div class="c {cls}">'+(f'<h3>{title}</h3>' if title else '')+body+'</div>'
def grid(*items,three=False): return f'<div class="g{3 if three else 2}">'+''.join(items)+'</div>'
def bullets(*items): return '<ul>'+''.join('<li>'+item+'</li>' for item in items)+'</ul>'
def table(headers,rows):return '<table><thead><tr>'+''.join(f'<th>{h}</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{v}</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table>'
def code(src,label='App.tsx · complete file',full=True,source=None):
    attr=f' data-source="{e(source,quote=True)}"' if source else ''
    cls='code' if full else 'snippet'
    return f'<div class="{cls}" data-n="{e(label,quote=True)}"{attr}><pre>{e(src.rstrip())}</pre></div>'
def sample(number):return (root/f'examples/M{number:02}/App.tsx').read_text(encoding='utf-8')
def full(number):return code(sample(number),source=f'../examples/M{number:02}/App.tsx')
def diagram(labels):
    width=760; gap=24; cell=(width-(len(labels)-1)*gap)/len(labels)
    shapes=[]
    for i,label in enumerate(labels):
        x=i*(cell+gap)
        shapes.append(f'<rect x="{x}" y="25" width="{cell}" height="72" rx="12" fill="#1a1430" stroke="#8b5cf6"/><text x="{x+cell/2}" y="68" fill="#f1ecff" text-anchor="middle" font-size="20">{e(label)}</text>')
        if i<len(labels)-1:shapes.append(f'<path d="M{x+cell+3} 61h{gap-6}l-6 -5m6 5l-6 5" fill="none" stroke="#d946ef" stroke-width="2"/>')
    return '<svg viewBox="0 0 760 125" role="img"><title>'+e(' → '.join(labels))+'</title>'+''.join(shapes)+'</svg>'
def phone(title,lines):
    return '<svg viewBox="0 0 300 360" role="img"><title>'+e(title)+'</title><rect x="45" y="5" width="210" height="345" rx="28" fill="#07050d" stroke="#d946ef" stroke-width="3"/><rect x="58" y="35" width="184" height="285" rx="10" fill="#1a1430"/>'+''.join(f'<text x="75" y="{90+i*42}" fill="{("#d8b4fe" if i==0 else "#f1ecff")}" font-size="18">{e(line)}</text>' for i,line in enumerate(lines))+'</svg>'
def slide(title,body,kicker='Main lesson'):return f'<section class="s" tabindex="-1"><div class="eb">{kicker}</div><h2>{title}</h2>{body}</section>'
def hero(number,title,subtitle,visual):return f'<section class="s" tabindex="-1"><div class="hero"><div><div class="eb">ADET · Module {number:02} · Prelim</div><h1>{title}</h1><p>{subtitle}</p><span class="tag">React Native</span><span class="tag">Expo</span><span class="tag">TypeScript</span></div>{visual}</div></section>'
def setup(number):
    command=f'npx create-expo-app@latest ADET-M{number:02}-LASTNAME --template blank-typescript@sdk-58 --no-agents-md\ncd ADET-M{number:02}-LASTNAME\nnpx tsc --noEmit\nnpx expo start'
    return grid(code(command,'Online preparation · before class'),card('Prepared offline lab',bullets('Copy the prepared starter with <code>node_modules</code>.','Copy the lesson’s <code>App.tsx</code>, then type-check again.','Run <code>npx expo start --offline</code>.','No extra packages for this core lesson.','A native client and working local connection still need the smoke test.')))+ '<p class="caption">SDK 58 · TypeScript 6.0.3. Metro transpiles; it does not type-check. <code>--tunnel</code> requires internet.</p>'
def prepare(number):
    return slide(f'Prepare your laptop for M{number:02}',setup(number)+ '<div class="c mt"><p>Bring <b>your own prepared laptop</b> next coding meeting. Open the app once before class; bring a screenshot or the exact error. Use campus Wi-Fi, an agreed hotspot or a USB copy if needed. The instructor confirms the date and naming pattern.</p></div>','Before next meeting')
def source_links(number,extras=''):
    return f'<p class="caption"><a href="../modules/ADET_M{number:02}.md">Full lesson</a> · <a href="../examples/M{number:02}/App.tsx">Copyable App.tsx</a> · <a href="../offline-lab/SMOKE-TEST.md">Lab smoke test</a>{extras}</p>'
def modes():return grid(card('1 · Offline lab','<p>Prepared dependencies. Run in class if the actual native display route passes the smoke test.</p>'),card('2 · Own laptop','<p>Install before class; bring your laptop and complete the same activity during class.</p>'),card('3 · Written alternative','<p>Equivalent trace and explanation. Same 10-point maximum; no fabricated screenshot.</p>'),three=True)
rubric=table(['Evidence','Points'],[['Working independent change / correct written trace','4'],['Meaningful edge case and response','2'],['Explain the data flow and decisions','2'],['Reproducible setup / ordered, readable evidence','2']])
def submission(number):return slide('What to submit',grid(card('Source and evidence',bullets('Your modified source, package.json and lockfile.','README: run commands, actual activity date and explanation.','One normal case and one failure/edge case.','Do not upload node_modules, caches or secrets.')),card('Repository and date',f'<p class="big">ADET-M{number:02}-LASTNAME</p><p>The instructor sets the real naming pattern and deadline. Write the actual class date in the README.</p><p class="mt">This activity uses template packages. No new npm install is required during class.</p>')),'Activity · submission')
def quizzes(questions):
    result=[]
    for offset in range(0,10,4):
        items=questions[offset:offset+4]
        result.append(slide(f'Quiz · items {offset+1}–{offset+len(items)}','<div class="q2">'+''.join(card(f'{offset+i+1}. {q}',f'<span class="opt">{opts}</span>' if opts else '<p class="mu">Write a short, precise answer.</p>') for i,(q,opts) in enumerate(items))+'</div><p class="caption">Individual · 1 point each · answers are kept in the separate instructor key.</p>','Assessment · 10-item quiz'))
    return result

decks={}
s=[]
s += [hero(2,'Screens, components &amp; lifecycle','What changes when a component updates—and what disappears when it is removed?',phone('Timer demonstration',['App state: active','Seconds: 3','[ Hide timer ]']))]
s += [slide('Trace the life of a screen',card('',diagram(['Mount','Update','Unmount']))+grid(card('Today you will…',bullets('Distinguish app, screen and component.','Trace state and effect cleanup.','Separate backgrounding from removal.')),card('Review M01','<p>A function returns a result. A React component returns the UI description. A setter asks React to render again.</p>')),'Lesson preview')]
s += [slide('Small components make a screen',grid(card('One app, several pieces','<pre class="tree">App\n ├─ App-state label\n ├─ Timer\n │   └─ Text\n └─ Show / Hide button</pre>'),card('In plain words','<p>A <b>component</b> describes part of the UI. A <b>screen</b> supports one user task. The <b>app</b> connects those screens and their behavior.</p><p class="mt">Android Activity is only an approximate comparison for a screen—not what this code creates directly.</p>')))]
s += [slide('State remembers; a setter requests an update',grid(code('const [seconds, setSeconds] = useState(0);\nsetSeconds((current) => current + 1);','Excerpt · read with the complete file',False),card('Follow the value',bullets('<code>seconds</code> holds the current count.','<code>setSeconds</code> schedules its next value.','The updater receives the previous count.','An ordinary local variable does not request a render.')))+card('Predict first','<p>Starting at 0, what value follows three delivered interval callbacks?</p>','mt'))]
s += [slide('Render, commit, then synchronize',card('',diagram(['Render','Commit','Effect setup']))+grid(card('Render and commit','<p>Render describes the UI. Commit applies the result. Effects synchronize with resources outside rendering.</p>'),card('Cleanup','<p>When dependencies change, old cleanup runs before new setup. On removal, cleanup releases the resource.</p><p class="mu mt">Development Strict Mode may probe setup and cleanup again.</p>')))]
s += [slide('One interval needs one cleanup',grid(code('useEffect(() => {\n  const intervalId = setInterval(\n    () => setSeconds((current) => current + 1),\n    1000\n  );\n  return () => clearInterval(intervalId);\n}, []);','Excerpt · Timer effect',False),card('Why these lines matter',bullets('<code>[]</code>: no reactive values to resynchronize here.','The return function releases this interval.','Starting an interval in render creates extra work.','Callbacks can be delayed; this is not an accurate clock.'))))]
s += [slide('Removing is different from hiding',grid(code('{visible && <Timer />}','Excerpt · conditional rendering',False),card('Predict first','<p>The counter shows 3. Set visible to false, then true. Does it return at 3 or 0?</p>'))+ '<div class="c mt">'+table(['Action','Tree','Result'],[['visible = false','Timer removed','Cleanup; state discarded'],['visible = true','New Timer mounted','Starts at 0'],['Hide pixels / navigation blur','May remain mounted','Do not assume state resets']])+'</div>')]
s += [slide('AppState observes the whole app',grid(card('Reported status',table(['Value','Meaning'],[['active','Foreground use'],['background','App moved to background'],['inactive','An iOS transition state']])),card('What this sample does NOT do',bullets('It does not pause the interval on backgrounding.','It does not measure exact elapsed time.','It cannot promise cleanup when the OS kills the process.'))))]
s += [slide('Prepare, paste, check, run',setup(2),'Install first')]
s += [slide('The complete lifecycle checkpoint','<div class="row">'+full(2)+card('Read in three parts',bullets('<b>Timer:</b> local count, interval, cleanup.','<b>App:</b> visible and appState values.','<b>UI:</b> conditionally include Timer and pass a press callback.')+'<p class="caption">Copy gets the entire file. Scroll inside the code panel; the explanation stays beside it.</p>','scroll-panel')+'</div>'+source_links(2),'Guided program')]
s += [slide('Observe the result deliberately',grid(card('Try these steps','<ol><li>Mount Timer; observe the count.</li><li>Remove it with Hide timer.</li><li>Show it again; expect 0 initially.</li><li>Background and return to the app.</li></ol>'),card('Where to inspect logs','<p>With a compatible app connected, press <code>j</code> in Expo and open <b>React Native DevTools → Console</b>.</p><p class="mt">Terminal forwarding varies. This is the documented route; actual device observation is still pending.</p>')))]
s += [slide('Parang entablado',grid(card('Analogy','<p>Itinatayo ang set: <b>mount</b>. Nagbabago ang eksena: <b>update</b>. Binabaklas ang set: <b>unmount</b>.</p><p class="mt">Cleanup returns borrowed equipment; state is the information kept by that mounted instance.</p>'),card('Ungraded change','<p>Rename the buttons “Remove timer” and “Mount timer”. Explain why those labels describe this code more precisely.</p>')))]
s += [slide('Fix the cause, not the symptom',grid(card('Count speeds up','<p>Inspect cleanup and whether intervals are created during render.</p>'),card('No logs','<p>Inspect DevTools connection and Console filters, not only the terminal.</p>'),card('State unexpectedly resets','<p>Check whether the component was removed and mounted again.</p>'),card('Background count looks wrong','<p>AppState only reports status; timers can be delayed or suspended.</p>')))]
s += [slide('What we covered',card('',diagram(['State','Render','Effect','Cleanup']))+card('Explain it back','<p>Why can a screen lose focus without losing state? Why does removing Timer reset its count?</p>','mt')+source_links(2,' · <a href="https://react.dev/reference/react/useEffect">Effect reference</a>'),'Recap')]
s += quizzes([
('What is a screen?','A. UI for one task<br>B. A database<br>C. A package manager<br>D. A cable'),
('When does an effect with [] set up?','A. Never<br>B. After initial commit, with possible development checks<br>C. Only on errors<br>D. Before Node starts'),
('What is the returned effect function called?','A. Cleanup<br>B. Reducer<br>C. Router<br>D. Manifest'),
('Which AppState value means background?','A. active<br>B. background<br>C. loading<br>D. paused-forever'),
('Which Android term loosely matches a screen?','A. Activity<br>B. Service<br>C. Content Provider<br>D. APK'),
('What happens to local useState values after unmount?',''),
('Which API reports whole-app foreground/background status?',''),
('Which debugging tool’s Console should show this app’s JavaScript logs?',''),
('Why clear an interval during cleanup?',''),
('Name the three component lifecycle phases.','')])
s += [prepare(3)]
decks[2]=s

s=[]
s += [hero(3,'Build a screen:<br>layout &amp; a form','Read typed input, apply one explicit validation rule, and explain the message.',phone('Form layout',['Login','[ Username ]','[ Password ]','[ LOG IN ]','Welcome, Virel!']))]
s += [slide('Type → state → press → message',card('',diagram(['Type','State','Press','Message']))+grid(card('Learning targets',bullets('Arrange View, Text, TextInput and Button.','Connect input values to state.','Explain the exact validation rule.')),card('Review M02','<p>State is remembered data for a mounted component. A setter causes the screen to reflect a new value.</p>')),'Lesson preview')]
s += [slide('Four building blocks',grid(card('View','<p>A container: groups and positions components.</p>'),card('Text','<p>Displays raw text nodes. Loose text belongs inside Text.</p>'),card('TextInput','<p>Reports what the user types and displays its value.</p>'),card('Button','<p>Accepts a string title and a callback for onPress.</p>'))+ '<p class="caption">String props such as Button.title are valid. The raw-text rule concerns children outside Text.</p>')]
s += [slide('Flexbox arranges the boxes',grid(card('',diagram(['Title','Fields','Button'])),card('Default direction: column',bullets('<code>justifyContent</code> follows the main axis.','<code>alignItems</code> crosses that axis.','Change to row and the axes change.','padding is inside space; gap separates children.')))+ '<p class="caption">StyleSheet gives repeated style objects names; it is not HTML or a CSS stylesheet.</p>')]
s += [slide('A controlled field keeps UI and data together',card('',diagram(['New string','setUsername','Render','value']))+grid(code('value={username}\nonChangeText={setUsername}','Excerpt · TextInput props',False),card('Predict first','<p>If onChangeText only logs the input, does username change?</p><p class="mt">No setter means no state update. A label changing elsewhere does not repair that connection.</p>')))]
s += [slide('The exact validation rule',grid(code('if (username.trim() === "" || password === "") {\n  setMessage("Enter both username and password.");\n  return;\n}\nsetMessage("Welcome, " + username.trim() + "!");','Excerpt · handleLogin body',False),card('Read each decision',bullets('Trim only the username.','Reject if either required test is empty.','Return stops the success line from replacing the error.','No account or server is checked.'))))]
s += [slide('Trace the edge cases',card('',table(['Username','Password','Expected result'],[['empty','empty','Enter both username and password.'],['three spaces','secret','Enter both username and password.'],['Virel','empty','Enter both username and password.'],['Virel','three spaces','Welcome, Virel!'],['Virel','secret','Welcome, Virel!']]))+card('Predict, then explain','<p>Why does a spaces-only password pass? The rule checks password === "", without trimming it.</p>','mt'))]
s += [slide('Prepare the form checkpoint',setup(3),'Install first')]
s += [slide('Complete program: copy once, then trace','<div class="row">'+full(3)+card('Find these connections',bullets('username ↔ its input.','password ↔ its input.','handleLogin → validation.','message → feedback Text.','StyleSheet → screen layout.')+'<p class="caption">Use invented credentials. This local demo is not authentication.</p>','scroll-panel')+'</div>'+source_links(3),'Guided program')]
s += [slide('Pass the callback; do not call it while rendering',grid(code('onPress={handleLogin}','Correct prop · excerpt',False),card('What happens on press?','<p>The native button invokes the function. It reads current state, chooses a branch and updates message. React then displays that message.</p>'))+card('Common mistake','<p><code>onPress={handleLogin()}</code> invokes the function during rendering instead of passing it for later.</p>','mt'))]
s += [slide('Hidden characters do not mean secure login',grid(card('secureTextEntry','<p>Obscures the displayed characters. It does not encrypt a password or verify an account.</p>'),card('Accessible input','<p>Use meaningful labels. A placeholder disappears when typing, so it is not a persistent visible label.</p>'))+card('Layout limitation','<p>A keyboard can cover this minimal centered form. Dismiss it to inspect feedback and record the issue; a production form needs fuller keyboard/layout testing.</p>','mt'))]
s += [slide('Optional: clear feedback after a delay',grid(code('useEffect(() => {\n  if (message === "") return;\n  const timeoutId = setTimeout(() => setMessage(""), 4000);\n  return () => clearTimeout(timeoutId);\n}, [message]);','Excerpt · optional effect',False),card('Which timer owns the message?',bullets('A new message cancels old scheduled work.','The new effect schedules its own timeout.','The same unchanged message does not restart it.','The delay is not a precise clock.')))+ '<p class="caption"><a href="../examples/M03/App.timeout.tsx">Complete optional file</a> · copy as App.tsx in a spare starter; React useEffect is included. No extra dependency.</p>','Optional ungraded comparison')]
s += [slide('Parang form sa registrar',grid(card('Analogy','<p>State ang nakasulat sa form. Validation ang guard na tumitingin kung kumpleto. Message ang malinaw na sagot.</p><p class="mt">Hindi pa ito pag-verify ng identity—kumpletong input lang ang sinusuri.</p>'),card('Troubleshoot',bullets('Text error: inspect raw text outside Text.','Typing fails: inspect value/setter pairing.','Error becomes success: inspect early return.'))))]
s += [slide('What we covered',card('',diagram(['Layout','Controlled input','Validation','Feedback']))+card('Explain it back','<p>Trace a spaces-only username through the function. Which line prevents the success message?</p>','mt')+source_links(3,' · <a href="https://reactnative.dev/docs/textinput">TextInput reference</a>'),'Recap')]
s += [slide('Your form, with one clear improvement',grid(card('One individual activity',bullets('Add showPassword / setShowPassword state.','Toggle visibility with secureTextEntry={!showPassword}.','Give an empty username its own clear message.','Keep the stated password rule unchanged.')),card('Evidence to capture',bullets('One successful form submission.','One empty/whitespace username failure.','A spaces-only password result.','Explain the branch and state update responsible.'))),'Activity · coding')]
s += [submission(3)]
s += [slide('Written alternative: explain the form',grid(card('Paper trace','<p>Trace empty fields, a spaces-only username, a spaces-only password and a normal pair. Show input → condition → message.</p>'),card('150–250 words','<p>Explain the early return and design the show-password state change. Describe what fails when an input updates the wrong setter.</p>'))+ '<p class="caption">This is the equal-point alternative if you cannot run the app, not an additional graded essay for students who complete the coding activity.</p>','Activity · written alternative')]
s += [slide('One activity, three delivery modes',modes()+'<div class="c mt">'+rubric+'</div>','Assessment · 10 points')]
s += [prepare(4)]
decks[3]=s

s=[]
s += [hero(4,'Reusable components,<br>readable screens','One OfficeCard definition, independent counts, and a layout that adapts.',phone('Reusable office cards',['Campus offices','Library: 0 / 2','[ Join Library ]','Clinic: 0 / 3','[ Join Clinic ]']))]
s += [slide('Reuse the design, keep the data clear',grid(card('Today you will…',bullets('Distinguish props from local state.','Trace two component instances.','Choose row/column from width and font scale.','Show status with text, not color alone.')),card('Review M03','<p>State changes the UI. Today we give each card its own state and receive configuration from its parent.</p>')),'Lesson preview')]
s += [slide('Props configure; state changes',card('',table(['Value','Owner / purpose','Example'],[['Props','Parent supplies settings','title, hours, capacity'],['Local state','Mounted card remembers data','visitors'],['Derived value','Calculated from current data','isFull = visitors >= capacity']]))+card('Common misconception','<p>A shared component function does not mean its instances share one count.</p>','mt'))]
s += [slide('A typed contract names the inputs',grid(code('type OfficeCardProps = {\n  title: string;\n  hours: string;\n  capacity: number;\n};','Excerpt · prop contract',False),card('Why name the types?',bullets('The parent must provide the required fields.','A number is expected for capacity.','Run tsc separately to find mismatched source types.','Types do not validate database values at runtime.'))))]
s += [slide('One definition, two separate instances',grid(card('Component tree','<pre class="tree">App\n ├─ OfficeCard: Library\n │   props: capacity 2\n │   state: visitors 0\n └─ OfficeCard: Clinic\n     props: capacity 3\n     state: visitors 0</pre>'),card('Predict first','<p>Press Join Library twice. Does Clinic change?</p><p class="mt">No. Each card owns a separate useState value.</p>')))]
s += [slide('Bound the count and explain the limit',grid(code('const isFull = visitors >= capacity;\n\nsetVisitors((current) =>\n  Math.min(current + 1, capacity)\n);','Excerpt · count logic',False),card('Three parts work together',bullets('Math.min bounds the next value.','disabled prevents the full queue action.','“Full — please wait” explains the state in words.'))))]
s += [slide('Responsive means adapting to available space',card('',table(['Width','Font scale','Our layout'],[['390','1.0','Column'],['800','1.0','Row'],['800','1.5','Column']]))+grid(code('const { width, fontScale } = useWindowDimensions();\nconst useColumns = width >= 700 && fontScale <= 1.3;','Excerpt · our design rule',False),card('Why include font scale?','<p>Larger text needs room. This threshold is our chosen rule, not a React Native default.</p>')))]
s += [slide('Accessibility needs more than a label',grid(card('Readable feedback',bullets('Use written status beside color.','Allow text scaling and flexible card height.','Let a taller screen scroll.')),card('Meaningful actions',bullets('Name the queue in each button label.','Keep heading structure understandable.','Test TalkBack/VoiceOver and larger text on a real device.')))+ '<p class="caption">These choices help accessibility; they do not certify the screen without testing.</p>')]
s += [slide('Prepare the reusable-card checkpoint',setup(4),'Install first')]
s += [slide('Complete reusable screen','<div class="row">'+full(4)+card('Read from top to bottom',bullets('OfficeCardProps names the settings.','OfficeCard owns visitors.','App supplies Library and Clinic props.','useWindowDimensions selects the arrangement.','ScrollView makes tall content reachable.')+'<p class="caption">Copy the whole file; use the next trace to check behavior.</p>','scroll-panel')+'</div>'+source_links(4),'Guided program')]
s += [slide('Follow just one card',card('',table(['Action','Library','Clinic'],[['Start','0','0'],['Join Library','1','0'],['Join Library again','2 — full','0'],['Attempt another Library join','2','0'],['Reset Library','0','0']]))+card('Predict the change','<p>What should Leave do at zero? It must stay at zero, not become negative.</p>','mt'))]
s += [slide('Optional: local images and a theme',grid(card('Bundled asset','<p>A local file such as assets/icon.png does not need a CDN. Give Image dimensions and a meaningful label when it conveys information.</p>'),card('Dark theme','<p>useColorScheme reports the preferred theme. Change foreground and background together, then check contrast.</p>'))+ '<p class="caption">Optional ungraded discussion; the assessed core has no image download or extra package.</p>')]
s += [slide('Parang dalawang queue counter',grid(card('Analogy','<p>Pareho ang disenyo, pero magkaiba ang pangalan at limit: props. Bawat counter may sariling bilang: state.</p><p class="mt">Kapag may pumila sa Library, hindi nadaragdagan ang Clinic.</p>'),card('Check these mistakes',bullets('Both counts move: inspect state ownership.','Text clips: inspect fixed heights and scrolling.','Wrong prop type: compare with the contract.'))))]
s += [slide('What we covered',card('',diagram(['Props','Instance state','Derived status','Layout']))+card('Explain it back','<p>Why can one OfficeCard function produce three independent counts? Which design choice helps large text?</p>','mt')+source_links(4,' · <a href="https://reactnative.dev/docs/accessibility">Accessibility reference</a>'),'Recap')]
s += [slide('Add a queue without copying the implementation',grid(card('One individual activity',bullets('Add Registrar with capacity 4 using OfficeCard.','Add Leave inside OfficeCard.','Decrease only that card’s count.','Never allow a value below zero.')),card('Verify and explain',bullets('Use a meaningful accessible Leave label.','Show normal join/leave and leave-at-zero cases.','Test narrow layout and enlarged text where available.','Explain props versus each instance’s state.'))),'Activity · coding')]
s += [submission(4)]
s += [slide('Written alternative: trace the queues',grid(card('Paper trace','<p>Trace Library, Clinic and Registrar through two joins, one leave and a leave at zero. Label each card’s independent state.</p>'),card('150–250 words','<p>Write a bounded decrement expression. Explain the width/font-scale rule and one accessibility improvement beyond color.</p>'))+ '<p class="caption">Equal-point alternative, not an extra assignment. Use the same success/edge-case reasoning as the coding route.</p>','Activity · written alternative')]
s += [slide('One assessment, equal points',modes()+'<div class="c mt">'+rubric+'</div>','Assessment · 10 points')]
s += [slide('Next: connect screens with navigation',grid(card('M05 is a quiz meeting','<p>Bring your notes on props and state. We will trace Home → Library → Back, then explain how routes connect screens.</p>'),card('Optional online Router preparation','<p>The next lesson supplies a separate Router extension with explicit packages and file layout. Its installation is optional; the core uses a template-only model.</p>'))+ '<p class="caption">Salamat! Explain the data first; reuse the component second.</p>','Before next meeting')]
decks[4]=s

s=[]
s += [hero(5,'Navigation &amp;<br>application structure','Find a screen, carry an ID and return safely.',phone('Navigation example',['Campus offices','[ Visit library ]','        ↓','Library — 8 AM','[ Back ]']))]
s += [slide('Trace a destination and its way back',card('',diagram(['Home','Push ID','Read ID','Office','Back']))+grid(card('Learning targets',bullets('Map route files to paths.','Distinguish stacks from tabs.','Handle unknown IDs.')),card('Two learning routes','<p>Core: a template-only stack model.<br>Optional: the real Expo Router extension.</p><p class="mt">The model is not a full navigation library.</p>')),'Lesson preview')]
s += [slide('A route file names a destination',grid(card('File map','<pre class="tree">app/\n ├─ _layout.tsx   shared navigator\n ├─ index.tsx     /\n └─ office/\n     └─ [id].tsx  /office/library</pre>'),card('Why brackets?', '<p><code>[id]</code> is a changing path segment. One detail component can display different offices.</p><p class="mt">A layout supplies shared navigation structure; it is not another office record.</p>')))]
s += [slide('Push adds; Back removes the top',card('',diagram(['[Home]','[Home, Library]','[Home]']))+grid(card('Push','<p>Add a destination to navigation history.</p>'),card('Back','<p>Return to the previous entry. Resetting to Home is a different operation.</p>')))]
s += [slide('Tabs select peer sections',grid(card('Stack example','<p>Home → office details → Back.</p><p class="mt">History tells us where to return.</p>'),card('Tab example','<p>Tasks ↔ Settings.</p><p class="mt">Changing focus need not unmount the earlier screen or erase its state.</p>')))]
s += [slide('An ID is input—not proof of a record',card('',diagram(['Read ID','Normalize','Look up','Show result']))+grid(card('Known ID','<p>library → Library — Open 8 AM.</p>'),card('Unknown ID','<p>unknown → Office not found.</p><p class="mt">A cold launch cannot assume a previous click supplied a full object.</p>')))]
s += [slide('Run the offline stack model',setup(5),'Install first · core model')]
s += [slide('Complete model: make history visible','<div class="row">'+full(5)+card('What this models',bullets('An array stores the destinations.','Spread appends an ID.','slice removes the last entry.','A guard keeps Home at the bottom.')+'<p class="mt">It has no native routing, external deep links or persisted history.</p>','scroll-panel')+'</div>'+source_links(5),'Guided program')]
s += [slide('Trace normal and missing destinations',card('',table(['Action','Stack','Screen'],[['Start','home','Home'],['Visit library','home → library','Library — Open 8 AM'],['Back','home','Home'],['Try unknown','home → unknown','Office not found']]))+card('Check the boundary','<p>At Home, Back is disabled. The model will not remove its last entry.</p>','mt'))]
s += [slide('Optional extension: install Router first',code('npx expo install expo-router react-native-safe-area-context react-native-screens expo-linking expo-constants expo-status-bar','Online only · in a separate SDK 58 blank project')+ '<div class="c mt">'+table(['Packages','Purpose'],[['expo-router','Routes and navigation'],['safe-area-context + screens','Native layout/screen support'],['expo-linking + expo-constants','Link and runtime support'],['expo-status-bar','Compatible status-bar package']])+'</div><p class="caption">Use the fresh-project command from the setup slide. Preserve the core offline starter. This extension is optional, not a quiz prerequisite.</p>','Optional · real Expo Router')]
s += [slide('Choose one entry and one route tree',grid(card('Configuration',bullets('package.json main: <code>expo-router/entry</code>.','app.json: add the expo-router plugin and scheme <code>adetlab</code>.','Include all app/**/*.tsx files in the strict TypeScript check.')),card('Files','<pre class="tree">ADET-M05-LASTNAME/\n package.json\n app.json\n tsconfig.json\n app/\n  _layout.tsx\n  index.tsx\n  office/[id].tsx</pre>'))+ '<p class="caption">App.tsx is unused in this separate Router extension. <a href="../examples/M05/router-extension/README.md">Complete setup and configuration guide</a>.</p>')]
layout=(root/'examples/M05/router-extension/app/_layout.tsx').read_text(encoding='utf-8')
home=(root/'examples/M05/router-extension/app/index.tsx').read_text(encoding='utf-8')
detail=(root/'examples/M05/router-extension/app/office/[id].tsx').read_text(encoding='utf-8')
s += [slide('The layout supplies the stack',grid(code(layout,'app/_layout.tsx · complete file',source='../examples/M05/router-extension/app/_layout.tsx'),card('One job','<p>Return the Stack navigator. Each route is displayed inside this shared navigation structure.</p><p class="mt">Keep this file small so screen code stays in its own route.</p>')),'Router file 1 of 3')]
s += [slide('Home pushes a destination','<div class="row">'+code(home,'app/index.tsx · complete file',source='../examples/M05/router-extension/app/index.tsx')+card('Read the callback',bullets('The button passes a function.','The function calls router.push.','The path supplies library or unknown as the ID.','Stack.Screen sets this screen’s title.'),'scroll-panel')+'</div>','Router file 2 of 3')]
s += [slide('Detail checks the ID before displaying it','<div class="row">'+code(detail,'app/office/[id].tsx · complete file',source='../examples/M05/router-extension/app/office/[id].tsx')+card('Trace the lookup',bullets('Normalize a possible array parameter.','Check that offices owns the key.','Render the record or the missing message.','Use Back when history exists; otherwise offer Home.'),'scroll-panel')+'</div>','Router file 3 of 3')]
s += [slide('Links and guards have boundaries',grid(card('Deep link','<p>A URL can open a destination directly. In-app navigation can use compatible Expo Go; a custom installed scheme requires a build containing that native configuration.</p>'),card('Guard ≠ authorization','<p>A redirect helps users navigate. The server still decides whether a request may access protected data.</p><p class="mt">Keep passwords and tokens out of routes.</p>'))+ '<p class="caption">Real-device links and navigation have not been tested here. Bundle generation alone does not establish their behavior.</p>')]
s += [slide('Parang room number ang route',grid(card('Analogy','<p>Ang ID ay room number, hindi ang buong opisina. History ang dinaanan mo para makabalik.</p><p class="mt">Kapag mali ang number, sabihin na hindi nahanap—huwag magpakita ng ibang opisina.</p>'),card('Troubleshoot',bullets('Old App.tsx appears: inspect main.','Unmatched route: inspect the file tree.','Unknown ID crashes: validate the lookup.','No history: offer a Home fallback.'))))]
s += [slide('What we covered',card('',diagram(['Route','Parameter','Lookup','History']))+card('Explain it back','<p>How do a route ID, component state and navigation history differ? Why is a client-side guard insufficient security?</p>','mt')+source_links(5,' · <a href="https://docs.expo.dev/router/installation/">Router installation reference</a>'),'Recap')]
s += quizzes([
('A route is…','A. A destination path<br>B. A password<br>C. A database<br>D. A font'),
('Which file supplies the shared navigator?','A. package-lock.json<br>B. app/_layout.tsx<br>C. README.md<br>D. assets/icon.png'),
('Which filename accepts changing office IDs?','A. office.txt<br>B. [id].tsx<br>C. icon.png<br>D. app.json'),
('A tab usually represents…','A. A peer section<br>B. A timer<br>C. A password<br>D. A compiler error'),
('Does a route guard replace server authorization?','A. Always<br>B. No; it controls navigation feedback<br>C. Only offline<br>D. Only on iOS'),
('Trace [Home], push Library, then Back. What remains?',''),
('An unknown ID arrives. What should this example display?',''),
('Must losing focus unmount a screen? Explain.',''),
('Can the template-only model open an external deep link? Explain.',''),
('With no previous history, what safe navigation option is provided?','')])
s += [prepare(6)]
decks[5]=s

runtime=r'''
(()=>{
const slides=[...document.querySelectorAll('.s')],bar=document.querySelector('#bar'),counter=document.querySelector('#ctr'),help=document.querySelector('#help');let index=0,scale=1;
try{scale=Number(localStorage.getItem('adet-text-scale'))||1}catch{}
function label(){counter.textContent=`${index+1} / ${slides.length}${scale!==1?' · '+Math.round(scale*100)+'%':''}`}
function show(next){index=Math.max(0,Math.min(slides.length-1,next));slides.forEach((slide,n)=>{slide.classList.toggle('on',n===index);slide.classList.toggle('prev',n<index);slide.setAttribute('aria-hidden',String(n!==index));slide.inert=n!==index});slides[index].scrollTop=0;bar.style.width=`${(index+1)/slides.length*100}%`;label()}
function resize(delta){scale=delta===0?1:Math.min(2,Math.max(.8,Math.round((scale+delta)*100)/100));document.documentElement.style.setProperty('--scale',scale);try{localStorage.setItem('adet-text-scale',String(scale))}catch{}label()}
document.addEventListener('keydown',event=>{if(event.ctrlKey||event.metaKey){if(['+','=','-','0'].includes(event.key)){event.preventDefault();resize(event.key==='0'?0:event.key==='-'?-.1:.1)}return}if(event.key==='ArrowRight'){event.preventDefault();show(index+1)}else if(event.key==='ArrowLeft'){event.preventDefault();show(index-1)}else if(event.key==='Home'){event.preventDefault();show(0)}else if(event.key==='End'){event.preventDefault();show(slides.length-1)}else if(event.key==='?')help.classList.toggle('on');else if(event.key==='Escape')help.classList.remove('on')});
document.addEventListener('contextmenu',event=>{event.preventDefault();show(index+1)});
for(const name of ['mousedown','mouseup','auxclick'])window.addEventListener(name,event=>{if(event.button===3||event.button===4){event.preventDefault();event.stopImmediatePropagation();if(name==='mousedown')show(index+(event.button===3?1:-1))}},true);
window.addEventListener('wheel',event=>{if(event.ctrlKey||event.metaKey){event.preventDefault();resize(event.deltaY<0?.1:-.1)}},{passive:false});
let touchX=0,touchY=0;document.addEventListener('touchstart',event=>{touchX=event.touches[0].clientX;touchY=event.touches[0].clientY},{passive:true});document.addEventListener('touchend',event=>{const dx=event.changedTouches[0].clientX-touchX,dy=event.changedTouches[0].clientY-touchY;if(Math.abs(dx)>70&&Math.abs(dx)>Math.abs(dy)*1.5&&!event.target.closest('pre'))show(index+(dx<0?1:-1))},{passive:true});
const esc=value=>value.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
function highlight(source){const regex=/(\/\/[^\n]*)|("[^"\n]*"|'[^'\n]*'|`[^`]*`)|(\b(?:import|from|export|default|function|const|let|for|of|if|else|return|type|undefined|true|false)\b)|(\b\d+\b)|(\b[A-Za-z_]\w*(?=\())/g;let output='',last=0,match;while((match=regex.exec(source))){output+=esc(source.slice(last,match.index));const cls=match[1]?'cm':match[2]?'st':match[3]?'kw':match[4]?'nu':'fn';output+=`<span class="${cls}">${esc(match[0])}</span>`;last=regex.lastIndex}return output+esc(source.slice(last))}
async function copyText(source){if(navigator.clipboard){try{await navigator.clipboard.writeText(source);return true}catch{}}const area=document.createElement('textarea');area.value=source;area.style.cssText='position:fixed;left:-9999px';document.body.append(area);area.select();let success=false;try{success=document.execCommand('copy')}catch{}area.remove();return success}
document.querySelectorAll('.code,.snippet').forEach(panel=>{const pre=panel.querySelector('pre'),source=pre.textContent.replace(/\n+$/,''),header=document.createElement('header'),name=document.createElement('span');name.textContent=panel.dataset.n;header.append(name);panel.prepend(header);pre.innerHTML=highlight(source);pre.tabIndex=0;pre.setAttribute('aria-label',panel.dataset.n+'; scroll to read');if(panel.classList.contains('code')){const button=document.createElement('button');button.className='cp';button.textContent='Copy';button.setAttribute('aria-label','Copy '+panel.dataset.n);header.append(button);button.addEventListener('click',async()=>{const success=await copyText(source);button.textContent=success?'Copied!':'Select code to copy';button.classList.toggle('d',success);setTimeout(()=>{button.textContent='Copy';button.classList.remove('d')},1800)})}});
resize(0);try{scale=Number(localStorage.getItem('adet-text-scale'))||1}catch{}document.documentElement.style.setProperty('--scale',scale);show(0);
})();
'''
# Python raw text contains escaped regex backslashes intended for JS; normalize only doubled slashes.
runtime=runtime.replace('\\\\','\\')

chrome='<div id="frame"><i></i><i></i><i></i><i></i></div><div id="bar"></div><div id="ctr" aria-live="polite"></div><div id="help"><div><h3>Keyboard shortcuts</h3><p>→ / right-click / Mouse4: next<br>← / Mouse5: previous<br>Home / End: first / last<br>Ctrl + / − / 0: text size<br>? / Escape: help · swipe on touchscreens</p></div></div>'
manifest=[]
for number,slides in decks.items():
    assert len(slides)<=25
    title=f'ADET M{number:02} · '+re.sub('<[^>]+>','',re.search(r'<h1>(.*?)</h1>',slides[0]).group(1))
    document='<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>'+css+scroll+extras+'</style></head><body>'+chrome+'\n'+'\n'.join(slides)+'\n<script>'+runtime+'</script></body></html>'
    (here/f'ADET_M{number:02}_slides.html').write_text(document,encoding='utf-8')
    manifest.append({'module':number,'slides':len(slides),'file':f'ADET_M{number:02}_slides.html'})

# Only scrollbar styling changes in the user's two reference files; keep exact originals.
backup=root/'instructor/presentation-backup-2026-11-07'
backup.mkdir(parents=True,exist_ok=True)
for number in [0,1]:
    path=here/f'ADET_M{number:02}_slides.html'
    original=path.read_text(encoding='utf-8')
    if 'ADET themed scrollbars' not in original:
        shutil.copy2(path,backup/path.name)
        path.write_text(original.replace('</style>',scroll+'\n</style>',1),encoding='utf-8')
(here/'deck-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps(manifest,indent=2))
