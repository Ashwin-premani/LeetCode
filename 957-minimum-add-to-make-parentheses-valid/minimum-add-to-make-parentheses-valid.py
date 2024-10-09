class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        res = 0
        for i in s:
            if i == '(':
                open+=1
            else:
                if open ==0:
                    res+=1
                open = max(open-1,0)

        return res+open