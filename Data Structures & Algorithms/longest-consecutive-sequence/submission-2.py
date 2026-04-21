class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        new_nums = set(nums)
        res = 0

        for num in new_nums:
            
            if num - 1 not in new_nums:
                length = 1
                while num + length in new_nums:
                    length += 1
                res = max(res, length)

        return res
            

