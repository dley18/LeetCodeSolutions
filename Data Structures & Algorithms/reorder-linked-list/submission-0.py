# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find Middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse
        second = slow.next
        slow.next = None
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # Merge
        second = prev
        first = head
        while second:
            tmp = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp
            first = tmp
            second = tmp2