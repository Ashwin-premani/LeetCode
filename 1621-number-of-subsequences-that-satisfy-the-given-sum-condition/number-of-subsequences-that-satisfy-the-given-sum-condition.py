from typing import List
from functools import lru_cache

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
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
