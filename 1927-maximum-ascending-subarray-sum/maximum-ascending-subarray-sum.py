class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                s += nums[i]
            else:
                s = nums[i]
            res = max(s, res)
        return res