class Solution:
    def frequencySort(self, s: str) -> str:
        hash = {}
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        hash = OrderedDict(sorted(hash.items(), key=lambda item: (-item[1], item[0])))
        s = ""
        for i,n in hash.items():
            s += i*n

        return s