class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        n = len(s)
        i = 0
        sign = ''
        if s[i] == '+' or s[i] == '-':
            sign = s[i]
            i += 1
        while i < n and s[i] == '0':
            i += 1
        num = ''
        while i < n and s[i].isnumeric():
            num += s[i]
            i += 1
        limitmin = -(2**31)
        limitmax = (2**31) - 1
        
        res = int(sign + num) if num else 0
        if res > limitmax:
            return limitmax
        elif  res < limitmin:
            return limitmin
        return res