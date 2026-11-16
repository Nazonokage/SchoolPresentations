import { Worker } from 'node:worker_threads';
const worker = new Worker(new URL('./worker.mjs', import.meta.url), { workerData: 1000000 });
worker.on('message', result => console.log('Worker result:', result));
worker.on('error', error => { console.error(error); process.exitCode = 1; });
worker.on('exit', code => { if (code !== 0) process.exitCode = 1; });
console.log('Main thread remains available');
