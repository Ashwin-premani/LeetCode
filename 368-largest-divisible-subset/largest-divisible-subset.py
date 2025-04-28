class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Tabulation
        if not nums:
            return []
        nums.sort() 
        n = len(nums)
        dp = [1] * n 
        prev = [-1] * n 

        max_idx = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > dp[max_idx]:
                max_idx = i
        ans = []
        while max_idx != -1:
            ans.append(nums[max_idx])
            max_idx = prev[max_idx]

        ans.reverse()
        return ans

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