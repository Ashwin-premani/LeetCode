class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def value(a):
            s=""
            for i in a:
                s=s+str(ord(i)-97)
            return s
        sum=0
        sum+=int(value(firstWord))
        sum+=int(value(secondWord))
        target=int(value(targetWord))
        return sum==target

        