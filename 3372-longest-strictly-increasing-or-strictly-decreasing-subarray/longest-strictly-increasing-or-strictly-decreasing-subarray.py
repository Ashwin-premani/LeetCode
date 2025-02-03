class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        dec = 1
        inc = 1
        ans = 0
        n = len(nums)
        if n == 1:
            return 1
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                inc += 1
                dec = 1
            elif nums[i - 1] > nums[i]:
                dec += 1
                inc = 1
            else:
                dec = inc = 1
            ans = max(ans, inc, dec)
        return ans