import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
const routes = new Map([
  ['/', 'm03-first.html'], ['/m03-first.html', 'm03-first.html'],
  ['/m03.html', 'm03.html'], ['/m08.html', 'm08.html'], ['/m09.html', 'm09.html'],
  ['/vendor/rxjs.umd.min.js', 'vendor/rxjs/dist/bundles/rxjs.umd.min.js']
]);
const server = createServer(async (req, res) => {
  if (req.url === '/events') {
    res.writeHead(200, { 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache' });
    let id = 0;
    const timer = setInterval(() => {
      res.write(`id: ${++id}\nevent: announcement\ndata: ${JSON.stringify({ text: 'Order ready ' + id })}\n\n`);
    }, 300);
    req.on('close', () => clearInterval(timer));
    return;
  }
  const file = routes.get(req.url);
  if (!file) { res.writeHead(404); res.end('Not found'); return; }
  try {
    const content = await readFile(new URL(file, import.meta.url));
    res.writeHead(200, { 'Content-Type': file.endsWith('.js') ? 'text/javascript; charset=utf-8' : 'text/html; charset=utf-8' });
    res.end(content);
  } catch { res.writeHead(500); res.end('Cannot read lesson file'); }
});
server.listen(4173, '127.0.0.1', () => console.log('Open http://127.0.0.1:4173/m03.html or /m09.html'));
// Stop with Ctrl+C. This loopback teaching service has no auth or durable replay.
