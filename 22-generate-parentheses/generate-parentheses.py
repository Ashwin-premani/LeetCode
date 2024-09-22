class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        res = []

        def backtrack(closedN, openN):
            if openN == closedN ==n:
                res.append("".join(stack))
                return
                
            if openN <n:
                stack.append("(")
                backtrack(closedN,openN+1)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(closedN+1,openN)
                stack.pop()
            
        backtrack(0,0)
        return res

        