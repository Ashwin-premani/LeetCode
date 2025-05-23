class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Optimized : Dictionary lookup is O(1)
        words.sort(key=len)
        dp = {}
        maxi = 1
    
        for word in words:
            dp[word] = 1  # Every word can at least be a chain of length 1
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
            maxi = max(maxi, dp[word])
            
        return maxi
        # tabulation
        words.sort(key=len)
        n = len(words)
        dp = [1] * n
        maxi = 1
        lastIndex = 0
        def check(s1, s2):
            if len(s1) !=  len(s2) + 1:
                return False
            i = 0
            j = 0
            while i < len(s1):
                if j < len(s2) and s1[i] == s2[j]:
                    i +=1
                    j += 1
                else:
                    i += 1
            if i == len(s1) and j == len(s2):
                return True
            return False

        for i in range(n):
            for prev in range(i):
                if check(words[i], words[prev]) and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
            if dp[i] > maxi:
                maxi = dp[i]
        return maxi
