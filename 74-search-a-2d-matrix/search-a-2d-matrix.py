class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:





        # O(m+log(n)):

        top = 0
        bottom = len(matrix) - 1
    
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                # Target might be in this row
                break
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1
    
        if top > bottom:
            return False
        r = mid
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
