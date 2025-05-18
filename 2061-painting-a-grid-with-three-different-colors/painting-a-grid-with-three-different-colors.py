class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        from functools import lru_cache

        mod = 10**9 + 7
        states = []

        def generate_col(cur, prev, l):
            if l == m:
                states.append(cur)
                return
            for c in "RGB":
                if c != prev:
                    generate_col(cur + c, c, l + 1)

        generate_col("", "", 0)

        compatible = {}
        for i, a in enumerate(states):
            compatible[i] = []
            for j, b in enumerate(states):
                if all(a[k] != b[k] for k in range(m)):
                    compatible[i].append(j)

        @lru_cache(None)
        def dp(col, prev):
            if col == n:
                return 1
            res = 0
            for nxt in compatible[prev]:
                res = (res + dp(col + 1, nxt)) % mod
            return res

        result = 0
        for i in range(len(states)):
            result = (result + dp(1, i)) % mod

        return result
