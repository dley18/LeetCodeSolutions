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
        idx = 0
        current = queue[idx]

        while True:
            if len(queue) == 1:
                node = current
                res.append(node.val)
                self.appendChildren(node, queue)
                idx += 1
                if len(queue) > idx:
                    current = queue[idx]
                else:
                    break
            else:
                last = queue[-1]
                while current != last:
                    node = current
                    self.appendChildren(node, queue)
                    idx += 1
                    if len(queue) > idx:
                        current = queue[idx]
                    else:
                        break

                node = current
                res.append(node.val)
                self.appendChildren(node, queue)
                idx += 1
                if len(queue) > idx:
                    current = queue[idx]
                else:
                    break
        
        return res