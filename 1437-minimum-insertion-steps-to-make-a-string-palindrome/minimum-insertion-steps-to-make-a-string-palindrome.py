class Solution:
    def minInsertions(self, s: str) -> int:
        def longestPalindromeSubseq(self, s: str) -> int:
            def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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
            t = s[::-1]
            return longestCommonSubsequence(self, s, t)
        return len(s) - longestPalindromeSubseq(self, s)