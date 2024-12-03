class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums = sorted(nums)
        m = 0
        for i in range(len(nums) - 1):
            m = max(m,abs(nums[i] - nums[i + 1]))
        return m
