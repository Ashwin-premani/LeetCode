class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_length = 1
        n = len(nums)
        
        for start in range(n):
            combined = 0  
            
            for end in range(start, n):
                if combined & nums[end] != 0:
                    break
                    
                combined |= nums[end]
                max_length = max(max_length, end - start + 1)
        
        return max_length