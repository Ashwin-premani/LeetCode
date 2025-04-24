class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Tabulation


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