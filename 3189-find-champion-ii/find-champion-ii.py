class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n

        for s,d in edges:
            incoming[d] += 1

        champions = []
        for i,n in enumerate(incoming):
            if n == 0:
                champions.append(i)
        return -1 if len(champions) > 1 else champions[0]