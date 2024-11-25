class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        r = 0
        while r < rows - 1:  # Check until second-to-last row
            if matrix[r][0] <= target and matrix[r + 1][0] > target:
                break
            r += 1  
        l = 0
        n = len(matrix[r]) - 1
        while l <= n:
            m = l + (n - l)//2
            if matrix[r][m] == target:
                return True
            elif matrix[r][m] > target:
                n = m - 1
            else:
                l = m + 1
        return False
