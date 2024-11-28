class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        inf = 10**20
        h = []
        heapq.heappush(h,(0,0,0)) #(heap,(distance,x co-ord,y co-ord))
        distances = [[inf] * c for i in range(r)]

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while len(h) > 0:
            d,x,y = heapq.heappop(h)
            if d > distances[x][y]:
                continue
            for dx,dy in directions:
                nx,ny = x + dx, y + dy

                if 0 <= nx < r and 0 <= ny < c:
                    nd = d

                    if grid[nx][ny] == 1:
                        nd += 1
                    if distances[nx][ny] > nd:
                        distances[nx][ny] = nd
                        heapq.heappush(h,(nd,nx,ny))
        return distances[r-1][c-1]