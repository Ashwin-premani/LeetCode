class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        total = 0
        count = defaultdict(int)
        for i in range(len(nums)):
            total += i
            good_pairs += count[nums[i] - i]
            count[nums[i] - i] += 1
        return total - good_pairs