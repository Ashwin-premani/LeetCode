class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_count = {}
        res = 0
        has_middle = False

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        for word in word_count:
            rev = word[::-1]
            if word != rev:
                if rev in word_count:
                    pairs = min(word_count[word], word_count[rev])
                    res += pairs * 4
                    word_count[word] -= pairs
                    word_count[rev] -= pairs
            else:
                pairs = word_count[word] // 2
                res += pairs * 4
                if word_count[word] % 2 == 1:
                    has_middle = True

        if has_middle:
            res += 2

        return res
