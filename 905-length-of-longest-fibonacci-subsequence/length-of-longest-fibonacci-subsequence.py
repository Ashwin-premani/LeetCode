class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        #DP
        arr_map = {n:i for i,n in enumerate(arr)}
        res = 0
        dp = [[0] * len(arr) for _ in range(len(arr))]
        for i in reversed(range(len(arr)-1)):
            for j in reversed(range(i+1, len(arr))):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                l = 2
                if nxt in arr_map:
                    l = 1 + dp[j][arr_map[nxt]]
                    res = max(res, l)

                dp[i][j] = l
        return res

        # linear
        # arr_set = set(arr)
        # res = 0
        # for i in range(len(arr)-1):
        #     for j in range(i+1, len(arr)):
        #         prev, cur = arr[i], arr[j]
        #         nxt = prev + cur
        #         l = 2
        #         while nxt in arr_set:
        #             l += 1
        #             prev, cur = cur, nxt
        #             nxt = prev + cur
        #             res = max(res, l)
        # return res