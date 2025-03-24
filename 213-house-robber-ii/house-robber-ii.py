class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def helper(temp):
            prev = temp[0]
            prev2 = 0
            for i in range(1, len(temp)):
                take = temp[i]
                if i > 1:
                    take += prev2
                not_take = prev
                cur = max(take, not_take)
                prev2 = prev
                prev = cur
            return prev

        temp1, temp2 = [], []
        for i in range(n):
            if i != 0:
                temp1.append(nums[i])
            if i != n - 1:
                temp2.append(nums[i])

        f = helper(temp1)
        s = helper(temp2)

        return max(f, s)

        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
    def helper(self, nums):
        r1, r2 = 0, 0
        for i in nums:
                temp=max(r1+i,  r2)
                r1=r2
                r2=temp
        return r2