import {createInterface} from 'node:readline/promises';
import {stdin,stdout} from 'node:process';
import {spawn} from 'node:child_process';
import {fileURLToPath} from 'node:url';
process.chdir(fileURLToPath(new URL('.',import.meta.url)));
const prompt=createInterface({input:stdin,output:stdout});
const n=Number(await prompt.question('EDP module (1-21): '));prompt.close();
if(!Number.isInteger(n)||n<1||n>21){console.error('Enter a module from 1 to 21.');process.exit(1);}
if(n===20){console.log('M20 is the written defense assessment. No program is required.');process.exit(0);}
let args;
if([3,8,9].includes(n)){
 console.log(`Open http://127.0.0.1:4173/m${String(n).padStart(2,'0')}.html in your browser. Keep this terminal open. Ctrl+C stops the local server.`);
 args=['server.mjs'];
}else if(n===11)args=['--test','m11.test.mjs'];
else args=[n===6?'m06.ts':`m${String(n===21?20:n).padStart(2,'0')}.mjs`];
const child=spawn(process.execPath,args,{stdio:'inherit'});child.on('exit',c=>process.exitCode=c??1);
