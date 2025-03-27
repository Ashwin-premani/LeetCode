class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Voting Algo


        # Hash
        n = -1
        count = 0

        for num in nums:
            if count == 0:
                n = num
            count += (1 if num == n else -1)
        x = sum(1 for num in nums if num == n)
        y = 0
        for i in range(len(nums)):
            if nums[i] == n:
                y += 1
                x -= 1
            if y > (i+1)//2 and x > (len(nums) - i - 1) // 2:
                return i
        return -1
            