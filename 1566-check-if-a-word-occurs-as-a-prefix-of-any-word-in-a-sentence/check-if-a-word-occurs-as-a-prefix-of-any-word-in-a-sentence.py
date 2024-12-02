class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word = sentence.split(' ')
        for i, word in enumerate(word,1):
            if word.startswith(searchWord):
                return i
        return -1