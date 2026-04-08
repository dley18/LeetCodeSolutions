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
        

        new_head = None
        head_ref = head
        map = {}

        while head:
            node = Node(head.val, None, None)

            map[head] = node

            head = head.next

        while head_ref:

            if head_ref is None:
                break

            if head_ref.next in map:
                map[head_ref].next = map[head_ref.next]
            else:
                map[head_ref].next = None

            if head_ref.random in map:
                map[head_ref].random = map[head_ref.random]
            else:
                map[head_ref].random = None

            if not new_head:
                new_head = map[head_ref]

            head_ref = head_ref.next

        return new_head