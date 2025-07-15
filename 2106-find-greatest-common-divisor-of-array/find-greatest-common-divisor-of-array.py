class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def GCD(num1, num2):
            m = min(num1, num2)
            gcd = 1
            for i in range(2, m+1):
                if num1 % i == 0 and num2 % i == 0:
                    gcd = i
            return gcd
        max_num = max(nums)
        min_num = min(nums)
        return GCD(max_num, min_num)