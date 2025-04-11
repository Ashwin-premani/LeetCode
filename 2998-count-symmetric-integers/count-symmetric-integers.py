class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def digit_sum(num_str):
            return sum(int(ch) for ch in num_str)

        res = 0
        for i in range(low, high + 1):
            s = str(i)
            n = len(s)
            if n % 2 == 0:
                mid = n // 2
                if digit_sum(s[:mid]) == digit_sum(s[mid:]):
                    res += 1
        return res


        res = 0
        for i in range(low, high + 1):
            f = str(i)
            n = len(f)
            if n % 2 != 0:
                continue  # Skip odd-digit numbers
            l = f[:n // 2]
            r = f[n // 2:]
            a = sum(int(d) for d in l)
            b = sum(int(d) for d in r)
            if a == b:
                res += 1
        return res
