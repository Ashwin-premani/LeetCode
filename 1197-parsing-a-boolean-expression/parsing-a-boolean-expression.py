class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        e = expression
        i = 0

        def helper():
            nonlocal i
            c = e[i]
            i+=1
            if c == 'f':
                return False
            if c == 't':
                return True
            if c == '!':
                i+=1
                res = not helper()
                i+=1
                return res
            s = []
            i+=1
            while e[i] != ')':
                if e[i] != ',':
                    s.append(helper())
                else:
                    i+=1
            i+=1
            
            if c == '&':
                return all(s)
            if c == '|':
                return any(s)



        
        return helper()