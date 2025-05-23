class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # Tabulation using n x 4
        n = len(prices)
        ahead = [0] * (2*k + 1)
        cur = [0] * (2*k + 1)
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n - 1))
        for i in range(n-1, -1, -1):
            for t in range(2*k-1, -1, -1):
                if t % 2 == 0:
                    # Buy
                    cur[t] = max(-prices[i] + ahead[t+1], ahead[t])
                else:
                    # Sell
                    cur[t] = max(prices[i] + ahead[t+1], ahead[t])
            ahead = cur.copy()

        return ahead[0]

        # Tabulation using n x 4
        n = len(prices)
        dp = [[0] * (2*k + 1) for _ in range(n+1)]
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n - 1))
        for i in range(n-1, -1, -1):
            for t in range(2*k-1, -1, -1):
                if t % 2 == 0:
                    # Buy
                    dp[i][t] = max(-prices[i] + dp[i+1][t+1], dp[i+1][t])
                else:
                    # Sell
                    dp[i][t] = max(prices[i] + dp[i+1][t+1], dp[i+1][t])

        return dp[0][0]

        # Memoization using n x 4
        n = len(prices)
        dp = {}
        def f(i, t):
            if i == n or t == 2*k:
                return 0
            if (i, t) in dp:
                return dp[(i, t)]
            if t % 2 == 0:
                dp[(i, t)] =  max(-prices[i] + f(i+1, t+1), f(i+1, t))
                return dp[(i, t)]
            dp[(i, t)] =  max(prices[i] + f(i+1, t+1), f(i+1, t))
            return dp[(i, t)]
        return f(0 , 0)

        # tabulation space optimized
        n = len(prices)
        if not prices or k == 0:
            return 0

        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n - 1))

        ahead = [[0] * 2 for _ in range(k + 1)]  
        cur = [[0] * 2 for _ in range(k + 1)]

        for i in range(n - 1, -1, -1):
            for txn in range(1, k + 1):
                cur[txn][0] = max(-prices[i] + ahead[txn][1], ahead[txn][0])
                cur[txn][1] = max(prices[i] + ahead[txn - 1][0], ahead[txn][1])
            ahead = [row[:] for row in cur]

        return ahead[k][0]
