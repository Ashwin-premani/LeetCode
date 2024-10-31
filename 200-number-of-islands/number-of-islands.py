class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visits = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            visits.add((r, c))
            q.append((r, c))
            directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and (nr, nc) not in visits:
                        visits.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visits:
                    bfs(r, c)
                    islands += 1

        return islands