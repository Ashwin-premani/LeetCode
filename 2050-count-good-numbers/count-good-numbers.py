class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9+7
        def pow(x, n):
            if n == 0:
                return 1
            res = 1
            while n > 1:
                if n % 2:
                    res = (res * x) % MOD
                n = n // 2
                x = (x * x) % MOD
            return res * x
        even = ceil(n/2)
        odd = n // 2
        return (pow(5, even) * pow(4, odd)) % MOD

        # TLE
        MOD = 10**9+7
        if n == 0:
            return 0
        even = n//2 + 1  if n%2 == 1 else n//2
        odd = n//2
        res = 1
        res *= 5**even
        res *= 4**odd
        return res % MOD

