class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Memoization
        m = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            cost = prices[i] - m
            profit = max(cost, profit)
            m = min(m, prices[i])
        return profit

        l,r=0,1
        profit = 0
        maxp = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(profit,  maxp)
            else:
                l = r
            r+=1

        return maxp