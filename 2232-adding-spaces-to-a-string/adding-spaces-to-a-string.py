class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        a = 0
        b = 0
        l = ""
        while a < len(s):
            if b < len(spaces) and a == spaces[b]:
                l += " "
                b += 1
            l += s[a]
            a += 1
        return l