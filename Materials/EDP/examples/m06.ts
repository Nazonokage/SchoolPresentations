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
