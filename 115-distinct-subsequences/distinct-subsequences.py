class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        

        # Memoization
        n = len(s)
        m = len(t)
        dp = {}
        def f(i, j):
            if j == 0:
                return 1
            if i == 0:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if s[i-1] == t[j-1]:
                dp[(i, j)] = f(i-1, j-1) + f(i-1, j)
                return dp[(i, j)]
            else:
                dp[(i, j)] = f(i-1, j)
                return dp[(i, j)]
        return f(n, m)