class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = 1
        suff = 1
        ans = float('-inf')
        n = len(nums)
        
        for i in range(n):
            # Reset pre to 1 if it becomes 0
            if pre == 0:
                pre = 1
            # Reset suff to 1 if it becomes 0
            if suff == 0:
                suff = 1
                
            # Calculate prefix product from left to right
            pre = pre * nums[i]
            
            # Calculate suffix product from right to left
            suff = suff * nums[n-1-i]
            
            # Update the answer with maximum of current pre, suff, and previous ans
            ans = max(ans, max(pre, suff))
            
        return ans

        
        # pre, suff = 1, 1
        # ans = min(nums)
        # n = len(nums)
        # for i in range(n):
        #     if pre == 0:
        #         pre = 1
        #     if suff == 0:
        #         suff = 1
        #     pre = pre * nums[i]
        #     suff = suff * nums[n - i - 1]
        #     ans = max(pre, suff, ans)
        # return ans
        
        # if len(nums) == 1:
        #     return nums[0]
        # p = 1
        # ans = 0
        # for i in nums:
        #     if i != 0:
        #         p *= i
        #         ans = max(ans,p)
        #     else:
        #         p = 1
        # p = 1
        # for i in reversed(nums):
        #     if i != 0:
        #         p *= i
        #         ans = max(ans,p)
        #     else:
        #         p = 1
        # return ans


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