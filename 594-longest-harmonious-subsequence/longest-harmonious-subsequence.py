class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        l = 0
        while l < n:
            r = l
            while r < n and nums[r] - nums[l] <= 1:
                r += 1
            if nums[r-1] - nums[l] == 1:
                res = max(res, r - l)
            l += 1
        
        return res