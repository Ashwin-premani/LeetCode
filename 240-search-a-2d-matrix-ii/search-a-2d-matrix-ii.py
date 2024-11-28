class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(row):
            l = 0
            r = len(matrix[row]) - 1
            while l <= r:
                m = l + (r - l)//2
                if target == matrix[row][m]:
                    return True
                elif matrix[row][m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return False
        row = 0
        while row <= len(matrix)-1:
            if binary_search(row):
                return True
            else:
                row += 1
        return False