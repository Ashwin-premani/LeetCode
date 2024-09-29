class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        cur = root
        n = 0

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            n += 1
            
            if n == k:
                return cur.val
            
            cur = cur.right
        
        # If we exit the loop without returning, it means k is out of bounds.
        return None  # or raise an error depending on how you want to handle this
