class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        b=set()
        for i in range(int(sqrt(c))+1):
            b.add(i*i)
        a=0
        while a*a<=c:
            target=c-a*a
            if target in b:
                return True
            a+=1
        return False

        