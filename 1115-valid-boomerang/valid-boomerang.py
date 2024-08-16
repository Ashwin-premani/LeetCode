class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        def slope(p1,p2):
            return (p2[1]-p1[1],p2[0]-p1[0])
        
        dx1 ,dy1=slope(points[0],points[1])
        dx2, dy2=slope(points[1],points[2])

        return dx1*dy2 !=dy1*dx2