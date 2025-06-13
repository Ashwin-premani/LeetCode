class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def can_form_pairs(max_diff):
            count = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= max_diff:
                    count += 1
                    i += 2  # Skip next index to avoid overlapping
                else:
                    i += 1
            return count >= p

        low, high = 0, nums[-1] - nums[0]
        answer = high

        while low <= high:
            mid = (low + high) // 2
            if can_form_pairs(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer

        # failed approach take all sorted differences from sorted nums and then taking max of p first elements
        nums.sort()
        diff = []
        for i in range(len(nums)-1):
            diff.append(abs(nums[i] - nums[i+1]))
        res = 0
        diff.sort()
        i = 0
        while p:
            res = max(res, diff[i])
            i += 1
            p -= 1
        return res