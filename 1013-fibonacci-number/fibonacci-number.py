class Solution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n + 1)
        def helper(n):
            if dp[n] != -1:
                return dp[n]
            if n <= 1:
                return n
            dp[n] = helper(n-1) + helper(n-2)
            return dp[n]
        return helper(n)

        memo = {}

        def helper(n):
            if n in memo:
                return memo[n]
            if n <= 1:
                return n
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        return helper(n)

        # recursion
        # if n <= 1:
        #     return n
        # return self.fib(n-1) + self.fib(n-2)
