class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        def backtrack(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]
            
            res = float('inf')
            j = i
            for c, d in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                res = min(res, c + backtrack(j))
            dp[i] = res
            return res
        return backtrack(0)
                

