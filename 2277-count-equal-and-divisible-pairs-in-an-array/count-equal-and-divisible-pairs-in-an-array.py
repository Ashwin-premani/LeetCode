class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        value_indices = defaultdict(list)
        res = 0

        # Group indices by the number's value
        for idx, num in enumerate(nums):
            value_indices[num].append(idx)

        # For each list of equal values, check index pairs
        for indices in value_indices.values():
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    if (indices[i] * indices[j]) % k == 0:
                        res += 1

        return res
        # Brute Force
        res = 0
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    if (i*j) % k == 0:
                        res += 1
        return res