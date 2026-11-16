const transitions = {
  waiting: { prepare: 'preparing', cancel: 'cancelled' },
  preparing: { finish: 'ready' },
  ready: { collect: 'collected' },
  collected: {}, cancelled: {}
};
let state = 'waiting';
const facts = []; // accepted facts only; rejected commands never appear here
function send(command) {
  const next = transitions[state][command];
  if (!next) { console.log('Rejected:', command, 'in', state); return false; }
  console.log(state, '->', next);
  state = next;
  facts.push('order.' + next); // fact is recorded AFTER the transition is accepted
  return true;
}
send('collect');
send('prepare'); send('finish'); send('collect');
send('collect');
console.log('Facts:', facts.join(', '));
