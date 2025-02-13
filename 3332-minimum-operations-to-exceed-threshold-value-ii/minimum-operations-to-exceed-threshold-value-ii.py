class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap = nums.copy()  # Create a copy to avoid modifying input
        heapify(min_heap)
        count = 0
        
        # We need at least 2 elements to perform an operation
        while len(min_heap) >= 2 and min_heap[0] < k:
            x = heappop(min_heap)
            y = heappop(min_heap)
            new_val = min(x, y) * 2 + max(x, y)
            heappush(min_heap, new_val)
            count += 1
        
        return count