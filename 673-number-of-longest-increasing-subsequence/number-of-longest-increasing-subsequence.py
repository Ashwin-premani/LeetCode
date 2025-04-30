class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n 

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    count[i] = count[j]
                elif nums[j] < nums[i] and dp[i] == 1 + dp[j]:
                    count[i] += count[j]
        max_len = max(dp)
        return sum(c for i, c in enumerate(count) if dp[i] == max_len)
