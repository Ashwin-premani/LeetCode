class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even = sum([1 for i in nums if i % 2 == 0])
        odd = sum([1 for i in nums if i % 2 == 1])
        alt = 1
        parity = nums[0] % 2
        for i in range(1, len(nums)):
            if nums[i] % 2 != parity:
                alt += 1
                parity = nums[i] % 2
        return max(alt, even, odd)

        # TLE
        if not nums:
            return 0
        def dfs(parity):
            max_len = 0
            for start in range(len(nums)):
                count = 1
                prev = nums[start]
                for i in range(start + 1, len(nums)):
                    if (prev + nums[i]) % 2 == parity:
                        count += 1
                        prev = nums[i]
                max_len = max(max_len, count)
            return max_len
        return max(dfs(0), dfs(1))