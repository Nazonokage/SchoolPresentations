import test from 'node:test';
import assert from 'node:assert/strict';
import { createBoard } from './project.mjs';
test('valid transition produces a history, invalid transition does not', () => {
  const board = createBoard(); board.add('A1', 'Bread'); board.ready('A1');
  assert.equal(board.list()[0].status, 'ready');
  assert.throws(() => board.ready('A1'), /Invalid transition/);
  assert.equal(board.history().length, 2); board.close();
  assert.equal(board.listenerCount(), 0);
});
test('rejects blanks and duplicates; callers cannot change internal state', () => {
  const board = createBoard();
  assert.throws(() => board.add('A1', '  '), /required/);
  board.add('A1', 'Bread');
  assert.throws(() => board.add('A1', 'Milk'), /Duplicate/);
  board.list()[0].status = 'hacked';
  assert.equal(board.list()[0].status, 'waiting'); board.close();
});
