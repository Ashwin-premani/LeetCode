class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Tabulation
        n = len(prices)
        dp = [[[0] * 3 for _ in range((2))]for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for b in range(2):
                for t in range(2,-1,-1):
                    if b:
                        sell = prices[i] + dp[i+1][0][t+1] if t < 2 else 0
                        skip = dp[i+1][1][t]
                        dp[i][1][t] = max(sell, skip)
                    else:
                        buy = -prices[i] + dp[i+1][1][t]
                        skip = dp[i+1][0][t]
                        dp[i][0][t] = max(buy, skip)
        return dp[0][0][0]
                    

        # LRu cache
        @lru_cache(maxsize=None)
        def f(i, holding, t):
            if t == 2 or i == len(prices):
                return 0
            if holding:
                sell = prices[i] + f(i + 1, 0, t + 1)
                skip = f(i + 1, 1, t)
                return max(sell, skip)
            else:
                buy = -prices[i] + f(i + 1, 1, t)
                skip = f(i + 1, 0, t)
                return max(buy, skip)

        return f(0, 0, 0)
        # Memoization
        dp = {}
        def f(i, holding, t):
            if t == 2:
                return 0
            if i == len(prices):
                return 0
            if (i, holding, t) in dp:
                return dp[(i, holding, t)]
            if holding:
                sell = prices[i] + f(i + 1, False, t + 1)
                skip = f(i + 1, True, t)
                dp[(i, holding, t)] = max(sell, skip)
                return dp[(i, holding, t)]
            else:
                buy = -prices[i] + f(i + 1, True, t)
                skip = f(i + 1, False, t)
                dp[(i, holding, t)] = max(buy, skip)
                return dp[(i, holding, t)]

        return f(0, False, 0)