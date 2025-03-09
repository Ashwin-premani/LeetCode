class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        count = 0

        for i in range(n):
            l = colors[(i - 1)%n]
            m = colors[i]
            r = colors[(i+1)%n]
            if l != m and m != r:
                count += 1
        return count