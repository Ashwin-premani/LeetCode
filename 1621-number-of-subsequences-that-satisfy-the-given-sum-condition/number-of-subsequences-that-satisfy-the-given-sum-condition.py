class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # every suseq will take 2^n
        # uing 2 pointer
        MOD = 10**9 + 7

        n = len(nums)
        nums.sort()

        
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD
        l = 0
        r = n - 1
        res = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                res = (res + pow2[r - l]) % MOD
                l += 1
            else:
                r -= 1
        return res


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