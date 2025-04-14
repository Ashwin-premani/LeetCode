class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        n = len(arr)
        pre_cnt = [0] * 1001
        for j in range(n-1):
            for k in range(j+1, n):
                if abs(arr[j] - arr[k]) <= b:
                    r = min(arr[j] + a, arr[k] + c)
                    l = max(arr[j] - a, arr[k] - c)
                    l = max(l, 0)
                    r = min(r, 1000)
                    if l <= r:
                        res += pre_cnt[r] - (0 if l == 0 else pre_cnt[l-1])
            for i in range(arr[j], 1001):
                pre_cnt[i] += 1
        return res


        # Brute Force
        # res = 0
        # n = len(arr)
        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         for k in range(j+1, n):
        #             if (abs(arr[i] - arr[j]) <= a and 
        #                 abs(arr[j] - arr[k]) <= b and 
        #                 abs(arr[i] - arr[k]) <= c):
        #                 res += 1
        # return res