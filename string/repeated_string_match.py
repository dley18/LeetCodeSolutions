class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 1
        letters = a
        while len(letters) < len(b):
            letters = letters + a
            count += 1
        if b in letters:
                return count
        if b in letters + a:
            return count + 1
        return -1