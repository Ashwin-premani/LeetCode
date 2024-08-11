class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hash1=Counter(target)
        hash2=Counter(arr)
        return hash1==hash2