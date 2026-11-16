import { createBoard } from './project.mjs';
const board = createBoard();
for (const [id, title] of [['A1', 'Juice'], ['A2', 'Bread']]) board.add(id, title);
board.ready('A1');
const checks = [
  ['two orders', board.list().length === 2],
  ['first ready', board.list()[0].status === 'ready'],
  ['three domain events', board.history().length === 3]
];
board.close(); checks.push(['listeners cleaned', board.listenerCount() === 0]);
for (const [label, passed] of checks) console.log(passed ? 'PASS' : 'FAIL', label);
if (checks.some(([, passed]) => !passed)) process.exitCode = 1;
