/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {
        let current = head;
        let length = 0;
        while (current) {
            length += 1;
            current = current.next;
        }

        let count = 0;
        current = head;
        let prev = null;
        while (current) {
            if (length - count == n) {
                if (prev) {
                    prev.next = current.next;
                } else {
                    head = current.next;
                }
            }
            prev = current;
            current = current.next;
            count += 1;
        }
        return head;
    }
}
