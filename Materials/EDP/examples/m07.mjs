const transitions = {
  waiting: { prepare: 'preparing', cancel: 'cancelled' },
  preparing: { finish: 'ready' },
  ready: { collect: 'collected' },
  collected: {}, cancelled: {}
};
let state = 'waiting';
function send(command) {
  const next = transitions[state][command];
  if (!next) { console.log('Rejected:', command, 'in', state); return false; }
  console.log(state, '->', next);
  state = next;
  return true;
}
send('collect');
send('prepare'); send('finish'); send('collect');
send('collect');
