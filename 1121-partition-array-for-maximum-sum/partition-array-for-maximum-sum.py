class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Tabulation
        n = len(arr)
        dp = [-1] * (n+1)
        dp[n] = 0
        res = 0
        for i in range(n-1, -1 ,-1):
            l = 0
            maxi = float('-inf')
            for j in range(i, min(n, i+k)):
                l += 1
                maxi = max(maxi, arr[j])
                s = (l * maxi) + dp[j+1]
                res = max(s, res)
            dp[i]  = res
        return dp[0]

        # Memoization
        n = len(arr)
        dp = [-1] * n
        def f(i):
            if i == n:
                return 0
            if dp[i] != -1:
                return dp[i]
            res = 0
            l = 0
            maxi = float('-inf')
            for j in range(i, min(n, i+k)):
                l += 1
                maxi = max(maxi, arr[j])
                s = (l * maxi) + f(j+1)
                res = max(s, res)
            dp[i]  = res
            return dp[i]
        return f(0)