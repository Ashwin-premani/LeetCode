class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # optimized Memoization
        nums.sort()
        cache = {}

        def dfs(i):
            if i == len(nums):
                return []
            if i in cache:
                return cache[i]
            res = [nums[i]]
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + dfs(j)
                    if len(tmp) > len(res):
                        res = tmp
            cache[i] = res
            return cache[i]
        res = []
        for i in range(len(nums)):
            tmp = dfs(i)
            if len(tmp) > len(res):
                res = tmp
        return res

        # Memoization
        nums.sort()
        cache = {}
        def backtrack(i, prev):
            if i == len(nums):
                return []
            if (i, prev) in cache:
                return cache[(i, prev)]
            
            res = backtrack(i+1, prev)
            if nums[i] % prev == 0:
                tmp = [nums[i]] + backtrack(i+1, nums[i])
                res = tmp if len(tmp) > len(res) else res
            cache[(i, prev)] = res
            return res
        return backtrack(0, 1)