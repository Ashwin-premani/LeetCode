class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val

        self.cnt[old_val] -= 1
        if self.cnt[old_val] == 0:
            del self.cnt[old_val]

        self.cnt[new_val] += 1
        self.nums2[index] = new_val

    def count(self, tot: int) -> int:
        pairs = 0
        for i in self.nums1:
            complement = tot - i
            pairs += self.cnt.get(complement, 0)
        return pairs


    # def __init__(self, nums1: List[int], nums2: List[int]):
    #     self.nums1 = nums1
    #     self.nums2 = nums2
    #     self.cnt = Counter(nums2)

    # def add(self, index: int, val: int) -> None:
    #     self.cnt[self.nums2[index]] -= 1
    #     self.nums2[index] += val
    #     self.cnt[self.nums2[index]] += 1

    # def count(self, tot: int) -> int:
    #     pairs = 0
    #     for i in self.nums1:
    #         complement = tot - i
    #         pairs += self.cnt.get(complement, 0)
    #     return pairs

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)