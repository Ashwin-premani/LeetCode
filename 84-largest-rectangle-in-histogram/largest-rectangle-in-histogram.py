class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left = [0] * n
        right = [0] * n
        for i in range(len(heights)):
            while stack  and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                left[i] = 0
            else:
                left[i] = stack[-1] + 1
            stack.append(i)
            
        while stack:
            stack.pop()
        
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                right[i] = n - 1
            else:
                right[i] = stack[-1] - 1
            stack.append(i)
        
        res = 0
        for i in range(n):
            res = max(res, heights[i] * (right[i] - left[i] + 1))
        return res

        # Brute force -> TLE
        m = max(heights)
        n = len(heights)
        res = 0
        for i in range(m+1):
            l = 0
            total = 0
            for j in range(n):
                if heights[j] >= i:
                    l += 1
                else:
                    l = 0
                total = max(total, l)
            res = max(res, total * i)
        return res % mod