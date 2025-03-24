class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # tabulation space optimization
        dp = [0 for i in range(n)]
        for i in range(m):
            temp = [0 for _ in range(n)]
            for j in range(n):
                if i == 0 and j == 0:
                    temp[0] = 1  # Base case (start point)
                else:
                    temp[j] = dp[j] + temp[j - 1]
            dp = temp
        
        return temp[n - 1]


        # tabulation O(nxm)
        # dp = [[-1] * n for _ in range(m)]
        # dp[0][0] = 1
        
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0:
        #             dp[0][0] = 1  # Base case (start point)
        #         else:
        #             up = dp[i - 1][j] if i > 0 else 0
        #             left = dp[i][j - 1] if j > 0 else 0
        #             dp[i][j] = up + left
        
        # return dp[m - 1][n - 1]


        # memoization
        # dp = [[-1] * n for _ in range(m)]

        # def helper(i, j):
        #     if i == 0 and j == 0:
        #         return 1
        #     if i < 0 or j < 0:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     left = helper(i - 1, j)
        #     up = helper(i, j - 1)
        #     dp[i][j] = up + left
        #     return dp[i][j]
        # return helper(m-1, n-1)

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
            