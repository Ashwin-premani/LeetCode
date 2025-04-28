class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        s = 0
        res = 0

        for r in range(len(nums)):
            s += nums[r]
            while (r - l + 1) * s >= k and l <= r:
                s -= nums[l]
                l += 1
            res += r - l + 1
        return res