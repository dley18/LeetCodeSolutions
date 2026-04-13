class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        table = {}
        
        for num in nums:
            if num in table:
                return True
            table[num] = num
    
        return False
