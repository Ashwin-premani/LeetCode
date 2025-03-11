class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(cur, used):
            if len(cur) == len(nums):
                if cur not in res:
                    res.append(cur.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                cur.append(nums[i])
                used[i] = True
                backtrack(cur, used)
                cur.pop()
                used[i] = False

        backtrack([], [False] * len(nums))
        return res