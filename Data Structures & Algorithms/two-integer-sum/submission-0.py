class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        table = {}

        for index, value in enumerate(nums):
            if target - value in table:
                return [table[target - value], index]
            else:
                table[value] = index

        return None