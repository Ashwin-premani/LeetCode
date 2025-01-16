class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums2) % 2 == 1:
            for n in nums1:
                res ^= n
        if len(nums1) % 2 == 1:
            for n in nums2:
                res ^= n
        return res
        

        #Brute force 2 (time limit)
        # res = 0
        # for i in nums1:
        #     for j in nums2:
        #         res ^= i ^ j
        # return res

        # Brute force(memory and time limit)
        # nums3 = []
        # for i in nums1:
        #     for j in nums2:
        #         nums3.append(i^j)
        # xor = 0
        # for i in nums3:
        #     xor ^= i
        # return xor