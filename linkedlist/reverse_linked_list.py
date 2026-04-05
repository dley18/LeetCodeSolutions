# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        prev = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        return prev
    
    def reverseListRecursion(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head
        
        result = self.reverseListRecursion(head.next)
        head.next.next = head
        head.next = None
        return result
            