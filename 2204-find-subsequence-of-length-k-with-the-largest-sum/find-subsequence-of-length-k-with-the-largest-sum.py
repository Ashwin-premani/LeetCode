class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Brute Force -> using sorting
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        indexed_nums.sort(key=lambda x: x[0], reverse=True)
        top_k = sorted(indexed_nums[:k], key=lambda x: x[1])  # sort back by original index

        return [num for num, i in top_k]