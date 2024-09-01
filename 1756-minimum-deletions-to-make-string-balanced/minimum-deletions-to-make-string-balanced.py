class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = 0
        for i in s:
            a_count+=1 if i=='a' else 0

        b_count = 0
        res = len(s)
        for i,c in enumerate(s):
            if c=='a':
                a_count-=1
            res = min(res,a_count+b_count)
            if c=='b':
                b_count+=1
        return res
        
        
