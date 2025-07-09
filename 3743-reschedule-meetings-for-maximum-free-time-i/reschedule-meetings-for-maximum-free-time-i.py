class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        free = []
        last = 0

        for i in range(n):
            free.append(startTime[i] - last)
            last = endTime[i]
        free.append(eventTime - endTime[-1])  

        m = len(free)
        window_size = k + 1

        if window_size >= m:
            return sum(free)

        curr_sum = sum(free[:window_size])
        max_sum = curr_sum

        for i in range(window_size, m):
            curr_sum = curr_sum - free[i - window_size] + free[i]
            max_sum = max(max_sum, curr_sum)

        return max_sum



        free = []
        last = 0
        for i in range(len(startTime)):
            free.append(startTime[i] - last)
            last = endTime[i]
        free.append(eventTime - endTime[-1])
        
        if k + 1 > len(free):
            return sum(free) 

        curr_sum = sum(free[:k+1])
        max_sum = curr_sum

        for r in range(k+1, len(free)):
            curr_sum = curr_sum - free[r - k - 1] + free[r]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
