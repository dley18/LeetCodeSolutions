# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        while current and current.val != 1000000:
            current.val = 1000000
            current = current.next
        
        if current and current.val == 1000000:
            return True
        return False