class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
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
        t = s[::-1]
        return longestCommonSubsequence(self, s, t)
        
        
        def is_palindrome(a):
            i = 0
            j = len(a) - 1
            while i <= j:
                if a[i] != a[j]:
                    return False
                i += 1
                j += 1
            return True

        def f(i):
            if i < 0:
                return 0
            
