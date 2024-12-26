class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # optimized bottom up
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1 # (elements, sum) -> 1 way (1 way to sum to zero with first 0 elements)

        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                dp[i + 1][cur_sum + nums[i]] += count
                dp[i + 1][cur_sum - nums[i]] += count
        return dp[len(nums)][target]


        # backtrack using hash O(n * m)
        # dp = {} #(index, cur_sum)
        # def backtrack(i, cur_sum):
        #     if (i, cur_sum) in dp:
        #         return dp[(i, cur_sum)]
        #     if i == len(nums):
        #         return 1 if cur_sum == target else 0

        #     dp[(i, cur_sum)] =  (
        #         backtrack(i + 1, cur_sum + nums[i]) +
        #         backtrack(i + 1, cur_sum - nums[i])
        #     )
        #     return dp[(i, cur_sum)]
        # return backtrack(0, 0)



        # brute force backtrack O(2^n) (timeout)
        # def backtrack(i, cur_sum):
        #     if i == len(nums):
        #         return 1 if cur_sum == target else 0

        #     return (
        #         backtrack(i + 1, cur_sum + nums[i]) +
        #         backtrack(i + 1, cur_sum - nums[i])
        #     )

        # return backtrack(0, 0)

