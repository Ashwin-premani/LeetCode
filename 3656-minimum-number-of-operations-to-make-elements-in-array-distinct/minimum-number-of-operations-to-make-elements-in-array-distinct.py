class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # reverse
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])
        return 0

        # linear
        operations = 0
        seen  = set()
        i = 0
        while i < len(nums):
            if nums[i] in seen:
                # remove 3 elements from the front
                nums = nums[3:]
                seen.clear()
                operations += 1
                i = 0  # restart since array changed
            else:
                seen.add(nums[i])
                i += 1
        return operations