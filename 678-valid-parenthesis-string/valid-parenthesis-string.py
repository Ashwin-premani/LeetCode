class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0

            
        # stack = []
        # star = []
        # for i in s:
        #     if i == '(':
        #         stack.append(1)
        #     elif i == '*':
        #         stack.append("*")
        #     else:
        #         if not stack:
        #             return False
        #         stack.pop()
        # while star:
        #     star.pop()
        #     if not stack:
        #         return False
        #     stack.pop()
        # return True
        
        