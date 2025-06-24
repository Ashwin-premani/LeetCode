class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_positions = [j for j, val in enumerate(nums) if val == key]
        res = []
        j = 0  

        for i in range(len(nums)):
            while j < len(key_positions) and key_positions[j] < i - k:
                j += 1
            if j < len(key_positions) and abs(i - key_positions[j]) <= k:
                res.append(i)
        return res
        # looping from j - k <= i <= j + k + 1
        res = set()
        for j in range(len(nums)):
            if nums[j] == key:
                for i in range(max(0, j - k), min(len(nums), j + k + 1)):
                    res.add(i)
        return sorted(res)


        # Brute Force -> TLE
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i not in res:
                    if nums[j] == key and abs(i - j) <= k:
                        res.append(i)
        return res