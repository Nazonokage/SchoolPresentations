const jobs = ['A1', 'A2', 'A3', 'A4'];
const workers = ['Kitchen 1', 'Kitchen 2'];
jobs.forEach((job, index) => console.log('Queue:', workers[index % workers.length], job));
const subscribers = ['Invoice', 'Analytics'];
for (const name of subscribers) console.log('PubSub:', name, 'A1');
const retainedLog = ['created:A1', 'ready:A1', 'collected:A1'];
const offsets = { dashboard: 0, archive: 1 };
for (const [consumer, offset] of Object.entries(offsets)) {
  console.log('Replay:', consumer, retainedLog.slice(offset).join(','));
}
