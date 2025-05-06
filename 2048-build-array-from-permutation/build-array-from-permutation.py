class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Linear using n space
        res = [0] * len(nums)
        for i in range(len(nums)):
            # res.append(nums[nums[i]])
            res[i] = nums[nums[i]]
        return res

        # linear using no extra space but 2 loops and less optimized
        # When you do nums[i] += n * (nums[nums[i]] % n), you’re increasing the value of nums[i]. For example, if n = 1000 and nums[i] = 999, you're storing numbers up to ~999999, which take more bytes per integer in memory.
        n = len(nums)
        for i in range(n):
            nums[i] += n * (nums[nums[i]] % n)
        
        for i in range(n):
            nums[i] //= n
            
        return nums