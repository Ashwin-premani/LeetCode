class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = [] # list of queues
        nums_to_grps = {} # nums[i] -> group index

        for i in sorted(nums):
            if not groups or abs(i - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(i)
            nums_to_grps[i] = len(groups) - 1 
            
        res = []
        for i in nums:
            j = nums_to_grps[i]
            res.append(groups[j].popleft())
        return res