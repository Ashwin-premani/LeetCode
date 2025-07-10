class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        free = []
        last = 0
        for i in range(len(startTime)):
            free.append(startTime[i] - last)
            last = endTime[i]
        free.append(eventTime - last)
        res = max(free)
        n = len(free)
        right = [0] * n
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1], free[i+1])
        left = [0] * n
        for i in range(1, n):
            left[i] = max(left[i-1], free[i-1])
        
        res = 0
        for i in range(1, n):
            cur = endTime[i-1] - startTime[i-1]
            if cur <= max(left[i-1], right[i]):
                res = max(res, cur + free[i] + free[i-1])
            else:
                res = max(res, free[i] + free[i-1])
        return res