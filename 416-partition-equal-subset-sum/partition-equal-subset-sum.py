class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def subsetsum(n, k, arr):
            prev = [False] * (k+1)
        
            prev[0] = True  
            if arr[0] <= k:
                prev[arr[0]] = True

            for i in range(1, n):  
                cur = [False] * (k+1)
                cur[0] = True
                for target in range(1, k + 1):
                    not_take = prev[target]  
                    take = False
                    if arr[i] <= target:
                        take = prev[target - arr[i]]
                    cur[target] = take or not_take  
                prev = cur
            return prev[k]
        n = len(nums)
        s = 0
        for i in range(n):
            s += nums[i]
        if s % 2 != 0:
            return False
        target = s // 2
        return subsetsum(n, target, nums)

        # # Memoization Memory limit exceeded
        # totalSum = sum(nums)
        # if totalSum % 2 != 0:  # Odd total sum can't be partitioned equally
        #     return False

        # target = totalSum // 2
        # n = len(nums)
        
        # # Memoization dictionary instead of a 2D array
        # dp = {}
        # def f(i, cursum):
        #     if cursum == target:
        #         return True
        #     if i >= n or target < cursum:
        #         return False
        #     if (i, cursum) in dp:
        #         return dp[(i, cursum)]
        #     take = f(i+1, cursum + nums[i])
        #     not_take = f(i+1, cursum)
        #     dp[(i, cursum)] = take or not_take
        #     return dp[(i, cursum)]

        # return f(0, 0)

        # # Memoization (Wrong answer)
        # totalSum = sum(nums)
        # if totalSum % 2 != 0:  # Odd total sum can't be partitioned equally
        #     return False

        # target = totalSum // 2
        # n = len(nums)
        
        # # Memoization dictionary instead of a 2D array
        # dp = {}
        # def f(i, s1, s2):
        #     if i == n:
        #         return False
        #     if s1 == s2:
        #         return True
        #     if (s1, s2) in dp:
        #         return dp[(s1, s2)]
        #     a = f(i+1, s1 + nums[i], s2 - nums[i])
        #     b = f(i+1, s1, s2)
        #     dp[(s1, s2)] = a or b
        #     return dp[(s1, s2)]

        # return f(0, 0, sum(nums))


        # # Backtrack
        # n = len(nums)
        # def f(i, s1, s2):
        #     if i == n:
        #         return False
        #     if s1 == s2:
        #         return True
        #     a = f(i+1, s1 + nums[i], s2 - nums[i])
        #     b = f(i+1, s1, s2)
        #     return a or b
        # return f(0, 0, sum(nums))