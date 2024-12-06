class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        b_set = set(banned)
        sum = 0
        count = 0
        for i in range(1,n+1):
            if i in b_set:
                continue
            else:
                sum += i
                if sum > maxSum:
                    break
                count += 1
        return count