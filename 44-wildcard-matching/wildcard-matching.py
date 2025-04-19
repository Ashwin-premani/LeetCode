class Solution:
    def isMatch(self, s: str, p: str) -> bool:
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
