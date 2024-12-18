class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Monotonic increasing stack O(n)
        # intution is to pop elemets whenever smaller element is encountere 
        # till that element is larger that element below it
        stack = [] # Monotonic stack (index (value in increasing order))
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                prices[j] -= prices[i]
            stack.append(i)
            
        return prices


        # brute force O(n^2)
        # j = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         if prices[j] <= prices[i]:
        #             prices[i] -= prices[j]
        #             break
        # return prices