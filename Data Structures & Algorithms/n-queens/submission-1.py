class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["." for _ in range(n)] for _ in range(n)]
        res = []
        
        def is_valid_spot(x: int, y: int, current_board: List[List[str]]):
            
            # Check Horz
            for col in current_board[y]:

                if col == "Q":
                    return False

            # Check Vert
            for row in current_board:
                if row[x] == "Q":
                    return False

            temp_x = x
            # Check Left up Diag
            for i in range(y - 1, -1, -1):
                temp_x -= 1
                if temp_x >= 0:
                    if current_board[i][temp_x] == "Q":
                        return False
                else:
                    break
            
            temp_x = x
            # Check right up Diag
            for i in range(y - 1, -1, -1):
                temp_x += 1
                if temp_x < len(current_board):
                    if current_board[i][temp_x] == "Q":
                        return False
                else:
                    break
            
            return True
                    
        def dfs(x, y, board):

            # Board complete
            if y >= n:
                new_board = []
                for row in board:
                    row_str = ""
                    for col in row:
                        row_str += col
                    new_board.append(row_str)

                res.append(new_board)
                return

            # Dead end
            if x >= n:
                return

            # Backtrack
            if not is_valid_spot(x, y, board):
                dfs(x + 1, y, board)
                return

            board[y][x] = "Q"
            dfs(0, y + 1, board)
            board[y][x] = "."
            dfs(x + 1, y, board)

        dfs(0, 0, board)

        return res
