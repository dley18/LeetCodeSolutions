from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        prev = None
        for i in range(len(nums)):
            if nums[i] == prev:
                continue
            prev = nums[i]
            front = i + 1
            back = len(nums) - 1
            while front < back:
                if nums[front] + nums[i] + nums[back] == 0:
                    res.append([nums[front], nums[i], nums[back]])
                    temp_front = nums[front]
                    temp_back = nums[back]
                    front += 1
                    back -= 1
                    while(front < back and nums[front] == temp_front and nums[back] == temp_back):
                        front += 1
                        back -= 1

                elif nums[front] + nums[i] + nums[back] > 0:
                    back -= 1
                else:
                    front += 1

        return res