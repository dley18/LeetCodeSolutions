class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = [char for char in s]

        for char in t:
            if char in s_list:
                s_list.remove(char)
            else:
                return False

        return True