class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # DP array with size (n+1) to handle edge cases

        for i in range(n - 1, -1, -1):  # Process in reverse order (bottom-up)
            points, skip = questions[i]
            take = points + (dp[i + skip + 1] if i + skip + 1 < n else 0)
            not_take = dp[i + 1]
            dp[i] = max(take, not_take)

        return dp[0]


        # # memoization
        # n = len(questions)
        # memo = {}
        # def dp(i):
        #     if i >= n:
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     take = questions[i][0] + dp(i + questions[i][1] + 1)
        #     not_take = dp(i+1)
        #     memo[i] = max(take, not_take)
        #     return memo[i]
        # return dp(0)

        # recursion
        # n = len(questions)
        # def dp(i):
        #     if i == (n-1):
        #         return 0
        #     take = questions[i][0] + dp(i + questions[i][1] + 1)
        #     not_take = dp(i+1)
        #     return max(take, not_take)
        # return dp(0)