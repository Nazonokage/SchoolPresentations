// LOCAL MODEL ONLY: no network, no persistence, no real parallel workers.
// 1. Work queue: each job goes to ONE worker; an un-acknowledged job is redelivered.
const workers = ['Kitchen 1', 'Kitchen 2'];
const queue = ['A1', 'A2', 'A3', 'A4'];
const crashOnce = new Set(['Kitchen 2:A2']); // deliberate failure: worker dies before ack
const attempts = {};
const done = [];
let turn = 0;
while (queue.length > 0) {
  const job = queue.shift();
  const worker = workers[turn++ % workers.length];
  attempts[job] = (attempts[job] ?? 0) + 1;
  if (crashOnce.delete(`${worker}:${job}`)) {
    console.log('Queue:', worker, job, 'crashed, no ack -> redeliver');
    queue.push(job);
    continue;
  }
  console.log('Queue:', worker, job, 'ack');
  done.push(job);
}
console.log('Completed order:', done.join(','), '| A2 attempts:', attempts.A2);

// 2. Pub/Sub: every ONLINE subscriber gets its own copy; an offline one simply misses it.
const subscribers = [{ name: 'Invoice', online: true }, { name: 'Analytics', online: false }];
for (const { name, online } of subscribers) {
  console.log('PubSub:', name, online ? 'A1' : 'offline, missed A1');
}

// 3. Retained log: events stay; each consumer keeps its own offset and can catch up.
const retainedLog = ['created:A1', 'ready:A1', 'collected:A1'];
const offsets = { dashboard: 0, archive: 1, analytics: 0 }; // analytics was offline above
function replay(consumer, offset) {
  if (!Number.isInteger(offset) || offset < 0 || offset > retainedLog.length) {
    console.log('Rejected offset:', consumer, offset);
    return;
  }
  console.log('Replay:', consumer, retainedLog.slice(offset).join(',') || '(nothing new)');
}
for (const [consumer, offset] of Object.entries(offsets)) replay(consumer, offset);
replay('broken', 9); // failure case: offset outside the retained log
