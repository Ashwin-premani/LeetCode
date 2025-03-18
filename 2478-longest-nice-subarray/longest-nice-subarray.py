class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        a = 0
        l = 0
        res = 1
        for r in range(len(nums)):
            while a & nums[r]: # here we have a which is or of all prev elements which means all 1's with position
                a ^= nums[l]  # doing xor to remove or of removed element
                l += 1         
            
            a |= nums[r]  # or operation to have all 1's position to check if next eleemts satisfies & 
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