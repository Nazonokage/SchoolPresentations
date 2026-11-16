import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn, spawnSync } from 'node:child_process';
const here=path.dirname(fileURLToPath(import.meta.url));
const base=path.resolve(here,'../..');
const cwd=path.join(here,'router-check');
fs.mkdirSync(cwd,{recursive:true});
fs.cpSync(path.join(base,'examples/M05/router-extension/app'),path.join(cwd,'app'),{recursive:true});
const modules=path.join(cwd,'node_modules');
if(!fs.existsSync(modules))fs.symlinkSync(path.join(base,'examples/mobile/node_modules'),modules,'junction');
const dependencies={};
for(const name of ['expo','expo-router','expo-linking','expo-constants','expo-status-bar','react','react-native','react-native-screens','react-native-safe-area-context']) {
 dependencies[name]=JSON.parse(fs.readFileSync(path.join(modules,name,'package.json'),'utf8')).version;
}
fs.writeFileSync(path.join(cwd,'package.json'),JSON.stringify({name:'adet-router-validation',version:'1.0.0',private:true,main:'expo-router/entry',dependencies},null,2));
fs.writeFileSync(path.join(cwd,'app.json'),JSON.stringify({expo:{name:'ADET Router Check',slug:'adet-router-check',scheme:'adetlab',plugins:['expo-router']}}));
fs.writeFileSync(path.join(cwd,'tsconfig.json'),JSON.stringify({extends:'expo/tsconfig.base',compilerOptions:{strict:true},include:['app/**/*.tsx']}));
const tsc=path.join(base,'offline-lab/starter/node_modules/typescript/bin/tsc');
const check=spawnSync(process.execPath,[tsc,'--noEmit'],{cwd,encoding:'utf8',windowsHide:true});
fs.writeFileSync(path.join(here,'router-typecheck.log'),(check.stdout??'')+(check.stderr??''));
let log='',androidBundle=false,error='';
const child=spawn(process.execPath,[path.join(modules,'expo/bin/cli'),'start','--offline','--port','8301'],{cwd,env:{...process.env,CI:'1'},windowsHide:true});
child.stdout.on('data',chunk=>log+=chunk);child.stderr.on('data',chunk=>log+=chunk);
try {
 let ready=false;
 for(let attempt=0;attempt<45;attempt++) {
  try {const response=await fetch('http://127.0.0.1:8301/status');if(response.ok){ready=true;break;}}catch{}
  await new Promise(resolve=>setTimeout(resolve,1000));
 }
 if(!ready)throw Error('Metro startup timeout');
 const response=await fetch('http://127.0.0.1:8301/node_modules/expo-router/entry.bundle?platform=android&dev=true&minify=false',{signal:AbortSignal.timeout(120000)});
 const body=await response.text(); androidBundle=response.ok&&body.includes('Campus offices')&&body.includes('Missing office');
 if(!androidBundle)error=body.slice(0,1600);
}catch(problem){error=String(problem);}finally{
 spawnSync('taskkill',['/PID',String(child.pid),'/T','/F'],{windowsHide:true});
 fs.writeFileSync(path.join(here,'router-metro.log'),log);
}
const result={date:'2026-11-07',typescript:'6.0.3',dependencies,typecheckExit:check.status,androidBundle,error,deviceRun:false,scope:'Isolated Router source/config using existing installed mobile dependencies through a junction. No fresh dependency installation or device navigation test.'};
fs.writeFileSync(path.join(here,'router-validation.json'),JSON.stringify(result,null,2));
console.log(JSON.stringify(result,null,2));
if(check.status!==0||!androidBundle)process.exitCode=1;
