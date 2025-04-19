class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        # Tabulation
        def longestPalindromeSubseq(self, s: str, t: str) -> int:
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
            return longestCommonSubsequence(self, s, t)
        val = longestPalindromeSubseq(self, word1, word2)
        return (len(word1) - val) + (len(word2) - val) 