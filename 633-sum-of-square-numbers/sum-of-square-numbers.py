class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        lst=[x*x for x in range(int(sqrt(c))+1)]
        i=0
        n=len(lst)-1
        while i<=n:
            if lst[i]+lst[n]==c:
                return True
            elif lst[i]+lst[n]<c:
                i+=1
            else:
                n-=1
        return False

        # b=set()
        # for i in range(int(sqrt(c))+1):
        #     b.add(i*i)
        # a=0
        # while a*a<=c:
        #     target=c-a*a
        #     if target in b:
        #         return True
        #     a+=1
        # return False

        