class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m)]
        def path(i, j):
            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            left = path(i - 1, j)
            up = path(i, j - 1)
            dp[i][j] = left + up
            return dp[i][j]
        return path(m - 1, n - 1)