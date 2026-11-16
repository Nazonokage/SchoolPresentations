from pathlib import Path
import os,tempfile,sys,asyncio
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'examples/api'))
import httpx
with tempfile.TemporaryDirectory() as tmp:
 os.environ['DATABASE_URL']='sqlite:///'+(Path(tmp)/'qa.db').as_posix()
 import main
 async def check():
  async with httpx.AsyncClient(transport=httpx.ASGITransport(app=main.app),base_url='http://lab') as c:
   assert (await c.get('/tasks')).json()==[]
   assert (await c.post('/tasks',json={'title':' '})).status_code==422
   new=await c.post('/tasks',json={'title':' Study '})
   assert new.status_code==201
   record=new.json()
   assert record['title']=='Study' and record['done'] is False
   path='/tasks/'+record['id']
   assert (await c.patch(path,json={'done':'yes'})).status_code==422
   assert (await c.patch(path,json={'done':True})).json()['done']
   main.engine.dispose()
   assert (await c.get('/tasks')).json()[0]['done']
   assert (await c.delete(path)).status_code==204
   assert (await c.delete(path)).status_code==404
   assert (await c.get('/suggest')).json()['tip']
 asyncio.run(check())
 main.engine.dispose()
 print('PASS: create/read/update/delete, invalid payloads, reconnect, missing record, suggestion')
