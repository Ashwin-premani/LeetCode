class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7
        n = len(words)
        l = len(words[0])
        t = len(target)
        
        @cache
        def get_count(windex):
            f = collections.Counter()
            for i in range(n):
                f[words[i][windex]] += 1
            
            return f

        @cache
        def count(windex, tindex):
            if tindex == t:
                return 1
            if windex == l:
                return 0
            
            total = 0
            #take
            total += get_count(windex)[target[tindex]] * count(windex + 1, tindex + 1)
            total %= mod

            # no take
            total += count(windex + 1, tindex)
            total %= mod
            return total
        
        return count(0, 0) % mod