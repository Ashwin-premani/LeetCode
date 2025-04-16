class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hash = defaultdict(int)
        l = 0
        res = 0
        pairs = 0
        for r in range(n):
            pairs += hash[nums[r]]
            hash[nums[r]] += 1

            while pairs >= k:
                res += (n - r)
                hash[nums[l]] -= 1
                pairs -= hash[nums[l]]
                l += 1
        return res
