class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            for char in string:
                encoded_str += format(ord(char), "b") + "2"
            encoded_str += "3"

        return encoded_str



    def decode(self, s: str) -> List[str]:
        strs = []
        temp_str = ""
        temp_char = ""
        for char in s:
            if char == "3":
                strs.append(temp_str)
                temp_str = ""
            elif char == "2":
                temp_str += chr(int(temp_char, 2))
                temp_char = ""
            else:
                temp_char += (char)

        return strs