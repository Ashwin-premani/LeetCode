class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def search(l,r,target):
            while l <= r:
                m = (l+r)//2 # l+(r-l)//2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m+1
            return r

        
        nums.sort()
        res = 0
        for i in range(len(nums)):
            low = lower - nums[i]
            up = upper - nums[i]
            res += (
                search(i+1,len(nums)-1,up+1) - 
                search(i+1,len(nums)-1,low)
            )
            
        return res