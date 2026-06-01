# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  
        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        count = 0
        current = head
        prev = None
        while current:
            if (length - count) == n:
                if prev:
                    prev.next = current.next
                else:
                    head = current.next
                break
            prev = current
            current = current.next
            count += 1

        return head

