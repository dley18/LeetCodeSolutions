// class Node {
//   constructor(val, next = null, random = null) {
//       this.val = val;
//       this.next = next;
//       this.random = random;
//   }
// }

class Solution {
    /**
     * @param {Node} head
     * @return {Node}
     */
    copyRandomList(head) {
        let hashMap = new Map();
        let current = head;
        let prev = null;
        let newHead = null;
        while (current) {
            const newNode = new Node(current.val);
            if (!newHead) {
                newHead = newNode;
            }
            if (prev) {
                prev.next = newNode;
            }

            prev = newNode;
            hashMap.set(current, newNode);
            current = current.next;
        }

        current = head;
        while (current) {
            if (!!current.random) {
                hashMap.get(current).random = hashMap.get(current.random);
            } else {
                hashMap.get(current).random = null;
            }
            current = current.next;
        }

        return newHead;
    }
}
