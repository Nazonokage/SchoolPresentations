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
