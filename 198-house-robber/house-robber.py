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
        return helper(nums)


        

        # r1, r2 = 0, 0
        # for i in nums:
        #     temp = max(r1+i, r2)
        #     r1=r2
        #     r2=temp
        # return r2