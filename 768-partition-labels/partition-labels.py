class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = {}
        for i in range(len(s)):
            hash[s[i]] = i
        res = []
        start = 0
        end = 0
        l = 0
        for i, char in enumerate(s):
            end = max(end, hash[char])  
            if i == end:
                res.append(i - start + 1)  
                start = i + 1   
        return res
            