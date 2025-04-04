# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # return (lowest commen ancestor, depth)
        def dfs(node, depth):
            if not node:
                return (None, depth + 1)
            left_node, ldepth = dfs(node.left, depth + 1)
            right_node, rdepth = dfs(node.right, depth + 1)
            if ldepth > rdepth:
                return left_node, ldepth
            elif ldepth < rdepth:
                return right_node, rdepth
            return node, ldepth
            
        node, _ = dfs(root, 0)
        return node