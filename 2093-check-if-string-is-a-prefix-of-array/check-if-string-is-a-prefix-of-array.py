class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i=0
        a=''
        while i<len(words):
            a+=words[i]
            if a==s:
                return True
            i+=1
        return False