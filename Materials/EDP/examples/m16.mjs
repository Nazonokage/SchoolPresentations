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
