class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        dp = {}
        def f(i, j):
            if i == j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            mini = float('inf')
            for k in range(i, j):
                steps = (values[i-1] * values[k] * values[j]) + f(i, k) + f(k + 1, j)
                mini = min(mini, steps)
            dp[(i, j)] = mini
            return mini
        return f(1, len(values) - 1)
