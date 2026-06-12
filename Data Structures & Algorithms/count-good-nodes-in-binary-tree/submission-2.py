# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def recurse(self, root: TreeNode, maximum: int):
        if root is None:
            return
        
        if root.val >= maximum:
            self.good_nodes += 1
        
        maximum = max(maximum, root.val)
        self.recurse(root.left, maximum)
        self.recurse(root.right, maximum)
        return

    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0
        self.recurse(root, root.val)
        return self.good_nodes