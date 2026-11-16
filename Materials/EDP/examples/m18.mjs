import { createBoard } from './project.mjs';
const board = createBoard();
board.add('A1', 'Pandesal'); board.ready('A1');
try { board.ready('A1'); } catch (error) { console.log('Handled:', error.message); }
console.log('Orders:', JSON.stringify(board.list()));
console.log('Events:', board.history().length);
board.close(); console.log('Listeners:', board.listenerCount());
