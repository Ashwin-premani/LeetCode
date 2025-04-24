class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for holding in range(2):
                if holding:
                    dp[i][1] = max(prices[i] + dp[i + 1][0], dp[i + 1][1])
                else:
                    dp[i][0] = max(-prices[i] + dp[i + 1][1], dp[i + 1][0])
                    
        return dp[0][0]

        # Memoization
        dp = {}
        def f(i, holding):
            if i == len(prices):
                return 0
            if (i, holding) in dp:
                return dp[(i, holding)]
            if holding:
                sell = prices[i] + f(i + 1, False)
                skip = f(i + 1, True)
                dp[(i, holding)] = max(sell, skip)
                return dp[(i, holding)]
            else:
                buy = -prices[i] + f(i + 1, True)
                skip = f(i + 1, False)
                dp[(i, holding)] = max(buy, skip)
                return dp[(i, holding)]

        return f(0, False)


        # Linear
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i-1]
        return profit