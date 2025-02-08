"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque()
        q.append([root, 0]) 
        dummy = Node()
        prev = None
        prev_val = 0
        while q:
            node, val = q.popleft()
            if prev and prev_val == val:
                prev.next = node
            prev = node
            prev_val = val
            if node.left:
                q.append([node.left, val+1])
            if node.right:
                q.append([node.right, val+1])
        return root