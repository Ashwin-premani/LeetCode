class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        left = right = nums[0][0]
        min_heap = []

        for i  in range(k):
            l = nums[i]
            left = min(left,l[0])
            right = max(right,l[0])
            heapq.heappush(min_heap, (l[0],i,0))  # (n,index of list, index of n)

        res = [left,right]
        while True:
            n,i,x = heapq.heappop(min_heap)
            x+=1
            if x == len(nums[i]):
                return res
            next_val = nums[i][x]
            heapq.heappush(min_heap,(next_val,i,x))
            right = max(right,next_val)
            left = min_heap[0][0]
            if right - left < res[1] - res[0]:
                res = [left,right]
            