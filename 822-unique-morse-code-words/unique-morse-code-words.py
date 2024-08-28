class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        lst=[]
        for i in words:
            s=""
            for j in i:
                s+=code[ord(j)%97]
            lst.append(s)
        unique=0
        test=[]
        for i in lst:
            if i not in test:
                unique+=1
                test.append(i)
        return unique