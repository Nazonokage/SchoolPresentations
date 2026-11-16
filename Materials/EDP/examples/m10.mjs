import { Readable, Transform, Writable } from 'node:stream';
import { pipeline } from 'node:stream/promises';
const source = Readable.from(['order a1', 'order a2', 'order a3']);
const uppercase = new Transform({
  objectMode: true,
  transform(chunk, encoding, done) { done(null, chunk.toUpperCase()); }
});
const destination = new Writable({
  objectMode: true, highWaterMark: 1,
  write(chunk, encoding, done) {
    setTimeout(() => { console.log('Saved:', chunk); done(); }, 10);
  }
});
try { await pipeline(source, uppercase, destination); console.log('Pipeline complete'); }
catch (error) { console.log('Pipeline failed:', error.message); }
