class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        # Meomoization
        n = len(grid)
        m = len(grid[0])
        dp = [[[-1] * m for _ in range(m)] for _ in range(n)]
        def f(i, j1, j2):
            if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
                return float('-inf')
            if i == n - 1:
                if j1 == j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]
            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]
            dj = [-1, 0, 1]
            maxi = 0
            for dj1 in dj:
                for dj2 in dj:
                    if  j1 == j2:
                        value = grid[i][j1]
                    else:
                        value =  grid[i][j1] + grid[i][j2]
                    value += f(i+1, dj1 + j1, dj2 + j2)
                    maxi = max(maxi, value)
            dp[i][j1][j2] = maxi
            return dp[i][j1][j2]
        return f(0, 0, m-1)
        

        # Backtrack
        # n = len(grid)
        # m = len(grid[0])
        
        # def f(i, j1, j2):
        #     if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
        #         return float('-inf')
        #     if i == n - 1:
        #         if j1 == j2:
        #             return grid[i][j1]
        #         else:
        #             return grid[i][j1] + grid[i][j2]
        #     dj = [-1, 0, 1]
        #     maxi = 0
        #     for dj1 in dj:
        #         for dj2 in dj:
        #             if  j1 == j2:
        #                 maxi = max(maxi, grid[i][j1] + f(i+1, j1+dj1, j1+dj2))
        #             else:
        #                 maxi = max(maxi, grid[i][j1] + grid[i][j2] + f(i+1, j1+dj1, j1+dj2))
        #     return maxi
        # return f(0, 0, m-1)