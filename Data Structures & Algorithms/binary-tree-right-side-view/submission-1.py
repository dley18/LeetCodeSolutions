# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def appendChildren(self, node: Optional[TreeNode], queue: []) -> None:
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = []
        res = []
        queue.append(root)

        while queue:
            if len(queue) == 1:
                node = queue.pop(0)
                res.append(node.val)
                self.appendChildren(node, queue)

            else:
                last = queue[-1]
                while queue[0] != last:
                    node = queue.pop(0)
                    self.appendChildren(node, queue) 

                node = queue.pop(0)
                res.append(node.val)
                self.appendChildren(node, queue)
        
        return res