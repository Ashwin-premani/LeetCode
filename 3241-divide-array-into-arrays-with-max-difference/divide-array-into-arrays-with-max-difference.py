class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        if n % 3 != 0:
            return []
        
        for i in range(0, n, 3):
            grp = nums[i:i+3]
            if grp[-1] - grp[0] > k:
                return []
            res.append(grp)
        return res



        
        res = []
        nums.sort()
        if len(nums) % 3 != 0:
            return []

        for i in range(0, len(nums), 3):
            group = nums[i:i+3]
            if group[-1] - group[0] > k:
                return []
            res.append(group)
        return res