class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[1] * n for _ in range(k)]
        maxSub = 1

        for i in range(1, n):
            for j in range(i):
                mod = (nums[i] + nums[j]) % k
                dp[mod][i] = max(dp[mod][i], 1 + dp[mod][j])
                maxSub = max(maxSub, dp[mod][i])

        return maxSub


        n = len(nums)
        # dp = {}
        @lru_cache(None)
        def lis(i, mismatch, parity):
            if i >= n:
                return 0
            
            cur = nums[i] % 2
            if cur == parity:
                take = 1 + lis(i+1, mismatch, parity)
            else:
                if mismatch < k:
                    take = 1 + lis(i+1, mismatch+1, parity)
                else:
                    take = 0
            skip = lis(i+1, mismatch, parity)
            return max(skip, take)
        max_length = 0
        max_length = max(max_length, lis(0, 0, 0), lis(0, 0, 1))
        return max_length