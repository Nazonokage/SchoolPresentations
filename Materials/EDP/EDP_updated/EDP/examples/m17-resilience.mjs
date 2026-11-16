// Bounded retry + a tiny circuit breaker. Teaching model, not a production library.
import { setTimeout as delay } from 'node:timers/promises';

async function withRetry(operation, { attempts = 3, baseMs = 5 } = {}) {
  for (let attempt = 1; attempt <= attempts; attempt++) {
    try { return await operation(attempt); }
    catch (error) {
      console.log('Retry decision: attempt', attempt, 'failed:', error.message);
      if (attempt === attempts) throw new Error('Gave up after ' + attempts + ' attempts');
      await delay(baseMs * 2 ** (attempt - 1)); // real systems usually add random jitter
    }
  }
}

function createBreaker({ failureLimit = 2, coolDownMs = 40 } = {}) {
  let failures = 0, openedAt = 0, state = 'closed';
  return {
    get state() { return state; },
    async call(operation) {
      if (state === 'open') {
        if (Date.now() - openedAt < coolDownMs) throw new Error('Circuit open: call skipped');
        state = 'half-open'; // allow ONE probe
      }
      try {
        const result = await operation();
        failures = 0; state = 'closed'; return result;
      } catch (error) {
        failures++;
        if (state === 'half-open' || failures >= failureLimit) { state = 'open'; openedAt = Date.now(); }
        throw error;
      }
    }
  };
}

// Part 1: a temporary outage is worth a bounded retry.
console.log('Result:', await withRetry(async attempt => {
  if (attempt < 3) throw new Error('timeout');
  return 'recovered on attempt ' + attempt;
}));

// Part 2: a persistent outage must stop consuming calls.
let dependencyCalls = 0; let dependencyUp = false;
const breaker = createBreaker();
async function dependency() {
  dependencyCalls++;
  if (!dependencyUp) throw new Error('Dependency down');
  return 'ok';
}
for (let i = 1; i <= 4; i++) {
  try { await breaker.call(dependency); }
  catch (error) { console.log('Call', i + ':', error.message, '| breaker:', breaker.state); }
}
console.log('Dependency actually called:', dependencyCalls, 'times');
await delay(50); dependencyUp = true; // cool-down passes, dependency recovers
console.log('Probe:', await breaker.call(dependency), '| breaker:', breaker.state);
