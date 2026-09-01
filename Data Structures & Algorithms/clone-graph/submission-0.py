"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, node, visited):
        if not node:
            return None

        if node in visited:
            return visited[node]

        clone = Node(node.val)
        visited[node] = clone
        for neighbor in node.neighbors:
            clone.neighbors.append(self.dfs(neighbor, visited))

        return clone

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.dfs(node, {})