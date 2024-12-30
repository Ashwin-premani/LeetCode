class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using heap
        heap = []
        heapify(heap)
        for i in nums:
            heapq.heappush(heap, -i)
        for i in range(k - 1):
            heapq.heappop(heap)
        return -heap[0]


        # baisc approach 
        # nums=sorted(nums)
        # n=len(nums)
        # return nums[n-k]