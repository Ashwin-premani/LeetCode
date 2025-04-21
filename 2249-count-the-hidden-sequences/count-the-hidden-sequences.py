class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        cur = 0
        min_val = 0
        max_val = 0
        for i in differences:
            cur += i
            min_val = min(min_val, cur)
            max_val = max(max_val, cur)
            if ((upper - max_val) - (lower - min_val) +1) <= 0:
                return 0
        return max(0, (upper - max_val) - (lower - min_val) + 1)
