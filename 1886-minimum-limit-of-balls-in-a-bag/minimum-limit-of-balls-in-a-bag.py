class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def binary_search(start, end):

            while start < end:

                splits = 0

                mid = (start + end) // 2

                for num in nums:
                    if num > mid:
                        splits += (num - 1) // mid
                
                if splits <= maxOperations:
                    end = mid
                else:
                    start = mid + 1

            return start
        
        return binary_search(1, max(nums))