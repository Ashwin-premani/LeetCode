class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = {}
        for i in range(len(s)):
            hash[s[i]] = i
        res = []
        size = 0
        end = 0
        l = 0
        for i, char in enumerate(s):
            end = max(end, hash[char])  
            size += 1 
            if i == end:
                res.append(size)  
                size = 0
        return res