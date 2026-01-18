# 36. Valid Sudoku
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Rows
        rows = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in rows:
                        return False
                    rows.add(board[i][j])
            rows = set()

        # Columns
        columns = set()
        for i in range(9):
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in columns:
                        return False
                    columns.add(board[j][i])
            columns = set()

        # Boxes
        starts = [(0, 0), (0, 3), (0, 6),
                  (3, 0), (3, 3), (3, 6),
                  (6, 0), (6, 3), (6, 6)]
        for i, j in starts:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        return True
print(Solution().isValidSudoku(
[[".","8","7","6","5","4","3","2","1"],
 ["2",".",".",".",".",".",".",".","."],
 ["3",".",".",".",".",".",".",".","."],
 ["4",".",".",".",".",".",".",".","."],
 ["5",".",".",".",".",".",".",".","."],
 ["6",".",".",".",".",".",".",".","."],
 ["7",".",".",".",".",".",".",".","."],
 ["8",".",".",".",".",".",".",".","."],
 ["9",".",".",".",".",".",".",".","."]]))