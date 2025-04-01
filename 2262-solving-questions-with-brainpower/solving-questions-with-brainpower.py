class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = {}
        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            take = questions[i][0] + dp(i + questions[i][1] + 1)
            not_take = dp(i+1)
            memo[i] = max(take, not_take)
            return memo[i]
        return dp(0)