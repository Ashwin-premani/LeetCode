class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return -1
        current = None
        streak = 0
        f = collections.defaultdict(collections.Counter)
        def process(i, steak):
            s = streak
            count = 1

            while s > 0:
                f[i][s] += count
                count += 1
                s -= 1
        for i in s:
            if i == current:
                streak += 1
            else:
                process(current, streak)
                current = i
                streak = 1
        else:
            process(current, streak)
        best = -1
        for c in f.keys():
            for l in f[c]:
                if f[c][l] >= 3:
                    best = max(best, l)
        return best