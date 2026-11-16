"""Run against a new disposable loopback mongod and API, never an existing database."""
import json,os,socket,subprocess,tempfile,time,urllib.request,urllib.error,sys
from pathlib import Path
api=Path(__file__).resolve().parents[1]/'examples/api'
def port():
 with socket.socket() as sock:
  sock.bind(('127.0.0.1',0))
  return sock.getsockname()[1]
dbport,webport=port(),port()
def call(method,path,body=None):
 req=urllib.request.Request(f'http://127.0.0.1:{webport}'+path,method=method,data=json.dumps(body).encode() if body is not None else None,headers={'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req,timeout=2) as r:
   raw=r.read()
   return r.status,json.loads(raw) if raw else None
 except urllib.error.HTTPError as err: return err.code,None
with tempfile.TemporaryDirectory() as tmp:
 with open(Path(tmp)/'mongo.log','w') as log:
  db=subprocess.Popen([sys.argv[1],'--bind_ip','127.0.0.1','--port',str(dbport),'--dbpath',tmp],stdout=log,stderr=log)
  server=None
  try:
   server=subprocess.Popen(['node','api.mjs'],cwd=api,env={**os.environ,'PORT':str(webport),'LAB_HOST':'127.0.0.1','MONGO_URI':f'mongodb://127.0.0.1:{dbport}'})
   for _ in range(80):
    try:
     if call('GET','/tasks')==(200,[]):break
    except OSError:pass
    time.sleep(.25)
   else:raise RuntimeError('Temporary API did not start')
   assert call('POST','/tasks',{'title':' '})[0]==422
   status,row=call('POST','/tasks',{'title':' Lab '})
   assert status==201 and row['title']=='Lab' and row['done']==False
   path='/tasks/'+row['id']
   assert call('PATCH',path,{'done':'yes'})[0]==422
   assert call('PATCH',path,{'done':True})[1]['done']
   assert call('GET','/tasks')[1][0]['done']
   assert call('DELETE',path)[0]==204
   assert call('DELETE',path)[0]==404
   assert call('GET','/suggest')[1]['tip']
   print('PASS: MongoDB CRUD, validation, missing record and helper')
  finally:
   for child in [server,db]:
    if child:
     child.terminate()
     child.wait(timeout=12)
