class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let lengths = [0];
        let seen = new Set();
        let right = 0;
        let left = 0;
        while (right != s.length && left != s.length) {
            while (!seen.has(s[right]) && right != s.length) {
                seen.add(s[right]);
                right += 1;
            }
            seen.delete(s[left]);
            lengths.push(right - left);
            left += 1;
        }
        return Math.max(...lengths);
    }
}