class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Tabulation
        nums.insert(0,1)
        nums.append(1)
        n = len(nums)
        dp = [[0] * (n) for i in range(n)]
        for i in range(n - 2, 0, -1):
            for j in range(i, n - 1):
                maxi = float('-inf')
                for ind in range(i, j + 1):  
                    cost = nums[i - 1] * nums[ind] * nums[j + 1] + dp[i][ind - 1] + dp[ind + 1][j]
                    maxi = max(maxi, cost)
                dp[i][j] = maxi
        return dp[1][n-2]


        # Memoization
        nums.insert(0,1)
        nums.append(1)
        n = len(nums)
        dp = [[-1] * (n+1) for i in range(n+1)]
        def f (i, j):
            if i > j:      
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            maxi = float('-inf')
            for ind in range(i, j+1):
                cost = nums[i-1] * nums[ind] * nums[j+1] + f(i, ind - 1) + f(ind + 1, j)
                maxi = max(maxi, cost)
            dp[i][j] = maxi
            return maxi
        return f(1, n-2)