class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        let stack = [];

        for (let i = 0; i < tokens.length; i++) {
            if (tokens[i] === "+") {
                let res = stack.pop();
                res += stack.pop();
                stack.push(res);
            } else if (tokens[i] === "-") {
                let res = stack.pop();
                res = stack.pop() - res;
                stack.push(res);
            } else if (tokens[i] === "*") {
                let res = stack.pop();
                res *= stack.pop();
                stack.push(res);
            } else if (tokens[i] === "/") {
                let res = stack.pop();
                res = Math.trunc(stack.pop() / res);
                stack.push(res);
            } else {
                stack.push(Number(tokens[i]));
            }
        }
        return Number(stack.pop());
    }
}
