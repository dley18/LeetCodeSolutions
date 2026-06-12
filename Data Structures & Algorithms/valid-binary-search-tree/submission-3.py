# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self, root: Optional[TreeNode], interval: List):
        if root is None:
            return True

        if root.val <= interval[0]:
            return False

        if root.val >= interval[1]:
            return False

        valid_left = self.recurse(root.left, [interval[0], root.val])
        valid_right = self.recurse(root.right, [root.val, interval[1]])
        
        return valid_left and valid_right

        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recurse(root, [-math.inf, math.inf])
        

    