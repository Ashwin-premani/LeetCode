class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        results = True
        
        for j in range(0,len(nums)-1):
            if nums[j]%2==nums[j+1]%2:
                results=False
                break
                
        
        return results