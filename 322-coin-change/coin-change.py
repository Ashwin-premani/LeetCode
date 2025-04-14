from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def f(i, a):
            if i == 0:
                if a % coins[0] == 0:
                    return a // coins[0]
                else:
                    return float('inf')
            if a < 0:
                return float('inf')
            if (i, a) in dp:
                return dp[(i, a)]
            
            not_take = f(i - 1, a)
            take = float('inf')
            if coins[i] <= a:
                take = 1 + f(i, a - coins[i])
            dp[(i, a)] = min(not_take, take)
            return dp[(i, a)]
        res = f(len(coins) - 1, amount)
        return -1 if res == float('inf') else res
