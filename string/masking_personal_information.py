class Solution:
    def maskPII(self, s: str) -> str:
        res = self.maskEmail(s) if "@" in s else self.maskPhone(s)
        return res
    
    
    def maskEmail(self, email: str) -> str:
        parts = email.split("@")
        name = parts[0].lower()
        first, last = name[0], name[-1]
        name = first + "*****" + last
        domain = parts[1].lower()

        return "".join([name, "@", domain])

    def maskPhone(self, phone: str) -> str:

        phone = phone.replace("+", "").replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
        local_number = phone[-10:]
        area_code = phone[:-10]

        res = ""

        if len(area_code) == 0:
            res = "***-***-" + local_number[-4:]
        elif len(area_code) == 1:
            res = "+*-***-***-" + local_number[-4:]
        elif len(area_code) == 2:
            res = "+**-***-***-" + local_number[-4:]
        else:
            res = "+***-***-***-" + local_number[-4:]

        return res


sol = Solution()

print(sol.maskPII("+86(88)1513-7-74"))