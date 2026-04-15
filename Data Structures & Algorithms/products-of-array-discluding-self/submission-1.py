class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)

        for i in range(len(nums)):
            prefixes[i] = prefixes[i-1] * nums[i - 1] if i > 0  else 1

        for i in range(len(nums) - 1, -1, -1):
            suffixes[i] = suffixes[i+1] * nums[i+1] if i < len(nums) - 1 else 1

        res = []
        for i in range(len(nums)):
            res.append(prefixes[i] * suffixes[i])

        return res
