class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
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

        # memoization


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
