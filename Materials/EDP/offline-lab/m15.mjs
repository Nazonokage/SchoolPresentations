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
