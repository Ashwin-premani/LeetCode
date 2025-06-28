class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # using index only(Sort-based approach)
        a = [(num, i) for i, num in enumerate(nums)]
        top_k = sorted(a, key=lambda x: x[0], reverse=True)[:k]
        top_k.sort(key=lambda x: x[1])
        return [num for num, _ in top_k]


        # using heap
        heap = [(-nums[i], i) for i in range(len(nums))]
        heapq.heapify(heap)

        top_k = [heapq.heappop(heap) for _ in range(k)]
        top_k.sort(key=lambda x: x[1])
        res = [nums[i] for _, i in top_k]
        return res
        



        # Brute Force -> using sorting
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        indexed_nums.sort(key=lambda x: x[0], reverse=True)
        top_k = sorted(indexed_nums[:k], key=lambda x: x[1])  # sort back by original index

        return [num for num, i in top_k]