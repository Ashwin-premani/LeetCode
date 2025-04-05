class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # using OR 
        # here the intution is take all one's bit and multiplying it with respective number as no of times it occurs 
        # so by taking or we get all one's in one numsber and we multiply let's say 4 or 100 by no of times that bit can occur so if or_all is 0111 we get 4*4 + 2*4 + 1*4 = 28
        or_all = 0
        for i in nums:
            or_all |= i
        return or_all * (2**(len(nums) - 1))

        def backtrack(i, xor):
            if i == len(nums):
                return xor
            return backtrack(i+1, xor^nums[i]) + backtrack(i+1, xor)
        return backtrack(0, 0)

        # optimized solution
        xor_all = 0
        for num in nums:
            xor_all |= num  # Bitwise OR of all numbers
        return xor_all * (1 << (len(nums) - 1))


        # backtrack
        res = 0
        n = len(nums)
        def backtrack(i, xor):
            nonlocal res
            if i == n:
                res += xor
                return
            backtrack(i+1, xor^nums[i])
            backtrack(i+1, xor)
        backtrack(0, 0)
        return res

        # res = []
        # n = len(nums)
        # def backtrack(i, xor):
        #     if i == (n-1):
        #         res.append(xor)
        #         return
        #     if i >= n:
        #         return
        #     backtrack(i+1, xor^nums[i+1])
        #     backtrack(i+1, xor)
        # backtrack(0, nums[0])
        # return sum(res) * 2