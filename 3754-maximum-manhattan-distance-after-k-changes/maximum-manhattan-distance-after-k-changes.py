class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        e = 0
        w = 0
        n = 0
        su = 0
        md = 0
        steps = 0
        for i in range(len(s)):
            if s[i] == 'E':
                e += 1
            elif s[i] == 'W':
                w += 1
            elif s[i] == 'N':
                n += 1
            elif s[i] == 'S':
                su += 1
            cur = abs(e- w) + abs(n - su)
            steps = i + 1
            wasted = steps - cur

            extra = 0
            if wasted != 0:
                extra = min(2*k, wasted)
            final = cur + extra

            md = max(md, final)
        return md


        return md + extra