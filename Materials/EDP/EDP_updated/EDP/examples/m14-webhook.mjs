// Webhook receiver model: verify the sender, reject stale deliveries, dedupe by event ID.
// Teaching model: the secret is hard-coded here; real secrets live in protected server config.
import { createHmac, timingSafeEqual } from 'node:crypto';
const SECRET = 'classroom-demo-secret';
const TOLERANCE_SECONDS = 300;
const seen = new Set();
const sign = (timestamp, body) => createHmac('sha256', SECRET).update(`${timestamp}.${body}`).digest('hex');

function receive({ timestamp, signature, body }, nowSeconds) {
  const expected = Buffer.from(sign(timestamp, body), 'hex');
  const given = Buffer.from(String(signature), 'hex');
  if (given.length !== expected.length || !timingSafeEqual(given, expected)) return 'Rejected: bad signature';
  if (Math.abs(nowSeconds - timestamp) > TOLERANCE_SECONDS) return 'Rejected: stale timestamp';
  const event = JSON.parse(body); // parse only AFTER the sender is verified
  if (seen.has(event.id)) return 'Duplicate ignored: ' + event.id;
  seen.add(event.id);
  return 'Accepted: ' + event.id;
}

const now = 1_800_000_000;
const body = JSON.stringify({ id: 'evt_1', type: 'payment.paid', orderId: 'A1' });
const good = { timestamp: now, signature: sign(now, body), body };
console.log(receive(good, now));                                   // first delivery
console.log(receive(good, now));                                   // sender retried
console.log(receive({ ...good, body: body.replace('A1', 'A9') }, now)); // tampered body
console.log(receive({ ...good, timestamp: now - 3600, signature: sign(now - 3600, body) }, now)); // replayed old request
