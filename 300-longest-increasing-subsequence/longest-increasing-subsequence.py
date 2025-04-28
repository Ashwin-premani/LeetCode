class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(n)
        n = len(nums)
        dp = [1] * n
        m = 1
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
            m = max(m, dp[i])
        return m

        # Tabulation space optimized time : O(n^2) and space : O(2n)
        n = len(nums)
        prev = [0] * (n+1)
        cur = [0] * (n+1)
        for i in range(n-1, -1, -1):
            for j in range(i-1, -2, -1):
                not_take = prev[j+1]
                take = 0
                if j == -1 or nums[i] > nums[j]:
                    take = 1 + prev[i+1]
                cur[j+1] = max(not_take, take)
            prev = cur.copy()
        return prev[0]



        # Memoization
        n = len(nums)
        dp = [[-1] * (n+1) for i in range(n+1)]
        def f(i, j):
            if i == n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            not_take = f(i + 1, j)

            take = 0
            if j == -1 or nums[i] > nums[j]:
                take = 1 + f(i + 1, i)
            dp[i][j] = max(take, not_take)
            return dp[i][j]
        return f(0, -1)
            
        # Tabulation
        lst = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    lst[i] = max(lst[i],1+lst[j])
        return max(lst)