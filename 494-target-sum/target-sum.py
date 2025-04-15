class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Memoization
        dp = {}
        def f(i, cur):
            if (i, cur) in dp:
                return dp[(i, cur)]
            if i == len(nums):
                return 1 if cur == target else 0

            s = f(i+1, cur - nums[i])
            a = f(i+1, cur + nums[i])
            dp[(i, cur)] = a + s
            return dp[(i, cur)]
        return f(0, 0)



        # optimized bottom up and space
        dp = defaultdict(int)

        dp[0] = 1 # (sum) -> 1 way (1 way to sum to zero with first 0 elements)

        for i in range(len(nums)):
            next = defaultdict(int)
            for cur_sum, count in dp.items():
                next[cur_sum + nums[i]] += count
                next[cur_sum - nums[i]] += count
            dp = next
        return dp[target]

        # # optimized bottom up
        # dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        # dp[0][0] = 1 # (elements, sum) -> 1 way (1 way to sum to zero with first 0 elements)

        # for i in range(len(nums)):
        #     for cur_sum, count in dp[i].items():
        #         dp[i + 1][cur_sum + nums[i]] += count
        #         dp[i + 1][cur_sum - nums[i]] += count
        # return dp[len(nums)][target]


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

