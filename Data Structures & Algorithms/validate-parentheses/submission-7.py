class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            try:
                if c == ")" and stack[-1] ==  "(":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(c)
            except:
                return False
                
        return True if len(stack) == 0 else False