class Solution:
    def possibleStringCount(self, word: str) -> int:
        # Little optimized using for loop
        count = 1
        res = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                count += 1
            else:
                if count > 1:
                    res += (count - 1)
                count = 1
        if count > 1:
            res += (count - 1)
        return res

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