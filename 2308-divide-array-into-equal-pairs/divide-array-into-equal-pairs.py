class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # hash = Counter(nums)
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        for i,v in count.items():
            if v % 2 != 0:
                return False
        return True