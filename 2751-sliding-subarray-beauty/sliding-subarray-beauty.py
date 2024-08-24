from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        ans=[]
        sl=SortedList()
        n=len(nums)
        for i in range(n):
            sl.add(nums[i])
            if i-k>=0:
                sl.remove(nums[i-k])
            if len(sl)>=k:
                t=sl[x-1]
                if t>=0:
                    ans.append(0)
                else:
                    ans.append(t)
        return ans


        # l=nums[0:k]
        # lst=[]
        # i=k
        # while i<len(nums):
        #     l.sort()
        #     if l[x-1]<=0:
        #         lst.append(l[x-1])
        #     else:
        #         lst.append(0)
        #     l.pop(0)
        #     l.append(nums[i])
        #     i+=1
        # return lst
