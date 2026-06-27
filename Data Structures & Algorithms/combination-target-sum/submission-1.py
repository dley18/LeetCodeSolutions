class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        combo = []
        def dfs(idx: int, total: int):
            if total == target:
                res.append(combo.copy())
                return

            if total > target:
                return

            if idx >= len(nums):
                return 

            combo.append(nums[idx])
            total += nums[idx]
            dfs(idx, total)

            total -= combo.pop()
            dfs(idx + 1, total)

        dfs(0, 0)
        return res