class Solution:
    def reverseBits(self, n: int) -> int:
        s = format(n, "032b")
        return int(s[::-1],2)
