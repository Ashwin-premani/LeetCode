import math
from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isprime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True
        
        res = []
        for i in range(left, right+1):
            if isprime(i):
                res.append(i)
        
        n1 = -1
        n2 = -1
        m = float('inf')
        
        for i in range(len(res) - 1):
            current_gap = res[i+1] - res[i]
            if current_gap < m:  # Changed from '>' to '<' and using strictly less than
                m = current_gap
                n1 = res[i]
                n2 = res[i+1]
        
        return [n1, n2]