# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = []
        prev = None
        ref = head

        if not head:
            return head

        while head:
            if head.val in seen:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                seen.append(head.val)
                head = head.next
        
        return ref
