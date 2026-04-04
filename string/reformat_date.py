from datetime import datetime

class Solution:
    def reformatDate(self, date: str) -> str:
        date_parts = date.split(" ")
        month = str(datetime.strptime(date_parts[1], "%b").month)
        month = "0" + month if len(month) == 1 else month
        day = "".join([char for char in date_parts[0] if char.isdigit()])
        day = "0" + day if len(day) == 1 else day
        return date_parts[2] + "-" + month + "-" + day


solution = Solution()
print(solution.reformatDate("6th Jun 1933"))