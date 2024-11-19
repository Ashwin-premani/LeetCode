class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend)
        dv = abs(divisor)
        output = 0

        while d >= dv:
            mul = 1
            tmp = dv
            while d >= tmp:
                d -= tmp
                output += mul
                mul += mul
                tmp += tmp
        if (dividend < 0 and divisor >=0) or (dividend >= 0 and divisor < 0):
            output = -output
            
        return min(2147483647,max(-2147483648,output))
