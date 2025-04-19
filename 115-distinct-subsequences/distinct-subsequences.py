class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Tabulationspace optimization
        n = len(s)
        m = len(t)
        prev = [0] * (m+1)
        prev[0] = 1
        cur = [0] * (m+1)
        for i in range(1, n+1):
            cur[0] = 1
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    cur[j] = prev[j-1] + prev[j]
                else:
                    cur[j] = prev[j]
            prev = cur.copy()
        return prev[m]

        # Tabulation 
        n = len(s)
        m = len(t)
        dp = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][m]
        

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