class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                L = len(words[i])
                if words[i] == words[j][:L] and words[i] == words[j][-L:]:
                    res += 1
        return res