class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # Memoization
        n, m = len(grid), len(grid[0])
        dp = [[-1] * m for _ in range(n)]
        def helper(i, j):
            if  i == 0 and j == 0:
                return grid[0][0]
            if  i < 0 or j < 0:
                return float('inf')
            if dp[i][j] != -1:
                return dp[i][j]
            left = grid[i][j] + helper(i - 1, j)
            up = grid[i][j] + helper(i, j - 1)
            dp[i][j] = min(left, up) 
            return dp[i][j]
        return helper(len(grid) - 1, len(grid[0]) - 1)

        # Backtrack
        def helper(i, j):
            if  i == 0 and j == 0:
                return grid[0][0]
            if  i < 0 or j < 0:
                return float('inf')
            left = grid[i][j] + helper(i - 1, j)
            up = grid[i][j] + helper(i, j - 1)
            return min(left, up)
        return helper(len(grid) - 1, len(grid[0]) - 1)