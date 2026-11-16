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
