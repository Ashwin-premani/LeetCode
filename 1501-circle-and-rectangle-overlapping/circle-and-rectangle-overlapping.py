class Solution:
    def checkOverlap(self, radius: int, xc: int, yc: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nx = max(x1, min(x2, xc))
        ny = max(y1, min(y2, yc))

        dx = nx - xc
        dy = ny - yc

        return (dx**2 + dy**2) <= (radius**2)