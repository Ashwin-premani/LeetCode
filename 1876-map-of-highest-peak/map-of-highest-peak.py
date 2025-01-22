class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        q = deque() # (r, c)

        res = [[-1] * cols for _ in range(rows)]
        # enqueue all water cells
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c]:
                    q.append((r, c))
                    res[r][c] = 0
            
        # BFS
        while q:
            r, c = q.popleft()
            h = res[r][c]

            neighbors = [[r+1, c], [r,c + 1], [r - 1, c],[r, c-1]]
            for nr, nc in neighbors:
                if nr < 0 or nc < 0 or nr == rows or nc == cols or res[nr][nc] != -1:
                    continue
                q.append((nr, nc))
                res[nr][nc] = h + 1
        return res

