# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def same_tree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False

        return self.same_tree(root1.left, root2.left) and self.same_tree(root1.right, root2.right)        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None:
            return False
        
        isRoot = self.same_tree(root, subRoot)
        return isRoot or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        