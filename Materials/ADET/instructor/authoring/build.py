"""Refresh student Markdown and original lesson figures from the reviewed outline and examples."""
from pathlib import Path
import json,re,html,textwrap
root=Path(__file__).resolve().parents[2]
data=json.loads((Path(__file__).parent/'lesson-data.json').read_text(encoding='utf8'))
outline=(root/'ADET_compiled contents.md').read_text(encoding='utf8')
parts=re.split(r'^## Module (\d+): (.+)$',outline,flags=re.M)
def save(name,value):
 p=root/name
 p.parent.mkdir(exist_ok=True,parents=True)
 p.write_text(value,encoding='utf8')
index='# ADET teaching modules\n\n[Example setup](../examples/README.md) · [Instructor guide](../instructor/TEACHING_GUIDE.md) · [Visual guide](../visuals/README.md)\n\n| Period | Lesson | Classroom evidence |\n|---|---|---|\n'
keys='# Instructor answer key and coding criteria\n\nAward one point per quiz answer. Accept equivalent explanations. M01 is diagnostic. Instructor distribution only.\n'
for j,row in enumerate(data['lessons']):
 n=j+1
 number=f'{n:02d}'
 assert int(parts[1+3*j])==n
 title=parts[2+3*j].strip()
 section=parts[3+3*j].split('## Source coverage')[0]
 focus=re.search(r'\*\*In a nutshell:\*\* (.+)',section)[1]
 topics=re.findall(r'^### [^\n]+\n+([^\n]+)',section,re.M)
 hook,lesson,deep,analogy,expected,task,repair,flow,url=row
 period='Prelim' if n<=5 else 'Midterm' if n<=11 else 'Pre-final' if n<=18 else 'Finals'
 quiz=n%2==1
 assessment='10-item quiz' if quiz else 'Individual coding activity'
 index+=f'| {period} | [M{number} · {title}](ADET_M{number}.md) | {assessment} |\n'
 steps=flow.split(' → ')
 esc=html.escape
 svg='<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="t d" viewBox="0 0 800 420"><title id="t">'+esc(title)+'</title><desc id="d">'+esc(flow)+'</desc><rect width="800" height="420" rx="20" fill="#11263b"/>'
 for ix,step in enumerate(steps):
  y=54+80*ix
  svg+=f'<circle cx="60" cy="{y}" r="23" fill="#97e5d3"/><text x="60" y="{y+8}" text-anchor="middle" font-family="sans-serif" font-size="24">{ix+1}</text><text x="112" y="{y+9}" fill="white" font-family="sans-serif" font-size="30">{esc(step)}</text>'
  if ix<3:svg+=f'<path d="M60 {y+26} v22 l-5 -6 m5 6 l5 -6" stroke="#97e5d3" fill="none" stroke-width="3"/>'
 svg+=f'<text x="40" y="392" fill="#97e5d3" font-family="sans-serif" font-size="22">ADET · Module {number} · Follow the change</text></svg>'
 save(f'visuals/M{number}.svg',svg)
 msg=f'# ADET M{number} · {title}\n\n[Module index](README.md) · {period} · 60–90 minutes · {assessment}\n\n## A. Lesson Preview & Review\n\n**{hook}** {focus}\n\nBy the end, trace **{flow}**, run the checkpoint, and explain this result in your own words: {expected}\n\n## B. Detailed Main Lesson\n\n{lesson}\n\n{deep}\n\n### Curriculum connections\n\n'
 msg+='\n'.join('- '+t for t in topics)+'\n\nUse the working screen first. Use the remaining comparisons for discussion or the extra 30 minutes.\n\n'
 msg+=f'![{flow}](../visuals/M{number}.svg)\n\n*Figure {n}.* {flow}. Show the first stage on the concept slide and ask students to predict the last. On the demonstration slide, place the example beside its actual output. For projector sizing see the [visual guide](../visuals/README.md).\n\n## C. Analogy, Guided Program & Practice\n\n{analogy}\n\n**Run it.** Follow the [Expo setup](../examples/README.md). From the examples folder select this checkpoint:\n\n```powershell\nnode select.mjs {number}\ncd mobile\nnpm start -- --clear\n```\n\n'
 if n in [7,8,10,16,18]:msg+='Start one [database API](../examples/api/README.md) and configure EXPO_PUBLIC_API_URL before opening the app.\n\n'
 if n==15:msg+='The selector copies the supplied [original local sound](../examples/M15/tone.wav) next to App.tsx.\n\n'
 for p in sorted((root/'examples'/f'M{number}').glob('*.tsx')):
  msg+=f'**{p.name}** · [Example file](../examples/M{number}/{p.name.replace("[","%5B").replace("]","%5D")})\n\n```tsx\n'+p.read_text(encoding='utf8').strip()+'\n```\n\n'
 msg+=f'**Expected behavior.** {expected}\n\n**Independent change.** {task}\n\n**Troubleshooting.** {repair}\n\n## D. Assessment, Wrap-Up & References\n\n'
 keys+=f'\n## M{number} · {title}\n\n'
 if quiz:
  qa=data['quizzes'][j//2];assert len(qa)==20
  msg+='### 10-item quiz\n\nGive a short answer for each item. The guided change above is ungraded.\n\n'
  for k in range(0,20,2):
   msg+=f'{k//2+1}. {qa[k]}\n';keys+=f'{k//2+1}. {qa[k+1]}\n'
 else:
  msg+='### One individual coding activity\n\n'+task+' Submit the modified source, exact run command, one successful result and one edge or failure result. Explain the line responsible for the difference.\n\n| Evidence | Points |\n|---|---:|\n| Working core and independent change | 4 |\n| Meaningful edge case and response | 2 |\n| Explain data flow and your own change | 2 |\n| Reproducible setup and readable source | 2 |\n'
  keys+=f'Look for this observed behavior: {expected} Required independent work: {task} Use the four criteria in the student sheet. An unchanged sample earns no independent-change credit.\n'
 msg+=f'\n**Wrap-up.** Explain how the program moves from “{steps[0]}” to “{steps[-1]}”. Name the layer you would inspect if the expected result disappeared.\n\n[Technical reference]({url}) · [Research notes and corrections](../adet%20research%20folder%20JS/TECHNICAL_REVIEW.md)\n'
 save(f'modules/ADET_M{number}.md',msg)
save('modules/README.md',index)
save('instructor/ANSWER_KEY.md',keys)
