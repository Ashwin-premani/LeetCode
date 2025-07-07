import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        heap = []
        day = 1
        i = 0
        count = 0
        
        while i < n or heap:
            if not heap:
                day = events[i][0]
            
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1

            while heap and heap[0] < day:
                heapq.heappop(heap)
            
            if heap:
                heapq.heappop(heap)  
                count += 1
            
            day += 1

        return count
