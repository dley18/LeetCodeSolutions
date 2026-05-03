class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t: return t
        if len(t) > len(s): return ""
        t_count = {}
        s_count = {}

        for i in range(len(t)):
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
            s_count[s[i]] = 1 + s_count.get(s[i], 0)

        l = 0
        res = ""

        for r in range(len(t) - 1, len(s)):
            s_count[s[r]] = 1 + s_count.get(s[r], 0) if r != len(t) - 1 else s_count.get(s[r], 0)

            while all(s_count.get(k, 0) >= v for k, v in t_count.items()):
                new_res = s[l:r + 1]
                if res == "" or len(new_res) < len(res):
                    res = new_res
                s_count[s[l]] -= 1
                l += 1
            print(f"L: {l}, R: {r}")

        return res