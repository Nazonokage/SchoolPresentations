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
