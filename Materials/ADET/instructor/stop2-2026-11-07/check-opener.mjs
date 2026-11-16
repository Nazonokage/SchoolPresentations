import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn, spawnSync } from 'node:child_process';
const here = path.dirname(fileURLToPath(import.meta.url));
const base = path.resolve(here, '../..');
const cwd = path.join(base, 'offline-lab/starter');
const original = fs.readFileSync(path.join(cwd, 'App.tsx'));
const cases = [
  ['M01','M01/App.tsx','Hello, ADET!'],
  ['M02','M02/App.tsx','Timer mounted'],
  ['M03','M03/App.tsx','Enter both username and password.'],
  ['M04','M04/App.tsx','Space available'],
  ['M05','M05/App.tsx','Navigation paper-model companion'],
  ['M03-timeout','M03/App.timeout.tsx','Enter both username and password.'],
];
const results = [];
try {
  for (const [name, relative, marker] of cases) {
    fs.copyFileSync(path.join(base,'examples',relative), path.join(cwd,'App.tsx'));
    const check = spawnSync(process.execPath,['node_modules/typescript/bin/tsc','--noEmit'],{cwd,encoding:'utf8',windowsHide:true});
    fs.writeFileSync(path.join(here,`${name}-typecheck.log`),(check.stdout??'')+(check.stderr??''));
    let log='', bundle=false, error='';
    const port = 8291 + results.length;
    const child=spawn(process.execPath,['node_modules/expo/bin/cli','start','--offline','--port',String(port)],{cwd,env:{...process.env,CI:'1'},windowsHide:true});
    child.stdout.on('data',chunk=>log+=chunk); child.stderr.on('data',chunk=>log+=chunk);
    try {
      let ready=false;
      for (let attempt=0;attempt<45;attempt++) {
        try { const response=await fetch(`http://127.0.0.1:${port}/status`); if(response.ok){ready=true;break;} } catch {}
        await new Promise(resolve=>setTimeout(resolve,1000));
      }
      if(!ready) throw Error('Metro startup timed out');
      const response=await fetch(`http://127.0.0.1:${port}/index.bundle?platform=android&dev=true&minify=false`,{signal:AbortSignal.timeout(120000)});
      const body=await response.text(); bundle=response.ok&&body.includes(marker);
      if(!bundle) error=body.slice(0,1200);
    } catch(problem) {error=String(problem);} finally {
      spawnSync('taskkill',['/PID',String(child.pid),'/T','/F'],{windowsHide:true});
      fs.writeFileSync(path.join(here,`${name}-metro.log`),log);
    }
    const result={name,typecheckExit:check.status,androidBundle:bundle,error,deviceRun:false};
    results.push(result); console.log(JSON.stringify(result));
  }
} finally {
  fs.writeFileSync(path.join(cwd,'App.tsx'),original);
  fs.writeFileSync(path.join(here,'validation.json'),JSON.stringify({date:'2026-11-07',node:process.version,results,scope:'Local TypeScript and Metro Android bundle checks; no physical device or network certification.'},null,2));
}
if(results.length!==cases.length||results.some(result=>result.typecheckExit!==0||!result.androidBundle))process.exitCode=1;
