class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        word=""
        n=len(word1)
        m=len(word2)
        # one way
        # while i < n and j < m:
        #     word += word1[i] +word2[j]
        #     j += 1
        #     i += 1
        # while i < n:
        #     word += word1[i]
        #     i += 1
        # while j < m:
        #     word += word2[j]
        #     j += 1

        # Other way
        for i in range(min(len(word1), len(word2))):
            word += word1[i] + word2[i]
        # word += word1[i+1:] + word2[i+1:] one way to do it
        # clever way
        i = min(len(word1), len(word2))
        word += word1[i:] + word2[i:]

        return word



        i=0
        word=""
        n=len(word1)
        m=len(word2)
        if n>m:
            a=m
        else:
            a=n
        while i<a:
            word+=word1[i]
            word+=word2[i]
            i+=1
        if n>m:
            for j in range(a,n):
                word+=word1[j]
        else:
            for j in range(a,m):
                word+=word2[j]

        return word
