class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        lst=[]
        for i in nums:
            for j in range(i[0],i[1]+1):
                if j not in lst:
                    lst.append(j)
        return len(lst)