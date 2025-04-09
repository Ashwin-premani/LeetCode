class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # tabulation
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD
        res = 0
        left, right = 0, n - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + pow2[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return  res

        # Memoization
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        @lru_cache(maxsize=None)
        def dfs(left: int, right: int) -> int:
            if left > right:
                return 0
            if nums[left] + nums[right] > target:
                return dfs(left, right - 1)
            else:
                count = pow(2, right - left, MOD)
                count += dfs(left + 1, right)
                return count % MOD

        return dfs(0, n - 1)
