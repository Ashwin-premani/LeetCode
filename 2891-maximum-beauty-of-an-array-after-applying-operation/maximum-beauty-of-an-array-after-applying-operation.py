class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        res = 1
        for r in range(len(nums)):
            while (nums[r] - nums[l]) > (2*k):
                l += 1
            res = max(res,r - l + 1)
        return res
            