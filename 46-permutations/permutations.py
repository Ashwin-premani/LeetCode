class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr_perm, used):
            if len(curr_perm) == len(nums):
                res.append(curr_perm[:]) 
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                    
                curr_perm.append(nums[i])
                used[i] = True
                
                backtrack(curr_perm, used)
                
                curr_perm.pop()
                used[i] = False
        
        res = []
        backtrack([], [False] * len(nums))
        return res

        
        # result=[]
        # if len(nums)==1:
        #     return [nums[:]]

        # for i in range(len(nums)):
        #     n=nums.pop(0)
        #     perms=self.permute(nums)

        #     for perm in perms:
        #         perm.append(n) 
        #     result.extend(perms)
        #     nums.append(n)
        # return result