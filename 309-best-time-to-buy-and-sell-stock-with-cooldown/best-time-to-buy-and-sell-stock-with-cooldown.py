class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        front2 = [0, 0]
        front1 = [0, 0]
        cur = [0, 0]

        for ind in range(n - 1, -1, -1):
            # When we can buy (buy = 1)
            cur[1] = max(-prices[ind] + front1[0], front1[1])

            # When we can sell (buy = 0)
            cur[0] = max(prices[ind] + front2[1], front1[0])

            front2 = front1[:]
            front1 = cur[:]

        return cur[1]

        # tabulation
        n = len(prices)
        if n == 0:
            return 0
        
        ahead = [0, 0] 
        after_cooldown = 0 
        
        for i in range(n - 1, -1, -1):
            cur = [0, 0]
            buy = -prices[i] + ahead[1]
            skip = ahead[0]
            cur[0] = max(buy, skip)
            
            sell = prices[i] + after_cooldown
            skip = ahead[1]
            cur[1] = max(sell, skip)

            after_cooldown = ahead[0]
            ahead = cur[:]
        
        return ahead[0]


        # Memoization
        dp = {}
        def f(i, holding):
            if i >= len(prices):
                return 0
            if (i, holding) in dp:
                return dp[(i, holding)]
            if holding:
                sell = prices[i] + f(i + 2, False)
                skip = f(i + 1, True)
                dp[(i, holding)] = max(sell, skip)
            else:
                buy = -prices[i] + f(i + 1, True)
                skip = f(i + 1, False)
                dp[(i, holding)] = max(buy, skip)
            return dp[(i, holding)]
        
        return f(0, False)
