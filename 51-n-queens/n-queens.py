class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def isSafe(row, col, board, n):
            dup_row = row
            dup_col = col
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1
            row = dup_row
            col = dup_col
            while col >= 0:
                if board[row][col] == 'Q':
                    return False
                col -= 1

            row = dup_row
            col = dup_col
            while row < n and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row += 1
                col -= 1
            return True

        def Solve(col, board, ans, n):
            if col == n:
                current_board = [''.join(row) for row in board]
                ans.append(current_board)
                return
            
            for row in range(n):
                if isSafe(row, col, board, n):
                    board[row][col] = 'Q'
                    Solve(col+1, board, ans, n)
                    board[row][col] = '.'
                

        Solve(0, board, ans, n)
        return ans