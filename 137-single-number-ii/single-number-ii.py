class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash=Counter(nums)
        for key,value in hash.items():
            if value!=3:
                return key