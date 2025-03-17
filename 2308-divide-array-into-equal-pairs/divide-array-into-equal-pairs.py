class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash = Counter(nums)
        for i,v in hash.items():
            if v % 2 != 0:
                return False
        return True