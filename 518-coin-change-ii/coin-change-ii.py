class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1  # 1 way to make amount 0: use no coins

        for coin in coins:
            for v in range(coin, amount + 1):
                dp[v] += dp[v - coin]

        return dp[amount]


        # tabulation with space optimization
        n = len(coins)
        prev = [0] * (amount + 1)
        for i in range(n):
            prev[0] = 1
        
        for a in range(amount + 1):
            if a % coins[0] == 0:
                prev[a] = 1

        for i in range(1,n):
            cur = [0] * (amount+1)
            for a in range(amount + 1):
                not_take = prev[a]
                take = 0
                if coins[i] <= a:
                    take = cur[a - coins[i]]
                cur[a] = take + not_take
            prev = cur.copy()
        return prev[amount]


        # tabulation
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        
        for a in range(amount + 1):
            if a % coins[0] == 0:
                dp[0][a] = 1

        for i in range(1,n):
            for a in range(amount + 1):
                not_take = dp[i - 1][a]
                take = 0
                if coins[i] <= a:
                    take = dp[i][a - coins[i]]
                dp[i][a] = take + not_take
        return dp[n-1][amount]



        # Memoization
        n = len(coins)
        dp = {}

        def f(i, a):
            if (i, a) in dp:
                return dp[(i, a)]

            if i == 0:
                if a % coins[0] == 0:
                    return 1
                else:
                    return 0

            not_take = f(i - 1, a)
            take = 0
            if coins[i] <= a:
                take = f(i, a - coins[i]) 

            dp[(i, a)] = take + not_take
            return dp[(i, a)]

        return f(n - 1, amount)
