const darrays = [[9,11,10],
                  [5,61,14],
                  [8,12,15],]


// console.log(darrays[0][1]) // 11
// console.log(darrays[2][2]);
// console.log('+++++++++++++++++++++');



// for (let i = 0; i < darrays.length; i++) {
//     for (let j = 0; j < darrays[i].length; j++) {
//         console.log(darrays[i][j]);
//     }
// }

function tictactoe(arr, player) {
    const winningCombos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
        [0, 4, 8], [2, 4, 6]             // diagonals
    ];

    let result = 'No winner yet';

    for (const [a, b, c] of winningCombos) {
        if (arr[a] === player && arr[b] === player && arr[c] === player) {
            result = `${player} wins!`;
            break;
        }
    }

    const display = arr.map(cell => cell === null ? ' ' : cell);
    console.log(`
 ${display[0]} | ${display[1]} | ${display[2]}
-----------
 ${display[3]} | ${display[4]} | ${display[5]}
-----------
 ${display[6]} | ${display[7]} | ${display[8]}
`);

    return result;
}

const board = ['X', 'X', 'X',
               'O', 'O', null,
               null, null, null];

console.log(tictactoe(board, 'X'));