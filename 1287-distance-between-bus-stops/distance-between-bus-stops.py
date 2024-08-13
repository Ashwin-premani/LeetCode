class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        dist=0
        dist2=0
        for i in range(start,destination):
            dist+=distance[i]
        total_distance = sum(distance)
        dist2=total_distance-dist
        return min(dist,dist2)