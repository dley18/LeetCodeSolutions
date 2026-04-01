class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "")
        s = s.upper()

        parts = []
        count = 0
        for i, char in enumerate(reversed(s)):
            parts.append(char)
            count += 1
            if count == k and i != len(s) - 1:
                parts.append("-")
                count = 0

        return "".join(reversed(parts))
    
sol = Solution()

print(sol.licenseKeyFormatting("2-5g-3-J", 2))
