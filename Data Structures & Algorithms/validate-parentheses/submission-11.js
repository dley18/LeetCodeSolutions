class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack = [];
        const matching = {")": "(", "}": "{", "]": "["};

        for (let i = 0; i < s.length; i++) {
            if (Object.hasOwn(matching, s[i])) {
                if (stack.length === 0 || stack[stack.length - 1] != matching[s[i]]) {
                    return false;
                }
                stack.pop();
            } else {
                stack.push(s[i]);
            }
        }

        return stack.length === 0;
    }
}
