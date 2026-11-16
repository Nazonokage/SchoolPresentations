from pathlib import Path
import re, json
from urllib.parse import unquote
here=Path(__file__).resolve().parent
base=here.parent.parent
issues=[]
records=[]
for number in range(6):
    path=base/f'modules/ADET_M{number:02}.md'
    text=path.read_text(encoding='utf-8')
    for section in ['## A.', '## B.', '## C.', '## D.', '### Instructor notes']:
        if section not in text: issues.append(f'{path.name}: missing {section}')
    if '### In plain words' not in text or '### Common mistakes' not in text:
        issues.append(f'{path.name}: plain-language/mistakes headings missing')
    if number in [0,2,5]:
        assessment=text.split('### 10-item quiz',1)[1].split('**Wrap-up',1)[0]
        questions=re.findall(r'^\s*(\d+)\. ',assessment,re.M)
        if questions!=[str(n) for n in range(1,11)]: issues.append(f'{path.name}: quiz numbers {questions}')
    else:
        for mode in ['Mode 1','Mode 2','Mode 3']:
            if mode not in text: issues.append(f'{path.name}: missing {mode}')
    for line in text.splitlines():
        if line.startswith('npx create-expo-app') and '--template blank-typescript@sdk-58 --no-agents-md' not in line:
            issues.append(f'{path.name}: unpinned command')
    if re.search(r'\*\*Answer key',text): issues.append(f'{path.name}: inline answer key')
    if number:
        block=re.search(r'```tsx\n(.*?)\n```',text,re.S).group(1)
        example=(base/f'examples/M{number:02}/App.tsx').read_text(encoding='utf-8').strip()
        if block.strip()!=example: issues.append(f'{path.name}: source mismatch')
    records.append({'module':f'M{number:02}','evidence':'coding' if number in [1,3,4] else '10-item quiz','sourceMatches':number!=0})

files=[base/'README.md',base/'modules/README.md',base/'examples/README.md',base/'instructor/TEACHING_GUIDE.md',base/'instructor/OPENER_ANSWER_KEY.md',here/'CHANGELOG.md',here/'VALIDATION.md']
files += [base/f'modules/ADET_M{n:02}.md' for n in range(6)]
files += list((base/'examples/M05/router-extension').glob('*.md'))
for path in files:
    text=path.read_text(encoding='utf-8')
    for match in re.finditer(r'\[[^\]\n]*\]\(([^)\n]+)\)',text):
        target=unquote(match.group(1).split('#')[0])
        if not target or re.match(r'https?://',target): continue
        if target=='static-check.json': continue # this run writes it below
        if not (path.parent/target).exists(): issues.append(f'{path.relative_to(base)}: broken link {target}')
index=(base/'modules/README.md').read_text(encoding='utf-8')
index_ids=re.findall(r'\[M(\d{2}) ·',index)
if index_ids!=[f'{n:02}' for n in range(22)]:issues.append(f'Index IDs: {index_ids}')
result={'date':'2026-11-07','modules':records,'indexRows':len(index_ids),'issues':issues,'scope':'Updated opener and supporting links only; later-module full consistency remains pending.'}
(here/'static-check.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
raise SystemExit(bool(issues))
