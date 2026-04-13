class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = [char for char in s]

        for char in t:
            try:
                s_list.remove(char)
            except Exception as e:
                return False

        return True if len(s_list) == 0 else False