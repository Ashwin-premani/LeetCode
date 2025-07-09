class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
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
