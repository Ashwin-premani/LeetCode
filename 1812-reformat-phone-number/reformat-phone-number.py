class Solution:
    def reformatNumber(self, number: str) -> str:

        digits = ''.join(c for c in number if c.isdigit())
        
        result = []
        i = 0
        n = len(digits)
        
        while n > 4:
            result.append(digits[i:i+3])
            i += 3
            n -= 3
        if n == 4:
            result.append(digits[i:i+2])
            result.append(digits[i+2:i+4])
        else:
            result.append(digits[i:])
        
        return '-'.join(result)
