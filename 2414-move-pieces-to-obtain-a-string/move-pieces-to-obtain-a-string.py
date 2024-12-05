class Solution:
    def canChange(self, start: str, target: str) -> bool:
        cntl, cntr = 0, 0
        strs, strt = "", ""
        for i in range(len(start)):
            if start[i] == 'L':
                cntl += 1
                strs += 'L'
            if start[i] == 'R':
                cntr += 1
                strs += 'R'

            if target[i] == 'L':
                cntl -= 1
                strt += 'L'
            if target[i] == 'R':
                cntr -= 1
                strt += 'R'
            
            if cntl > 0 or cntr < 0:
                return False
        
        return strt == strs