/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[][]}
     */
    levelOrder(root) {
        if (!root) return [];
        let queue = [];
        queue.push(root);
        let res = [];

        while (queue.length > 0) {
            let sublist = [];
            const levelSize = queue.length;

            for (let i = 0; i < levelSize; i++) {
                let node = queue.shift();
                sublist.push(node.val);

                if (node.left) {
                    queue.push(node.left);
                }

                if (node.right) {
                    queue.push(node.right);
                }
            }
            res.push(sublist);
        }
        return res;
    }
}
