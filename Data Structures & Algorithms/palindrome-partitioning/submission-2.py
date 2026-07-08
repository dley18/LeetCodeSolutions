class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        path = []

        def is_palindrome(palin_word):
            if not palin_word:
                return False
            return palin_word == palin_word[::-1]
        
        def dfs(i: int):
            if i >= len(s):
                res.append(path.copy())
                return

            for j in range(i, len(s)):
                if is_palindrome(s[i:j+1]):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
            
            return

        dfs(0)

        return res