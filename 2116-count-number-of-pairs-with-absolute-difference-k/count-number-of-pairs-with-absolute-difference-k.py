class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        lst=[]
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    lst.append([i,j])

        return len(lst)