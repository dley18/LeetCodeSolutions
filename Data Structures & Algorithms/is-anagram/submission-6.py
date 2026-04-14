class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_table = {}
        t_table = {}

        for i in range(len(s)):
            if s[i] in s_table:
                s_table[s[i]] += 1
            else:
                s_table[s[i]] = 1

            if t[i] in t_table:
                t_table[t[i]] += 1
            else:
                t_table[t[i]] = 1

        for key, value in s_table.items():
            if key not in t_table or value != t_table[key]:
                return False

        return True