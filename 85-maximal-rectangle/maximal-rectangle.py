class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # here we have used largest area of histogram leetcode 84 which takes heigh
        # i have converted each row x upto jth col into a histogram by adding new rows to prev one and if new one contains a 0 height is reset to 0 and for each row max is calculated and updated 
        # O(n⋅m) - Time
        # O(m) - Space
        def histogram(heights):
            stack = []
            max_area = 0
            n = len(heights)

            for i in range(n+1):
                while stack and (i == n or heights[stack[-1]] >= heights[i]):
                    height = heights[stack[-1]]
                    stack.pop()
                    width = 0
                    if not stack: 
                        width = i
                    else:
                        width = i - stack[-1] - 1
                    max_area = max(max_area, width * height)
                stack.append(i)
            return max_area
        
        n = len(matrix)
        m = len(matrix[0])
        hist = [0] * m
        max_area = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    hist[j] += 1
                else:
                    hist[j] = 0
            # using stack
            stack = []
            for k in range(m + 1):
                current_height = hist[k] if k < m else 0  # Add dummy 0 height at end
                while stack and hist[stack[-1]] >= current_height:
                    height = hist[stack.pop()]
                    width = k if not stack else k - stack[-1] - 1
                    max_area = max(max_area, width * height)
                stack.append(k)

            # normal
            # area = histogram(hist)
            # max_area = max(max_area, area)
        return max_area