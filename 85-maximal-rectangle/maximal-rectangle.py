class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
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
                elif matrix[i][j] == "0":
                    hist[j] = 0
            area = histogram(hist)
            max_area = max(max_area, area)
        return max_area