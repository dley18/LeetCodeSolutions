class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for string in strs:
            for char in string:
                parts.append(format(ord(char), "b") + "2")
            parts.append("3")

        return "".join(parts)



    def decode(self, s: str) -> List[str]:
        strs = []
        temp_str = []
        temp_char = []
        for char in s:
            if char == "3":
                strs.append("".join(temp_str))
                temp_str = []
            elif char == "2":
                temp_str.append(chr(int("".join(temp_char), 2)))
                temp_char = []
            else:
                temp_char.append(char)

        return strs