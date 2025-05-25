class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mp = {}
        result = 0

        for word in words:
            reversed_word = word[::-1]
            if mp.get(reversed_word, 0) > 0:
                result += 4
                mp[reversed_word] -= 1
            else:
                mp[word] = mp.get(word, 0) + 1

        for word, count in mp.items():
            if word[0] == word[1] and count > 0:
                result += 2
                break

        return result


        
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
