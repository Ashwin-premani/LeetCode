class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if numFriends == 1:
            return word
        p = n - (numFriends - 1)
        res = ""
        for i in range(n):
            cantake = min(p, n - i)
            res = max(res, word[i:i+cantake])

        return res

        n = len(word)
        p = n - numFriends  # exclusive end index for max substring
        idx = [0]
        
        # Step 1: Find all positions with the lexicographically largest character
        for i in range(1, n):
            if word[i] > word[idx[0]]:
                idx = [i]
            elif word[i] == word[idx[0]]:
                idx.append(i)

        res = ""
        for i in idx:
            if i <= p: 
                sub = word[i:p+1]
                if sub > res:
                    res = sub

        return res
