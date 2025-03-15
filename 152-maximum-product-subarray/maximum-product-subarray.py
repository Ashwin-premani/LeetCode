class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        p = 1
        ans = 0
        for i in nums:
            if i != 0:
                p *= i
                ans = max(ans,p)
            else:
                p = 1
        p = 1
        for i in reversed(nums):
            if i != 0:
                p *= i
                ans = max(ans,p)
            else:
                p = 1
        return ans
        # # Brute Force
        # if not nums:
        #     return 0
            
        # max_product = nums[0]
        
        # for i in range(len(nums)):
        #     current_product = 1
        #     for j in range(i, len(nums)):
        #         current_product *= nums[j]
        #         max_product = max(max_product, current_product)
                
        # return max_product