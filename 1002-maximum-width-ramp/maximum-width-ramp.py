class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        m = [0] * len(nums)
        i=len(nums)-1
        prev_max=0

        for c in reversed(nums):
            m[i] = max(c, prev_max)
            prev_max = m[i]
            i-=1
        res = 0
        l = 0
        for r in range(len(nums)):
            while nums[l] > m[r]:
                l+=1
            res = max(res, r-l)

        return res