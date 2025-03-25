class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Tabulation
        n = len(triangle)
        dp = [row[:] for row in triangle]  
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                    diag = triangle[i][j] + dp[i+1][j+1]
                    down = triangle[i][j] + dp[i+1][j]
                    dp[i][j] = min(diag, down)
        return dp[0][0]

        # Memoization
        n = len(triangle)  
        dp = [[-1] * len(row) for row in triangle]
        def f(i, j):
            if i == n - 1:
                return triangle[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            diag = triangle[i][j] + f(i+1, j+1)
            down = triangle[i][j] + f(i+1, j)
            dp[i][j] = min(diag, down)
            return dp[i][j]
        return f(0, 0)