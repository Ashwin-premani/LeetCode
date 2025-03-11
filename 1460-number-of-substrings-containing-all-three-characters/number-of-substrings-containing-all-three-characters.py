class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        res = 0
        hash = defaultdict(int)
        for r in range(len(s)):
            hash[s[r]] += 1
            
            while len(hash) == 3:
                res += len(s) - r
                
                hash[s[l]] -= 1
                if hash[s[l]] == 0:
                    del hash[s[l]]
                l += 1
        return res

        # brute force
        # res = 0
        # for l in range(len(s)):
        #     hash = defaultdict(int) 
        #     for r in range(l,len(s)):
        #         if s[r] in 'abc':
        #             hash[s[r]] += 1
        #             if len(hash) == 3:
        #                 res += 1
        # return res