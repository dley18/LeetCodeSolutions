class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        word = s + s
        word = word[1:-1]
        return s in word