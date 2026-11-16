from pathlib import Path
import json,html
root=Path(__file__).resolve().parents[2]
rows=[
 ['Campus budget','Baon: PHP 50','Kulang: 10','Try changing the budget'],
 ['Campus offices','Library: 2 visits','Clinic: 0 visits','Visit'],
 ['Campus dashboard','Registrar','Library','Try a wider window'],
 ['New task','Bring library card','18 characters','Saved: Bring library card'],
 ['Campus offices','Visit library','Library • Open 8 AM','Back'],
 ['Campus tasks','Filter: lib','Library ✓','Edit Library'],
 ['Campus announcements','Load campus tasks','No tasks yet','Server returned an empty list'],
 ['Shared tasks','Library visit ✓','Finish / Delete','Refresh'],
 ['Offline draft','Bring ID','Save draft / Restore','Loaded'],
 ['Server state','Server count: 1','Add visit','Refetch after success'],
 ['Local session model','login   read   logout','Denied','Ben owns this record'],
 ['Report a chair','Take campus photo','Camera denied','Continue without a photo'],
 ['Study reminder','Schedule local reminder','Scheduled','Observe delivery on device'],
 ['Study meetup','Share study meetup','Open Iloilo map','Returned to app'],
 ['Study timer sound','playing','Play cue / Pause','Visible status follows playback'],
 ['Study suggestion','Get a study suggestion','Offline fallback','Review your unfinished task'],
 ['Boundary checks','Case 1: PASS','Case 2: PASS','Case 3: PASS'],
 ['My campus errands','Show unfinished','Library visit','Refresh after restart'],
 ['Form rehearsal','Input: three spaces','Check','Rejected'],
 ['Final rehearsal','Clean launch ✓','Failure and recovery ✓','Rehearsed 2/5']
]
icons={1:['react','typescript'],2:['react'],6:['typescript'],8:['fastapi','mysql','mongodb'],16:['fastapi']}
for i,(title,*lines) in enumerate(rows,1):
 n=f'{i:02d}';e=html.escape
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 390" role="img" aria-labelledby="t d"><title id="t">{e(title)}</title><desc id="d">Illustrated screen: {e(", ".join(lines))}</desc><rect width="640" height="390" rx="18" fill="#e2eee9"/><rect x="38" y="24" width="564" height="340" rx="24" fill="#fff" stroke="#315f57" stroke-width="4"/><text x="66" y="75" font-family="sans-serif" fill="#183e38" font-size="30">{e(title)}</text>'
 for j,line in enumerate(lines):
  y=132+64*j
  svg+=f'<rect x="64" y="{y-33}" width="508" height="50" rx="10" fill="#eef5f2"/><text x="82" y="{y}" font-family="sans-serif" fill="#183e38" font-size="23">{e(line)}</text>'
 svg+='<text x="66" y="337" font-family="sans-serif" fill="#365951" font-size="18">Illustrative classroom wireframe</text></svg>'
 (root/'visuals'/f'M{n}-screen.svg').write_text(svg,encoding='utf8')
 p=root/'modules'/f'ADET_M{n}.md';s=p.read_text(encoding='utf8')
 block='![Illustration of '+title+f'](../visuals/M{n}-screen.svg)\n\n*Sample screen illustration.* '+lines[-1]+'. Place beside the code, then replace with a student device capture after running the checkpoint.\n\n'
 if i in icons:block+=' '.join(f'<img src="../visuals/assets/{name}.svg" width="36" height="36" alt="{name} logo">' for name in icons[i])+'\n\n'
 s=s.replace('## C. Analogy, Guided Program & Practice',block+'## C. Analogy, Guided Program & Practice')
 walk=json.loads((Path(__file__).parent/'walkthroughs.json').read_text(encoding='utf8'))[i-1]
 s=s.replace('### Curriculum connections','### Work through the behavior\n\n'+walk+'\n\n### Curriculum connections')
 p.write_text(s,encoding='utf8')
