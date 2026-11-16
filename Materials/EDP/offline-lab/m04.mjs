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
