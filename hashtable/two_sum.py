class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        number_dict = {}

        for index, value in enumerate(nums):
            if target - value in number_dict:
                return [number_dict[target - value], index]
            else:
                number_dict[value] = index

        return None

