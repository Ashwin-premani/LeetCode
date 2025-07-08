class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Tabulation
        events.sort()
        n = len(events)
        
        start_times = [e[0] for e in events]

        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(1, k + 1):
                not_take = dp[i + 1][j]

                _, end, value = events[i]
                next_index = bisect.bisect_right(start_times, end)
                take = value + dp[next_index][j - 1]

                dp[i][j] = max(take, not_take)

        return dp[0][k]


        # Recursion + lru + bisect + start time arr
        events.sort()
        start_times = [event[0] for event in events]
        n = len(events)

        @lru_cache(None)
        def dfs(i: int, remaining: int) -> int:
            if i == n or remaining == 0:
                return 0

            skip = dfs(i + 1, remaining)

            _, end, value = events[i]
            next_index = bisect.bisect_right(start_times, end)
            take = value + dfs(next_index, remaining - 1)

            return max(skip, take)

        return dfs(0, k)

        # memoization -> TLE
        events.sort()
        n = len(events)

        dp = [[-1] * (k + 1) for _ in range(n)]

        def dfs(i: int, remaining: int) -> int:
            if i == n or remaining == 0:
                return 0

            if dp[i][remaining] != -1:
                return dp[i][remaining]

            not_take = dfs(i + 1, remaining)

            start_i, end_i, value_i = events[i]

            next_i = i + 1
            while next_i < n and events[next_i][0] <= end_i:
                next_i += 1

            take = value_i + dfs(next_i, remaining - 1)

            dp[i][remaining] = max(take, not_take)
            return dp[i][remaining]

        return dfs(0, k)

        # Recursion + lru_cache -> TLE
        events.sort()
        n = len(events)
        @lru_cache(None)
        def dfs(i: int, remaining: int) -> int:
            if i == n or remaining == 0:
                return 0

            not_take = dfs(i + 1, remaining)

            start_i, end_i, value_i = events[i]

            next_i = i + 1
            while next_i < n and events[next_i][0] <= end_i:
                next_i += 1

            take = value_i + dfs(next_i, remaining - 1)

            return max(take, not_take)

        return dfs(0, k)
