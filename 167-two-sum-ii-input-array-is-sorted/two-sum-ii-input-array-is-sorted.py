from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_to_index={}
        n=len(numbers)

        for i in range(n):
            complement=target-numbers[i]
            if complement in num_to_index:
                return [num_to_index[complement]+1,i+1]
            num_to_index[numbers[i]]=i
        return []