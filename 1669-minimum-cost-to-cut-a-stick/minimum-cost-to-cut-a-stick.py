class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # Add start and end of stick
        cuts = [0] + sorted(cuts) + [n]
        c = len(cuts)

        # Memoization table
        dp = [[0] * c for _ in range(c)]

        # Bottom-up DP
        for length in range(2, c):  # segment length
            for i in range(c - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    cost = cuts[j] - cuts[i] + dp[i][k] + dp[k][j]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[0][c - 1]
