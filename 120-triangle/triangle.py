class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)  
        dp = [[-1] * len(row) for row in triangle]
        def f(i, j):
            if i == n - 1:
                return triangle[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            right = triangle[i][j] + f(i+1, j+1)
            down = triangle[i][j] + f(i+1, j)
            dp[i][j] = min(right, down)
            return dp[i][j]
        return f(0, 0)