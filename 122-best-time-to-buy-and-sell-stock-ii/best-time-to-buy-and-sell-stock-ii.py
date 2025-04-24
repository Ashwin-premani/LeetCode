class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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