class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        if n < 3:
            return 0
        count = 0
        window = colors + colors[:2]
        for i in range(n):
            if window[i+1] != window[i] and window[i+1] != window[i+2]:
                count += 1
        return count