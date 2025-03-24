class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memoization
        dp = [[-1] * n for _ in range(m)]

        def helper(i, j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            left = helper(i - 1, j)
            up = helper(i, j - 1)
            dp[i][j] = up + left
            return dp[i][j]
        return helper(m-1, n-1)

        # def helper(i, j):
        #     if i == 0 and j == 0:
        #         return 1
        #     if i < 0 or j < 0:
        #         return 0
        #     right = helper(i - 1, j)
        #     down = helper(i, j - 1)
        #     return right + down

        # # Assuming m and n are defined earlier
        # return helper(m - 1, n - 1)
        # # stack overflow
        # def helper(i, j):
        #     if i == 0 and j == 0:
        #         return 1
        #     right = helper(i - 1, j)
        #     down = helper(i, j - 1)
        #     return right + down
        # return helper(m - 1, n - 1)
            