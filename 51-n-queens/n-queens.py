class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        # Initialize tracking arrays
        leftRow = [0] * n
        upperDiagonal = [0] * (2 * n - 1)
        lowerDiagonal = [0] * (2 * n - 1)
        
        def solve(col, board, ans, leftRow, upperDiagonal, lowerDiagonal, n):
            if col == n:
                # Convert the board to the required format
                solution = [''.join(row) for row in board]
                ans.append(solution)
                return
            
            for row in range(n):
                # Check if position is safe using O(1) lookup in tracking arrays
                if (leftRow[row] == 0 and 
                    lowerDiagonal[row + col] == 0 and 
                    upperDiagonal[n - 1 + col - row] == 0):
                    
                    # Place queen and update tracking arrays
                    board[row][col] = 'Q'
                    leftRow[row] = 1
                    lowerDiagonal[row + col] = 1
                    upperDiagonal[n - 1 + col - row] = 1
                    
                    # Recurse to next column
                    solve(col + 1, board, ans, leftRow, upperDiagonal, lowerDiagonal, n)
                    
                    # Backtrack
                    board[row][col] = '.'
                    leftRow[row] = 0
                    lowerDiagonal[row + col] = 0
                    upperDiagonal[n - 1 + col - row] = 0
        
        solve(0, board, ans, leftRow, upperDiagonal, lowerDiagonal, n)
        return ans