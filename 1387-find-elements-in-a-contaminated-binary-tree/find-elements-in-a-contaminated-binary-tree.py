# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()  # Initialize values as instance variable
        def reval(root, v):
            if not root:
                return
            self.values.add(v)  # Add value to the set
            if root.left:
                reval(root.left, v * 2 + 1)
            if root.right:
                reval(root.right, v * 2 + 2)
        
        root.val = 0  # Reset root value to 0
        reval(root, 0)  # Start recovery from root with value 0
    
    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)