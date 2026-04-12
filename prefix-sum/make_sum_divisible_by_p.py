from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        table = {}
        table[0] = -1
        target = sum(nums) % p

        if target == 0:
            return 0
        
        current_sum = 0
        min_len = len(nums)

        for i in range(len(nums)):
            current_sum += nums[i]
            remainder = current_sum % p

            if (remainder - target) % p in table:
                min_len = min(min_len, i - table[(remainder - target) % p])

            table[remainder] = i

        return -1 if min_len == len(nums) else min_len