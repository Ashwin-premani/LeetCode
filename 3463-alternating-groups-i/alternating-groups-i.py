class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        colors += colors
        count = 0
        for i in range(n):
            if colors[i] == colors[i+2] and colors[i] != colors[i+1]:
                count += 1
        return count