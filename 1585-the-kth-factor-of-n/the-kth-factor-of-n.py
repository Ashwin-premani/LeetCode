class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        lst=[]
        for i in range(1,(n//2)+1):
            if n%i==0:
                lst.append(i)
        lst.append(n)
        if len(lst)<k:
            return -1
        else:
            return lst[k-1]