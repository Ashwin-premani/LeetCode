class Solution:
    def kthCharacter(self, k: int) -> str:
        word= 'a'

        while len(word) < k:
            s = ''
            for i in word:
                s += chr(ord(i) + 1)
            word += s
        return word[k-1]