class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num,i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        while k:
            n, i = heapq.heappop(heap)
            n *= multiplier
            heapq.heappush(heap, (n, i))
            k -= 1
        res = [0] * len(nums)
        while heap:
            v, i = heapq.heappop(heap)
            res[i] = v
        return res