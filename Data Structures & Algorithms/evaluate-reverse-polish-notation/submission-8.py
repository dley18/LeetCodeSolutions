class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "*":
                res = stack.pop()
                res *= stack.pop()
                stack.append(res)

            elif token == "/":
                
                res = stack.pop()
                res = int(stack.pop() / res)
                stack.append(res)

            elif token == "+":
                res = stack.pop()
                res += stack.pop()
                stack.append(res)

            elif token == "-":
                res = stack.pop()
                res = stack.pop() - res
                stack.append(res)
            else:
                stack.append(int(token))

        return int(stack.pop())