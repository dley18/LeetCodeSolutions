class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        suffixes = []

        for i in range(len(nums)):
            if i == 0:
                prefixes.append(1)
            else:
                prefix_product = 1
                for num in nums[:i]:
                    prefix_product *= num
                prefixes.append(prefix_product)

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffixes.append(1)
            else:
                suffix_product = 1
                for num in nums[i + 1:]:
                    suffix_product *= num
                suffixes.append(suffix_product)

        res = []
        for i in range(len(nums)):
            res.append(prefixes[i] * suffixes[len(nums) -1 - i])

        return res
