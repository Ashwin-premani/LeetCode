class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Tabulation
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = 1
                elif  obstacleGrid[i][j] == 1:
                    continue
                else:
                    up = dp[i - 1][j] if i > 0 else 0
                    left = dp[i][j - 1] if j > 0 else 0
                    dp[i][j] = up + left
        return dp[m - 1][n - 1]


        # Memoization
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

        # Brute Force
        def path(i, j):
            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            left = path(i - 1, j)
            up = path(i, j - 1)
            return left + up
        return path(len(obstacleGrid)-1, len(obstacleGrid[0]) - 1)