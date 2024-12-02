class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        avg = s/k
        l = 0
        for r in range(k,len(nums)):
            s += nums[r]
            s -= nums[l]
            l += 1
            avg = max(avg,s/k)
        return avg
