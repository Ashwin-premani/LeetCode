class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        a = 0
        l = 0
        res = 1
        for r in range(len(nums)):
            while a & nums[r]:
                a ^= nums[l]  
                l += 1         
            
            a |= nums[r]  
            res = max(res, r - l + 1) 
        return res


        # max_length = 1
        # left = 0
        # combined = 0  
        
        # for right in range(len(nums)):
        #     while combined & nums[right] != 0:
        #         combined ^= nums[left]
        #         left += 1
                
        #     combined |= nums[right]
        #     max_length = max(max_length, right - left + 1)
                
        # return max_length

        # max_length = 1
        # n = len(nums)
        
        # for start in range(n):
        #     combined = 0  
            
        #     for end in range(start, n):
        #         if combined & nums[end] != 0:
        #             break
                    
        #         combined |= nums[end]
        #         max_length = max(max_length, end - start + 1)
        
        # return max_length