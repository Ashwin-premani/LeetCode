class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Tabulation wit space optimization
        n = len(triangle)
        prev = triangle[-1][:]  # Initialize with the last row of the triangle

        for i in range(n - 2, -1, -1):
            cur = [0] * len(triangle[i])  # Create a current row
            for j in range(len(triangle[i])):
                down = prev[j]  # Moving downward
                diag = prev[j + 1]  # Moving diagonally
                cur[j] = triangle[i][j] + min(down, diag)  # Store the minimum path sum
            prev = cur  # Update previous row

        return prev[0]  # Top element contains the minimum path sum



        # # Optimized tabulation O(1) but rewrites given grid (should be avoided)
        # n = len(triangle)

        # # Start from the second-last row and move upwards
        # for i in range(n - 2, -1, -1):
        #     for j in range(len(triangle[i])):
        #         triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        # return triangle[0][0]


        # # Tabulation
        # n = len(triangle)
        # dp = [row[:] for row in triangle]  
        # for i in range(n - 2, -1, -1):
        #     for j in range(len(triangle[i])):
        #             diag = triangle[i][j] + dp[i+1][j+1]
        #             down = triangle[i][j] + dp[i+1][j]
        #             dp[i][j] = min(diag, down)
        # return dp[0][0]



        # # Memoization
        # n = len(triangle)  
        # dp = [[-1] * len(row) for row in triangle]
        # def f(i, j):
        #     if i == n - 1:
        #         return triangle[i][j]
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     diag = triangle[i][j] + f(i+1, j+1)
        #     down = triangle[i][j] + f(i+1, j)
        #     dp[i][j] = min(diag, down)
        #     return dp[i][j]
        # return f(0, 0)