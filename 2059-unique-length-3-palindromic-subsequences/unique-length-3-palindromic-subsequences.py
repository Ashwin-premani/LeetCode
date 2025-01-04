class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)
        for c in s:
            right[c] -= 1
            for i in left:
                if right[i] > 0:
                    res.add((c, i))
            left.add(c)

        return len(res)