class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Find first non-negative number (binary search)
        left = 0
        right = len(nums) - 1
        first_non_negative = len(nums)  
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:  
                first_non_negative = mid
                right = mid - 1
        
        neg_count = first_non_negative  
        
        left = 0
        right = len(nums) - 1
        first_positive = len(nums)  
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= 0:
                left = mid + 1
            else: 
                first_positive = mid
                right = mid - 1
        
        pos_count = len(nums) - first_positive
        
        return max(neg_count, pos_count)



        # # O(n) linear 
        # n = 0
        # p = 0 
        # for i in nums:
        #     if i < 0:
        #         n += 1
        #     if i > 0:
        #         p += 1
        # return max(n,p)