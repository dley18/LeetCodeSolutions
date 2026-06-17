# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self, root):
        if root is None:
            return 0
        
        max_left = self.recurse(root.left)
        max_right = self.recurse(root.right)
        max_current_node = max_left + root.val if max_left > max_right else max_right + root.val
        max_current_node = root.val if root.val > max_current_node else max_current_node
        max_to_consider = max(0, max_left) + root.val + max(0, max_right)
        
        self.global_max = max(self.global_max, max(max_current_node, max_to_consider))
        return max_current_node

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = root.val
        self.recurse(root)
        return self.global_max
        