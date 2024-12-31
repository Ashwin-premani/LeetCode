class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = { len(days) : 0}

        def backtrack(i):
            if i in dp:
                return dp[i]
            
            dp[i] = float('inf')
            j = i
            for c, d in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + backtrack(j))
            return dp[i]
        return backtrack(0)
                

