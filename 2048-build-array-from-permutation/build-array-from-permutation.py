class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] += n * (nums[nums[i]] % n)
        
        for i in range(n):
            nums[i] //= n
            
        return nums

        # Linear using n space
        res = [0] * len(nums)
        for i in range(len(nums)):
            # res.append(nums[nums[i]])
            res[i] = nums[nums[i]]
        return res