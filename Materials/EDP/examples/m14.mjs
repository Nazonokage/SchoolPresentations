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
