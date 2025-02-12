class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sums = {}
        for i in nums:
            digit_sum = sum(int(digit) for digit in str(i))
            if digit_sum not in digit_sums:
                digit_sums[digit_sum] = [i]
            else:
                digit_sums[digit_sum].append(i)
        res = -1
        for i in digit_sums:
            l = digit_sums[i]
            if len(l) > 1:
                l.sort(reverse=True)
                res = max(res
                , l[0] + l[1])
            
        return res