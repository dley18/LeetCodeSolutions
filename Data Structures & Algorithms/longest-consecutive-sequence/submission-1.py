class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        new_nums = sorted(set(nums))

        counter = 0
        res = 0
        prev = None

        for i in range(len(new_nums)):
            
            if prev is None or prev + 1 == new_nums[i]:
                counter += 1
                prev = new_nums[i]
            
            else:
                res = max(res, counter)
                counter = 1
                prev = new_nums[i]

        return max(res, counter)
            

