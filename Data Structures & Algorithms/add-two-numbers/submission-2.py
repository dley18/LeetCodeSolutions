# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0
        head = None
        prev = None
        while curr1 or curr2:
            new_node = ListNode()
            if not head:
                head = new_node
            if prev:
                prev.next = new_node
            
            prev = new_node

            total = 0
            if carry:
                total += carry
                carry = 0

            if curr1:
                total += curr1.val
                curr1 = curr1.next
            if curr2:
                total += curr2.val
                curr2 = curr2.next
            
            val = total
            if total >= 10:
                val = total % 10
                carry = (total - val) // 10

            new_node.val = val

        if carry > 0:
            new_node = ListNode()
            prev.next = new_node
            new_node.val = carry
            new_node.next = None

        return head
            


            


            
