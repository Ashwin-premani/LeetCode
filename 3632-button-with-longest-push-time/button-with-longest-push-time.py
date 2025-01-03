class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        n = len(events)
        
        if n == 1:
            return events[0][0]
        
        max_time = events[0][1]
        index = events[0][0]
        
        for i in range(1, n):
            time_diff = events[i][1] - events[i-1][1]
            
            if time_diff > max_time:
                max_time = time_diff
                index = events[i][0]
            elif time_diff == max_time and events[i][0] < index:
                index = events[i][0]
        
        return index