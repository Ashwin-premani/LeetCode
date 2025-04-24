class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Tabulation using 4 vars
        n = len(prices)
        ahead_buy = 0
        ahead_not_buy = 0
        cur_buy = 0
        cur_not_buy = 0

        for i in range(n - 1, -1, -1):
            cur_buy = max(-prices[i] + ahead_not_buy, ahead_buy)
            cur_not_buy = max(prices[i] + ahead_buy - fee, ahead_not_buy)
            
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
                    profit = max(prices[i] + ahead[1] - fee, ahead[0])
                cur[buy] = profit
            ahead = cur.copy()
        return ahead[1]