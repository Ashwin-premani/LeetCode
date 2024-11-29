import math
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        prime = 0
        start=math.ceil(math.sqrt(l))

        if start==1:
            start=2

        end=int(math.sqrt(r))+1

        def isPrime(n):
            for j in range(2, int(math.sqrt(n)) + 1):
                if n % j == 0:
                    return False

            return True

        for i in range(start, end):
            if isPrime(i):
                prime += 1

        return r-l+1-prime
        