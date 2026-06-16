# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self, low: int, high: int):
        if low > high:
            return None

        node = TreeNode(self.queue[self.front], None, None)
        self.front += 1
        mid = self.table[node.val]

        node.left = self.recurse(low, mid - 1)
        node.right = self.recurse(mid + 1, high)

        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.table = {}
        for i in range(len(inorder)):
            self.table[inorder[i]] = i
        
        self.queue = preorder
        self.front = 0
        return self.recurse(0, len(inorder) - 1)



