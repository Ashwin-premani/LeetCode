class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        count = defaultdict(int)
        for i in range(m):
            for j in range(m):
                count[grid[i][j]] += 1

        double, missing = 0, 0
        for num in range(1, m*m + 1):
            if count[num] == 0:
                missing = num
            if count[num] == 2:
                double = num
        return [double, missing]
            