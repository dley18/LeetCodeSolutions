class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {char: i for i, char in enumerate(s)}
        stack = []

        for i, char in enumerate(s):
            if char in stack:
                continue

            while stack and char < stack[-1] and last_index[stack[-1]] > i:
                stack.pop()
            stack.append(char)

        return "".join(stack)