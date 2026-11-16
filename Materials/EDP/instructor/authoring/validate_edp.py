from pathlib import Path
import subprocess,json,re
from urllib.parse import unquote
root=Path('Application Development and Emerging Technologies (Inluding event Driven programming)/EDP')
ex=root/'examples'
checks={
'm01.mjs':['Total: 60','Taking the next order','Ready na ang order!'],
'm01-types.ts':['A1: PHP 60'],
'm02.mjs':['A: synchronous start','B: synchronous end','C: promise callback','D: timer callback','Ready: A1','Handled: Unavailable: A2','Preparation finished'],
'm04.mjs':['Invoice: A1','Kitchen: A1','First order bonus','Kitchen: A2','Handled: Printer offline','Ready: A2','Remaining: 0'],
'm05.mjs':['Cancelled: old','Show: NEW','Debounced: canteen'],
'm06.ts':['Invoice: A1 60','Bad payload accepted: false'],
'm07.mjs':['Rejected: collect in waiting','waiting -> preparing','preparing -> ready','ready -> collected','Rejected: collect in collected'],
'm08.mjs':['Results: CANTEEN','Handled: Search unavailable','Search subscription closed'],
'm10.mjs':['Saved: ORDER A1','Saved: ORDER A2','Saved: ORDER A3','Pipeline complete'],
'm10-worker.mjs':['Main thread remains available','Worker result: 500000500000'],
'm12.mjs':['Queue: Kitchen 1 A1','Queue: Kitchen 2 A2','PubSub: Invoice A1','PubSub: Analytics A1','Replay: archive ready:A1,collected:A1'],
'm13.mjs':['Applied: A1 attempt 2','Duplicate: A1','Total: 60 Dead letters: 1'],
'm14.mjs':['Commit cancelled','Received: A1','Duplicate ignored: event-A1','Orders: 1 Pending: 0'],
'm15.mjs':['Rebuilt stock: 8','From snapshot: 8','Replay again: 8'],
'm16.mjs':['Reserved: A1','Compensated: A1','Reserved: A2','Confirmed: A2','Active reservations: 1'],
'm17.mjs':['"outcome":"accepted"','"outcome":"rejected"','Metrics: {"accepted":1,"rejected":1}'],
'm18.mjs':['Handled: Invalid transition','Events: 2','Listeners: 0'],
'm19.mjs':['Calls: 1','Input accepted: false','Listener count: 0'],
'm20.mjs':['PASS two orders','PASS first ready','PASS three domain events','PASS listeners cleaned']
}
results=[]
for file,expected in checks.items():
 p=subprocess.run(['node',file],cwd=ex,capture_output=True,text=True,encoding='utf-8',timeout=15)
 assert p.returncode==0,(file,p.stderr)
 cursor=0
 for line in expected:
  pos=p.stdout.find(line,cursor)
  assert pos>=0,(file,line,p.stdout)
  cursor=pos+len(line)
 assert 'SHOULD NOT RUN' not in p.stdout
 results.append({'file':file,'passed':True,'stdout':p.stdout})
modules=list((root/'modules').glob('EDP_M*.md'))
assert len(modules)==20
for p in modules:
 s=p.read_text(encoding='utf-8'); i=int(p.stem[-2:])
 assert all(x in s for x in ['## A.','## B.','## C.','## D.'])
 if i%2:
  quiz=s.split('### 10-item quiz')[1].split('### Wrap-up')[0]
  assert len(re.findall(r'^\d+\. ',quiz,re.M))==10,(p,'quiz count')
 for name,lang,code in re.findall(r'### File: `([^`]+)`.*?```(\w+)\n(.*?)```',s,re.S):
  assert code==(ex/name).read_text(encoding='utf-8'),(p,name,'code drift')
 # Validation report is authored after these checks, so allow that one pending link.
 for link in re.findall(r'\]\(([^)]+)\)',s):
  if not link.startswith('http') and not link.endswith('/VALIDATION.md'):
   assert (p.parent/unquote(link)).exists(),(p,link)
(root/'instructor/console-results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(f'{len(checks)} entry points passed output/order assertions; 20 module structures, embedded-code equality and 100 quiz items checked.')
print('Total module words:',sum(len(p.read_text(encoding='utf-8').split()) for p in modules))
