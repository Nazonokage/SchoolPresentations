// Repair rehearsal: this executable version shows the corrected behavior.
import { EventEmitter } from 'node:events';
const bus = new EventEmitter(); let calls = 0;
function handle() { calls++; }
bus.on('ready', handle); // Register the function, not handle().
bus.emit('ready');
bus.off('ready', handle); // Same function identity.
bus.emit('ready');
console.log('Calls:', calls);
const input = '   ';
console.log('Input accepted:', input.trim().length > 0);
console.log('Listener count:', bus.listenerCount('ready'));
