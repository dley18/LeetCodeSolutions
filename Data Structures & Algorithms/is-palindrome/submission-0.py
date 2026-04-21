class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        letters = ''.join(char.lower() for char in s if char.isalnum())

        front = 0

        back = len(letters) - 1

        while front < back:

            if letters[front] != letters[back]:
                return False
            
            front += 1
            back -= 1
        
        return True