class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Now to optimize this instead of checking each number we can check twice that is for tops[0] and bottoms[0] making it O(2n) ~ O(n) (small optimization from last)
        def check(num):
            top = 0
            bottom = 0
            for i in range(len(tops)):
                if tops[i] != num and bottoms[i] != num:
                    return float('inf')
                elif tops[i] == num and bottoms[i] != num:
                    bottom += 1
                elif tops[i] != num and bottoms[i] == num:
                    top += 1
            return min(top, bottom)

        res = min(check(tops[0]), check(bottoms[0]))
        return res if res != float('inf') else -1

        

        # brute Force (trying every number from 1 to 6 and taking min and valid)
        # O(6n) ~ O(n)
        res = float('inf')
        for i in range(1, 7):
            top = 0
            bottom = 0
            for j in range(len(tops)):
                if tops[j] != i and bottoms[j] != i:
                    break
                if tops[j] != i and bottoms[j] == i:
                    top += 1
                elif tops[j] == i and bottoms[j] != i:
                    bottom += 1
            else:
                res = min(res, top, bottom)
        return res if res != float('inf') else -1
