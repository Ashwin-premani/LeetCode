class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        heapify(dist)
        def eucledian(x,y):
            return math.sqrt((abs(y[0]-x[0]))**2+(abs(y[1]-x[1]))**2)
        res = []
        for i, p in enumerate(points):
            heapq.heappush(dist, (eucledian(p,[0,0]), i))
        print(dist)
        while k:
            d, idx = heapq.heappop(dist)
            res.append(points[idx]) 
            k -= 1
        return res