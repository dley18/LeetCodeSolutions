class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        return word == word.upper() or word == word.lower() or word == word.capitalize()


solution = Solution()

print(solution.detectCapitalUse("FlaG"))