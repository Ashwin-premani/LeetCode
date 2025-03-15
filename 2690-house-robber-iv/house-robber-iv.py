class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def is_valid(m):
            i = 0
            count = 0
            while i < len(nums):
                if nums[i] <= m :
                    i += 2
                    count += 1
                else:
                    i += 1
                if count == k:
                    break
            return count == k

        l, r = min(nums), max(nums)
        # 1. Brute Force
        # 2. Optimize
        # 3. Binary search - Range -  here it's [1, max(nums)] - Binary search for this range
        while l <= r:
            m = (l+r) // 2
            if is_valid(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
        # O(n^2) space and time Top up (Memory limit exceeded) and if bottom up (time limit exceeded)
        # cache = {}
        # def backtrack(i, k):
        #     if i >= len(nums):
        #         if k:
        #             return float('inf')
        #         return 0
        #     if (i, k) in cache:
        #         return cache[(i,k)]
        #     res1 = max(nums[i], backtrack(i+2, k-1))
        #     res2 = backtrack(i+1, k)
        #     res = min(res1, res2)
        #     cache[(i, k)] = res
        #     return res
        
        # return backtrack(0, k)