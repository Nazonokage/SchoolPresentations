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
