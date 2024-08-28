from sortedcontainers import SortedList
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        sl = SortedList(nums)
        score = 0
        current_max = 0

        for index, x in enumerate(nums):
            sl.remove(x)

            if 1 <= index <= n - 2:  
                if current_max < x < sl[0]: 
                    score += 2
                elif nums[index - 1] < x < nums[index + 1]:  
                    score += 1

            current_max = max(current_max, x)
        return score
