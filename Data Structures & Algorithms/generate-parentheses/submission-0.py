class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        target_len = 2 * n
        
        def backtrack(string: str, open_p: int, close_p: int):

            if open_p > n or close_p > n:
                return

            if len(string) == target_len and close_p == open_p:
                res.append(string)
                return
            
            open_string = string + "("
            backtrack(open_string, open_p + 1, close_p)      

            if close_p < open_p:
                close_string = string + ")"
                backtrack(close_string, open_p, close_p + 1)     
        
        backtrack("", 0, 0)
        return res
