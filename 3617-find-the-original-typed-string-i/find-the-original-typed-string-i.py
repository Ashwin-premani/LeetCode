class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        res = 1
        i = 0
        while i < n:
            j = i
            while j < n and word[i] == word[j]:
                j += 1
            length = j - i
            if length > 1:
                res += (length - 1)
            i = j
        return res