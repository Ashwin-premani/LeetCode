# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        height = defaultdict(lambda : 0)

        def dfs(root):
            if not root:
                return -1
            height[root.val] = 1 + max(dfs(root.left),dfs(root.right))
            return height[root.val]
        dfs(root)

        removed_height = defaultdict(lambda : 0)
        dummy = TreeNode(-1)
        height[dummy.val] = -1
        q = [root]
        lvl = 0
        while q:
            u,v = heapq.nlargest(2,q + [dummy],key = lambda node: height[node.val])
            for node in q:
                removed_height[node.val] = lvl + height[u.val] * int(u.val != node.val) + height[v.val] * int(u.val == node.val) 
            q = [child for node in q for child in [node.left,node.right] if child]
            lvl+=1
        return [removed_height[query] for query in queries]