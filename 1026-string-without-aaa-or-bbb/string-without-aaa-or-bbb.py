class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []
        
        while a > 0 or b > 0:
            # Check if adding 'a' is safe and beneficial
            if a > b:
                if a > 1 and a - 2 >= b:
                    result.append('aa')
                    a -= 2
                else:
                    result.append('a')
                    a -= 1
                
                # Add 'b' if it's safe and available
                if b > 0:
                    result.append('b')
                    b -= 1
            else:
                if b > 1 and b - 2 >= a:
                    result.append('bb')
                    b -= 2
                else:
                    result.append('b')
                    b -= 1

                # Add 'a' if it's safe and available
                if a > 0:
                    result.append('a')
                    a -= 1

        return ''.join(result)
