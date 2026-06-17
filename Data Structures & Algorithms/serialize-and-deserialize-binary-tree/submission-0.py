# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "None,"
        
        output = f"{root.val},"
        output += self.serialize(root.left)
        output += self.serialize(root.right)

        return output

    # Decodes your encoded data to tree.
    def recurse(self):
        if self.nodes[self.idx] == "None":
            return None
        
        node = TreeNode(self.nodes[self.idx])
        self.idx += 1
        node.left = self.recurse()
        self.idx += 1
        node.right = self.recurse()

        return node


    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data[:-1]
        self.nodes = data.split(",")
        self.idx = 0
        return self.recurse()



        

