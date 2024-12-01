class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash = defaultdict(int)
        for i in arr:
            hash[i] += 1
        for i in arr:
            if i != 0 and (i*2) in hash:
                return True
            elif i == 0 and hash[i] >= 2:
                return True
        return False 