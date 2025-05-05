class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b, c = 1, 1, 2
        for i in range(3, n+1):
            cur = (2 * c + a) % mod
            a, b, c = b, c, cur
        return c



        # Tabulation space optimized
        mod = 10**9 + 7
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        a, b, c = 1, 1, 2
        for i in range(3, n+1):
            cur = (2 * c + a) % mod
            a, b, c = b, c, cur
        return c


        # Memoization
        mod = 10**9 + 7
        memo = {}

        def dp(k):
            if k in memo:
                return memo[k]
            if k == 0:
                return 1
            if k == 1:
                return 1
            if k == 2:
                return 2
            memo[k] = (2 * dp(k - 1) + dp(k - 3)) % mod
            return memo[k]

        return dp(n)

        # recursion
        mod = 10**9 + 7

        @lru_cache(None)
        def dp(k):
            if k == 0:
                return 1
            if k == 1:
                return 1
            if k == 2:
                return 2
            return (2 * dp(k - 1) + dp(k - 3)) % mod

        return dp(n)


        # Tabulation
        mod = 10**9 + 7
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = (2 * dp[i-1] + dp[i-3]) % mod
        return dp[n]