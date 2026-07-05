class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        nums.sort()

        def backtrack(idx: int):
            if idx == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[idx])
            backtrack(idx + 1)

            old_idx = idx
            while idx < len(nums) and nums[old_idx] == nums[idx]:
                idx += 1

            subset.pop()
            backtrack(idx)

        backtrack(0)
        return res