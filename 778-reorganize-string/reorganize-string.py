class Solution:
    def reorganizeString(self, s: str) -> str:
        hash = Counter(s)
        heap = []
        n = len(s)
        for i, v in hash.items():
            if v > (n + 1) // 2:
                return ""
            heapq.heappush(heap, (-v, i))
        max_heap = [(-v, k) for k, v in hash.items()]
        heapq.heapify(max_heap)

        res = []
        prev = (0, '')  # (count, char)

        while max_heap:
            cnt, char = heapq.heappop(max_heap)
            res.append(char)

            if prev[0] < 0:
                heapq.heappush(max_heap, prev)

            prev = (cnt + 1, char)  

        return ''.join(res)