class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] =  dp[i-1][j-1]
                else:
                    replace = 1 + dp[i-1][j-1]
                    insert = 1 + dp[i][j-1]
                    delete = 1 + dp[i-1][j]
                    dp[i][j]  = min(replace, insert, delete)
        return dp[n][m]


        # Memoization
        n = len(word1)
        m = len(word2)
        dp = {}
        def f(i, j):
            if i == 0:
                return j
            if j == 0:
                return i
            if (i, j) in dp:
                return dp[(i, j)]
            if word1[i-1] == word2[j-1]:
                return f(i-1, j-1)
            replace = 1 + f(i-1, j-1)
            insert = 1 + f(i, j-1)
            delete = 1 + f(i-1, j)
            dp[(i, j)]  = min(replace, insert, delete)
            return dp[(i, j)]
        return f(n, m)