class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        def count(n):
            res = 0
            while n > 0:
                res += 1 & n
                n = n >> 1
            return res
        cnt1, cnt2 = count(num1), count(num2)
        x = num1
        i = 0
        while cnt1 > cnt2:
            if x & (1 << i):
                cnt1 -= 1
                x = x ^ (1 << i)

            i += 1
        while cnt1 < cnt2:
            if x & (1 << i) == 0:
                cnt1 += 1
                x = x | (1 << i)

            i += 1
        

        return x