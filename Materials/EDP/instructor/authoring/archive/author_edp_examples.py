from pathlib import Path
import textwrap

root=Path('Application Development and Emerging Technologies (Inluding event Driven programming)/EDP/examples')
root.mkdir(exist_ok=True)
files={
'm01.mjs':r'''
const prices = [25, 35];
let total = 0;
for (const price of prices) total += price;
function canAfford(budget, amount) { return budget >= amount; }
console.log('Total:', total);
if (canAfford(100, total)) console.log('Order accepted');
else console.log('Kulang ang baon');
function invoice(order) { console.log('Invoice:', order.id); }
function kitchen(order) { console.log('Kitchen:', order.id); }
const listeners = [invoice, kitchen];
const order = { id: 'A1', total };
for (const listener of listeners) listener(order);
setTimeout(() => console.log('Ready na ang order!'), 50);
const cancelled = setTimeout(() => console.log('SHOULD NOT RUN'), 100);
clearTimeout(cancelled);
console.log('Taking the next order');
''',
'm01-types.ts':r'''
interface Order { id: string; total: number }
function receipt(order: Order): string {
  return `${order.id}: PHP ${order.total}`;
}
console.log(receipt({ id: 'A1', total: 60 }));
// Change total to "60" to see a type error, then restore the number.
''',
'm02.mjs':r'''
console.log('A: synchronous start');
setTimeout(() => console.log('D: timer callback'), 0);
Promise.resolve().then(() => console.log('C: promise callback'));
console.log('B: synchronous end');
function prepare(id, fail = false) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (fail) reject(new Error(`Unavailable: ${id}`));
      else resolve(`Ready: ${id}`);
    }, 30);
  });
}
async function main() {
  try {
    console.log(await prepare('A1'));
    console.log(await prepare('A2', true));
  } catch (error) {
    console.log('Handled:', error.message);
  } finally {
    console.log('Preparation finished');
  }
}
await main();
''',
'm03.html':r'''
<!doctype html>
<html lang="en"><meta charset="utf-8"><title>EDP Order Board</title>
<body>
<h1>Canteen order board</h1>
<button id="hello" type="button">Say hello</button>
<p id="message" aria-live="polite">Waiting for your click.</p>
<form id="orderForm">
  <label for="food">Food name</label>
  <input id="food" maxlength="40" required>
  <button>Add order</button>
</form>
<ul id="orders"></ul>
<button id="stop" type="button">Stop listeners</button>
<script>
const hello = document.getElementById('hello');
const message = document.getElementById('message');
const form = document.getElementById('orderForm');
const food = document.getElementById('food');
const orders = document.getElementById('orders');
const stop = document.getElementById('stop');
const controller = new AbortController();
const options = { signal: controller.signal };
let count = 0;
hello.addEventListener('click', () => {
  message.textContent = 'Hello, coder!';
}, options);
form.addEventListener('submit', (event) => {
  event.preventDefault();
  const title = food.value.trim();
  if (!title) { message.textContent = 'Enter a food name.'; return; }
  const row = document.createElement('li');
  row.dataset.id = String(++count);
  row.append(document.createTextNode(title + ' '));
  const button = document.createElement('button');
  button.type = 'button';
  button.textContent = 'Collected';
  button.dataset.action = 'collect';
  row.append(button);
  orders.append(row);
  food.value = '';
  orders.dispatchEvent(new CustomEvent('order-added', { detail: { id: count } }));
}, options);
orders.addEventListener('click', (event) => {
  if (!(event.target instanceof Element)) return;
  const button = event.target.closest('button[data-action="collect"]');
  if (!button || !orders.contains(button)) return;
  button.closest('li').remove();
  message.textContent = 'Order collected.';
}, options);
orders.addEventListener('order-added', (event) => {
  message.textContent = 'Added order ' + event.detail.id;
}, options);
stop.addEventListener('click', () => {
  controller.abort();
  hello.disabled = true;
  form.querySelector('button').disabled = true;
  for (const button of orders.querySelectorAll('button')) button.disabled = true;
  stop.disabled = true;
  message.textContent = 'Listeners stopped. Reload to restart.';
}, { once: true });
</script>
</body></html>
''',
'm04.mjs':r'''
import { EventEmitter, once } from 'node:events';
const orders = new EventEmitter({ captureRejections: true });
function invoice(order) { console.log('Invoice:', order.id); }
orders.on('error', error => console.log('Handled:', error.message));
orders.on('order.created', invoice);
orders.on('order.created', order => console.log('Kitchen:', order.id));
orders.once('order.created', () => console.log('First order bonus'));
orders.emit('order.created', { id: 'A1' });
orders.off('order.created', invoice);
orders.emit('order.created', { id: 'A2' });
orders.emit('error', new Error('Printer offline'));
const ready = once(orders, 'ready'); // Subscribe BEFORE emitting.
orders.emit('ready', 'A2');
console.log('Ready:', (await ready)[0]);
orders.removeAllListeners();
console.log('Remaining:', orders.eventNames().length);
''',
'm05.mjs':r'''
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
''',
'm06.ts':r'''
type Order = { id: string; total: number };
type Events = { 'order.created': Order; 'order.cancelled': { id: string } };
class Channel<T> {
  private listeners = new Set<(payload: T) => void>();
  on(listener: (payload: T) => void): () => void {
    this.listeners.add(listener);
    return () => { this.listeners.delete(listener); };
  }
  emit(payload: T): void {
    for (const listener of [...this.listeners]) listener(payload);
  }
}
type Channels<M> = { [K in keyof M]: Channel<M[K]> };
const bus: Channels<Events> = {
  'order.created': new Channel<Order>(),
  'order.cancelled': new Channel<{ id: string }>()
};
function emit<K extends keyof Events>(name: K, payload: Events[K]): void {
  bus[name].emit(payload);
}
function isOrder(value: unknown): value is Order {
  if (typeof value !== 'object' || value === null) return false;
  const candidate = value as Record<string, unknown>;
  return typeof candidate.id === 'string' && candidate.id.length > 0
    && typeof candidate.total === 'number'
    && Number.isFinite(candidate.total) && candidate.total >= 0;
}
const off = bus['order.created'].on(order => console.log('Invoice:', order.id, order.total));
const input: unknown = JSON.parse('{"id":"A1","total":60}');
if (isOrder(input)) emit('order.created', input);
const bad: unknown = { id: 'A2', total: 'sixty' };
console.log('Bad payload accepted:', isOrder(bad));
off();
emit('order.created', { id: 'A3', total: 30 });
// Uncomment to see a compile-time error, then restore before submitting:
// emit('order.created', { id: 'A4', total: 'wrong' });
''',
'm07.mjs':r'''
const transitions = {
  waiting: { prepare: 'preparing', cancel: 'cancelled' },
  preparing: { finish: 'ready' },
  ready: { collect: 'collected' },
  collected: {}, cancelled: {}
};
let state = 'waiting';
function send(command) {
  const next = transitions[state][command];
  if (!next) { console.log('Rejected:', command, 'in', state); return false; }
  console.log(state, '->', next);
  state = next;
  return true;
}
send('collect');
send('prepare'); send('finish'); send('collect');
send('collect');
''',
'm08.mjs':r'''
import { Subject, of, timer } from 'rxjs';
import { debounceTime, distinctUntilChanged, switchMap, map, catchError, finalize } from 'rxjs/operators';
const terms = new Subject();
const subscription = terms.pipe(
  debounceTime(10),
  distinctUntilChanged(),
  switchMap(term => timer(30).pipe(
    map(() => {
      if (term === 'error') throw new Error('Search unavailable');
      return 'Results: ' + term.toUpperCase();
    }),
    catchError(error => of('Handled: ' + error.message))
  )),
  finalize(() => console.log('Search subscription closed'))
).subscribe(value => console.log(value));
terms.next('c'); terms.next('ca'); terms.next('canteen');
await new Promise(resolve => setTimeout(resolve, 80));
terms.next('error');
await new Promise(resolve => setTimeout(resolve, 80));
subscription.unsubscribe();
terms.complete();
''',
'm09.html':r'''
<!doctype html><html lang="en"><meta charset="utf-8"><title>Live announcements</title>
<body><h1>Live announcements</h1><p id="status" aria-live="polite">Connecting</p>
<ul id="messages"></ul><button id="stop">Disconnect</button>
<script>
const status = document.getElementById('status');
const list = document.getElementById('messages');
const source = new EventSource('/events');
source.addEventListener('open', () => { status.textContent = 'Connected'; });
source.addEventListener('error', () => { status.textContent = 'Connection interrupted; retrying'; });
source.addEventListener('announcement', event => {
  try {
    const message = JSON.parse(event.data);
    if (typeof message.text !== 'string') throw new Error('Invalid message');
    const li = document.createElement('li');
    li.textContent = message.text;
    list.append(li);
    if (list.children.length > 20) list.firstElementChild.remove();
  } catch { status.textContent = 'Rejected invalid announcement'; }
});
function close() { source.close(); status.textContent = 'Disconnected'; }
document.getElementById('stop').addEventListener('click', close);
window.addEventListener('pagehide', close, { once: true });
</script></body></html>
''',
'server.mjs':r'''
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
const routes = new Map([
  ['/', 'm03.html'], ['/m03.html', 'm03.html'], ['/m09.html', 'm09.html']
]);
const server = createServer(async (req, res) => {
  if (req.url === '/events') {
    res.writeHead(200, { 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache' });
    let id = 0;
    const timer = setInterval(() => {
      res.write(`id: ${++id}\nevent: announcement\ndata: ${JSON.stringify({ text: 'Order ready ' + id })}\n\n`);
    }, 300);
    req.on('close', () => clearInterval(timer));
    return;
  }
  const file = routes.get(req.url);
  if (!file) { res.writeHead(404); res.end('Not found'); return; }
  try {
    const content = await readFile(new URL(file, import.meta.url));
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(content);
  } catch { res.writeHead(500); res.end('Cannot read lesson file'); }
});
server.listen(4173, '127.0.0.1', () => console.log('Open http://127.0.0.1:4173/m03.html or /m09.html'));
// Stop with Ctrl+C. This loopback teaching service has no auth or durable replay.
''',
'm10.mjs':r'''
import { Readable, Transform, Writable } from 'node:stream';
import { pipeline } from 'node:stream/promises';
const source = Readable.from(['order a1', 'order a2', 'order a3']);
const uppercase = new Transform({
  objectMode: true,
  transform(chunk, encoding, done) { done(null, chunk.toUpperCase()); }
});
const destination = new Writable({
  objectMode: true, highWaterMark: 1,
  write(chunk, encoding, done) {
    setTimeout(() => { console.log('Saved:', chunk); done(); }, 10);
  }
});
try { await pipeline(source, uppercase, destination); console.log('Pipeline complete'); }
catch (error) { console.log('Pipeline failed:', error.message); }
''',
'worker.mjs':r'''
import { parentPort, workerData } from 'node:worker_threads';
let sum = 0;
for (let i = 1; i <= workerData; i++) sum += i;
parentPort.postMessage(sum);
''',
'm10-worker.mjs':r'''
import { Worker } from 'node:worker_threads';
const worker = new Worker(new URL('./worker.mjs', import.meta.url), { workerData: 1000000 });
worker.on('message', result => console.log('Worker result:', result));
worker.on('error', error => { console.error(error); process.exitCode = 1; });
worker.on('exit', code => { if (code !== 0) process.exitCode = 1; });
console.log('Main thread remains available');
''',
'm11.test.mjs':r'''
import test from 'node:test';
import assert from 'node:assert/strict';
import { EventEmitter, once } from 'node:events';
test('listeners run in order and removed listeners stay removed', () => {
  const bus = new EventEmitter(); const trace = [];
  const first = value => trace.push('first:' + value);
  bus.on('ready', first);
  bus.once('ready', value => trace.push('once:' + value));
  bus.emit('ready', 'A1'); bus.off('ready', first); bus.emit('ready', 'A2');
  assert.deepEqual(trace, ['first:A1', 'once:A1']);
  assert.equal(bus.listenerCount('ready'), 0);
});
test('waiting is registered before dispatch', async () => {
  const bus = new EventEmitter();
  const result = once(bus, 'ready'); bus.emit('ready', { id: 'A1' });
  assert.deepEqual(await result, [{ id: 'A1' }]);
});
test('failure can be asserted without crashing the suite', () => {
  const bus = new EventEmitter();
  assert.throws(() => bus.emit('error', new Error('printer')), /printer/);
});
''',
'm12.mjs':r'''
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
''',
'm13.mjs':r'''
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
''',
'm14.mjs':r'''
// Model an atomic commit using copy-on-write, NOT a real database transaction.
let db = { orders: [], outbox: [] };
function placeOrder(id, fail = false) {
  const draft = structuredClone(db);
  draft.orders.push({ id });
  draft.outbox.push({ id: 'event-' + id, version: 1, type: 'order.created', data: { id } });
  if (fail) throw new Error('Commit cancelled');
  db = draft;
}
try { placeOrder('BAD', true); } catch (error) { console.log(error.message); }
placeOrder('A1');
const inbox = new Set();
function receive(event) {
  if (event.version !== 1 || typeof event.data?.id !== 'string') throw new Error('Unsupported contract');
  if (inbox.has(event.id)) { console.log('Duplicate ignored:', event.id); return; }
  console.log('Received:', event.data.id); inbox.add(event.id);
}
const pending = db.outbox[0];
receive(pending); // Simulate send succeeded but relay lost acknowledgment.
receive(pending); // Retry is expected.
db.outbox.shift();
console.log('Orders:', db.orders.length, 'Pending:', db.outbox.length);
''',
'm15.mjs':r'''
const history = [
  { sequence: 1, type: 'stock.received', quantity: 10 },
  { sequence: 2, type: 'stock.reserved', quantity: 3 },
  { sequence: 3, type: 'stock.released', quantity: 1 }
];
function evolve(stock, event) {
  if (!Number.isInteger(event.quantity) || event.quantity < 0) throw new Error('Invalid quantity');
  switch (event.type) {
    case 'stock.received': case 'stock.released': return stock + event.quantity;
    case 'stock.reserved':
      if (event.quantity > stock) throw new Error('Insufficient stock');
      return stock - event.quantity;
    default: throw new Error('Unknown event');
  }
}
console.log('Rebuilt stock:', history.reduce(evolve, 0));
const snapshot = { sequence: 2, stock: 7 };
console.log('From snapshot:', history.filter(e => e.sequence > snapshot.sequence).reduce(evolve, snapshot.stock));
console.log('Replay again:', history.reduce(evolve, 0));
// No emails, network writes or payments inside evolve().
''',
'm16.mjs':r'''
const reservations = new Set(); const statuses = new Map();
async function checkout(id, failPayment) {
  reservations.add(id); statuses.set(id, 'pending');
  console.log('Reserved:', id);
  try {
    if (failPayment) throw new Error('Payment declined');
    statuses.set(id, 'confirmed'); console.log('Confirmed:', id);
  } catch (error) {
    reservations.delete(id); // Idempotent compensation in this small model.
    statuses.set(id, 'cancelled'); console.log('Compensated:', id);
  }
}
await checkout('A1', true); await checkout('A2', false);
const readModel = [...statuses].map(([id, status]) => ({ id, status }));
console.log(JSON.stringify(readModel));
console.log('Active reservations:', reservations.size);
// Real sagas persist progress and can fail during compensation too.
''',
'm17.mjs':r'''
const records = []; const metrics = { accepted: 0, rejected: 0 };
function log(eventId, outcome, reason) {
  const record = { eventId, correlationId: 'checkout-A1', outcome, reason };
  records.push(record); console.log(JSON.stringify(record));
}
function handle(input, actor) {
  if (!input || typeof input.id !== 'string' || typeof input.owner !== 'string') {
    metrics.rejected++; log('unknown', 'rejected', 'invalid shape'); return;
  }
  if (input.owner !== actor.id) { metrics.rejected++; log(input.id, 'rejected', 'not owner'); return; }
  metrics.accepted++; log(input.id, 'accepted', 'authorized');
}
handle({ id: 'E1', owner: 'student-1' }, { id: 'student-1' });
handle({ id: 'E2', owner: 'student-2' }, { id: 'student-1' });
console.log('Metrics:', JSON.stringify(metrics));
// actor is trusted only in this model; a real server derives it from verified identity.
''',
'project.mjs':r'''
import { EventEmitter } from 'node:events';
export function createBoard() {
  const bus = new EventEmitter(); const orders = new Map(); const log = [];
  const record = event => log.push({ ...event });
  bus.on('order.changed', record);
  function add(id, title) {
    if (typeof id !== 'string' || !id.trim() || typeof title !== 'string' || !title.trim()) throw new Error('ID and title required');
    if (orders.has(id)) throw new Error('Duplicate ID');
    const order = { id, title: title.trim(), status: 'waiting' };
    orders.set(id, order); bus.emit('order.changed', { ...order });
  }
  function ready(id) {
    const order = orders.get(id);
    if (!order || order.status !== 'waiting') throw new Error('Invalid transition');
    const updated = { ...order, status: 'ready' };
    orders.set(id, updated); bus.emit('order.changed', { ...updated });
  }
  return {
    add, ready,
    list: () => [...orders.values()].map(order => ({ ...order })),
    history: () => log.map(event => ({ ...event })),
    close: () => bus.off('order.changed', record),
    listenerCount: () => bus.listenerCount('order.changed')
  };
}
''',
'm18.mjs':r'''
import { createBoard } from './project.mjs';
const board = createBoard();
board.add('A1', 'Pandesal'); board.ready('A1');
try { board.ready('A1'); } catch (error) { console.log('Handled:', error.message); }
console.log('Orders:', JSON.stringify(board.list()));
console.log('Events:', board.history().length);
board.close(); console.log('Listeners:', board.listenerCount());
''',
'm19.mjs':r'''
// Repair rehearsal: this executable version shows the corrected behavior.
import { EventEmitter } from 'node:events';
const bus = new EventEmitter(); let calls = 0;
function handle() { calls++; }
bus.on('ready', handle); // Register the function, not handle().
bus.emit('ready');
bus.off('ready', handle); // Same function identity.
bus.emit('ready');
console.log('Calls:', calls);
const input = '   ';
console.log('Input accepted:', input.trim().length > 0);
console.log('Listener count:', bus.listenerCount('ready'));
''',
'm20.mjs':r'''
import { createBoard } from './project.mjs';
const board = createBoard();
for (const [id, title] of [['A1', 'Juice'], ['A2', 'Bread']]) board.add(id, title);
board.ready('A1');
const checks = [
  ['two orders', board.list().length === 2],
  ['first ready', board.list()[0].status === 'ready'],
  ['three domain events', board.history().length === 3]
];
board.close(); checks.push(['listeners cleaned', board.listenerCount() === 0]);
for (const [label, passed] of checks) console.log(passed ? 'PASS' : 'FAIL', label);
if (checks.some(([, passed]) => !passed)) process.exitCode = 1;
''',
'project.test.mjs':r'''
import test from 'node:test';
import assert from 'node:assert/strict';
import { createBoard } from './project.mjs';
test('valid transition produces a history, invalid transition does not', () => {
  const board = createBoard(); board.add('A1', 'Bread'); board.ready('A1');
  assert.equal(board.list()[0].status, 'ready');
  assert.throws(() => board.ready('A1'), /Invalid transition/);
  assert.equal(board.history().length, 2); board.close();
  assert.equal(board.listenerCount(), 0);
});
test('rejects blanks and duplicates; callers cannot change internal state', () => {
  const board = createBoard();
  assert.throws(() => board.add('A1', '  '), /required/);
  board.add('A1', 'Bread');
  assert.throws(() => board.add('A1', 'Milk'), /Duplicate/);
  board.list()[0].status = 'hacked';
  assert.equal(board.list()[0].status, 'waiting'); board.close();
});
'''
}
for name,code in files.items(): (root/name).write_text(textwrap.dedent(code).strip()+'\n',encoding='utf-8')
print('Wrote',len(files),'independent example/support files')
