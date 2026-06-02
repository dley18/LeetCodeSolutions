"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hash_map = {}
        current = head
        prev = None
        new_head = None
        while current:
            new_node = Node(current.val)
            if not new_head:
                new_head = new_node
            
            if prev:
                prev.next = new_node
            
            prev = new_node
            hash_map[current] = new_node
            current = current.next

        
        current = head
        while current:
            if current.random:
                hash_map[current].random = hash_map[current.random]
            else:
                hash_map[current].random = None
            current = current.next

        return new_head