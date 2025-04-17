class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        prev = [0] * (m + 1)
        for i in range(1, n + 1):
            cur = [0] * (m+1)
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    cur[j] = 1 + prev[j - 1]
                else:
                    cur[j] = max(prev[j], cur[j - 1])
            prev = cur.copy()
                    
        return prev[m]


        # Tabulation
        n = len(text1)
        m = len(text2)
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        return dp[n][m]


        # Memoization
        dp = {}
        def f(i, j):
            if i < 0 or j < 0:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + f(i-1, j-1)
                return dp[(i, j)]
            else:
                dp[(i, j)] = max(f(i-1, j), f(i, j-1))
                return dp[(i, j)]
            
        return f(len(text1)-1, len(text2) - 1)