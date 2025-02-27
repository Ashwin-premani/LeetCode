class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        sum_count = {0: 1}  
        
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in sum_count:
                count += sum_count[prefix_sum - k]
            
            sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
            
        return count


        # def backtrack(i,s,a, count):
        #     if s == k and a:
        #         count += 1
        #     if i >= len(nums):
        #         return count
        #     a.append(nums[i])
        #     backtrack(i+1,s+nums[i],a,count)
        #     a.pop()
        #     backtrack(i+1,s-nums[i],a,count)
        #     return count
        # return backtrack(0,0,[],0)