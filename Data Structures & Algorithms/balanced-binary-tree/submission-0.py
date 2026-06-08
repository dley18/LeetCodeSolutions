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

        if abs(left_height - right_height) > 1:
            self.balanced = False
        else:
            self.balanced = True and self.balanced

        return max(left_height, right_height)
        


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        self.balanced = True
        self.recurse(root)
        return self.balanced