class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 3 ** 19
        return n>0 and x % n == 0