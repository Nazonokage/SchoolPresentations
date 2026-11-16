from pathlib import Path
from urllib.request import urlopen
import json,xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
out=Path(__file__).resolve().parents[2]/'visuals/assets'
out.mkdir(parents=True,exist_ok=True)
def download(name):
 url=f'https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/{name}/{name}-original.svg'
 with urlopen(url,timeout=15) as response:
  data=response.read()
  assert response.status==200 and ET.fromstring(data).tag.endswith('svg')
 (out/(name+'.svg')).write_bytes(data)
 return {'name':name,'source':url,'local':'assets/'+name+'.svg','status':200}
records=list(ThreadPoolExecutor(5).map(download,['react','typescript','fastapi','mongodb','mysql']))
with urlopen('https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/LICENSE',timeout=15) as response:
 (out/'LICENSE.txt').write_bytes(response.read())
(out.parent/'image-sources.json').write_text(json.dumps(records,indent=2))
print('Verified and cached',len(records),'SVG assets')
