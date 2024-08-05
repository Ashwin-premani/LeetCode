class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash=Counter(arr)
        lst=[]
        for key,value in hash.items():
            if value==1:
                lst.append(key)
        return lst[k - 1] if k <= len(lst) else ""