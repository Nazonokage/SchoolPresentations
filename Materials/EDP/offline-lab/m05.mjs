import { setTimeout as delay } from 'node:timers/promises';
let latestRequest = 0;
let active;
async function search(term, milliseconds) {
  const request = ++latestRequest;
  active?.abort();
  const controller = new AbortController();
  active = controller;
  try {
    await delay(milliseconds, undefined, { signal: controller.signal });
    const results = [term.toUpperCase()];
    if (request !== latestRequest) return;
    console.log('Show:', results.join(', '));
  } catch (error) {
    if (error.name === 'AbortError') console.log('Cancelled:', term);
    else throw error;
  }
}
const old = search('old', 60);
const fresh = search('new', 10);
await Promise.all([old, fresh]);
function debounce(fn, milliseconds) {
  let timer;
  const run = (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), milliseconds);
  };
  run.cancel = () => clearTimeout(timer);
  return run;
}
const announce = debounce(term => console.log('Debounced:', term), 10);
announce('c'); announce('ca'); announce('canteen');
await delay(30);
announce.cancel();
