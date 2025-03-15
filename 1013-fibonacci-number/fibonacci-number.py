class Solution:
    def fib(self, n: int) -> int:
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
