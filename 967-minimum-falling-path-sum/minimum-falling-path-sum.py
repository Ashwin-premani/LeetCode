class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # tabulation
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        if n == 1:
            return matrix[0][0]
        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(n):
            for j in range(n):
                up = dp[i-1][j]
                left_diag = dp[i-1][j-1] if j > 0 else float('inf')
                right_diag = dp[i-1][j+1] if j < n-1 else float('inf')
                dp[i][j] = matrix[i][j] + min(up, left_diag, right_diag)
        return min(dp[-1])

        # Memoization (TLE)
        # n = len(matrix)
        # dp = [[-1] * n for _ in range(n)]
        # def f(i, j):
        #     if i == 0:
        #         return matrix[0][j]
            
        #     if j < 0 or j >= n:
        #         return float('inf')
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     up = f(i - 1, j)
        #     left_diag = f(i - 1, j - 1) if j > 0 else float('inf')
        #     right_diag = f(i - 1, j + 1) if j < n - 1 else float('inf')
        #     dp[i][j] = matrix[i][j] + min(left_diag, right_diag, up)
        #     return dp[i][j]


        # return min(f(n - 1, j) for j in range(n))