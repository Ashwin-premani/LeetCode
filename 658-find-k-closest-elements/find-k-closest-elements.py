class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        heapify(heap)
        for num in arr:
            diff = abs(x - num)
            heapq.heappush(heap, (diff, num))

        result = sorted([heapq.heappop(heap)[1] for _ in range(k)])
        return result