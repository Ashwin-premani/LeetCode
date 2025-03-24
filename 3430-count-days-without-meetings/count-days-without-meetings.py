from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev_end = -1
        occupied = 0

        for s, e in meetings:
            if s > prev_end:
                occupied += e - s + 1
                prev_end = e
            else:
                if e > prev_end:
                    occupied += e - prev_end
                    prev_end = e

        return days - occupied



        # Passed TLE but Memory Limit exceeded
        # meetings.sort()  
        # res = set() 
        # prev = 0

        # for s, e in meetings:
        #     if s > prev:
        #         res.update(range(s, e + 1))
        #     else:
        #         res.update(range(prev, e + 1))
        #     prev = max(prev, e)  

        # return days - len(res)  


        # Time Limit Exceeded
        # res = set(range(1, days+1))
        # for s, e in meetings:
        #     for i in range(s, e+1):
        #         res.discard(i)
        # return len(res)