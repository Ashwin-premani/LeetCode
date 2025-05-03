class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
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
