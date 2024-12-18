class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        j = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices