class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # lst=[]
        # e=[]
        # for i in nums:
        #     if i not in lst:
        #         lst.append(i)
        #     else:
        #         e.append(i)
        # for i in lst:
        #     if i not in e:
        #         return i
        result =0
        for i in nums:
           result = result^i
        return result

        
        
        
        
        # hash=Counter(nums)
        # for key,value in hash.items():
        #     if value==1:
        #         return key