class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        
        dp = [[[-1] * n for _ in range(n)] for _ in range(n)]
        
        def dfs(row1, col1, row2, col2):
            if (row1 == n or col1 == n or row2 == n or col2 == n or
                grid[row1][col1] == -1 or grid[row2][col2] == -1):
                return float('-inf')
            
            if row1 == n-1 and col1 == n-1:
                return grid[row1][col1]
            
            if dp[row1][col1][row2] != -1:
                return dp[row1][col1][row2]
            
            result = grid[row1][col1]
            if row1 != row2 or col1 != col2:
                result += grid[row2][col2]
            
            max_cherries = max(
                dfs(row1+1, col1, row2+1, col2),   
                dfs(row1+1, col1, row2, col2+1),
                dfs(row1, col1+1, row2+1, col2),
                dfs(row1, col1+1, row2, col2+1)
            )
            
            dp[row1][col1][row2] = result + max_cherries
            return dp[row1][col1][row2]
        
        return max(0, dfs(0, 0, 0, 0))

        # n = len(grid)
        # dp = [[-1] * n for _ in range(n)]

        # def cherry(i, j):
        #     if i < 0 or j < 0:
        #         return 0
        #     if grid[i][j] == -1:
        #         return 0
        #     if i == 0 and j == 0:
        #         return 1 if grid[i][j] else 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     left = grid[i][j] + cherry(i-1, j)
        #     up = grid[i][j] + cherry(i, j - 1)
        #     dp[i][j] = max(left, up)
        #     return dp[i][j]
        
        # def cherry2(i, j):
        #     if i > n or j > n:
        #         return 0
        #     if grid[i][j] == -1:
        #         return 0
        #     if i == n - 1 and j == n - 1:
        #         return 1 if grid[i][j] else 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     right = grid[i][j] + cherry(i+1, j)
        #     down = grid[i][j] + cherry(i, j + 1)
        #     dp[i][j] = max(right, down)
        #     return dp[i][j]
        # return cherry(0, 0)+cherry2(n-1, n-1)
            