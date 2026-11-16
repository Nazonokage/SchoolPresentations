// Two-way messaging over WebSocket, loopback only. Needs the pinned `ws` package for the SERVER;
// the client is Node's built-in WebSocket. No auth, no reconnect, no history: teaching model.
import { WebSocketServer } from 'ws';
const server = new WebSocketServer({ host: '127.0.0.1', port: 4174 });
server.on('connection', socket => {
  socket.send(JSON.stringify({ text: 'Server: welcome' }));          // server speaks first (SSE can do this too)
  socket.on('message', data => {                                      // client -> server (SSE cannot do this)
    let message;
    try { message = JSON.parse(data.toString()); } catch { socket.send(JSON.stringify({ error: 'Invalid JSON' })); return; }
    if (typeof message.text !== 'string') { socket.send(JSON.stringify({ error: 'text must be a string' })); return; }
    socket.send(JSON.stringify({ text: 'Echo: ' + message.text }));
  });
});
await new Promise(resolve => server.once('listening', resolve));
const client = new WebSocket('ws://127.0.0.1:4174');
const received = [];
client.addEventListener('message', event => {
  const message = JSON.parse(event.data);
  console.log('Client got:', message.text ?? 'ERROR ' + message.error);
  received.push(message);
  if (received.length === 4) client.close();                          // welcome + 3 replies
});
client.addEventListener('open', () => {
  client.send(JSON.stringify({ text: 'Order A1 ready?' }));
  client.send(JSON.stringify({ text: 42 }));                          // wrong shape: rejected
  client.send('not json');                                            // not JSON: rejected
});
await new Promise(resolve => client.addEventListener('close', resolve));
console.log('Client closed; shutting server down');
server.close();
