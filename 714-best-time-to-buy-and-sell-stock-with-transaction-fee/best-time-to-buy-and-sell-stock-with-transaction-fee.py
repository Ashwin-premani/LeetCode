class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        ahead = [0] * 2
        cur = [0] * 2
        for i in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[i] + ahead[0], ahead[1])
                else:
                    profit = max(prices[i] + ahead[1] - fee, ahead[0])
                cur[buy] = profit
            ahead = cur.copy()
        return ahead[1]