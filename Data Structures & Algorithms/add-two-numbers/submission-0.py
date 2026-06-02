# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2

        l1_string = ""
        l2_string = ""

        while curr1 or curr2:
            if curr1:
                l1_string += str(curr1.val)
                curr1 = curr1.next
            if curr2:
                l2_string += str(curr2.val)
                curr2 = curr2.next

        val1 = int(l1_string[::-1])
        val2 = int(l2_string[::-1])

        total = str(val1 + val2)[::-1]
        
        prev = None
        head = None
        for char in total:
            new_node = ListNode(char)
            if not head:
                head = new_node
            if prev:
                prev.next = new_node

            prev = new_node

        return head
            


            
