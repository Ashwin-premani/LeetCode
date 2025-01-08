class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, w):
        cur = self.root

        for c1, c2 in zip(w, reversed(w)):
            if (c1, c2) not in cur.children:
                cur.children[(c1, c2)] = TrieNode()
            cur = cur.children[(c1, c2)]
            cur.count += 1
    def count(self, w):
        cur = self.root

        for c1, c2 in zip(w, reversed(w)):
            if (c1, c2) not in cur.children:
                return 0
            cur = cur.children[(c1, c2)]
        return cur.count

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        root = Trie()

        for w in reversed(words):
            res += root.count(w)
            root.add(w)
        return res

# class Solution:
#     def countPrefixSuffixPairs(self, words: List[str]) -> int:
#         res = 0
#         for i in range(len(words)):
#             for j in range(i + 1, len(words)):
#                 L = len(words[i])
#                 if words[j].startswith(words[i]) and words[j].endswith(words[i]):
#                     res += 1
#                 # if words[i] == words[j][:L] and words[i] == words[j][-L:]:
#                 #     res += 1
#         return res