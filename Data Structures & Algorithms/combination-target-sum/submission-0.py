class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        combo = []
        def dfs(idx: int):
            if sum(combo) == target:
                res.append(combo.copy())
                return

            if sum(combo) > target:
                return

            if idx >= len(nums):
                return 

            combo.append(nums[idx])
            dfs(idx)

            combo.pop()
            dfs(idx + 1)

        dfs(0)
        return res