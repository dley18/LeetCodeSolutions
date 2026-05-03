class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_set = Counter(s1)
        for r in range(len(s1) - 1, len(s2)):
            if Counter(s2[l: r + 1]) == s1_set:
                return True
            l += 1

        return False