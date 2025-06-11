class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # Memoization
        cuts = [0] + sorted(cuts) + [n]
        c = len(cuts)

        dp = {}

        def dfs(i, j):
            if j - i <= 1:  # no space to cut
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            min_cost = float('inf')
            for k in range(i + 1, j):
                cost = cuts[j] - cuts[i] + dfs(i, k) + dfs(k, j)
                min_cost = min(min_cost, cost)

            dp[(i, j)] = min_cost
            return min_cost

        return dfs(0, c - 1)



        # Tabulation
        cuts = [0] + sorted(cuts) + [n]
        c = len(cuts)

        dp = [[0] * c for _ in range(c)]

        for length in range(2, c):  # segment length
            for i in range(c - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    cost = cuts[j] - cuts[i] + dp[i][k] + dp[k][j]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[0][c - 1]
