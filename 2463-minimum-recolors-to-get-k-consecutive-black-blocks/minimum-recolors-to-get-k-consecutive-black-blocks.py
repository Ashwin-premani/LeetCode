class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        m = 0
        l = 0
        res = k
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                m += 1 
            if (r - l + 1) == k:
                print(m)
                res = min(res, m)
                if blocks[l] == 'W':
                    m -= 1
                l += 1
        return res
            
            