import { setTimeout as delay } from 'node:timers/promises';
const processed = new Set(); const deadLetters = []; let total = 0;
async function consume(message) {
  if (processed.has(message.id)) { console.log('Duplicate:', message.id); return; }
  for (let attempt = 1; attempt <= 3; attempt++) {
    try {
      if (message.poison || (message.transient && attempt === 1)) throw new Error('Temporary service failure');
      total += message.amount; processed.add(message.id);
      console.log('Applied:', message.id, 'attempt', attempt); return;
    } catch (error) {
      console.log('Retry decision:', message.id, attempt);
      if (attempt === 3) { deadLetters.push(message); return; }
      await delay(5 * 2 ** (attempt - 1));
    }
  }
}
await consume({ id: 'A1', amount: 60, transient: true });
await consume({ id: 'A1', amount: 60 });
await consume({ id: 'A2', amount: 40, poison: true });
console.log('Total:', total, 'Dead letters:', deadLetters.length);
// In-memory sequential model only: a real consumer needs durable atomic deduplication.
