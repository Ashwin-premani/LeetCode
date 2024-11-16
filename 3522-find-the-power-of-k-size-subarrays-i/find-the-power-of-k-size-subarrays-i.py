from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        j = 0
        n = len(nums) - k
        res = []
        
        while j <= n:
            arr = nums[j:j + k]
            
            is_sorted_and_consecutive = True
            for i in range(1, k):
                if arr[i] <= arr[i - 1] or arr[i] != arr[i - 1] + 1:
                    is_sorted_and_consecutive = False
                    break
            
            if is_sorted_and_consecutive:
                res.append(max(arr))
            else:
                res.append(-1)
            
            j += 1
        
        return res


# class Solution:
#     def resultsArray(self, nums: List[int], k: int) -> List[int]:
#         j=0
#         n=len(nums)-k
#         res=[]
#         while j<=n:
#             arr=nums[j:k+j]
#             if max(arr)==arr[k-1]:
#                 for i in range(1,len(arr)):
#                     if arr[i-1]<arr[i]:
#                         pass
#                     else:
#                         res.append(-1)
#                         break
#                 res.append(max(arr))
#             else:
#                 res.append(-1)
#             j+=1
#         return res