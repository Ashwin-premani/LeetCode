class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Tabulation using 4 vars
        n = len(prices)
        ahead_buy = 0
        ahead_not_buy = 0
        cur_buy = 0
        cur_not_buy = 0

        for i in range(n - 1, -1, -1):
            cur_buy = max(-prices[i] + ahead_not_buy, ahead_buy)
            cur_not_buy = max(prices[i] + ahead_buy, ahead_not_buy)
            
            ahead_buy = cur_buy
            ahead_not_buy = cur_not_buy

        return ahead_buy

        # tabulation with 2 list(1x2) or 4 variables
        n = len(prices)
        ahead = [0] * 2
        cur = [0] * 2
        for i in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[i] + ahead[0], ahead[1])
                else:
                    profit = max(prices[i] + ahead[1], ahead[0])
                cur[buy] = profit
            ahead = cur.copy()
        return ahead[1]


        # tabulation
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[n][0], dp[n][1] = 0, 0
        for i in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[i] + dp[i + 1][0], dp[i + 1][1])
                else:
                    profit = max(prices[i] + dp[i + 1][1], dp[i + 1][0])
                dp[i][buy] = profit
        return dp[0][1]

        # Memoization other way
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