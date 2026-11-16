import { parentPort, workerData } from 'node:worker_threads';
let sum = 0;
for (let i = 1; i <= workerData; i++) sum += i;
parentPort.postMessage(sum);
