class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        subsets = []

        def backtrack(i):
            if i >= len(nums):
                if res not in subsets:
                    subsets.append(res.copy())
                return
            res.append(nums[i])
            backtrack(i+1)
            res.pop()
            backtrack(i+1)

        backtrack(0)
        return subsets


        # res = []
        # nums.sort()
        # subset = []
        # def dfs(i):
        #     if i>=len(nums):
        #         if subset not in res:
        #             res.append(subset.copy())
        #         return
        #     subset.append(nums[i])
        #     dfs(i+1)
        #     subset.pop()
        #     dfs(i+1)
        # dfs(0)
        # return res