class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash = Counter(arr)
        m = -1
        for i, v in hash.items():
            if i == v:
                m = max(m, v)

        return m