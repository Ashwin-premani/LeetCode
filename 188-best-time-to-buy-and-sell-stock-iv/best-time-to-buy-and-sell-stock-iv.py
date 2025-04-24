from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
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
