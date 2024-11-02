class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        lst = sentence.split(' ')
        i = 0
        n = len(lst)
        
        while i < n:
            l = lst[i][-1]
            if (i + 1 < n and l != lst[i + 1][0]) or (i == n - 1 and lst[0][0] != l):
                return False
            i += 1
            
        return True