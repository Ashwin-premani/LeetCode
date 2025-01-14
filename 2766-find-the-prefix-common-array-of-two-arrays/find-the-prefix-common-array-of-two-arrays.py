class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        count = 0
        c = collections.Counter()
        for x, y in zip(A, B):
            c[x] -= 1
            c[y] += 1
            if c[x] == 0:
                count += 1
            if c[y] == 0:
                count += 1
            if x == y:
                count -= 1
            ans.append(count)
        return ans

        # n = len(A)
        
        # C = [0] * n
        # seta, setb = set(), set()
        # for i in range(n):
        #     C[i] = C[i - 1]
        #     if A[i] == B[i]:
        #         C[i] += 1
        #     else:
        #         if A[i] in setb:
        #             C[i] += 1
        #         if B[i] in seta:
        #             C[i] += 1
        #         seta.add(A[i])
        #         setb.add(B[i])
        # return C




        # C = collections.Counter()

        # ans = []
        # for x, y in zip(A, B):
        #     C[x] += 1
        #     C[y] += 1

        #     ans.append(sum(1 for x in C.keys() if C[x] == 2))
        # return ans