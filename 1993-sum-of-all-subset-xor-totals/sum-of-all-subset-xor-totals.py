class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
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