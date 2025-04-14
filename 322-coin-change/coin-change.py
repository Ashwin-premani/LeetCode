class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Tabulation
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]
        for a in range(amount+1):
            if a % coins[0] == 0:
                dp[0][a] = a / coins[0]
            else:
                dp[0][a] = float('inf')
        
        for i in range(1, n):
            for a in range(amount+1):
                not_take = dp[i-1][a]
                take = float('inf')
                if coins[i] <= a:
                    take = 1 + dp[i][a- coins[i]]
                dp[i][a] = min(not_take, take)
                
        res = dp[n-1][amount]
        return -1 if res >= float('inf') else int(res)

        # Memoization
        # dp = {}
        # def f(i, a):
        #     if i == 0:
        #         if a % coins[0] == 0:
        #             return a // coins[0]
        #         else:
        #             return float('inf')
        #     if a < 0:
        #         return float('inf')
        #     if (i, a) in dp:
        #         return dp[(i, a)]
            
        #     not_take = f(i - 1, a)
        #     take = float('inf')
        #     if coins[i] <= a:
        #         take = 1 + f(i, a - coins[i])
        #     dp[(i, a)] = min(not_take, take)
        #     return dp[(i, a)]
        # res = f(len(coins) - 1, amount)
        # return -1 if res == float('inf') else res
