class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # a = 0
        # b = 0
        # l = ""
        # while a < len(s):
        #     if b < len(spaces) and a == spaces[b]:
        #         l += " "
        #         b += 1
        #     l += s[a]
        #     a += 1
        # return l

        #using array
        i, j = 0, 0
        res = []

        while i < len(s) and j < len(spaces):
            if i < spaces[j]:
                res.append(s[i])
                i += 1
            else:
                res.append(" ")
                j += 1
        if i < len(s):
            res.append(s[i:])

        return "".join(res)