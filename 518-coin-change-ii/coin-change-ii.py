from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
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
