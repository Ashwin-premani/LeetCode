class Solution:
    def minCut(self, s: str) -> int:
        # Tabulation
        n = len(s)
        dp = [0] * (n + 1)  
        dp[n] = 0

        # Precompute palindromes
        pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        for i in range(n - 1, -1, -1):
            mincost = float('inf')
            for j in range(i, n):
                if pal[i][j]:
                    cost = 1 + dp[j + 1]
                    mincost = min(cost, mincost)
            dp[i] = mincost

        return dp[0] - 1


        # Memoizarion -> TLE
        n = len(s)
        dp = [-1] * n
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        def f(i):
            if i == n:
                return 0
            if dp[i] != -1:
                return dp[i]
            mincost = float('inf')
            for j in range(i, n):
                if is_palindrome(i, j):
                    cost = 1 + f(j+1)
                    mincost = min(cost, mincost)
            dp[i] =  mincost
            return dp[i]
        return f(0) - 1


        # LRU cache -> TLE
        n = len(s)
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        @lru_cache(None)
        def f(i):
            if i == n:
                return 0
            mincost = float('inf')
            for j in range(i, n):
                if is_palindrome(i, j):
                    cost = 1 + f(j+1)
                    mincost = min(cost, mincost)
            return mincost
        return f(0) - 1