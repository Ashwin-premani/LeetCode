class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        m = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > m:
                m = nums[i]
                continue
            for k in range(i + 1, len(nums)):
                res = max(res, (m - nums[i]) * nums[k])
        return res


        # brute Force
        # res = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             res = max(res, (nums[i] - nums[j]) * nums[k])
        # return res