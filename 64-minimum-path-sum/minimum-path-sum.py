class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # tabulation with space optimization
        n, m = len(grid), len(grid[0])
        prev = [float('inf')] * m
        for i in range(n):
            cur = [0] * m
            for j in range(m):
                if i == 0 and j == 0:
                    cur[j] = grid[i][j]
                else:
                    left = prev[j] if i > 0 else float('inf')
                    up = cur[j-1] if j > 0 else float('inf')
                    cur[j] = grid[i][j] + min(up, left)
            prev = cur
        return prev[m-1]

        # Tabulation
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    left = dp[i-1][j] if i > 0 else float('inf')
                    up = dp[i][j-1] if j > 0 else float('inf')
                    dp[i][j] = grid[i][j] + min(left, up)
        
        return dp[n-1][m-1]

        # # Memoization
        # n, m = len(grid), len(grid[0])
        # dp = [[-1] * m for _ in range(n)]
        # def helper(i, j):
        #     if  i == 0 and j == 0:
        #         return grid[0][0]
        #     if  i < 0 or j < 0:
        #         return float('inf')
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     left = grid[i][j] + helper(i - 1, j)
        #     up = grid[i][j] + helper(i, j - 1)
        #     dp[i][j] = min(left, up) 
        #     return dp[i][j]
        # return helper(len(grid) - 1, len(grid[0]) - 1)

        # # Backtrack
        # def helper(i, j):
        #     if  i == 0 and j == 0:
        #         return grid[0][0]
        #     if  i < 0 or j < 0:
        #         return float('inf')
        #     left = grid[i][j] + helper(i - 1, j)
        #     up = grid[i][j] + helper(i, j - 1)
        #     return min(left, up)
        # return helper(len(grid) - 1, len(grid[0]) - 1)