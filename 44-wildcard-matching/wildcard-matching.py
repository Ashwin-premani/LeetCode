class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Tabulation space optimization
        n = len(s)
        m = len(p)
        prev = [False] * (m+1)
        prev[0] = True
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 1]
            else:
                prev[j] = False
                
        cur = [False] * (m+1)
        for i in range(1, n+1):
            cur[0] = False
            for j in range(1, m+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    cur[j] = prev[j-1]
                elif p[j-1] == '*':
                    cur[j] = prev[j] or cur[j-1]
                else:
                    cur[j] = False
            prev = cur.copy()
                
        return prev[m]

        # Tabulation
        n = len(s)
        m = len(p)
        dp = [[False] * (m+1) for _ in range(n+1)]
        dp[0][0] = True
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
            else:
                dp[0][j] = False

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = False
                
        return dp[n][m]


        # Memoization
        n = len(s)
        m = len(p)
        dp = {}
        def f(i, j):
            if i == 0 and j == 0:
                return True

            if j == 0 and i > 0:
                return False
            if (i, j) in dp:
                return dp[(i, j)]

                if i == 0:
                    for k in range(j):
                        if p[k] != '*':
                            return False
                    return True

            if s[i-1] == p[j-1] or p[j-1] == '?':
                dp[(i, j)] = f(i-1, j-1)
            elif p[j-1] == '*':
                dp[(i, j)] = f(i-1, j) or f(i, j-1)
            else:
                dp[(i, j)] = False

            return dp[(i, j)]

        return f(n, m)
