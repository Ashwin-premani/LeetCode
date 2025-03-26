class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # Tabulation
        n = len(grid)
        m = len(grid[0])
        dp = [[[-1] * m for _ in range(m)] for _ in range(n)]
        for j1 in range(m):
            for j2 in range(m):
                if  j1 == j2:
                    dp[n-1][j1][j2] = grid[n-1][j1]
                else:
                    dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2]
        dj = [-1, 0, 1]
        for i in range(n-2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    maxi = float('-inf')
                    for dj1 in dj:
                        for dj2 in dj:
                            if  j1 == j2:
                                value = grid[i][j1]
                            else:
                                value =  grid[i][j1] + grid[i][j2]
                            if 0 <= j1+dj1 < m and 0 <= j2+dj2 < m:
                                value += dp[i+1][j1+dj1][j2+dj2]
                            else:
                                value = float('-inf')
                            maxi = max(maxi, value)
                    dp[i][j1][j2] = maxi

        return dp[0][0][m-1]


        # Meomoization
        # n = len(grid)
        # m = len(grid[0])
        # dp = [[[-1] * m for _ in range(m)] for _ in range(n)]
        # def f(i, j1, j2):
        #     if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
        #         return float('-inf')
        #     if i == n - 1:
        #         if j1 == j2:
        #             return grid[i][j1]
        #         else:
        #             return grid[i][j1] + grid[i][j2]
        #     if dp[i][j1][j2] != -1:
        #         return dp[i][j1][j2]
        #     dj = [-1, 0, 1]
        #     maxi = 0
        #     for dj1 in dj:
        #         for dj2 in dj:
        #             if  j1 == j2:
        #                 value = grid[i][j1]
        #             else:
        #                 value =  grid[i][j1] + grid[i][j2]
        #             value += f(i+1, dj1 + j1, dj2 + j2)
        #             maxi = max(maxi, value)
        #     dp[i][j1][j2] = maxi
        #     return dp[i][j1][j2]
        # return f(0, 0, m-1)
        

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