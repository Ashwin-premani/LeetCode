class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum=0
        sum1=0
        for i in t:
            sum+=ord(i)
        for i in s:
            sum1+=ord(i)
        l=sum-sum1
        return chr(l)
