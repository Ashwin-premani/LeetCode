class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
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