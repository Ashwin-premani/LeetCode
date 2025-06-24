class Solution:
    def maxCoins(self, nums: List[int]) -> int:
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