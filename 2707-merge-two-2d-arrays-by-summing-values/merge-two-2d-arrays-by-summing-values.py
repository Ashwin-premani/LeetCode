class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        n, m = 0, 0
        while n < len(nums1) and m < len(nums2):
            if nums1[n][0] < nums2[m][0]:
                res.append(nums1[n])
                n += 1
            elif nums1[n][0] > nums2[m][0]:
                res.append(nums2[m])
                m += 1
            else:
                res.append([nums1[n][0], nums1[n][1] + nums2[m][1]])
                m += 1
                n += 1
        while n < len(nums1):
            res.append(nums1[n])
            n += 1
        while m < len(nums2):
            res.append(nums2[m])
            m += 1
        return res