class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # prefix sum
        vowels = ['a', 'e', 'i', 'o','u']
        ans = [0] * (len(words) + 1)
        for i,w in enumerate(words):
            v = 0
            if w[0] in vowels and w[-1] in vowels:
                v += 1
            ans[i + 1] = (
                ans[i] + v
            )
        
        res = [0] * len(queries)

        for i,q in enumerate(queries):
            l, r = q
            res[i] = ans[r + 1] - ans[l]
        return res



        # bruteforce (time limit exceeded)
        # vowels = ['a', 'e', 'i', 'o','u']
        # ans = [0] * len(words)
        # for i in range(len(words)):
        #     if words[i][0] in vowels and words[i][-1] in vowels:
        #         ans[i] = 1
        # res = []
        # for i in queries:
        #     res.append(sum(ans[i[0]:i[1] + 1]))
        # return res
