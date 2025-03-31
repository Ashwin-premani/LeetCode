class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0

        split = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        
        max_score = weights[0] + weights[-1] + sum(heapq.nlargest(k - 1, split))
        min_score = weights[0] + weights[-1] + sum(heapq.nsmallest(k - 1, split))
        
        return max_score - min_score

        
        # # Using sort
        # if k == 1:
        #     return 0
        # split = [weights[i] + weights[i+1] for i in range(len(weights) - 1)]
        # split.sort()
        # i = k - 1
        # max_score = weights[0] + weights[-1] + sum(split[-i:])
        # min_score = weights[0] + weights[-1] + sum(split[:i])
        # return max_score - min_score


        # Wrong answer after 10 test cases because k is not considered
        # max_score = float('-inf')  # Start with negative infinity for max
        # min_score = float('inf')   # Start with positive infinity for min
        # left = weights[0]
        # right = weights[-1]

        # for i in range(len(weights) - 1):  # Use 'i' instead of 'r'
        #     l = left + weights[i]  # Corrected left-side calculation
        #     r = right + weights[i + 1]     # Corrected right-side calculation
            
        #     max_score = max(max_score, l + r)
        #     min_score = min(min_score, l + r)

        # return max_score - min_score
