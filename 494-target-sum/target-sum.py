class Solution:
    def findWays(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        prev = [0] * (k + 1)
        prev[0] = 1

        if arr[0] <= k and arr[0] != 0:
            prev[arr[0]] = 1
        elif arr[0] == 0:
            prev[0] = 2  # Because we can include or exclude the 0

        for i in range(1, n):
            cur = [0] * (k + 1)
            for s in range(k + 1):
                not_pick = prev[s]
                pick = prev[s - arr[i]] if arr[i] <= s else 0
                cur[s] = (pick + not_pick) % MOD
            prev = cur

        return prev[k]

    def countPartitions(self, d: int, arr: List[int]) -> int:
        total_sum = sum(arr)
        MOD = 10**9 + 7
        if (total_sum - d) < 0 or (total_sum - d) % 2 != 0:
            return 0
        target = (total_sum - d) // 2
        return self.findWays(arr, target)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.countPartitions(target, nums)



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

