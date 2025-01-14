class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = collections.Counter()

        ans = []
        for x, y in zip(A, B):
            C[x] += 1
            C[y] += 1

            ans.append(sum(1 for x in C.keys() if C[x] == 2))
        return ans