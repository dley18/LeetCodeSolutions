class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if not word:
            return 0
        max_k = len(sequence) // len(word)
        for k in range(max_k, 0, -1):
            if word * k in sequence:
                return k
        return 0