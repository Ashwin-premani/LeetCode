class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        hash=Counter(number)
        lst=[]
        if hash[digit]==1:
            return number.replace(digit,"")
        else:
            for i in range(len(number)):
                if number[i]==digit:
                    lst.append(int(number[:i]+number[i+1:]))
        return str(max(lst))
