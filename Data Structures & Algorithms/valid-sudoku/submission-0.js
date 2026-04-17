class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {

        let row_table = {};
        let col_table = {};
        let square_table = {};
        
        for (let i = 0; i < board.length; i++) {

            let row = board[i];
            row_table[i] = new Set();

            for (let j = 0; j < row.length; j++) {
                if (row[j] === ".") {
                    continue;
                }
                
                let square = Math.floor(i / 3) * 3 + Math.floor(j / 3);
                if (!square_table[square]) {
                    square_table[square] = new Set();
                }
                if (!col_table[j]) {
                    col_table[j] = new Set();
                }

                if (row_table[i].has(row[j])) {
                    return false;
                }
                else {
                    row_table[i].add(row[j]);
                }

                if (col_table[j].has(row[j])) {
                    return false;
                }
                else {
                    col_table[j].add(row[j]);
                }

                if (square_table[square].has(row[j])) {
                    return false;
                }
                else {
                    square_table[square].add(row[j]);
                }
            }
        }

        return true;

    }
}
