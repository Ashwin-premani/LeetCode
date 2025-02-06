class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        pair = defaultdict(int)
        prod = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                p = nums[i] * nums[j]
                pair[p] += prod[p]
                prod[p] += 1
        res = 0
        for v in pair.values():
            res += 8 * v
        return res