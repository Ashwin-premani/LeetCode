class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
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