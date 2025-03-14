class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        l = 1
        r = sum(candies) // k
        
        while l <= r:
            m = (l + r) // 2
            count = 0
            
            for candy in candies:
                count += candy // m
            
            if count >= k:
                l = m + 1
            else:
                r = m - 1
        
        return r  