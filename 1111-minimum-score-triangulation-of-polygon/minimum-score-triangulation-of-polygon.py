class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # Tabulation
        n = len(values)
        dp = [[-1] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        for i in range(n-1,-1, -1):
            for j in range(i+1, n):
                mini = float('inf')
                for k in range(i, j):
                    steps = (values[i-1] * values[k] * values[j]) + dp[i][k] + dp[k+1][j]
                    mini = min(mini, steps)
                dp[i][j] = mini
        return dp[1][n-1]

            
        # Memoization
        dp = {}
        def f(i, j):
            if i == j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            mini = float('inf')
            for k in range(i, j):
                steps = (values[i-1] * values[k] * values[j]) + f(i, k) + f(k + 1, j)
                mini = min(mini, steps)
            dp[(i, j)] = mini
            return mini
        return f(1, len(values) - 1)
