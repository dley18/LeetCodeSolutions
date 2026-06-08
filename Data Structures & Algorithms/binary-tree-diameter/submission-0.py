# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, root):
        if root is None:
            return -1

        left_height = 1 + self.recurse(root.left)
        right_height = 1 + self.recurse(root.right)
        self.diameter = max(self.diameter, left_height + right_height)
        return max(left_height, right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.recurse(root)
        return self.diameter
