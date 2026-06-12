# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self, root: Optional[TreeNode]):
        if root is None:
            return

        self.recurse(root.left)
        self.ordered_list.append(root.val)
        self.recurse(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ordered_list = []
        self.recurse(root)
        return self.ordered_list[k-1]