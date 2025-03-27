class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)
        n, x = count.most_common(1)[0]
        y = 0
        for i in range(len(nums)):
            if nums[i] == n:
                y += 1
                x -= 1
            if y > (i+1)//2 and x > (len(nums) - i - 1) // 2:
                return i
        return -1
            