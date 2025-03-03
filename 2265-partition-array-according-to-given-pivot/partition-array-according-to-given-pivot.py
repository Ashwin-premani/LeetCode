class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        p = []
        greater = []
        for i in nums:
            if i == pivot:
                p.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                less.append(i)
        less.extend(p)
        less.extend(greater)
        return less